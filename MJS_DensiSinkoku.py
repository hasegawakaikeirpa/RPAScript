#----------------------------------------------------------------------------------------------------------------------
def DriverUIWaitXPATH(UIPATH,driver):#XPATH要素を取得するまで待機
    for x in range(10000):
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
    for x in range(10000):
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
    for x in range(10000):
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
    for x in range(10000):
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
        elif Hub == "LOOP":
            if DriverUILoop(ObjName,driver) == True:#OMSメニューの年調起動ボタンを判定して初期処理分け
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
        return False
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
    for x in range(100):
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
        return False
#----------------------------------------------------------------------------------------------------------------------
def ImgClick(FolURL2,FileName,conf,LoopVal):#画像があればクリックしてx,y軸を返す
    ImgURL = FolURL2 + "/" + FileName
    for x in range(10000):
        if ImgCheck(FolURL2,FileName,conf,LoopVal)[0] == True:#OMSメニューの年調起動ボタンを判定して初期処理分け
            #正常待機後処理
            for y in range(10000):
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
def SortCSVItem(SortURL,SortName,Key):#CSVと列名を4つ与えて4つの複合と引数Keyが一致する行数を返す
    Sort_url = SortURL.replace("\\","/") + '/' + SortName + '.CSV'
    with codecs.open(Sort_url, "r", "Utf-8", "ignore") as file:
        C_Child = pd.read_table(file, delimiter=",")
    C_CforCount = 0
    for C_ChildItem in C_Child:
        if Key == C_ChildItem:
            return C_CforCount
        else:
            C_CforCount = C_CforCount + 1

