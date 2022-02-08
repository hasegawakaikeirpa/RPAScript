#----------------------------------------------------------------------------------------------------------------------
from queue import Empty
from pyparsing import And
#-------------------------------------------------------------------------------------------------------------------------------
def getFileEncoding( file_path ) :#.format( getFileEncoding( "sjis.csv" ) )
    detector = UniversalDetector()
    with open(file_path, mode= "rb" ) as f:
        for binary in f:
            detector.feed( binary )
            if detector.done:
                break
    detector.close()
    return detector.result[ "encoding" ]
#------------------------------------------------------------------------------------------------------------------------------
def CsvPlus(URL,LogList,LogMSG):
    try:
        SerchEnc = format(getFileEncoding(URL))
        df_shape = LogList.shape
        #最終行に追加
        LogList.loc[df_shape[0]] = LogMSG
        pd.DataFrame(LogList).to_csv(URL, encoding = SerchEnc, index = False) 
        return True
    except:
        return False
#------------------------------------------------------------------------------------------------------------------------------- 
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
#例外処理判定の為のtracebackインポート
import traceback
#pandas(pd)で関与先データCSVを取得
import pyautogui
import time
import shutil
import codecs
import pyperclip #クリップボードへのコピーで使用
from collections import OrderedDict
import jaconv
import WarekiHenkan
from chardet.universaldetector import UniversalDetector
import calendar
