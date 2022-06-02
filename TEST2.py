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

# logger設定------------------------------------------------------------------------------------------------------------
import logging.config

logging.config.fileConfig(r"LogConf\logging_debug.conf")
logger = logging.getLogger(__name__)
# ----------------------------------------------------------------------------------------------------------------------

# RPA用画像フォルダの作成---------------------------------------------------------
FolURL = os.getcwd().replace("\\", "/")  # 先
TFolURL = FolURL + r"\RPAPhoto\MJS_SystemNextCreate"  # 先
XLSURL = TFolURL + r"\ミロク更新項目.xlsx"
# --------------------------------------------------------------------------------
Exlsx = EFA.XlsmRead(XLSURL)
if Exlsx[0] is True:
    try:
        dt_now = datetime.datetime.now()
        WriteEx = openpyxl.load_workbook(XLSURL)
        WriteExSheet = WriteEx["更新申請"]
        c = 5
        r = 7
        cn = 8
        WriteExSheet.cell(row=r, column=cn).value = dt_now
        WriteExSheet.cell(row=r, column=c).value = "*"
        print("シート書き込み完了")
        WriteEx.save(XLSURL)
    except:
        traceback.print_exc()
else:
    print("Excel読み込みエラー")
    logger.debug("Excel読み込みエラー")
