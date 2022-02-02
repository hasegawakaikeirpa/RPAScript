#----------------------------------------------------------------------------------------------------------------------
def DriverUIWaitXPATH(UIPATH,driver):#XPATH要素を取得するまで待機
    for x in range(1000):
        try:
            driver.find_element_by_xpath(UIPATH)
            Flag = 1
            return True
        except:
            Flag = 0
    if Flag == 0:
        return False
#----------------------------------------------------------------------------------------------------------------------
def DriverUIWaitAutomationId(UIPATH,driver):#XPATH要素を取得するまで待機
    for x in range(1000):
        try:
            driver.find_element_by_accessibility_id(UIPATH)
            Flag = 1
            return True
        except:
            Flag = 0
    if Flag == 0:
        return False
#----------------------------------------------------------------------------------------------------------------------
def DriverUIWaitName(UIPATH,driver):#XPATH要素を取得するまで待機
    for x in range(1000):
        try:
            driver.find_element_by_Name(UIPATH)
            Flag = 1
            return True
        except:
            Flag = 0
    if Flag == 0:
        return False
#----------------------------------------------------------------------------------------------------------------------
def DriverUIWaitclassname(UIPATH,driver):#XPATH要素を取得するまで待機
    for x in range(10000):
        try:
            driver.find_element_by_class_name(UIPATH)
            Flag = 1
            return True
        except:
            Flag = 0
    if Flag == 0:
        return False
#----------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------
def DriverFindClass(UIPATH,driver):#XPATH要素を取得するまで待機
    for x in range(10000):
        try:
            elList = driver.find_elements_by_class_name(UIPATH)
            Flag = 1
            return True,elList
        except:
            Flag = 0
    if Flag == 0:
        return False
#----------------------------------------------------------------------------------------------------------------------
def DriverCheck(Hub,ObjName,driver):#XPATH要素を取得するまで待機
    for x in range(1000):
        if Hub == "AutomationID":
            if DriverUIWaitAutomationId(ObjName,driver) == True:#OMSメニューの年調起動ボタンを判定して初期処理分け
                #正常待機後処理
                OMSObj = driver.find_element_by_accessibility_id(ObjName)#一括電子申告送信ボタン
                return True
            else:
                #異常待機後処理
                print("要素取得に失敗しました。")
        elif Hub == "XPATH":
            if DriverUIWaitXPATH(ObjName,driver) == True:#OMSメニューの年調起動ボタンを判定して初期処理分け
                #正常待機後処理
                OMSObj = driver.find_element_by_xpath(ObjName)#一括電子申告送信ボタン
                return True
            else:
                #異常待機後処理
                print("要素取得に失敗しました。")
        elif Hub == "Name":
            if DriverUIWaitName(ObjName,driver) == True:#OMSメニューの年調起動ボタンを判定して初期処理分け
                #正常待機後処理
                OMSObj = driver.find_element_by_Name(ObjName)#一括電子申告送信ボタン
                return True
            else:
                #異常待機後処理
                print("要素取得に失敗しました。")
#----------------------------------------------------------------------------------------------------------------------
def DriverClick(Hub,ObjName,driver):
    if Hub == "AutomationID":
        if DriverUIWaitAutomationId(ObjName,driver) == True:#OMSメニューの年調起動ボタンを判定して初期処理分け
            #正常待機後処理
            OMSObj = driver.find_element_by_accessibility_id(ObjName)#一括電子申告送信ボタン
            OMSObj.click()
            return OMSObj
        else:
            #異常待機後処理
            print("要素取得に失敗しました。")
    elif Hub == "XPATH":
        if DriverUIWaitXPATH(ObjName,driver) == True:#OMSメニューの年調起動ボタンを判定して初期処理分け
            #正常待機後処理
            OMSObj = driver.find_element_by_xpath(ObjName)#一括電子申告送信ボタン
            OMSObj.click()
            return OMSObj
        else:
            #異常待機後処理
            print("要素取得に失敗しました。")
    elif Hub == "Name":
        if DriverUIWaitName(ObjName,driver) == True:#OMSメニューの年調起動ボタンを判定して初期処理分け
            #正常待機後処理
            OMSObj = driver.find_element_by_Name(ObjName)#一括電子申告送信ボタン
            OMSObj.click()
            return OMSObj
        else:
            #異常待機後処理
            print("要素取得に失敗しました。")
    elif Hub == "class_name":
        if DriverUIWaitclassname(ObjName,driver) == True:#OMSメニューの年調起動ボタンを判定して初期処理分け
            #正常待機後処理
            OMSObj = driver.find_element_by_class_name(ObjName)#一括電子申告送信ボタン
            OMSObj.click()
            return OMSObj
        else:
            #異常待機後処理
            print("要素取得に失敗しました。")
