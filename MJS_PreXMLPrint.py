#----------------------------------------------------------------------------------------------------------------------
from ast import For
from queue import Empty
from pyparsing import And
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
#------------------------------------------------------------r----------------------------------------------------------
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
def ImgCheckForList(FolURL2,List,conf,LoopVal):#リスト内の画像があればTrueと画像名を返す
    for x in range(LoopVal):
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
    with codecs.open(Sort_url, "r", "utf-8", "ignore") as file:
        C_Child = pd.read_table(file,delimiter=",")
    C_CforCount = 0
    C_dfRow = np.array(C_Child).shape[0]#配列行数取得
    for x in range(C_dfRow):
        C_ChildDataRow = C_Child.iloc[x,:]
        C_Val = int(C_ChildDataRow['SyanaiCode'])
        if Key == C_Val:
            return True,C_ChildDataRow
        else:
            C_CforCount = C_CforCount + 1
    return False,""
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
def SortPreList(PreList,Key):#CSVと列名を4つ与えて4つの複合と引数Keyが一致する行数を返す
    try:
        PL_List = []
        for PreListItem in PreList:
            if Key == PreListItem[1]:
                PL_List.append([PreListItem[0],PreListItem[3],PreListItem[2]])
        return True,PreListItem[0],PreListItem[3],PreListItem[2]
    except:
        return False,"","",""
#----------------------------------------------------------------------------------------------------------------------
def MainStarter(FolURL2):
    #画像が出現するまで待機してクリック------------------------------------------------------------------------------------
    List = ["DensiSinkokuIcon.png","DensiSinkokuIcon2.png"]
    conf = 0.9#画像認識感度
    LoopVal = 10000#検索回数
    ListCheck = ImgCheckForList(FolURL2,List,conf,LoopVal)#画像検索関数
    if ListCheck[0] == True:
        ImgClick(FolURL2,ListCheck[1],conf,LoopVal)
        time.sleep(1)
        pg.keyDown('alt')
        pg.press('a')
        pg.keyUp('alt')
    time.sleep(1)
    #----------------------------------------------------------------------------------------------------------------------
    #画像が出現するまで待機してクリック------------------------------------------------------------------------------------
    while pg.locateOnScreen(FolURL2 + "/" + "SyomeiBtn.png", confidence=0.9) is None:
        time.sleep(1)
        if ImgCheck(FolURL2,"FMSG.png",0.9,1)[0] == True:
            pg.keyDown('alt')
            pg.press('c')
            pg.keyUp('alt')
    ImgClick(FolURL2,"SyomeiBtn.png",conf,LoopVal)#電子申告・申請タブを押す
    #----------------------------------------------------------------------------------------------------------------------
    while pg.locateOnScreen(FolURL2 + "/" + "TyouhyouList.png", confidence=0.9) is None:
        time.sleep(1)
#----------------------------------------------------------------------------------------------------------------------
def MasterCSVGet(FolURL2): 
    # #出力したCSVを読込み----------------------------------------------------------------------------------------------------------
    CSVURL = FolURL2
    CSVName = '/SyomeiMaster'
    #C_url = CSVURL.replace("\\","/") + '/' + CSVName + '.CSV'
    C_url = CSVURL + '/' + CSVName + '.CSV'
    with codecs.open(C_url, "r", "Shift-JIS", "ignore") as file:
        C_df = pd.read_table(file, delimiter=",")
        ColLister = ['顧問先コード','年度', '税目','申告種類']
        C_df = C_df.drop_duplicates(subset=ColLister)
    print(C_df)
    return(C_df)
#------------------------------------------------------------------------------------------------------------------------------- 
def DataOpen(FolURL2,PreListItem):
    try:
        time.sleep(1)
        pyperclip.copy(str(PreListItem[0]))
        pg.hotkey('ctrl', 'v')#pg日本語不可なのでコピペ
        time.sleep(1)
        pg.press(['return'])
        time.sleep(2)
        WY = WarekiHenkan.Wareki.from_ad(int(TaisyouNen) - 1)
        WY = str(WY).replace("令和","").replace("年","")
        pg.write(WY,interval=0.01)
        time.sleep(1)
        pg.press('return')
        time.sleep(1)
        pg.press('return')
        time.sleep(1)
        while pg.locateOnScreen(FolURL2 + "/" + "PreCheckBar.png", confidence=0.9) is None:
            time.sleep(1)
        time.sleep(2)
        pg.keyDown('alt')
        pg.press('p')
        time.sleep(1)
        pg.press('k')
        pg.keyUp('alt')        
        while pg.locateOnScreen(FolURL2 + "/" + "FileOut.png", confidence=0.9) is None:
            time.sleep(1)
        ImgClick(FolURL2,"FileOut.png",0.9,1)
        time.sleep(1)
        ImgClick(FolURL2,"FTypeSelect.png",0.9,1)
        pg.press('return')
        time.sleep(1)
        pyperclip.copy(str(PreListItem[3]))
        pg.hotkey('ctrl', 'v')#pg日本語不可なのでコピペ
        pg.press(['return'])
        time.sleep(2)
        ImgClick(FolURL2,"FileOutPutBtn.png",0.9,1)
        time.sleep(1)
        while pg.locateOnScreen(FolURL2 + "/" + "PreCheck.png", confidence=0.9) is not None:
            time.sleep(1)
            FO = ImgCheck(FolURL2,"FileOverCheck.png",0.9,1)
            if FO[0] == True:
                ImgClick(FolURL2,"FileOverCheck.png",0.9,1)
                pg.press('y')
        time.sleep(1)
        pg.keyDown('alt')
        pg.press('x')
        pg.keyUp('alt')
        time.sleep(1)           
        return True         
    except:
        print("フォルダ名取得失敗")
        return False
