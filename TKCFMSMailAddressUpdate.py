#----------------------------------------------------------------------------------------------------------------------
from turtle import down

from sqlalchemy import false


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
def FMSOpen(FolURL2,Lday,driver):
    try:
        #要素クリック----------------------------------------------------------------------------------------------------------
        Hub = "AutomationID"
        ObjName = "um10PictureButton"
        DriverClick(Hub,ObjName,driver)
        #----------------------------------------------------------------------------------------------------------------------
        FileName = "TodayTitle.png"
        while pg.locateOnScreen(FolURL2 + "/" + FileName, confidence=0.9) is None:
            time.sleep(2)
        pg.press('return')
        pg.press('return')
        pg.write(str(Lday[1]), interval=0.01)#直接SENDできないのでpyautoguiで入力
        pg.press('return')
        conf = 0.9
        LoopVal = 10
        FileName = "TTOK.png"
        ImgClick(FolURL2, FileName, conf, LoopVal)
        time.sleep(3)
        conf = 0.8
        FileName = "BoxMenu.png"
        ImgClick(FolURL2, FileName, conf, LoopVal)
        pg.write('671', interval=0.01)#直接SENDできないのでpyautoguiで入力
        pg.press('return')
        FileName = "KanyoItiWin.png"
        while pg.locateOnScreen(FolURL2 + "/" + FileName, confidence=0.9) is None:
            time.sleep(1)
        while pg.locateOnScreen(FolURL2 + "/KanyoTAB.png" , confidence=0.99999) is None:
            time.sleep(1)    
            ImgClick(FolURL2, "KanyoSyatyouTAB.png", 0.9, 10)
        time.sleep(2)
        ImgClick(FolURL2, "FileOut.png", 0.9, 10)
        time.sleep(2)
        Kiri = ImgCheck(FolURL2, "Kiridasi.png", 0.9, 10)
        pg.click(Kiri[1] -200,Kiri[2])
        time.sleep(1)
        pg.keyDown('ctrl')
        pg.press(['right','right','right','right','right','right','right','right','right','right'])
        pg.keyUp('ctrl')
        #テキストボックスを削除-------------------------------------------------------------------
        time.sleep(1)
        while pg.locateOnScreen(FolURL2 + "/KiridasiBox.png",confidence=0.99999) is None:
            pg.press(['backspace','backspace','backspace','backspace','backspace','backspace','backspace','backspace','backspace','backspace'])
        time.sleep(1)
        #--------------------------------------------------------------------------------------
        KFol = FolURL2.replace("/","\\")
        pyperclip.copy(KFol)
        pg.hotkey('ctrl', 'v')#pg日本語不可なのでコピペ
        pg.press(['return'])
        time.sleep(1)
        pg.press(['delete'])
        pg.write("MailList.CSV")
        pg.press(['return'])
        time.sleep(1)
        pg.press(['return'])
        time.sleep(1)
        pg.keyDown('alt')
        pg.press('down')
        pg.keyUp('alt')
        time.sleep(1)
        pg.press(['down','down','down','down','down'])
        pg.press(['return'])
        time.sleep(1)
        ImgClick(FolURL2,"Hozon.png",0.9,5)
        while pg.locateOnScreen(FolURL2 + "/FileOverSTR.png", confidence=0.9) is not None:
            time.sleep(1)
            FOS = ImgCheck(FolURL2,"FileOverSTR.png",0.9,3)
            if FOS[0] == True:
                pg.press('y')
                break
        time.sleep(1)
        ImgClick(FolURL2,"KanyoTAB.png",0.9,3)
        while pg.locateOnScreen(FolURL2 + "/KanyoTAB.png", confidence=0.9) is not None:
            time.sleep(1)
        while pg.locateOnScreen(FolURL2 + "/SelectTab.png", confidence=0.99999) is None:
            time.sleep(1)
            ImgClick(FolURL2,"KanyoSyatyouTAB.png",0.9,5) 
            time.sleep(1)
            ImgClick(FolURL2,"TargetSelectTab.png",0.9,5) 
            time.sleep(1)
        time.sleep(1)
        pg.press('tab')
        return True
    except:
        return False
#----------------------------------------------------------------------------------------------------------------------
def FirstAction(FolURL2,CSVURL,ws,driver):
    time.sleep(2)
    LenRow = np.array(ws).shape[0]#配列行数取得
    for x in range(LenRow):
        wsRow = ws.iloc[x]
        wsNo = wsRow['コード']
        time.sleep(1)
        print(wsNo)
        TRow = CSVOut.CsvSortRow(CSVURL,"関与先コード",wsNo,'int')
        if TRow[0] == True:
            TRowPer = TRow[1]
            if TRowPer >= 19:
                PDV = int(TRowPer/19)
                for y in range(PDV):
                    pg.press('pagedown')
                time.sleep(1)
                PDA = int(TRowPer - (PDV*19))
                for y in range(PDA):
                    pg.press('down')
                time.sleep(1)
                FMSAction(FolURL2,wsRow,PDV)                
            else:
                for y in range(TRowPer):
                    pg.press('down')
                time.sleep(1)
                FMSAction(FolURL2,wsRow,0)
