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
#----------------------------------------------------------------------------------------------------------------------
def TaxLogin(FolURL2,driver,Sikibetu,ID,Hub,ObjName):
    conf = 0.9
    LoopVal = 10000
    FileName = "KokuzeiAnsyou.png"
    TaxNoBox = ImgCheck(FolURL2,FileName,conf,LoopVal)
    if TaxNoBox[0] == True:
        ImgClick(FolURL2,FileName,conf,LoopVal)
        pg.write(Sikibetu, interval=0.01)#直接SENDできないのでpyautoguiで入力
        pg.press('return')
    FileName = "TihouzeiAnsyou.png"
    time.sleep(1)
    TaxNoBox = ImgCheck(FolURL2,FileName,conf,LoopVal)
    if TaxNoBox[0] == True:
        ImgClick(FolURL2,FileName,conf,LoopVal)
        pg.write(ID, interval=0.01)#直接SENDできないのでpyautoguiで入力
        pg.press('return')
    FileName = "MSGLogin.png"
    ImgClick(FolURL2,FileName,conf,LoopVal)
    FileName = "MSGOKTrigger.png"
    try:
        while pg.locateOnScreen(FolURL2 + "/" + FileName, confidence=0.9) == None:
            List = ["KokuzeiLogErr.png","TihouzeiLogErr.png"]
            LogA = ImgCheckForList(FolURL2,List,conf)#リスト内の画像があればTrueと画像名を返す
            if LogA[0] == True:
                ImgClick(FolURL2,LogA[1],conf,LoopVal)
                pg.press('return')
                while all(pg.locateOnScreen(FolURL2 + "/" + "DataIdouKakunin.png", confidence=0.9)) == True:
                    time.sleep(1)
                    ImgClick(FolURL2,"DataIdouKakuninNo.png",conf,LoopVal)
                    EraceIMGWait(FolURL2,"DataCloseWait.png")
                    return False
            else:
                conf = 0.9
                LoopVal = 10
                NoMsg = ImgCheck(FolURL2, "NoMessage.png", conf, LoopVal)
                if NoMsg[0] == True:
                    pg.press('return')
                conf = 0.9
                LoopVal = 10
                NoMsg = ImgCheck(FolURL2, "KokuzeiKakunin.png", conf, LoopVal)
                if NoMsg[0] == True:
                    pg.press('return')
            time.sleep(1)
        return True
    except:
        return False
#----------------------------------------------------------------------------------------------------------------------
def IconStart(Hub,ObjName,driver):
    Hub = "AutomationID"
    try:
        if ObjName == "tax1PictureButton":
            DriverClick(Hub,ObjName,driver)#法人
            ObjName = "Button0101"#法人関与先MSG確認ボタン
            DriverClick(Hub,ObjName,driver)
            return True
        else:
            DriverClick(Hub,ObjName,driver)#個人
            ObjName = "Button0105"#個人関与先MSG確認ボタン
            DriverClick(Hub,ObjName,driver)
            return True
    except:
        return False 
#----------------------------------------------------------------------------------------------------------------------
def MaserFindSikibetu(MasterCSV,SyanaiCode,KeyCol,Col1,Col2,Col3,Col4,Col5,Col6):
    MRow = np.array(MasterCSV).shape[0]#配列行数取得
    MCol = np.array(MasterCSV).shape[1]#配列列数取得
    Hantei = False
    for y in range(MRow):
        #関与先DB配列をループして識別番号とPassを取得
        MDataRow = MasterCSV.iloc[y,:]
        Key = MDataRow[KeyCol]
        Key = int(Key)
        TSiki = MDataRow[Col1]
        TID = MDataRow[Col2]
        MSiki = MDataRow[Col3]
        MID = MDataRow[Col4]
        ep = MDataRow[Col5]
        elp = MDataRow[Col6]
        if SyanaiCode == Key:
            Hantei = True
            return TSiki,TID,MSiki,MID,ep,elp,True
    if Hantei == True:
        Hantei = False
        return "","","","","","",False
#----------------------------------------------------------------------------------------------------------------------
def SyanaiCDChange(intNo):
    if intNo<1000:
        return '{0:03d}'.format(intNo) 
    elif intNo >= 1000 and intNo < 2000:
        Te = intNo[-3:]
        return Te
    elif intNo >= 4000 and intNo < 5000:
        Te = intNo[-3:]
        return Te
    else:
        Te = intNo[-3:]
        return Te       
