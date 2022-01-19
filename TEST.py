    #モジュールインポート
from appium import webdriver
import subprocess
from subprocess import run
from subprocess import PIPE
import pyautogui as pg
import time
import MJSOpen
from selenium.webdriver.common.keys import Keys
#lxmlインポート
import lxml.html
#pandasインポート
import pandas as pd
#配列計算関数numpyインポート
import numpy as np
#小数点切り捨ての為にmathをインポート
import math
#timeインポート
import time
#reインポート
import re
#jsonインポート
import json
#osインポート
import os
#datetimeインポート
from datetime import datetime as dt
#日付加減算インポート
from dateutil.relativedelta import relativedelta
#glob(フォルダファイルチェックコマンド)インポート
import glob
#shutil(フォルダファイル編集コマンド)インポート
import shutil
#例外処理判定の為のtracebackインポート
import traceback
#pandas(pd)で関与先データCSVを取得
import pyautogui
import time
import shutil
import codecs
import pyperclip #クリップボードへのコピーで使用
from datetime import datetime, timedelta
import WarekiHenkan

C_forCount = 0
NoAction = False
Todays = dt.today()
CSVURL = "D:\PythonScript\RPAScript\RPAPhoto\TKC_DensiSinkoku"
CSVName = "HouteiKyuuhouJyusinMaster"
C_url = CSVURL.replace("\\","/") + '/' + CSVName + '.CSV'
C_Master = pd.read_csv(C_url,encoding='shiftjis')
C_dfRow = np.array(C_Master).shape[0]#配列行数取得
C_dfCol = np.array(C_Master).shape[1]#配列列数取得
#----------------------------------------------------------------------------------------------------------------------
#切出MasterCSVをループ処理---------------------------------------------------------------------------------------------
for x in range(C_dfRow):
    #関与先DB配列をループして識別番号とPassを取得
    if CSVName == 'SinseiJyusinMaster':#処理が申請の場合
        C_dfDataRow = C_Master.loc[x]
        C_SCode = C_dfDataRow["関与先コード"]
        C_Name = C_dfDataRow["納税者(関与先)"]
        C_Zeimoku = C_dfDataRow["申請・届出書類名"]
        C_Sousin = C_dfDataRow["送信"]
        C_UketukeDay = C_dfDataRow["申告受付日時"]
        C_All =  str(C_SCode) + str(C_Name) 
#元ネタ列名"→"行","事務所コード","関与先コード","納税者(関与先)","決算月","申請・届出書類名","提出先","電子申請データ作成","電子署名(納税者)","電子署名(税理士)","送信","申請受付日時","即時通知","受信通知","送付書","提出期限","報告書","実践報告","監査担当者"
    else:
        C_dfDataRow = C_Master.loc[x]
        C_SCode = C_dfDataRow["関与先コード"]
        C_Name = C_dfDataRow["納税者(関与先)"]
        C_Zeimoku = C_dfDataRow["税目"]
        C_Sousin = C_dfDataRow["送信"]
        C_UketukeDay = C_dfDataRow["申告受付日時"]
        C_All =  str(C_SCode) + str(C_Name) 
#元ネタ列名"→行","事務所コード","関与先コード","納税者(関与先)","決算月","税目","申告区分","電子申告データ作成","事業年度／課税期間","電子署名(添付書面)","電子署名(納税者)","電子署名(税理士)","送信","申告受付日時","即時通知","受信通知","送付書","申告期限","完了目標(3日前まで)","期限内","TISC","報告書","実践報告","監査担当者"
    C_UketukeDay = C_UketukeDay.replace("(",".").replace("（",".").replace(")","").replace("）","")
    C_UkeSplit = C_UketukeDay.split(".")
    WarekiSpl = WarekiHenkan.SeirekiDate("R",int(C_UkeSplit[0]),int(C_UkeSplit[1]),int(C_UkeSplit[2]))
    WarekiSpl = WarekiSpl + " 00:00:00"
    C_UketukeDay = dt.strptime(WarekiSpl, '%Y/%m/%d %H:%M:%S')
    DayCount = Todays - C_UketukeDay
    print(DayCount.days)
    stop