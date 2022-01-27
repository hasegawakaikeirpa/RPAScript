#----------------------------------------------------------------------------------------------------------------------
from msilib.schema import File


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
def EraceIMGWait(FolURL2,FileName):
    try:
        while all(pg.locateOnScreen(FolURL2 + "/" + FileName, confidence=0.9)) == True:
            time.sleep(1)
    except:
        print("待機終了")
#----------------------------------------------------------------------------------------------------------------------
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
def FMSOpen(driver,FolURL2,xls_data,KamokuCD,Lday):
    #要素クリック----------------------------------------------------------------------------------------------------------
    Hub = "AutomationID"
    ObjName = "um10PictureButton"
    DriverClick(Hub,ObjName,driver)
    #----------------------------------------------------------------------------------------------------------------------
    FileName = "TodayTitle.png"
    while pg.locateOnScreen(FolURL2 + "/" + FileName, confidence=0.9) is None:
        time.sleep(1)
    pg.press('return')
    pg.press('return')
    pg.write(str(Lday[1]), interval=0.01)#直接SENDできないのでpyautoguiで入力
    pg.press('return')
    conf = 0.9
    LoopVal = 10
    FileName = "TTOK.png"
    ImgClick(FolURL2, FileName, conf, LoopVal)
    time.sleep(3)
    FileName = "BoxMenu.png"
    ImgClick(FolURL2, FileName, conf, LoopVal)
    pg.write('202', interval=0.01)#直接SENDできないのでpyautoguiで入力
    pg.press('return')
    FileName = "KanyoItiWin.png"
    while pg.locateOnScreen(FolURL2 + "/" + FileName, confidence=0.9) is None:
        time.sleep(1)
    conf = 0.9
    LoopVal = 10
    FileName = "KanyoSyatyouTAB.png"
    ImgClick(FolURL2, FileName, conf, LoopVal)
    FileName = "SyatyouOpen.png"
    while pg.locateOnScreen(FolURL2 + "/" + FileName, confidence=0.9) is None:
        time.sleep(1)
#----------------------------------------------------------------------------------------------------------------------
def FindMenu(driver,FolURL2,xls_cd):
    pg.press('f8')
    FileName = "FindTitle.png"
    while pg.locateOnScreen(FolURL2 + "/" + FileName, confidence=0.9) is None:
        time.sleep(1)
    pg.write(xls_cd, interval=0.01)#直接SENDできないのでpyautoguiで入力
    pg.press('return')
    pg.write(xls_cd, interval=0.01)#直接SENDできないのでpyautoguiで入力
    pg.press('return')
    pg.press('f4')
#----------------------------------------------------------------------------------------------------------------------
def FirstAction(driver,FolURL2,xls_cd,xls_name,xls_mn,UpList):
    FindMenu(driver,FolURL2,xls_cd)
    time.sleep(1)
    conf = 0.9
    LoopVal = 10
    FileName = "BoxMenu.png"
    ImgClick(FolURL2, FileName, conf, LoopVal)
    pg.write("1", interval=0.01)#直接SENDできないのでpyautoguiで入力
    pg.press('return')
    pg.press('f4')
    FileName = "HousyuSaimoku.png"
    while pg.locateOnScreen(FolURL2 + "/" + FileName, confidence=0.9) is None:
        time.sleep(1)
    conf = 0.9
    LoopVal = 10
    FileName = "BoxMenu.png"
    ImgClick(FolURL2, FileName, conf, LoopVal)
    pg.write(KamokuCD, interval=0.01)#直接SENDできないのでpyautoguiで入力
    pg.press('return')
    pg.press('return')
    time.sleep(2)
    if KamokuCD == "222":
        pg.keyDown('alt')
        pg.press('down')
        pg.keyUp('alt')
        pg.press('2')
        pg.press('return')
    else:
        pg.keyDown('alt')
        pg.press('down')
        pg.keyUp('alt')
        pg.press('4')
        pg.press('return')
    time.sleep(1)
    pg.press(['return','return','return','return','return','return','return','return'])#一巡目
    time.sleep(1)
    pg.press(['return','return'])#一巡目
    pg.write(xls_mn, interval=0.01)#直接SENDできないのでpyautoguiで入力
    pg.press('return')
    time.sleep(1)
    pg.press('f4')
    pg.press('f4')
    FileName = "InputOK.png"
    while pg.locateOnScreen(FolURL2 + "/" + FileName, confidence=0.9) is None:
        time.sleep(1)
    pg.press('return')
    FileName = "KanyoItiWin.png"
    while pg.locateOnScreen(FolURL2 + "/" + FileName, confidence=0.9) is None:
        time.sleep(1) 
    UpList.append([KamokuCD,xls_cd,xls_name,xls_mn])
    with open(FolURL2 + "/Log/請求入力フロー結果.csv",mode="w",encoding="shift-jis",errors="ignore")as f:
        pd.DataFrame(UpList).to_csv(f)
    #pd.DataFrame(UpList).to_csv(FolURL2 + "/Log/請求入力フロー結果.csv", encoding = "shift-jis")