#----------------------------------------------------------------------------------------------------------------------
def OpenAction(LoopList,FolURL2):
    conf = 0.9
    LoopVal = 100
    for LoopListItem in LoopList:
        RowParList = LoopListItem[0].split("[")
        RowPar = RowParList[1].split("]")
        RowPar = RowPar[0]        
        time.sleep(1)
        FileName = "Gyousuu.png"
        ImgClick(FolURL2,FileName,conf,LoopVal)
        pg.press(['delete','delete','delete'])
        pg.write(RowPar, interval=0.01)#直接SENDできないのでpyautoguiで入力
        pg.press('return')
        time.sleep(1)
        FileName = "PreMSGTrigger.png"
        while pg.locateOnScreen(FolURL2 + "/" + FileName, confidence=0.9) is None:
            time.sleep(1)
        FileName = "PreKakuninBtn.png"
        ImgClick(FolURL2,FileName,conf,LoopVal)
        FileName = "Insatu.png"
        while pg.locateOnScreen(FolURL2 + "/" + FileName, confidence=0.9) is None:
            time.sleep(1)
            if ImgCheck(FolURL2, "PreMSG.png", conf, LoopVal)[0] == True:
                pg.press('return')
        ImgClick(FolURL2,FileName,conf,LoopVal)
        FileName = "SkyPDFBtn.png"
        while pg.locateOnScreen(FolURL2 + "/" + FileName, confidence=0.9) is None:
            time.sleep(1)
        ImgClick(FolURL2,FileName,conf,LoopVal)
        time.sleep(1)
        pyperclip.copy(str(LoopListItem[3]))
        pyautogui.hotkey('ctrl','v')
        FileName = "FileOpenCheck.png"
        FNO = ImgCheck(FolURL2, FileName, conf, LoopVal)
        if FNO[0] == True:
            ImgClick(FolURL2,FileName,conf,LoopVal)
        pg.keyDown('alt')
        pg.press('s')
        pg.keyUp('alt')
        time.sleep(1)
        conf = 0.9
        LoopVal = 10
        if ImgCheck(FolURL2, "PDFReplace.png", conf, LoopVal)[0] == True:
            pg.press('y')
        time.sleep(1)
        ImgClick(FolURL2,"PrintCancelBtn.png",conf,LoopVal) 
        FileName = "Insatu.png"
        while pg.locateOnScreen(FolURL2 + "/" + FileName, confidence=0.9) is None:
            time.sleep(1)
        pg.press('f4')
        time.sleep(1)
        FileName = "PreMSGTrigger.png"
        while pg.locateOnScreen(FolURL2 + "/" + FileName, confidence=0.9) is None:
            time.sleep(1)
        pg.press('f4')
        time.sleep(1) 
    FileName = "Gyousuu.png"
    while pg.locateOnScreen(FolURL2 + "/" + FileName, confidence=0.9) is None:
        time.sleep(1)
    ImgClick(FolURL2,FileName,conf,LoopVal)
    pg.press('f10')
    time.sleep(1)
    FileName = "DataMoveCheck.png"
    while pg.locateOnScreen(FolURL2 + "/" + FileName, confidence=0.9) is None:
        time.sleep(1)
    FileName = "DataPCMMove.png"
    ImgClick(FolURL2, FileName, conf, LoopVal)
    time.sleep(1)
