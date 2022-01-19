#-----------------------------------------------------------------------------------------------------------------------------------------------------
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
#seleniumインポート
from selenium import webdriver
from selenium.webdriver.chrome.options import Options#ブラウザオプションを与える
from selenium.webdriver.common.keys import Keys#センドキーコマンドを与える
from selenium.webdriver.common.action_chains import ActionChains#JavaScript実行の為にActionChainsコマンドを与える
from selenium.webdriver.support.ui import WebDriverWait#読込待機コマンドを与える
from selenium.webdriver.support import expected_conditions as EC#読込待機コマンドに条件式を与える
#jsonインポート
import json
#osインポート
import os
#datetimeインポート
from datetime import datetime as dt
#glob(フォルダファイルチェックコマンド)インポート
import glob
#shutil(フォルダファイル編集コマンド)インポート
import shutil
#例外処理判定の為のtracebackインポート
import traceback
import codecs
#pandas(pd)で関与先データCSVを取得
H_url = '//Sv05121a/e/C 作業台/RPA/ALLDataBase/Heidi関与先DB.csv'
H_df = pd.read_csv(H_url,encoding='utf-8')
H_Murl = '//Sv05121a/e/C 作業台/RPA/公会計時間分析/公会計名簿.csv'
H_Mdf = pd.read_csv(H_Murl,encoding='utf-8')
H_forCount = 0
tdy = dt.today()
H_dfRow = np.array(H_df).shape[0]#配列行数取得
H_dfCol = np.array(H_df).shape[1]#配列列数取得
OKLog = []
NGLog = []
Toyear = str(tdy.year)
for x in range(12):
    H_Marges = []
    s = format(x + 1, '02') 
    dir_path = "//Sv05121a/e/C 作業台/RPA/公会計時間分析/" + Toyear + "-" + s
    Tan_path = dir_path + "/担当者別"
    for current_dir, sub_dirs, files_list in os.walk(Tan_path):
        for fileobj in files_list:
            fileurl = Tan_path + "/" + fileobj.replace('\u3000', '　')#空白\u3000を置換 
            with codecs.open(fileurl,mode ="r", encoding= "cp932",errors="ignore") as file:
                H_df = pd.read_table(file,delimiter=",")

                H_forCount = 0
                H_dfRow = np.array(H_df).shape[0]#配列行数取得
                H_MdfRow = np.array(H_Mdf).shape[0]#配列行数取得
                H_dfCol = np.array(H_df).shape[1]#配列列数取得
                for x in range(H_dfRow):
                    try:
                        if x >= 0 and not x == H_dfRow - 1 :

                            if not fileobj == "移動時間.CSV": 
                                H_dfDataRow = H_df.loc[x]
                                H_Tan = fileobj.split("_")
                                H_Kanyo = H_Tan[0]
                                H_TTan = H_Tan[1]
                                H_TTan = H_TTan.replace('.CSV','').replace('\u3000', '　').replace('\u200b', '　').replace(' ', '　')#空白\u3000を置換
                                for y in range(H_MdfRow):
                                    H_MdfDataRow = H_Mdf.loc[y]
                                    T = H_MdfDataRow["氏名"].replace('\u3000', '　').replace('\u200b', '　').replace(' ', '　')
                                    if  T == H_TTan:
                                        H_Katudou = H_dfDataRow["活動"]
                                        H_Tougetu = str(H_dfDataRow["当  月(A)"])
                                        H_ZDougetu = H_dfDataRow["前年同月(B)"]
                                        CSVWriteRow = "" + H_TTan + "","" + H_Kanyo + "","" + H_Katudou + "","" + H_Tougetu + ""
                                        H_Marges.append(CSVWriteRow)
                                        break
                            else:
                                H_dfDataRow = H_df.loc[x]
                                H_Kanyo = "移動時間"
                                H_TTan = H_dfDataRow["担当者"].replace('\u3000', '　').replace('\u200b', '　').replace(' ', '　')#空白\u3000を置換
                                for y in range(H_MdfRow):
                                    H_MdfDataRow = H_Mdf.loc[y]
                                    T = H_MdfDataRow["氏名"].replace('\u3000', '　').replace('\u200b', '　').replace(' ', '　') 
                                    if  T == H_TTan:
                                        H_Katudou = "移動時間"
                                        H_Tougetu = H_dfDataRow["当  月(A)"]
                                        H_ZDougetu = H_dfDataRow["前年同月(B)"]
                                        CSVWriteRow = "" + H_TTan + "","" + H_Kanyo + "","" + H_Katudou + "","" + H_Tougetu + ""
                                        H_Marges.append(CSVWriteRow)
                                        break
                    except:
                        pass
        try:
            H_MargesRow = np.array(H_Marges).shape[0]#配列行数取得
            if H_MargesRow > 0:
                df = pd.DataFrame(H_Marges)
                df.columns = ["氏名","関与先","活動","当  期(A)"]
                pd.DataFrame(df).to_csv(dir_path + "/BACKUP/集計表.csv",index = False, encoding = "shift-jis")
        except:
            pass