#------------------------------------------------------------------------------------------------------------------------------- 
def MainFlow(FolURL2,PreList):
    BatUrl = FolURL2 + "/bat/AWADriverOpen.bat"#4724ポート指定でappiumサーバー起動バッチを開く
    driver = MJSOpen.MainFlow(BatUrl,FolURL2,"RPAPhoto/MJS_DensiSinkoku")#OMSを起動しログイン後インスタンス化
    FolURL2 = FolURL2 + "/RPAPhoto/MJS_DensiSinkoku"
    #----------------------------------------------------------------------------------------------------------------------
    MainStarter(FolURL2)#データ送信画面までの関数
    ItemList = []
    time.sleep(1)
    #クラス要素クリック----------------------------------------------------------------------------------------------------------
    for PreListItem in PreList:
        if os.path.isfile(PreListItem[3]) == False: ################################################################################################
            #CSV要素取得-------------------------------------------------------------------------------------------------------------
            TyouList = ["TyouhyouList.png","TyouhyouList2.png"]
            Imc = ImgCheckForList(FolURL2,TyouList,0.9,2)
            if Imc[0] == True:
                ImgClick(FolURL2,Imc[1],0.9,1)
            while pg.locateOnScreen(FolURL2 + "/" + "FOTitle.png", confidence=0.9) is None:
                time.sleep(1)
            DOList = DataOpen(FolURL2,PreListItem)
            time.sleep(1)    
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
#RPA用画像フォルダの作成---------------------------------------------------------
FolURL = "//Sv05121a/e/C 作業台/RPA/ALLDataBase/RPAPhoto/MJS_DensiSinkoku"#元
FolURL2 = os.getcwd().replace('\\','/')#先
#--------------------------------------------------------------------------------
TaisyouNen = input("対象[年]を西暦で入力してください。\n")
TaisyouTuki = input("対象[月]を西暦で入力してください。\n")
TaisyouFol = str(TaisyouNen) + "-" + str(TaisyouTuki)
#プレ申告のお知らせ保管フォルダチェック---------------------------------------------------------
Fol = TaisyouFol
pt = "\\\\Sv05121a\\e\\電子ファイル\\メッセージボックス\\" + Fol + "\\eLTAX"
#path = path.replace('\\','/')#先
PDFFileList = os.walk(pt)
Cou = 1
PreList=[]
SerchEnc = format(getFileEncoding(FolURL2 + "/RPAPhoto/eLTaxDLPresinkoku/Log/Log.csv"))
NgLog = pd.read_csv(FolURL2 + "/RPAPhoto/eLTaxDLPresinkoku/Log/Log.csv",encoding=SerchEnc)
NgRow = np.array(NgLog).shape[0]#配列行数取得
NgCol = np.array(NgLog).shape[1]#配列列数取得

for current_dir, sub_dirs, files_list  in PDFFileList:
    Count_dir = 0
    for file_name in files_list: 
        if ".xml" in file_name:
            Count_dir = Count_dir + 1
    for file_name in files_list: 
        if ".xml" in file_name:
            Nos = file_name.split("_")
            FolName = current_dir.split("_")
            FolName = FolName[1]
            NewTitle = os.path.join(current_dir,file_name)
            NewTitle = NewTitle.split("プレ申告データ")
            NewTitle = NewTitle[0] + "プレ申告データ印刷結果.pdf"
            #NGList = ["100","105","106","107","108","121","12","148","183","200","201","204","207","209","221",\
            #    "223","240","249","251","268","282","285","305","306","309","317"]
            NoF = True
            for x in range(NgRow):
                NgDataRow = NgLog.iloc[x,:]
                NgCodeCode = str(NgDataRow[1])
                if not Nos[0] == NgCodeCode:
                    NoF = True
                else:
                    NoF = False
                    break
            if NoF == True:
                PreList.append([os.path.join(current_dir,file_name),int(Nos[0]),Count_dir,NewTitle,FolName])
print(NgLog)
print(PreList)

try:
    MainFlow(FolURL2,PreList)
except:
    traceback.print_exc()