#----------------------------------------------------------------------------------------------------------------------
def DeleteOMSData(driver,FolURL2):
    FileName = "OMSTITLE.png"
    while pg.locateOnScreen(FolURL2 + "/" + FileName, confidence=0.9) is None:
        time.sleep(1)
    #要素クリック----------------------------------------------------------------------------------------------------------
    Hub = "AutomationID"
    ObjName = "hojoPictureButton"
    DriverClick(Hub,ObjName,driver)
    FileName = "HojyoKinouWin.png"
    while pg.locateOnScreen(FolURL2 + "/" + FileName, confidence=0.9) is None:
        time.sleep(1)
    #要素クリック----------------------------------------------------------------------------------------------------------
    Hub = "AutomationID"
    ObjName = "Button0102"
    DriverClick(Hub,ObjName,driver)
    FileName = "DataIchiranCol.png"
    while pg.locateOnScreen(FolURL2 + "/" + FileName, confidence=0.9) is None:
        time.sleep(1)
    conf = 0.9 
    LoopVal = 10
    FileName = "Gyouari.png"
    if ImgCheck(FolURL2, FileName, conf, LoopVal)[0] == True:
        #要素クリック----------------------------------------------------------------------------------------------------------
        Hub = "AutomationID"
        ObjName = "allSelButton"
        DriverClick(Hub,ObjName,driver)
        #要素クリック----------------------------------------------------------------------------------------------------------
        Hub = "AutomationID"
        ObjName = "deleteButton"
        DriverClick(Hub,ObjName,driver)
        FileName = "DOMSWin.png"
        while pg.locateOnScreen(FolURL2 + "/" + FileName, confidence=0.9) is None:
            time.sleep(1)
        FileName = "DOMSOK.png"
        ImgClick(FolURL2, FileName, conf, LoopVal)
        #----------------------------------------------------------------------------------------------------------
        FileName = "DeleteAfterList.png"
        while pg.locateOnScreen(FolURL2 + "/" + FileName, confidence=0.9) is None:
            time.sleep(1)
        print("削除データ無")
    Hub = "AutomationID"
    ObjName = "cancelButton"
    DriverClick(Hub,ObjName,driver)
    FileName = "HojyoKinouWin.png"
    while pg.locateOnScreen(FolURL2 + "/" + FileName, confidence=0.9) is None:
        time.sleep(1)
    #要素クリック----------------------------------------------------------------------------------------------------------
    Hub = "AutomationID"
    ObjName = "ButtonClose"
    DriverClick(Hub,ObjName,driver)
    FileName = "OMSTITLE.png"
    while pg.locateOnScreen(FolURL2 + "/" + FileName, confidence=0.9) is None:
        time.sleep(1)
    time.sleep(1)

