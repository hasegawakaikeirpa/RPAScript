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

def MainFlow(FolURL2):
    BatUrl = FolURL2 + "/bat/AWADriverOpen.bat"#4724ポート指定でappiumサーバー起動バッチを開く
    driver = OMSOpen.MainFlow(BatUrl,FolURL2,"RPAPhoto")#OMSを起動しログイン後インスタンス化
    FolURL2 = FolURL2 + "/RPAPhoto/TKC_DensiSinkoku"
    #----------------------------------------------------------------------------------------------------------------------
    #要素クリック----------------------------------------------------------------------------------------------------------
    Hub = "AutomationID"
    ObjName = "um12PictureButton"
    DriverClick(Hub,ObjName,driver)#一括電子申告ボタンを押す
    #----------------------------------------------------------------------------------------------------------------------
    #要素クリック----------------------------------------------------------------------------------------------------------
    FileName = "DensiSinkokuHub.png"
    conf = 0.9#画像認識感度
    LoopVal = 10#検索回数
    ImgClick(FolURL2,FileName,conf,LoopVal)#電子申告・申請タブを押す
    #----------------------------------------------------------------------------------------------------------------------
    #要素クリック----------------------------------------------------------------------------------------------------------
    Hub = "AutomationID"
    ObjName = "ao212Button"
    DriverClick(Hub,ObjName,driver)#一括電子申告起動ボタン2を押す
    #----------------------------------------------------------------------------------------------------------------------
    time.sleep(5)
    for x in range(10):#MSGが出てくるので、消えるまでエンターを押す
        if not DriverCheck(Hub,ObjName,driver) == True:
            pg.press('return')
        else:
            pg.press('return')
            break
    #要素クリック----------------------------------------------------------------------------------------------------------
    Hub = "AutomationID"    
    ObjName = "taxAccountantComboBox"#税理士選択コンボボックスをクリック
    DriverClick(Hub,ObjName,driver)
    time.sleep(1)
    pg.press('down')
    pg.press('return')#小林常務を選択
    #FileName = "KanyoHasegawa.png"#担当税理士所長判定
    #法人税消費税処理------------------------------------------------------------------------------------------------------
    # FileName = "KanyoZeirisi.png"#担当税理士小林常務判定
    # conf = 0.9#画像認識感度
    # LoopVal = 500
    # CSVName = 'HoujinSyouhizeiMaster'
    # CSVChildName = 'HoujinSyouhizeiChild'#チャイルドのCSVファイル名を指定
    # List = ["HoujinSyouhizei.png","HoujinSyouhizei2.png"]
    # TaxAns = TaxHantei(List,FolURL2,FileName,conf,LoopVal,CSVName,driver)#pandasにマスターCSVぶっこみ
    # C_Master = TaxAns[0]
    # C_MasterFlag = TaxAns[1]
    # if C_MasterFlag == False:
    #     print("C_Masterは空です")
    # else:
    #     C_Master = C_Master [C_Master['送信']=='可']#送信列「可」のみ抽出
    #     C_Master = C_Master.drop_duplicates(subset='関与先コード')#関与先コードをキーに重複削除
    #     C_dfRow = np.array(C_Master).shape[0]#配列行数取得
    #     C_dfCol = np.array(C_Master).shape[1]#配列列数取得
    #     print(C_Master)
    #     MasterLoop(List,FileName,CSVName,CSVChildName,C_Master,C_dfRow,C_dfCol,driver,FolURL2) 
    ##----------------------------------------------------------------------------------------------------------------------
    ##所得税消費税処理------------------------------------------------------------------------------------------------------
    #FileName = "KanyoZeirisi.png"#担当税理士小林常務判定
    #conf = 0.9#画像認識感度
    #LoopVal = 500
    #CSVName = 'SyotokuSyouhizeiMaster'
    #CSVChildName = 'SyotokuSyouhizeiChild'#チャイルドのCSVファイル名を指定
    #List = ["SyotokuSyouhizei.png","SyotokuSyouhizei2.png"]
    #TaxAns = TaxHantei(List,FolURL2,FileName,conf,LoopVal,CSVName,driver)#pandasにマスターCSVぶっこみ
    #C_Master = TaxAns[0]
    #C_MasterFlag = TaxAns[1]
    #if C_MasterFlag == False:
    #    print("C_Masterは空です")
    #else:
    #    C_Master = C_Master[C_Master['送信']=='可']#送信列「可」のみ抽出
    #    C_Master = C_Master.drop_duplicates(subset='関与先コード')#関与先コードをキーに重複削除
    #    C_dfRow = np.array(C_Master).shape[0]#配列行数取得
    #    C_dfCol = np.array(C_Master).shape[1]#配列列数取得
    #    MasterLoop(List,FileName,CSVName,CSVChildName,C_Master,C_dfRow,C_dfCol,driver,FolURL2)
    #    
    ##-----------------------------------------------------------------------------------------------------------------------
    #法定調書給報処理------------------------------------------------------------------------------------------------------
    FileName = "KanyoZeirisi.png"#担当税理士小林常務判定
    conf = 0.9#画像認識感度
    LoopVal = 500
    CSVName = 'HouteiKyuuhouMaster'
    CSVChildName = 'HouteiKyuuhouChild'#チャイルドのCSVファイル名を指定
    List = ["HouteiKyuuhou.png","HouteiKyuuhou2.png"]
    TaxAns = TaxHantei(List,FolURL2,FileName,conf,LoopVal,CSVName,driver)#pandasにマスターCSVぶっこみ
    C_Master = TaxAns[0]
    C_MasterFlag = TaxAns[1]
    if C_MasterFlag == False:
        print("C_Masterは空です")
    else:
        C_Master = C_Master [C_Master['送信']=='可']#送信列「可」のみ抽出
        C_Master = C_Master.drop_duplicates(subset='関与先コード')#関与先コードをキーに重複削除
        C_dfRow = np.array(C_Master).shape[0]#配列行数取得
        C_dfCol = np.array(C_Master).shape[1]#配列列数取得
        print(C_Master)
        MasterLoop(List,FileName,CSVName,CSVChildName,C_Master,C_dfRow,C_dfCol,driver,FolURL2)
    # #-----------------------------------------------------------------------------------------------------------------------
    # #償却資産処理------------------------------------------------------------------------------------------------------
    # FileName = "KanyoZeirisi.png"#担当税理士小林常務判定
    # conf = 0.9#画像認識感度
    # LoopVal = 500
    # CSVName = 'SyoukyakuMaster'
    # CSVChildName = 'SyoukyakuChild'#チャイルドのCSVファイル名を指定
    # List = ["Syoukyaku.png","Syoukyaku2.png"]
    # TaxAns = TaxHantei(List,FolURL2,FileName,conf,LoopVal,CSVName,driver)#pandasにマスターCSVぶっこみ
    # C_Master = TaxAns[0]
    # C_MasterFlag = TaxAns[1]
    # if C_MasterFlag == False:
    #     print("C_Masterは空です")
    # else:
    #     C_Master = C_Master[C_Master['送信']=='可']#送信列「可」のみ抽出
    #     C_Master = C_Master.drop_duplicates(subset='関与先コード')#関与先コードをキーに重複削除
    #     C_dfRow = np.array(C_Master).shape[0]#配列行数取得
    #     C_dfCol = np.array(C_Master).shape[1]#配列列数取得
    #     MasterLoop(List,FileName,CSVName,CSVChildName,C_Master,C_dfRow,C_dfCol,driver,FolURL2)
        
    # #-----------------------------------------------------------------------------------------------------------------------
    # #贈与税処理------------------------------------------------------------------------------------------------------
    # FileName = "KanyoZeirisi.png"#担当税理士小林常務判定
    # conf = 0.9#画像認識感度
    # LoopVal = 500
    # CSVName = 'ZouyoMaster'
    # CSVChildName = 'ZouyoChild'#チャイルドのCSVファイル名を指定
    # List = ["Zouyo.png","Zouyo2.png"]
    # TaxAns = TaxHantei(List,FolURL2,FileName,conf,LoopVal,CSVName,driver)#pandasにマスターCSVぶっこみ
    # C_Master = TaxAns[0]
    # C_MasterFlag = TaxAns[1]
    # if C_MasterFlag == False:
    #     print("C_Masterは空です")
    # else:
    #     C_Master = C_Master[C_Master['送信']=='可']#送信列「可」のみ抽出
    #     C_Master = C_Master.drop_duplicates(subset='関与先コード')#関与先コードをキーに重複削除
    #     C_dfRow = np.array(C_Master).shape[0]#配列行数取得
    #     C_dfCol = np.array(C_Master).shape[1]#配列列数取得
    #     MasterLoop(List,FileName,CSVName,CSVChildName,C_Master,C_dfRow,C_dfCol,driver,FolURL2)
        
    # #-----------------------------------------------------------------------------------------------------------------------
    # #相続税処理------------------------------------------------------------------------------------------------------
    # FileName = "KanyoZeirisi.png"#担当税理士小林常務判定
    # conf = 0.9#画像認識感度
    # LoopVal = 500
    # CSVName = 'SouzokuMaster'
    # CSVChildName = 'SouzokuChild'#チャイルドのCSVファイル名を指定
    # List = ["Souzoku.png","Souzoku2.png"]
    # TaxAns = TaxHantei(List,FolURL2,FileName,conf,LoopVal,CSVName,driver)#pandasにマスターCSVぶっこみ
    # C_Master = TaxAns[0]
    # C_MasterFlag = TaxAns[1]
    # if C_MasterFlag == False:
    #     print("C_Masterは空です")
    # else:
    #     C_Master = C_Master[C_Master['送信']=='可']#送信列「可」のみ抽出
    #     C_Master = C_Master.drop_duplicates(subset='関与先コード')#関与先コードをキーに重複削除
    #     C_dfRow = np.array(C_Master).shape[0]#配列行数取得
    #     C_dfCol = np.array(C_Master).shape[1]#配列列数取得
    #     MasterLoop(List,FileName,CSVName,CSVChildName,C_Master,C_dfRow,C_dfCol,driver,FolURL2)
        
    # #-----------------------------------------------------------------------------------------------------------------------
    # #配当調書処理------------------------------------------------------------------------------------------------------
    # FileName = "KanyoZeirisi.png"#担当税理士小林常務判定
    # conf = 0.9#画像認識感度
    # LoopVal = 500
    # CSVName = 'HaitouMaster'
    # CSVChildName = 'HaitouChild'#チャイルドのCSVファイル名を指定
    # List = ["Haitou.png","Haitou2.png"]
    # TaxAns = TaxHantei(List,FolURL2,FileName,conf,LoopVal,CSVName,driver)#pandasにマスターCSVぶっこみ
    # C_Master = TaxAns[0]
    # C_MasterFlag = TaxAns[1]
    # if C_MasterFlag == False:
    #     print("C_Masterは空です")
    # else:
    #     C_Master = C_Master[C_Master['送信']=='可']#送信列「可」のみ抽出
    #     C_Master = C_Master.drop_duplicates(subset='関与先コード')#関与先コードをキーに重複削除
    #     C_dfRow = np.array(C_Master).shape[0]#配列行数取得
    #     C_dfCol = np.array(C_Master).shape[1]#配列列数取得
    #     MasterLoop(List,FileName,CSVName,CSVChildName,C_Master,C_dfRow,C_dfCol,driver,FolURL2)
        
    # #-----------------------------------------------------------------------------------------------------------------------
    #申請処理---------------------------------------------------------------------------------------------------------------
    FileName = "KanyoZeirisi.png"#担当税理士小林常務判定
    conf = 0.9#画像認識感度
    LoopVal = 500
    CSVName = 'SinseiMaster'#マスターのCSVファイル名を指定
    CSVChildName = 'SinseiChild'#チャイルドのCSVファイル名を指定
    List = ["Sinsei.png","Sinsei2.png"]#税種目のタブアイコン画像名を2つ指定
    TaxAns = TaxHantei(List,FolURL2,FileName,conf,LoopVal,CSVName,driver)#pandasにマスターCSVぶっこみ
    C_Master = TaxAns[0]
    C_MasterFlag = TaxAns[1]
    if C_MasterFlag == False:
        print("C_Masterは空です")
    else:
        C_Master = C_Master[C_Master['送信']=='可']#送信列「可」のみ抽出
        C_Master = C_Master.drop_duplicates(subset='関与先コード')#関与先コードをキーに重複削除
        C_dfRow = np.array(C_Master).shape[0]#配列行数取得
        C_dfCol = np.array(C_Master).shape[1]#配列列数取得
        MasterLoop(List,FileName,CSVName,CSVChildName,C_Master,C_dfRow,C_dfCol,driver,FolURL2)     
    #-----------------------------------------------------------------------------------------------------------------------

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

#RPA用画像フォルダの作成---------------------------------------------------------
FolURL = "//Sv05121a/e/C 作業台/RPA/ALLDataBase/RPAPhoto/TKC_DensiSinkoku"#元
#FolURL2 = os.getcwd().replace('\\','/') + "/TKC_DensiSinkoku"#先
FolURL2 = os.getcwd().replace('\\','/')#先
#try:
#    shutil.copytree(FolURL,FolURL2)
#except:
#    print(FolURL2 + "あります。")
#--------------------------------------------------------------------------------
try:
    MainFlow(FolURL2)
except:
    traceback.print_exc()