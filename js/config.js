// 2026 達卡青年奧運（Dakar 2026）賽區與場館子標籤設定檔
export const SPREADSHEET_ID = '1vcdZRZd7907AaHBFdDiCKUTS3LT_oWiI';

export const ZONE_CONFIG = {
  ALL: {
    id: 'ALL',
    name: '全部賽區 (All Zones)',
    venues: ['COR', 'CTO', 'CID', 'DAR', 'SAW', 'DEX', 'SBW']
  },
  Dakar: {
    id: 'Dakar',
    name: '綠色賽區：Dakar (達卡市區)',
    color: 'green',
    venues: ['COR', 'CTO', 'CID']
  },
  Diamniadio: {
    id: 'Diamniadio',
    name: '黃色賽區：Diamniadio (新都賽區)',
    color: 'yellow',
    venues: ['DAR', 'SAW', 'DEX']
  },
  Saly: {
    id: 'Saly',
    name: '紅色賽區：Saly (薩莉海濱)',
    color: 'red',
    venues: ['SBW']
  }
};

export const VENUE_SUBTAGS = {
  COR: {
    code: 'COR',
    zone: 'Dakar',
    color: 'green',
    fullName: 'Corniche West',
    label: '綠色 COR：自由車',
    sports: ['自由車']
  },
  CTO: {
    code: 'CTO',
    zone: 'Dakar',
    color: 'green',
    fullName: "Complexe Tour de l'Œuf",
    label: '綠色 CTO：五人制棒球、3X3籃球、霹靂舞、滑輪板、游泳',
    sports: ['五人制棒球', '3X3籃球', '霹靂舞', '滑輪板', '游泳']
  },
  CID: {
    code: 'CID',
    zone: 'Dakar',
    color: 'green',
    fullName: 'Complexe Iba Mar Diop',
    label: '綠色 CID：田徑、跆拳道',
    sports: ['田徑', '跆拳道']
  },
  DAR: {
    code: 'DAR',
    zone: 'Diamniadio',
    color: 'yellow',
    fullName: 'Dakar Arena',
    label: '黃色 DAR：羽球',
    sports: ['羽球']
  },
  SAW: {
    code: 'SAW',
    zone: 'Diamniadio',
    color: 'yellow',
    fullName: 'Stade Abdoulaye Wade',
    label: '黃色 SAW：射箭（含開幕典禮）',
    sports: ['射箭', '開幕典禮']
  },
  DEX: {
    code: 'DEX',
    zone: 'Diamniadio',
    color: 'yellow',
    fullName: 'Dakar Exhibition Centre',
    label: '黃色 DEX：桌球、擊劍、武術、拳擊、柔道',
    sports: ['桌球', '擊劍', '武術', '拳擊', '柔道']
  },
  SBW: {
    code: 'SBW',
    zone: 'Saly',
    color: 'red',
    fullName: 'Saly Beach West',
    label: '紅色 SBW：鐵人三項、帆船',
    sports: ['鐵人三項', '帆船']
  }
};
