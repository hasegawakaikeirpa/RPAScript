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

#出力したCSVを読込み----------------------------------------------------------------------------------------------------------
CSVURL = 'D:\PythonScript\RPAScript\RPAPhoto\MJS_DensiSinkoku'
CSVName = '/SyomeiMaster'
#C_url = CSVURL.replace("\\","/") + '/' + CSVName + '.CSV'
C_url = CSVURL + '/' + CSVName + '.CSV'
with codecs.open(C_url, "r", "Shift-JIS", "ignore") as file:
    C_df = pd.read_table(file, delimiter=",")
print(C_df)
C_df=C_df.drop_duplicates(subset=['顧問先コード', '税目','申告種類'])
C_df=C_df.drop_duplicates(inplace=True)
print(C_df)
C_dfRow = np.array(C_df).shape[0]#配列行数取得
C_dfCol = np.array(C_df).shape[1]#配列列数取得
ItemList = []
time.sleep(1)