#----------------------------------------------------------------------------------------------------------------------
def ImgCheck(FolURL2,FileName,conf,LoopVal):#画像があればTrueを返す関数
    ImgURL = FolURL2 + "/" + FileName
    for x in range(LoopVal):
        try:
            p = pyautogui.locateOnScreen(ImgURL, confidence=conf)
            x, y = pyautogui.center(p)
            return True,x,y
        except:
            Flag = 0
    if Flag == 0:
        return False,"",""
#----------------------------------------------------------------------------------------------------------------------
def ImgNothingCheck(FolURL2,FileName,conf,LoopVal):#画像がなければTrueを返す
    ImgURL = FolURL2 + "/" + FileName
    for x in range(LoopVal):
        try:
            p = pyautogui.locateOnScreen(ImgURL, confidence=conf)
            x, y = pyautogui.center(p)
            return False
        except:
            Flag = 0
    if Flag == 0:
        return True
#----------------------------------------------------------------------------------------------------------------------
def ImgCheckForList(FolURL2,List,conf):#リスト内の画像があればTrueと画像名を返す
    for x in range(10):
        for ListItem in List:
            ImgURL = FolURL2 + "/" + ListItem
            try:
                p = pyautogui.locateOnScreen(ImgURL, confidence=conf)
                x, y = pyautogui.center(p)
                return True,ListItem
                break
            except:
                Flag = 0
    if Flag == 0:
        return False,""
#----------------------------------------------------------------------------------------------------------------------
def ImgClick(FolURL2,FileName,conf,LoopVal):#画像があればクリックしてx,y軸を返す
    ImgURL = FolURL2 + "/" + FileName
    for x in range(10):
        if ImgCheck(FolURL2,FileName,conf,LoopVal)[0] == True:#OMSメニューの年調起動ボタンを判定して初期処理分け
            #正常待機後処理
            for y in range(10):
                try:
                    p = pyautogui.locateOnScreen(ImgURL, confidence=conf)
                    x, y = pyautogui.center(p)
                    pyautogui.click(x, y)
                    time.sleep(1)
                    return x, y
                except:
                    print("失敗")
        else:
            #異常待機後処理
            print("要素取得に失敗しました。")
#----------------------------------------------------------------------------------------------------------------------
def getFileEncoding( file_path ) :#.format( getFileEncoding( "sjis.csv" ) )
    detector = UniversalDetector()
    with open(file_path, mode= "rb" ) as f:
        for binary in f:
            detector.feed( binary )
            if detector.done:
                break
    detector.close()
    return detector.result[ "encoding" ]
#---------------------------------------------------------------------------------------------------------------------- 
def main():
    ret = getFileEncoding( "sjis.csv" )
    print( "sjis.csv Encoding={0}".format( ret ) )
 
    ret = getFileEncoding( "utf8.csv" )
    print( "utf8.csv Encoding={0}".format( ret ) )
def EraceIMGWait(FolURL2,FileName):
    try:
        while all(pg.locateOnScreen(FolURL2 + "/" + FileName, confidence=0.9)) == True:
            time.sleep(1)
    except:
        print("待機終了")

