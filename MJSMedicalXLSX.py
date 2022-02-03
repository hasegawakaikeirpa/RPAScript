#----------------------------------------------------------------------------------------------------------------------
from cmath import nan
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
                PL_List.append([PreListItem[3].replace(".pdf",""),PreListItem[2]])
        return True,PL_List
    except:
        return False,""
#----------------------------------------------------------------------------------------------------------------------
def MainStarter(FolURL2,fol_path):
    try:
        ImgClick(FolURL2, "UtilTab.png", 0.9, 1)
        while pg.locateOnScreen(FolURL2 + "/DataItiranBtn.png", confidence=0.9) is None:
            time.sleep(1)
        ImgClick(FolURL2, "DataItiranBtn.png", 0.9, 1)
        while pg.locateOnScreen(FolURL2 + "/DataItiranBtnSysCombo.png", confidence=0.9) is None:
            time.sleep(1)
        ImgClick(FolURL2, "DataItiranBtnSysCombo.png", 0.9, 1)
        while pg.locateOnScreen(FolURL2 + "/syotokuzeiText.png", confidence=0.9) is None:
            time.sleep(1) 
        ImgClick(FolURL2, "syotokuzeiText.png", 0.9, 1)
        while pg.locateOnScreen(FolURL2 + "/DataOutBtn.png", confidence=0.9) is None:
            time.sleep(1)
        ImgClick(FolURL2, "DataOutBtn.png", 0.9, 1)
        while pg.locateOnScreen(FolURL2 + "/AfterDataOpen.png", confidence=0.9) is None:
            time.sleep(1)
        pg.keyDown('alt')
        pg.press('p')
        pg.keyUp('alt')
        while pg.locateOnScreen(FolURL2 + "/PrintMenuFileOut.png", confidence=0.9) is None:
            time.sleep(1)
        ImgClick(FolURL2, "PrintMenuFileOut.png", 0.9, 1)
        while pg.locateOnScreen(FolURL2 + "/PrintMenuUnderArrow.png", confidence=0.9) is None:
            time.sleep(1)
        ImgClick(FolURL2, "PrintMenuUnderArrow.png", 0.9, 1)
        time.sleep(1) 
        pg.press(['up','up','up','up','up']) 
        pg.press('return') 
        time.sleep(1)
        FName = fol_path + "/システム別データ一覧表.csv"
        ChooseUrl = FName
        FName = FName.replace('/','\\')
        pyperclip.copy(FName)
        pg.hotkey('ctrl', 'v')#pg日本語不可なのでコピペ
        pg.press(['return'])
        #pgじゃなくコピペでurl値貼り付け
        ImgClick(FolURL2, "PrintMenuFileOutOKBtn.png", 0.9, 1)
        while pg.locateOnScreen(FolURL2 + "/DataOutCancelBtn.png", confidence=0.9) is None:
            time.sleep(1)
            if ImgCheck(FolURL2,"FileOverWrite.png",0.9,1)[0] == True:
                pg.press('y')
        ImgClick(FolURL2, "DataOutCancelBtn.png", 0.9, 1)
        time.sleep(1)
        #画像が出現するまで待機してクリック------------------------------------------------------------------------------------
        List = ["IryouMenuOpen.png","IryouMenuOpen2.png"]
        conf = 0.9#画像認識感度
        LoopVal = 10000#検索回数
        ListCheck = ImgCheckForList(FolURL2,List,conf,LoopVal)#画像検索関数
        if ListCheck[0] == True:
            ImgClick(FolURL2,ListCheck[1],conf,LoopVal)
        time.sleep(1)
        #----------------------------------------------------------------------------------------------------------------------
        #画像が出現するまで待機してクリック------------------------------------------------------------------------------------
        while pg.locateOnScreen(FolURL2 + "/IryouOpenFlag.png", confidence=0.9) is None:
            time.sleep(1)
        return True,ChooseUrl
    except:
        return False,""
    #----------------------------------------------------------------------------------------------------------------------