#---------------------------------------------------------------------------------------------------------------------- 
def FMSAction(FolURL2,wsRow,PDV):
    wscd = wsRow['コード']
    wsName = wsRow['関与先名']
    wsAd = wsRow['アドレス']
    wsHassou = wsRow['発送方法']
    wsNyuu = wsRow['入力日時']
    wsUser = wsRow['入力ユーザー']
    wsDno = wsRow['データNo']
    ImgClick(FolURL2,"Syuusei.png",0.9,1)
    while pg.locateOnScreen(FolURL2 + "/Syuusei.png",0.9) is not None:
        time.sleep(1)
    if wsHassou == "メール":
        ICF = ImgCheck(FolURL2,"MailCheckBox.png",0.9,1)
        if ICF[0] == True:
            ImgClick(FolURL2,"MailCheckBox.png",0.9,1)
        IPF = ImgCheck(FolURL2,"KanyoSeikyuCheck.png",0.9,1)
        if IPF[0] == True:
            ImgClick(FolURL2,"KanyoSeikyuCheck.png",0.9,1)
        ImgClick(FolURL2,"ToKubun.png",0.9,1)
        time.sleep(1)
        pg.press('t')
        time.sleep(1)
        pg.press('return')
        time.sleep(1)
        ImgClick(FolURL2,"EmailCopy.png",0.9,1)
        time.sleep(1)
        ImgClick(FolURL2,"NyuuryokuEnd.png",0.9,1)
        time.sleep(1)
        while pg.locateOnScreen(FolURL2 + "/Kakunin.png",0.9) is None:
            time.sleep(1)
        time.sleep(1)
        pg.press('y')
        while pg.locateOnScreen(FolURL2 + "/EndFlag.png",0.9) is not None:
            time.sleep(1)
        for x in range(PDV + 1):
            pg.press('pageup')
        time.sleep(1)
    else:
        ICF = ImgCheck(FolURL2,"InsatuCheckBox.png",0.9,1)
        if ICF[0] == True:
            ImgClick(FolURL2,"InsatuCheckBox.png",0.9,1)
        ImgClick(FolURL2,"ToKubun.png",0.9,1)
        time.sleep(1)
        pg.press('t')
        time.sleep(1)
        pg.press('return')
        time.sleep(1)
        ImgClick(FolURL2,"EmailCopy.png",0.9,1)
        time.sleep(1)
        ImgClick(FolURL2,"NyuuryokuEnd.png",0.9,1)
        time.sleep(1)
        while pg.locateOnScreen(FolURL2 + "/Kakunin.png",0.9) is None:
            time.sleep(1)
        time.sleep(1)
        pg.press('y')
        while pg.locateOnScreen(FolURL2 + "/EndFlag.png",0.9) is not None:
            time.sleep(1)
        for x in range(PDV + 1):
            pg.press('pageup')
        time.sleep(1)      
#----------------------------------------------------------------------------------------------------------------------     
def MainFlow(FolURL2):
    BatUrl = FolURL2 + "/bat/AWADriverOpen.bat"#4724ポート指定でappiumサーバー起動バッチを開く
    driver = OMSOpen.MainFlow(BatUrl,FolURL2,"RPAPhoto")#OMSを起動しログイン後インスタンス化
    FolURL2 = FolURL2 + "/RPAPhoto/TKCFMSMailAddressUpdate"
    XlsmURL = "\\Sv05121a\e\C 作業台\請求書メールアドレス収集\アドレス新規登録シート.xlsm"
    XlsmURL = XlsmURL.replace("\\","/")
    XlsmURL = "/" + XlsmURL
    XlsmList = EF.XlsmRead(XlsmURL)
    input_book = XlsmList[1]
    #sheet_namesメソッドでExcelブック内の各シートの名前をリストで取得できる
    input_sheet_name = input_book.sheet_names
    #lenでシートの総数を確認
    num_sheet = len(input_sheet_name)
    #シートの数とシートの名前のリストの表示
    print ("Sheet の数:", num_sheet)
    print (input_sheet_name)
    x = 0
    for isnItem in input_sheet_name:
        if isnItem == 'アドレス登録':
            ws = input_book.parse(input_sheet_name[x])
            print(ws)
            break
        x = x + 1
    ws = ws.sort_values('入力日時', ascending=False)
    ws = ws.drop_duplicates(subset='コード')
    print(ws)
    FMSO = FMSOpen(FolURL2,Lday,driver)
    if FMSO == True:
        FirstAction(FolURL2,FolURL2 + "/MAILLIST.CSV",ws,driver)
    else:
        print('FMSログイン失敗')
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
import CSVOut
import ExcelFileAction as EF
import calendar
import pyperclip #クリップボードへのコピーで使用
#RPA用画像フォルダの作成-----------------------------------------------------------
Lday = calendar.monthrange(dt.today().year,dt.today().month)
FolURL = "//Sv05121a/e/C 作業台/RPA/ALLDataBase/RPAPhoto/TKC_DensiSinkoku"#元
FolURL2 = os.getcwd().replace('\\','/')#先
#--------------------------------------------------------------------------------
try:
    MainFlow(FolURL2)
except:
    traceback.print_exc()