def CSVOutPut(CSVURL,CSVName,driver,FolURL2):#TKCのCSVダイアログでの書出し操作
    while pg.locateOnScreen(FolURL2 + "/KiridasiWin.png" , confidence=0.99999) is None:
        time.sleep(1)
    #要素クリック----------------------------------------------------------------------------------------------------------
    Hub = "AutomationID"
    ObjName = "outputDirTextBox"
    DriverClick(Hub,ObjName,driver)
    pg.press(['right','right','right','right','right','right','right','right','right'\
        'right','right','right','right','right','right','right','right','right'\
        'right','right','right','right','right','right','right','right','right'\
        'right','right','right','right','right','right','right','right','right'\
        'right','right','right','right','right','right','right','right','right'\
        'right','right','right','right','right','right','right','right','right'\
        'right','right','right','right','right','right','right','right','right'\
        'right','right','right','right','right','right','right','right','right'\
        'right','right','right','right','right','right','right','right','right'])
    pg.press(['backspace','backspace','backspace','backspace','backspace','backspace','backspace','backspace','backspace'\
        'backspace','backspace','backspace','backspace','backspace','backspace','backspace','backspace','backspace'\
        'backspace','backspace','backspace','backspace','backspace','backspace','backspace','backspace','backspace'\
        'backspace','backspace','backspace','backspace','backspace','backspace','backspace','backspace','backspace'\
        'backspace','backspace','backspace','backspace','backspace','backspace','backspace','backspace','backspace'\
        'backspace','backspace','backspace','backspace','backspace','backspace','backspace','backspace','backspace'\
        'backspace','backspace','backspace','backspace','backspace','backspace','backspace','backspace','backspace'\
        'backspace','backspace','backspace','backspace','backspace','backspace','backspace','backspace','backspace'\
        'backspace','backspace','backspace','backspace','backspace','backspace','backspace','backspace','backspace'])
    pg.write(CSVURL, interval=0.01)#直接SENDできないのでpyautoguiで入力
    #----------------------------------------------------------------------------------------------------------------------
    #要素クリック----------------------------------------------------------------------------------------------------------
    Hub = "AutomationID"
    ObjName = "fileNameTextBox"
    DriverClick(Hub,ObjName,driver)
    pg.press(['right','right','right','right','right','right','right','right','right'\
        'right','right','right','right','right','right','right','right','right'\
        'right','right','right','right','right','right','right','right','right'\
        'right','right','right','right','right','right','right','right','right'\
        'right','right','right','right','right','right','right','right','right'\
        'right','right','right','right','right','right','right','right','right'\
        'right','right','right','right','right','right','right','right','right'\
        'right','right','right','right','right','right','right','right','right'\
        'right','right','right','right','right','right','right','right','right'])
    pg.press(['backspace','backspace','backspace','backspace','backspace','backspace','backspace','backspace','backspace'\
        'backspace','backspace','backspace','backspace','backspace','backspace','backspace','backspace','backspace'\
        'backspace','backspace','backspace','backspace','backspace','backspace','backspace','backspace','backspace'\
        'backspace','backspace','backspace','backspace','backspace','backspace','backspace','backspace','backspace'\
        'backspace','backspace','backspace','backspace','backspace','backspace','backspace','backspace','backspace'\
        'backspace','backspace','backspace','backspace','backspace','backspace','backspace','backspace','backspace'\
        'backspace','backspace','backspace','backspace','backspace','backspace','backspace','backspace','backspace'\
        'backspace','backspace','backspace','backspace','backspace','backspace','backspace','backspace','backspace'\
        'backspace','backspace','backspace','backspace','backspace','backspace','backspace','backspace','backspace'])
    pg.write(CSVName, interval=0.01)#直接SENDできないのでpyautoguiで入力
    #----------------------------------------------------------------------------------------------------------------------
    #要素クリック----------------------------------------------------------------------------------------------------------
    Hub = "AutomationID"
    ObjName = "fileTypeComboBox"
    DriverClick(Hub,ObjName,driver)
    pg.press('down')
    pg.press('down')
    pg.press('down')
    pg.press('return')
    #----------------------------------------------------------------------------------------------------------------------
    #要素クリック----------------------------------------------------------------------------------------------------------
    Hub = "AutomationID"
    ObjName = "saveButton"
    CsvPath = CSVURL + "/" + CSVName + ".CSV"
    if os.path.isfile(CsvPath) == True:
        DriverClick(Hub,ObjName,driver)
        time.sleep(1)
        FileNameList = ["FileOverQ.png","FileOverQ2.png"]
        conf = 0.9
        LoopVal = 10
        if ImgCheckForList(FolURL2,FileNameList,conf)[0] == True:
            pg.press('y')
    else:
        DriverClick(Hub,ObjName,driver)
        time.sleep(1)