def MainFlow(FolURL2):
    BatUrl = "D:/bat/AWADriverOpen.bat"#4724ポート指定でappiumサーバー起動バッチを開く
    driver = MJSOpen.MainFlow(BatUrl)#OMSを起動しログイン後インスタンス化
    #----------------------------------------------------------------------------------------------------------------------
    #画像が出現するまで待機してクリック------------------------------------------------------------------------------------
    List = ["DensiSinkokuIcon.png","DensiSinkokuIcon2.png"]
    conf = 0.9#画像認識感度
    LoopVal = 10000#検索回数
    ListCheck = ImgCheckForList(FolURL2,List,conf)#画像検索関数
    if ListCheck[0] == True:
        ImgClick(FolURL2,ListCheck[1],conf,LoopVal)
        time.sleep(1)
        pg.keyDown('alt')
        pg.press('a')
        pg.keyUp('alt')
    time.sleep(1)
    #----------------------------------------------------------------------------------------------------------------------
    #画像が出現するまで待機してクリック------------------------------------------------------------------------------------
    List = ["DensiKaiteiClose.png","DensiKaiteiClose2.png"]
    conf = 0.9#画像認識感度
    LoopVal = 10000#検索回数
    ListCheck = ImgCheckForList(FolURL2,List,conf)#画像検索関数
    if ListCheck[0] == True:
        ImgClick(FolURL2,ListCheck[1],conf,LoopVal)
        time.sleep(1)
    time.sleep(1)
    #----------------------------------------------------------------------------------------------------------------------
    #画像が出現するまで待機してクリック------------------------------------------------------------------------------------
    List = ["DensiKidouIcon.png","DensiKidouIcon2.png"]
    conf = 0.9#画像認識感度
    LoopVal = 10000#検索回数
    ListCheck = ImgCheckForList(FolURL2,List,conf)#画像検索関数
    if ListCheck[0] == True:
        ImgClick(FolURL2,ListCheck[1],conf,LoopVal)
        time.sleep(1)
    time.sleep(1)
    #----------------------------------------------------------------------------------------------------------------------
    ImgClick(FolURL2,"DensiSyomei.png",conf,LoopVal)#電子申告・申請タブを押す
    #画像が出現するまで待機してクリック------------------------------------------------------------------------------------
    List = ["DensiSyomeiOpen.png","DensiSyomeiOpen2.png"]
    conf = 0.9#画像認識感度
    LoopVal = 10000#検索回数
    ListCheck = ImgCheckForList(FolURL2,List,conf)#画像検索関数
    if ListCheck[0] == True:
        ImgClick(FolURL2,ListCheck[1],conf,LoopVal)
        time.sleep(1)
    time.sleep(1)
    #----------------------------------------------------------------------------------------------------------------------
    #pg.keyDown('alt')
    #pg.press('p')
    #pg.keyUp('alt')
    #time.sleep(1)
    ##画像が出現するまで待機してクリック------------------------------------------------------------------------------------
    #List = ["FileOut.png","FileOut2.png"]
    #conf = 0.9#画像認識感度
    #LoopVal = 10000#検索回数
    #ListCheck = ImgCheckForList(FolURL2,List,conf)#画像検索関数
    #if ListCheck[0] == True:
    #    ImgClick(FolURL2,ListCheck[1],conf,LoopVal)
    #    time.sleep(1)
    #time.sleep(1)
    #----------------------------------------------------------------------------------------------------------------------
    #↓MJSの印刷設定を保存しているのでコメントアウト
    ##クラス要素クリック----------------------------------------------------------------------------------------------------------
    #Hub = "class_name"
    #ObjName = "TdxImageComboBox"
    #ClassList = DriverFindClass(ObjName,driver)
    #ClassObjList = ClassList[1]
    #ClassObjList[2].click()
    #pg.press(['up','up','up','up','up'])
    #pg.press(['return'])
    ##----------------------------------------------------------------------------------------------------------------------
    #FileURL = FolURL2.replece('/','\\') + "\SyomeiMaster.CSV"
    #pg.write(FileURL, interval=0.01)#直接SENDできないのでpyautoguiで入力
    #pg.press(['return'])
    ##----------------------------------------------------------------------------------------------------------------------
    
    
    #ImgClick(FolURL2,"FileOutPutBtn.png",conf,LoopVal)
    #FileName = "FileOverCheck.png"
    #conf = 0.9#画像認識感度
    #LoopVal = 10000#検索回数
    #if ImgNothingCheck(FolURL2,FileName,conf,LoopVal) == True:#画像がなければTrueを返す
    #    pg.keyDown('alt')
    #    pg.press('j')
    #    pg.keyUp('alt')
    #    time.sleep(1)
    #    pg.keyDown('alt')
    #    pg.press('g')
    #    pg.keyUp('alt')
    #    time.sleep(1)
    #else:
    #    pg.press('y')
    #    time.sleep(1)
    #    pg.keyDown('alt')
    #    pg.press('j')
    #    pg.keyUp('alt')
    #    time.sleep(1)

    pg.keyDown('alt')
    pg.press('j')
    pg.keyUp('alt')

    #出力したCSVを読込み----------------------------------------------------------------------------------------------------------
    CSVURL = 'D:\RPAPhoto\MJS_DensiSinkoku'
    CSVName = '電子申告データ署名一覧'
    C_url = CSVURL.replace("\\","/") + '/' + CSVName + '.csv'
    with codecs.open(C_url, "r", "Shift-JIS", "ignore") as file:
        C_df = pd.read_table(file, delimiter=",")
    C_dfRow = np.array(C_df).shape[0]#配列行数取得
    C_dfCol = np.array(C_df).shape[1]#配列列数取得
    ItemList = []
    time.sleep(1)
    #クラス要素クリック----------------------------------------------------------------------------------------------------------
    for y in range(C_dfRow):
        #CSV要素取得-------------------------------------------------------------------------------------------------------------
        C_dfDataRow = C_df.loc[y]
        C_SCode = str(C_dfDataRow["顧問先コード"])
        C_Name = str(C_dfDataRow["顧問先名称"])
        C_Nendo = str(C_dfDataRow["年度"])
        C_Zeimoku = str(C_dfDataRow["税目"])
        C_Syurui = str(C_dfDataRow["申告種類"])
        #------------------------------------------------------------------------------------------------------------------------
        Hub = "class_name"
        ObjName = "TMNumEdit"#関与先コードボックス
        DriverClick(Hub,ObjName,driver)
        pg.write(C_SCode, interval=0.01)#直接SENDできないのでpyautoguiで入力
        pg.press(['return'])
        #クラス要素クリック----------------------------------------------------------------------------------------------------------
        Hub = "class_name"
        ObjName = "TMDateEdit"
        ClassList = DriverFindClass(ObjName,driver)
        ClassObjList = ClassList[1]
        ClassObjList[3].click()
        pg.write(C_Nendo, interval=0.01)#直接SENDできないのでpyautoguiで入力
        pg.press(['return'])
        pg.write(C_Nendo, interval=0.01)#直接SENDできないのでpyautoguiで入力
        pg.press(['return'])
        #----------------------------------------------------------------------------------------------------------------------
        pg.press(['right'])
        pg.press(['right'])
        pg.press(['tab'])
        time.sleep(1)
        #----------------------------------------------------------------------------------------------------------------------
        SortURL = 'D:\RPAPhoto\MJS_DensiSinkoku\ミロク税目分岐'
        ZeimokuRow = SortCSVItem(SortURL,"Master",C_Zeimoku)
        for x in range(ZeimokuRow):
            pg.press(['down'])
        pg.press(['space'])
        pg.press(['down'])
        time.sleep(1)
        SortURL = 'D:\RPAPhoto\MJS_DensiSinkoku\ミロク税目分岐'
        ZeimokuRow = SortCSVItem(SortURL,C_Zeimoku,C_Syurui)
        for x in range(ZeimokuRow):
            pg.press(['down'])
        pg.press(['space'])
        time.sleep(1)
        #クラス要素クリック----------------------------------------------------------------------------------------------------------
        Hub = "class_name"
        ObjName = "TMBitBtn"#関与先コードボックス
        ClassList = DriverFindClass(ObjName,driver)
        ClassObjList = ClassList[1]
        ClassObjList[1].click()
        #----------------------------------------------------------------------------------------------------------------------
        time.sleep(1)
        #画像が出現するまで待機してクリック------------------------------------------------------------------------------------
        List = ["FindCheckBox.png","FindCheckBox2.png","FindCheckBox3.png"]
        conf = 0.9#画像認識感度
        LoopVal = 10000#検索回数
        ListCheck = ImgCheckForList(FolURL2,List,conf)#画像検索関数
        if ListCheck[0] == True:
            ImgClick(FolURL2,ListCheck[1],conf,LoopVal)
            time.sleep(1)
        time.sleep(1)
        #----------------------------------------------------------------------------------------------------------------------





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
#RPA用画像フォルダの作成---------------------------------------------------------
FolURL = "//Sv05121a/e/C 作業台/RPA/ALLDataBase/RPAPhoto/MJS_DensiSinkoku"#元
FolURL2 = "D:/RPAPhoto/MJS_DensiSinkoku"#先
try:
    shutil.copytree(FolURL,FolURL2)
except:
    print(FolURL2 + "あります。")
#--------------------------------------------------------------------------------
try:
    MainFlow(FolURL2)
except:
    traceback.print_exc()