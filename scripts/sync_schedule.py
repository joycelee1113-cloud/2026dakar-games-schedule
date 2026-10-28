#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
每小時自動從 Google 試算表同步 2026 達卡青奧中華代表團賽程與賽果
重要規則：
1. 若 data/schedule.json 中某筆賽事已標註 resultLocked == True（已完賽並登錄對戰成績），
   則直接跳過該筆紀錄，不重複更新或覆寫，節省處理資源。
2. 若未完賽之場次在試算表中有時間、對手或階段異動，或新填入完賽成績，則自動更新並鎖定。
"""

import csv
import io
import json
import os
import urllib.request
from datetime import datetime, timezone

SPREADSHEET_ID = os.environ.get("SPREADSHEET_ID", "1vcdZRZd7907AaHBFdDiCKUTS3LT_oWiI")
SCHEDULE_JSON_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "schedule.json")

SPORT_CATEGORY_MAP = {
    "公路自由車 (Cycling Road)": "自由車",
    "五人制棒球 (Baseball5)": "五人制棒球",
    "女籃 3x3 (3x3 Basketball)": "3X3籃球",
    "霹靂舞 (Breaking)": "霹靂舞",
    "滑板 (Skateboarding)": "滑輪板",
    "游泳 (Swimming)": "游泳",
    "田徑 (Athletics)": "田徑",
    "跆拳道 (Taekwondo)": "跆拳道",
    "羽球 (Badminton)": "羽球",
    "射箭 (Archery)": "射箭",
    "開幕典禮 (Opening Ceremony)": "開幕典禮",
    "桌球 (Table Tennis)": "桌球",
    "擊劍 (Fencing)": "擊劍",
    "武術套路 (Wushu Taolu)": "武術",
    "拳擊 (Boxing)": "拳擊",
    "柔道 (Judo)": "柔道",
    "鐵人三項 (Triathlon)": "鐵人三項",
    "帆船 (Sailing)": "帆船",
}

ZONE_COLOR_MAP = {
    "Dakar": "green",
    "Diamniadio": "yellow",
    "Saly": "red",
}


def fetch_csv_rows(gid: str):
    url = f"https://docs.google.com/spreadsheets/d/{SPREADSHEET_ID}/export?format=csv&gid={gid}"
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=20) as resp:
        text = resp.read().decode("utf-8-sig")
    return list(csv.reader(io.StringIO(text)))


def main():
    if not os.path.exists(SCHEDULE_JSON_PATH):
        print("找不到 data/schedule.json，無法執行增量更新。")
        return

    with open(SCHEDULE_JSON_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)

    existing_by_id = {item["id"]: item for item in data.get("schedule", [])}

    try:
        rows = fetch_csv_rows("502502877")
    except Exception as exc:
        print(f"無法連線至雲端試算表（可能尚未開啟公開讀取權限）：{exc}")
        return

    updated_count = 0
    skipped_locked_count = 0
    new_schedule = []

    # 資料列從第 9 列開始（index 8）
    for idx, row in enumerate(rows[8:], start=1):
        if not any(cell.strip() for cell in row):
            continue
        item_id = f"TPE-{idx:03d}"
        old_item = existing_by_id.get(item_id)

        # 規則 2：已經完成登錄的賽果，填寫完畢之後就不需要再花力氣重複更新
        if old_item and old_item.get("resultLocked") is True:
            new_schedule.append(old_item)
            skipped_locked_count += 1
            continue

        raw_sport = row[6].strip() if len(row) > 6 else ""
        zone_str = row[3].strip() if len(row) > 3 else ""
        # 若試算表第 12 欄 (index 11) 有填寫對戰成績，則自動標註完賽並鎖定
        sheet_score = row[11].strip() if len(row) > 11 else ""
        is_finished = bool(sheet_score)

        new_item = {
            "id": item_id,
            "date": row[0].strip() if len(row) > 0 else "",
            "dakarTime": row[1].strip() if len(row) > 1 else "",
            "taipeiTime": row[2].strip() if len(row) > 2 else "",
            "zone": zone_str,
            "zoneColor": ZONE_COLOR_MAP.get(zone_str, "green"),
            "venue": row[4].strip() if len(row) > 4 else "",
            "venueFull": row[5].strip() if len(row) > 5 else "",
            "sport": raw_sport,
            "sportCategory": SPORT_CATEGORY_MAP.get(raw_sport, raw_sport),
            "stage": row[7].strip() if len(row) > 7 else "",
            "opponent": row[8].strip() if len(row) > 8 else "",
            "details": row[9].strip() if len(row) > 9 else "",
            "source": row[10].strip() if len(row) > 10 else "",
            "status": "FINISHED" if is_finished else (old_item.get("status", "UPCOMING") if old_item else "UPCOMING"),
            "score": sheet_score if is_finished else (old_item.get("score", "") if old_item else ""),
            "resultLocked": True if is_finished else False,
        }

        if old_item != new_item:
            updated_count += 1
        new_schedule.append(new_item)

    if new_schedule:
        data["schedule"] = new_schedule
        data["lastUpdated"] = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
        with open(SCHEDULE_JSON_PATH, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"同步完成：更新 {updated_count} 筆賽程，跳過 {skipped_locked_count} 筆已完賽鎖定項目。")


if __name__ == "__main__":
    main()