#----------------------------------------------------------------------------------------------------------------------
def SortCSVItem(C_Child,Col1,Col2,Col3,Col4,Key):#CSVと列名を4つ与えて4つの複合と引数Keyが一致する行数を返す
        #切出CSVをループ処理-------------------------------------------------------------------------------------------------------
    C_CforCount = 0
    C_CdfRow = np.array(C_Child).shape[0]#配列行数取得
    C_CdfCol = np.array(C_Child).shape[1]#配列列数取得
    ItemList = []
    for y in range(C_CdfRow):
        #関与先DB配列をループして識別番号とPassを取得
        C_CdfDataRow = C_Child.loc[y]
        C_CSCode = C_CdfDataRow[Col1]
        C_CName = C_CdfDataRow[Col2]
        C_CZeimoku = C_CdfDataRow[Col3]
        C_CSousin = C_CdfDataRow[Col4]
        C_CAll = str(C_CSCode) + str(C_CName) 
        if Key == C_CAll and C_CSousin == "済":
            ItemList.append(C_CforCount)
            C_CforCount = C_CforCount + 1
        else:
            C_CforCount = C_CforCount + 1
    return ItemList
#----------------------------------------------------------------------------------------------------------------------
def SortPDF(PDFName):
    Fol = str(dt.today().year) + "-" + str(dt.today().month)
    pt = "\\\\Sv05121a\\e\\電子ファイル\\メッセージボックス\\" + Fol + "\\送信分受信通知"
    #path = path.replace('\\','/')#先
    PDFFileList = os.listdir(pt)
    Cou = 1
    for PDFItem in PDFFileList:
        PDFName = PDFName.replace("\u3000","").replace("PDF","") .replace("pdf","")  
        PDFItem = PDFItem.replace("\u3000","").replace("PDF","") .replace("pdf","")  
        if PDFName in PDFItem:
            Cou = Cou + 1
    return str(Cou),pt
#----------------------------------------------------------------------------------------------------------------------
def MainFlow(FolURL2):
    BatUrl = FolURL2 + "/bat/AWADriverOpen.bat"#4724ポート指定でappiumサーバー起動バッチを開く
    driver = OMSOpen.MainFlow(BatUrl,FolURL2,"RPAPhoto")#OMSを起動しログイン後インスタンス化
    FolURL2 = FolURL2 + "/RPAPhoto/TKC_KoukaikeiTimetabulation"
    time.sleep(1)
    # while pg.locateOnScreen(FolURL2 + "/KiridasiWin.png" , confidence=0.99999) is None:
    #     time.sleep(1)
    ImgClick(FolURL2, "TMSOpen.png", 0.9, 2)
    while pg.locateOnScreen(FolURL2 + "/GyoumuBunsekiBtn.png" , confidence=0.9) is None:
        time.sleep(1)
    time.sleep(1)
    ImgClick(FolURL2, "GyoumuBunsekiBtn.png", 0.9, 2)
    while pg.locateOnScreen(FolURL2 + "/GyoumuBunsekiWin.png" , confidence=0.9) is None:
        time.sleep(1)
    time.sleep(1)
    pg.press('f7')
    time.sleep(1)
    while pg.locateOnScreen(FolURL2 + "/SiteiKikanStr.png" , confidence=0.9) is None:
        time.sleep(1)
    time.sleep(1)
    ImgClick(FolURL2, "SiteiKikanOKBtn.png", 0.9, 2)
    time.sleep(1)
#----------------------------------------------------------------------------------------------------------------------

#モジュールインポート
from appium import webdriver
import subprocess
from subprocess import run
from subprocess import PIPE
import pyautogui as pg
import time
import OMSOpen
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
from datetime import datetime, timedelta
import pyperclip #クリップボードへのコピーで使用
import WarekiHenkan #WarekiHenkan.SeirekiDate("R",4,1,19) = 返り値2022/1/19(str)
import sys
from tkinter import messagebox
import chardet
from chardet.universaldetector import UniversalDetector

#RPA用画像フォルダの作成---------------------------------------------------------
FolURL = "//Sv05121a/e/C 作業台/RPA/ALLDataBase/RPAPhoto/TKC_KoukaikeiTimetabulation"#元
#FolURL2 = os.getcwd().replace('\\','/') + "/TKC_DensiSinkoku"#先
FolURL2 = os.getcwd().replace('\\','/')#先
#--------------------------------------------------------------------------------
try:
    MainFlow(FolURL2)
except:
    traceback.print_exc()