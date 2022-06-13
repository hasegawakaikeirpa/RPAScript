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

# 例外処理判定の為のtracebackインポート
import traceback

# pandas(pd)で関与先データCSVを取得
import pyautogui
import pyperclip  # クリップボードへのコピーで使用
import Function.ExcelFileAction as EFA
import Function.CSVOut as FCO
import Function.MJSSPOPDFMarge as PDFM
import datetime
import openpyxl
from openpyxl.formatting.rule import Rule
from ctypes import windll

# logger設定------------------------------------------------------------------------------------------------------------
import logging.config

logging.config.fileConfig(r"LogConf\logging_debug.conf")
logger = logging.getLogger(__name__)
# ----------------------------------------------------------------------------------------------------------------------

# RPA用画像フォルダの作成---------------------------------------------------------
FolURL = os.getcwd().replace("\\", "/")  # 先
TFolURL = FolURL + r"\RPAPhoto\MJS_SystemNextCreate"  # 先
CFolURL = FolURL + r"\RPAPhoto\MJS_SystemPrintOut"  # 先
XLSURL = r"\\Sv05121a\e\C 作業台\RPA\RPA_ミロクシステム次年更新\ミロク更新項目.xlsx"
LURL = r"\\Sv05121a\e\C 作業台\RPA\RPA_ミロクシステム次年更新\MJSLog\MJSSysUpLog.txt"  # 処理状況CSVのURL
# --------------------------------------------------------------------------------
Title = str(490) + "_" + str("㈲ムカイハタタイヤ") + "_" + str("R3") + "_決算書.pdf"
PDFM.PDFMarge(
    CFolURL + r"\All\ListNumber.csv",
    CFolURL + r"\PDF",
    Title,
    490,
    "R3",
)
