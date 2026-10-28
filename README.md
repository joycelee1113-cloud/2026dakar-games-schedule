# 2026 達卡青年奧運（Dakar 2026）中華台北（TPE）代表團賽程與賽果系統

本專案以雲端硬碟之 `Dakar_2026_Chinese_Taipei_Schedule.xlsx`（檔案 ID：`1vcdZRZd7907AaHBFdDiCKUTS3LT_oWiI`）為基準資料（Base），完整呈現中華台北代表團 **17 項運動、37 名選手（全團 82 人）、共 91 個賽程時段** 之競賽時間、三大賽區、七大場館子標籤、競賽對手與競賽階段名稱。

## 一、專案資料夾結構

```text
2026dakar-games-schedule/
├── index.html                        # 網站主頁面（已內建完整 91 筆賽程、BS5 20 場對戰表、7 座場館統計）
├── css/
│   └── style.css                     # 綠色 (Dakar)、黃色 (Diamniadio)、紅色 (Saly) 賽區與子標籤樣式
├── js/
│   └── config.js                     # 賽區、場館代碼（COR/CTO/CID、DAR/SAW/DEX、SBW）與運動項目設定
├── data/
│   └── schedule.json                 # 結構化賽程與賽果資料庫（含 resultLocked 完賽鎖定標記）
├── scripts/
│   └── sync_schedule.py              # 每小時同步雲端試算表腳本（已鎖定之完賽成績自動跳過不重複處理）
└── .github/
    └── workflows/
        └── hourly_sync.yml           # GitHub Actions 每小時自動排程設定檔
```

## 二、賽區與場館子標籤對照

- **綠色賽區（Dakar 達卡市區）**
  - **COR**（Corniche West）：自由車
  - **CTO**（Complexe Tour de l'Œuf）：五人制棒球、3X3籃球、霹靂舞、滑輪板、游泳
  - **CID**（Complexe Iba Mar Diop）：田徑、跆拳道
- **黃色賽區（Diamniadio 新都賽區）**
  - **DAR**（Dakar Arena）：羽球
  - **SAW**（Stade Abdoulaye Wade）：射箭（含開幕典禮）
  - **DEX**（Dakar Exhibition Centre）：桌球、擊劍、武術、拳擊、柔道
- **紅色賽區（Saly 薩莉海濱）**
  - **SBW**（Saly Beach West）：鐵人三項、帆船

## 三、如何更新賽程與鎖定完賽成績

1. **直接部署單一檔案或完整資料夾**：
   - `index.html` 已將首頁畫面、三區子標籤篩選器與全部 91 筆基準賽程整合在一起，直接上傳覆蓋您 GitHub 儲存庫的 `index.html` 即可立即生效。
   - 若要啟用 GitHub 每小時自動同步，請將整個資料夾（含 `data/`、`scripts/`、`.github/workflows/hourly_sync.yml`）上傳至 GitHub，並確保 Google 試算表共用權限設為「知道連結的任何人皆可檢視」。
2. **完賽鎖定不重複更新**：
   - 當某場賽事完賽並填入對戰成績後，資料中的 `resultLocked` 會設為 `true`。每小時排程腳本 `scripts/sync_schedule.py` 遇到 `resultLocked: true` 的場次會直接跳過，不浪費資源重複更新。