def MainFlow(FolURL2,PreList,MasterCSV,NoList):
    BatUrl = FolURL2 + "/bat/AWADriverOpen.bat"#4724ポート指定でappiumサーバー起動バッチを開く
    driver = OMSOpen.MainFlow(BatUrl,FolURL2,"RPAPhoto")#OMSを起動しログイン後インスタンス化
    FolURL2 = FolURL2 + "/RPAPhoto/TKC_PreSinkokuDown"
    #----------------------------------------------------------------------------------------------------------------------
    for NoListItem in NoList:
        LoopList = []
        for PreListItem in PreList:#PreListItem[0]=URL,PreListItem=[1]=関与先コード
            if NoListItem == PreListItem[1]:
                LoopList.append(PreListItem)
        #for PreListItem in LoopList:#PreListItem[0]=URL,PreListItem=[1]=関与先コード
        #要素クリック----------------------------------------------------------------------------------------------------------
        Hub = "AutomationID"
        ObjName = "aoCodeComboBox"
        DriverClick(Hub,ObjName,driver)#事務所コードコンボクリック
        #社内コードに準じて事務所コード分岐----------------------------------------------------------------------------------------------------------------------
        if NoListItem < 1000:
            pg.press(['up','up','up','up'])
            pg.press(['return'])
        elif NoListItem >= 1000 and NoListItem < 2000:
            pg.press(['1'])
            pg.press(['return'])
        elif NoListItem >= 4000 and NoListItem < 5000:
            pg.press(['up','up','up','up'])
            pg.press(['down','down'])
            pg.press(['return'])
        else:        
            pg.press(['down','down','down','down'])
            pg.press(['return'])
        #要素クリック----------------------------------------------------------------------------------------------------------
        Hub = "AutomationID"
        ObjName = "codeTextBox"
        DriverClick(Hub,ObjName,driver)#事務所コードコンボクリック
        pg.write(SyanaiCDChange(NoListItem), interval=0.01)#直接SENDできないのでpyautoguiで入力
        pg.press(['return'])
        IDS = MaserFindSikibetu(MasterCSV,NoListItem,"SyanaiCode","TKCKokuzeiUserCode","TKCTihouzeiUserID","MirokuKokuzeiUserCode","MirokuTihouzeiUserID","etaxPass","eltaxPass")#マスターから社内コードで国・地方税識別番号とIDを取得
        Hub = "AutomationID"
        ObjName = "tax1PictureButton"#法人決算ボタン
        IconStart(Hub,ObjName,driver)
        FileName = "KanyoMSG.png"
        while pg.locateOnScreen(FolURL2 + "/" + FileName, confidence=0.9) is None:
            time.sleep(1)
        LLog = TaxLogin(FolURL2,driver,IDS[4],IDS[5],Hub,ObjName)
        if LLog == False:
            LoginErr = False
        else:
            LoginErr = True
        if LoginErr == True:
            conf = 0.9
            LoopVal = 100
            while pg.locateOnScreen(FolURL2 + "/MSGOKTrigger.png", confidence=0.9) is None:
                time.sleep(1)
            List = ["TihouzeiTab.png","TihouzeiTab2.png"]
            IA = ImgCheckForList(FolURL2,List,conf)
            if IA[0] == True:
                ImgClick(FolURL2,IA[1],conf,LoopVal)
                time.sleep(1)
                ImgClick(FolURL2,"DayStart.png",conf,LoopVal)
                pg.write(TaisyouNen, interval=0.01)#直接SENDできないのでpyautoguiで入力
                pg.press('return')
                pg.write(TaisyouTuki, interval=0.01)#直接SENDできないのでpyautoguiで入力
                pg.press('return')
                time.sleep(1)
                pg.press('1')
                time.sleep(1)
                pg.press(['return','return','return'])
                pg.write(TaisyouNen, interval=0.01)#直接SENDできないのでpyautoguiで入力
                pg.press('return')
                pg.write(TaisyouTuki, interval=0.01)#直接SENDできないのでpyautoguiで入力
                pg.press('return')
                Lday = calendar.monthrange(int(TaisyouNen),int(TaisyouTuki))
                pg.write(str(Lday[1]), interval=0.01)#直接SENDできないのでpyautoguiで入力
                pg.press('return')
                time.sleep(1)
                ImgClick(FolURL2,"FindBtn.png",conf,LoopVal)
                time.sleep(1)
                #同月同関与先のプレ申告のお知らせ数分ループ
                OpenAction(LoopList,FolURL2)
                DeleteOMSData(driver,FolURL2)
                time.sleep(1)
        #tax1PictureButton#法人決算ボタン
        #tax3PictureButton#個人決算ボタン

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
#RPA用画像フォルダの作成---------------------------------------------------------
FolURL = "//Sv05121a/e/C 作業台/RPA/ALLDataBase/RPAPhoto/TKC_DensiSinkoku"#元
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
for current_dir, sub_dirs, files_list  in PDFFileList:
    Count_dir = 0
    for file_name in files_list: 
        if "プレ申告のお知らせ" in file_name or "プレ申告データに関するお知らせ" in file_name:
            Count_dir = Count_dir + 1
    for file_name in files_list: 
        if "プレ申告のお知らせ" in file_name or "プレ申告データに関するお知らせ" in file_name:
            Nos = file_name.split("_")
            NewTitle = os.path.join(current_dir,file_name)
            NewTitle = NewTitle.split("プレ申告データ")
            NewTitle = NewTitle[0] + "プレ申告データ印刷結果.pdf"
            NGList = ["100","105","106","107","108","121","12","148","183","200","201","204","207","209","211"]
            if not Nos[0] in NGList:
                PreList.append([os.path.join(current_dir,file_name),int(Nos[0]),Count_dir,NewTitle])

print(PreList)
myList = []
for PreListItem in PreList: 
    myList.append(PreListItem[1])
NoList = list(OrderedDict.fromkeys(myList))
print(NoList)
MasterCSV = pd.read_csv(FolURL2 + "/RPAPhoto/TKC_PreSinkokuDown/" + "MasterDB.csv",\
    dtype={"TKCKokuzeiUserCode": str,"TKCTihouzeiUserID": str,"MirokuKokuzeiUserCode": str,"MirokuTihouzeiUserID": str,"etaxPass": str,"eltaxPass": str})
print(MasterCSV)
#--------------------------------------------------------------------------------
try:
    MainFlow(FolURL2,PreList,MasterCSV,NoList)
except:
    traceback.print_exc()