#----------------------------------------------------------------------------------------------------------------------        
def OuterAction(driver,FolURL2,xls_cd,xls_name,xls_mn,UpList):
    FindMenu(driver,FolURL2,xls_cd)
    time.sleep(1)
    conf = 0.9
    LoopVal = 10
    FileName = "BoxMenu.png"
    ImgClick(FolURL2, FileName, conf, LoopVal)
    pg.write("1", interval=0.01)#直接SENDできないのでpyautoguiで入力
    pg.press('return')
    pg.press('f4')
    FileName = "HousyuSaimoku.png"
    while pg.locateOnScreen(FolURL2 + "/" + FileName, confidence=0.9) is None:
        time.sleep(1)
    conf = 0.9
    LoopVal = 10
    FileName = "BoxMenu.png"
    ImgClick(FolURL2, FileName, conf, LoopVal)
    pg.write(KamokuCD, interval=0.01)#直接SENDできないのでpyautoguiで入力
    pg.press('return')
    pg.press('return')
    time.sleep(2)
    if KamokuCD == "222":
        pg.keyDown('alt')
        pg.press('down')
        pg.keyUp('alt')
        pg.press('2')
        pg.press('return')
    else:
        pg.keyDown('alt')
        pg.press('down')
        pg.keyUp('alt')
        pg.press('4')
        pg.press('return')
    time.sleep(1)
    pg.press(['return','return','return','return','return','return','return','return'])#一巡目
    time.sleep(1)
    pg.press(['return','return'])#一巡目
    pg.write(xls_mn, interval=0.01)#直接SENDできないのでpyautoguiで入力
    pg.press('return')
    time.sleep(1)
    pg.press('f4')
    pg.press('f4')
    FileName = "InputOK.png"
    while pg.locateOnScreen(FolURL2 + "/" + FileName, confidence=0.9) is None:
        time.sleep(1)
    pg.press('return')
    FileName = "KanyoItiWin.png"
    while pg.locateOnScreen(FolURL2 + "/" + FileName, confidence=0.9) is None:
        time.sleep(1) 
    UpList.append([KamokuCD,xls_cd,xls_name,xls_mn])
    with open(FolURL2 + "/Log/請求入力フロー結果.csv",mode="w",encoding="shift-jis",errors="ignore")as f:
        pd.DataFrame(UpList).to_csv(f)
    #pd.DataFrame(UpList).to_csv(FolURL2 + "/Log/請求入力フロー結果.csv", encoding = "shift-jis")
#----------------------------------------------------------------------------------------------------------------------  
def MainFlow(FolURL2,xls_data,KamokuCD,Lday):
    BatUrl = FolURL2 + "/bat/AWADriverOpen.bat"#4724ポート指定でappiumサーバー起動バッチを開く
    driver = OMSOpen.MainFlow(BatUrl,FolURL2,"RPAPhoto")#OMSを起動しログイン後インスタンス化
    FolURL2 = FolURL2 + "/RPAPhoto/TKC_SeikyuuNyuuryoku"
    FMSOpen(driver,FolURL2,xls_data,KamokuCD,Lday)
    UpList = []   
    for index, xls_Item in xls_data.iterrows():
        xls_cd = str(int(xls_Item['ｺｰﾄﾞ']))
        xls_name = xls_Item['関与先名'].replace("\u3000","")
        xls_mn = str(int(xls_Item['先生値決め']))
        if index == 0:
            FirstAction(driver,FolURL2,xls_cd,xls_name,xls_mn,UpList)
        else:
            OuterAction(driver,FolURL2,xls_cd,xls_name,xls_mn,UpList)
        #---------------------------------------------------------------------------------------------------------------------
    print("処理終了")
        
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
import calendar
import pyperclip
from collections import OrderedDict
import tkinter
from tkinter import filedialog

Lday = calendar.monthrange(dt.today().year,dt.today().month)
idir = r'\\Sv05121a\e\特２ 特別\Ⅲ総務\１　総務'
file_path = tkinter.filedialog.askopenfilename(initialdir = idir)
#file_path = file_path.replace("\u3000","\　")
xls_data = pd.read_excel(file_path, sheet_name=0)
print(xls_data)
HeadRow = input("ヘッダー行を指定してください。\n")
xls_data = pd.read_excel(file_path, sheet_name=0,header=int(HeadRow))
print(xls_data)
#--------------------------------------------------------------------------------
KamokuCD = input("科目コードを指定してください。償却資産 = 190 支払調書 = 140\n")
# ColName = input("関与先コードが記載されている列名を入力してください\n")
# MoneyColN = input("値決め金額が記載されている列名を入力してください\n")
#RPA用画像フォルダの作成---------------------------------------------------------
FolURL = "//Sv05121a/e/C 作業台/RPA/ALLDataBase/RPAPhoto/TKC_SeikyuuNyuuryoku"#元
FolURL2 = os.getcwd().replace('\\','/')#先
#--------------------------------------------------------------------------------
try:
    MainFlow(FolURL2,xls_data,KamokuCD,Lday)
except:
    traceback.print_exc()