# モジュールインポート
import pyautogui as pg
import time
import MJSOpen

# pandasインポート
import pandas as pd

# 配列計算関数numpyインポート
import numpy as np

# osインポート
import os

# datetimeインポート
from datetime import datetime as dt

# 例外処理判定の為のtracebackインポート
import traceback
import openpyxl
import datetime

# pandas(pd)で関与先データCSVを取得
import pyautogui
import codecs
import pyperclip  # クリップボードへのコピーで使用
import Function.ExcelFileAction as EFA
from openpyxl.formatting.rule import Rule

# logger設定------------------------------------------------------------------------------------------------------------
import logging.config

logging.config.fileConfig(r"LogConf\logging_debug.conf")
logger = logging.getLogger(__name__)
# ----------------------------------------------------------------------------------------------------------------------

# RPA用画像フォルダの作成---------------------------------------------------------
FolURL = os.getcwd().replace("\\", "/")  # 先
TFolURL = FolURL + r"\RPAPhoto\MJS_SystemNextCreate"  # 先
XLSURL = r"\\Sv05121a\e\C 作業台\RPA\RPA_ミロクシステム次年更新\ミロク更新項目.xlsx"
LURL = r"\\Sv05121a\e\C 作業台\RPA\RPA_ミロクシステム次年更新\MJSLog\MJSSysUpLog.txt"  # 処理状況CSVのURL
# --------------------------------------------------------------------------------
Exlsx = EFA.XlsmRead(XLSURL)
if Exlsx[0] is True:
    try:
        dt_now = datetime.datetime.now()
        WriteEx = openpyxl.load_workbook(XLSURL)
        WriteExSheet = WriteEx["更新申請"]
        WriteExSheet.cell(row=5, column=6).value = dt_now
        print("シート書き込み完了")
        WriteEx.save(XLSURL)
    except:
        traceback.print_exc()
else:
    print("Excel読み込みエラー")
    logger.debug("Excel読み込みエラー")
