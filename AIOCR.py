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
from openpyxl import Workbook, load_workbook
import pprint
from google.cloud import vision
from google.oauth2 import service_account
import io

def APIRead(FolURL,tar,ele):#Arg1 = 画像ファイルのdir,Arg2 = 読取画像,Arg3 = 比較画像 Arg2 - Arg3 のテキストを返す
    # GoogleAPI身元証明書のjson読み込み--------------------------------------------------------------------
    credentials = service_account.Credentials.from_service_account_file(FolURL2 + '/key.json')#GAPIキーのURL
    client = vision.ImageAnnotatorClient(credentials=credentials)
    #client = vision.ImageAnnotatorClient()PCにPath通してるならこっちでも認証可能
    #画像を読込んでテキストを返す
    path = FolURL + "\\" + tar
    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    response = client.text_detection(image=image)
    texts = response.text_annotations
    # OT = '\n"{}"'.format(texts.description)
    x = 0
    for text in texts:
        # OT = '\n"{}"'.format(text.description)
        if x == 0:
            OT = '\n"{}"'.format(text.description)
        x = x + 1
        # vertices = (['({},{})'.format(vertex.x, vertex.y)
        #             for vertex in text.bounding_poly.vertices])
        # print('bounds: {}'.format(','.join(vertices)))

    path = FolURL + "\\" + ele
    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    response = client.text_detection(image=image)
    texts = response.text_annotations
    x = 0
    for text in texts:
        if x == 0:
            ET = '\n"{}"'.format(text.description)
        x = x + 1
    #     print('\n"{}"'.format(text.description))
        # vertices = (['({},{})'.format(vertex.x, vertex.y)
        #             for vertex in text.bounding_poly.vertices])
        # print('bounds: {}'.format(','.join(vertices)))

    if response.error.message:
        raise Exception(
            '{}\nFor more info on error messages, check: '
            'https://cloud.google.com/apis/design/errors'.format(
                response.error.message))

    Final = OT.replace(ET,"")
    return OT,ET,Final

    

#RPA用画像フォルダの作成---------------------------------------------------------
FolURL = "\\\\Sv05121a\\e\\C 作業台\\Ⅰ 課別フォルダ\\和崎課\\01_改善作業資料\\0_情報収集\\医療費集計_202112"#元
#FolURL = FolURL.replace('\\','/')#先
FolURL2 = os.getcwd().replace('\\','/')#先
#--------------------------------------------------------------------------------
tar = "医療費領収書①Split.png"
ele = "医療費領収書①Split雛形.png"
APIRead(FolURL,tar,ele)