def CSVGet(FileUrl): 
    #出力したCSVを読込み----------------------------------------------------------------------------------------------------------
    try:
        SerchEnc = format(getFileEncoding(FileUrl))
        MasterCSV = pd.read_csv(FileUrl,encoding=SerchEnc)
        return True,MasterCSV
    except:
        return False,""
    #----------------------------------------------------------------------------------------------------------------------
def CSVCheck(CsvArr,CodeNo,CodeNendo):
    CsvArrRow = np.array(CsvArr).shape[0]#配列行数取得
    # #出力したCSVを読込み----------------------------------------------------------------------------------------------------------
    try:
        for x in range(CsvArrRow):
            CsvArr_Row = CsvArr.iloc[x,:]
            C_Val = int(CsvArr_Row['コード'])
            C_Nendo = CsvArr_Row['年度']
            if CodeNo == C_Val and CodeNendo == C_Nendo:
                return True,x
        return False,""
    except:
        return False,""
#------------------------------------------------------------------------------------------------------------------------------- 
def FolCreate(FolURL2):
    idir = r'\\Sv05121a\e\B 業務\Ⅰ 業務\８ 確申・年調・納特・労働保険\(3)確申'
    fol_path = tkinter.filedialog.askdirectory(initialdir = idir,title = "確申年度フォルダを指定してください。")
    file_path = tkinter.filedialog.askopenfilename(initialdir = fol_path,title = "確申受付Excelファイルを指定して下さい。")
    Cxmsl_path = tkinter.filedialog.askopenfilename(initialdir = fol_path,title = "各関与先フォルダにコピーする医療費控除集計表Excelファイルを指定してください。")
    Cxmsl_Name = Cxmsl_path.replace(fol_path,"")
    PDFFileList = os.walk(fol_path)
    xls_data = pd.read_excel(file_path, sheet_name="受付簿",header=None,engine="openpyxl")
    HeadRow = input("ヘッダー行を指定してください。\n")
    xls_data = pd.read_excel(file_path, sheet_name="受付簿",header=int(HeadRow),engine="openpyxl")
    xls_data = xls_data.rename(columns={'関与先\nコード':'関与先コード'})
    print(xls_data)
    Cou = 1
    PreList=[]
    Sub_Folders = []
    for fd_path, sb_folder, sb_file in PDFFileList:
        for fol in sb_folder:
            Sub_Folders.append(fol)

    for index, xls_Item in xls_data.iterrows():
        try:
            if xls_Item['№'] >= 1:
                try:
                    xlsKey = str(int(xls_Item['関与先コード']))
                except:
                    xlsKey = ""
                try:
                    xlsCKey = int(xls_Item['枝番'])
                    xlsCKey = str('{0:02}'.format(xlsCKey))
                except:
                    xlsCKey = ""            
                try:
                    xlsName = str(xls_Item['氏名／屋号'].replace("\u3000"," "))
                except:
                    xlsName = ""
                if xlsKey == "":
                    print('No関与先コード')
                    MergeNo = ""
                    dirFlag = False
                elif xlsCKey == "":
                    MergeNo = xlsKey
                    dirFlag = False
                else:
                    MergeNo = xlsKey + "-" + xlsCKey
                    dirFlag = False
                for Sub_FoldersItem in Sub_Folders:                
                    if MergeNo in Sub_FoldersItem:
                        dirFlag = True
                        break
                    else:
                        dirFlag = False
                if dirFlag == False:
                    fol_path = fol_path.replace('\\','/')
                    fol_Name = fol_path + "/" + MergeNo + " " + xlsName
                    os.mkdir(fol_Name)
                    shutil.copy(Cxmsl_path, fol_Name + Cxmsl_Name)
                    time.sleep(1)
        except:
            print('Nodata')
    time.sleep(1)
    Sub_Folders = []
    PDFFileList = os.walk(fol_path)
    for fd_path, sb_folder, sb_file in PDFFileList:
        for fol in sb_folder:
            Sub_Folders.append(fol)
    return Sub_Folders,xls_data,fol_path
#------------------------------------------------------------------------------------------------------------------------------- 
def MainFlow(FolURL2,PreList,NoList,MasterCSV,XmlList,fol_path):
    BatUrl = FolURL2 + "/bat/AWADriverOpen.bat"#4724ポート指定でappiumサーバー起動バッチを開く
    driver = MJSOpen.MainFlow(BatUrl,FolURL2,"RPAPhoto/MJS_DensiSinkoku")#OMSを起動しログイン後インスタンス化
    FolURL2 = FolURL2 + "/RPAPhoto/MJSMedicalXLSX"
    #----------------------------------------------------------------------------------------------------------------------
    MSOK = MainStarter(FolURL2,fol_path)#データ送信画面までの関数
    Get_csv = CSVGet(MSOK[1])
    if Get_csv[0] == True:
        Get_csvArr = Get_csv[1]
        time.sleep(1)
        #クラス要素クリック----------------------------------------------------------------------------------------------------------
        for PreListItem in PreList:
            if "-" in PreListItem:
                Key = PreListItem.split("-")
                Key = int(Key[0])
            else:
                Key = PreListItem.split(" ")
                Key = int(Key[0])                
            TyearPar = WarekiHenkan.Wareki.from_ad(dt.today().year).year
            TyearPar = "令和 " + str(TyearPar - 1) + "年"
            CsvC = CSVCheck(Get_csvArr,Key,TyearPar)
            if MSOK[0] == True and CsvC[0] == True:
                "KanyoCDMsg.png"
                ImgClick(FolURL2,"KanyoCDMsg.png",0.9999,1) 
                time.sleep(1)
                pg.write(Key,interval=0.01)
                time.sleep(1)
                pg.press('return')
                time.sleep(1)
                Tyeares = WarekiHenkan.Wareki.from_ad(dt.today().year).year
                Tyeares = str(Tyeares - 1)
                pg.write(Tyeares,interval=0.01)
                pg.press('return')
                time.sleep(1)
            else:
                print("ミロク起動失敗かミロクシステム利用状況CSVが取得できませんでした。")
    else:
        print('ミロクシステム利用状況CSVが取得できませんでした。')
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
import tkinter
from tkinter import filedialog

Lday = calendar.monthrange(dt.today().year,dt.today().month)
#return PDFFileList,xls_data
#RPA用画像フォルダの作成---------------------------------------------------------
FolURL = "//Sv05121a/e/C 作業台/RPA/ALLDataBase/RPAPhoto/MJS_DensiSinkoku"#元
FolURL2 = os.getcwd().replace('\\','/')#先
try:
    FolVariant = FolCreate(FolURL2)
    PreList = FolVariant[0]
    XmlList = FolVariant[1]
    fol_path = FolVariant[2]
    print(PreList)
    print(XmlList)
    myList = []
    for PreListItem in PreList: 
        myList.append(PreListItem[1])
    NoList = list(OrderedDict.fromkeys(myList))
    print(NoList)
    SerchEnc = format(getFileEncoding(FolURL2 + "/RPAPhoto/MJS_DensiSinkoku/" + "MasterDB.csv"))
    MasterCSV = pd.read_csv(FolURL2 + "/RPAPhoto/MJS_DensiSinkoku/" + "MasterDB.csv",\
        dtype={"TKCKokuzeiUserCode": str,"TKCTihouzeiUserID": str,"MirokuKokuzeiUserCode": str,"MirokuTihouzeiUserID": str,"etaxPass": str,"eltaxPass": str},encoding=SerchEnc)
    print(MasterCSV)
    try:
        MainFlow(FolURL2,PreList,NoList,MasterCSV,XmlList,fol_path)
    except:
        traceback.print_exc()
except:
    print('起動エラー')