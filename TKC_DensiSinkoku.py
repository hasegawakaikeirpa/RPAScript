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
import pyperclip #クリップボードへのコピーで使用
from logging import exception

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
def CSVOutPut(CSVURL,CSVName,driver,FolURL2):#TKCのCSVダイアログでの書出し操作
    #要素クリック----------------------------------------------------------------------------------------------------------
    Hub = "AutomationID"#取得要素種類を指定
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
    # pg.write(CSVURL, interval=0.01)#直接SENDできないのでpyautoguiで入力
    pyperclip.copy(CSVURL)
    pg.hotkey('ctrl', 'v')#pg日本語不可なのでコピペ
    pg.press(['return'])
    #----------------------------------------------------------------------------------------------------------------------
    #要素クリック----------------------------------------------------------------------------------------------------------
    Hub = "AutomationID"#取得要素種類を指定
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
    # pg.write(CSVName, interval=0.01)#直接SENDできないのでpyautoguiで入力
    pyperclip.copy(CSVName)
    pg.hotkey('ctrl', 'v')#pg日本語不可なのでコピペ
    pg.press(['return'])
    #----------------------------------------------------------------------------------------------------------------------
    #要素クリック----------------------------------------------------------------------------------------------------------
    Hub = "AutomationID"#取得要素種類を指定
    ObjName = "fileTypeComboBox"
    DriverClick(Hub,ObjName,driver)
    pg.press('down')
    pg.press('down')
    pg.press('down')
    pg.press('return')
    #----------------------------------------------------------------------------------------------------------------------
    #要素クリック----------------------------------------------------------------------------------------------------------
    Hub = "AutomationID"#取得要素種類を指定
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
        if Key == C_CAll and C_CSousin == "可":
            ItemList.append(C_CforCount)
            C_CforCount = C_CforCount + 1
        else:
            C_CforCount = C_CforCount + 1
    return ItemList
#----------------------------------------------------------------------------------------------------------------------
def TaxHantei(List,FolURL2,FileName,conf,LoopVal,CSVName,driver):#選択済と未選択状態のタブアイコンをクリックし、各税申告処理を分ける
    if ImgCheck(FolURL2,FileName,conf,LoopVal)[0] == True:
        if ImgCheckForList(FolURL2,List,conf)[0] == True:
            FindURL = ImgCheckForList(FolURL2,List,conf)[1]
            ImgClick(FolURL2,FindURL,conf,LoopVal)
        time.sleep(1)
    #----------------------------------------------------------------------------------------------------------------------
    time.sleep(1)
    #読込画面が消える(ImgCheck==False)まで待機-----------------------------------------------------------------------------
    FileName = "SinkokuLoad.png"
    time.sleep(1)
    while pg.locateOnScreen(FolURL2 + "/SinkokuLoad.png", confidence=0.9) is not None:
        time.sleep(1)
    time.sleep(1)
    #CSVOUT処理--------------------------------------------------------------------------------------------------------
    FileName = "NoCsvOutPut.png"
    conf = 0.9#画像認識感度
    time.sleep(1)
    if ImgNothingCheck(FolURL2,FileName,conf,10) == True:   
        FileName = "CsvOutPut.png"
        conf = 0.9#画像認識感度
        if ImgCheck(FolURL2,FileName,conf,LoopVal)[0] == True:
            ImgClick(FolURL2,FileName,conf,LoopVal)
            time.sleep(1)
            CSVURL = FolURL2
            CSVOutPut(CSVURL,CSVName,driver,FolURL2)
            C_url = CSVURL.replace("\\","/") + '/' + CSVName + '.CSV'
            C_Array = pd.read_csv(C_url,encoding='shiftjis')
            return C_Array,True
        else:
            print("ChildCSV無")
            return [],False           
    else:
        print("ChildCSV無")
        return [],False
    #------------------------------------------------------------------------------------------------------------------
def Sousin(driver,FolURL2,ItemRowArray,CSVName):
    if CSVName == 'SinseiMaster':
    #要素クリック----------------------------------------------------------------------------------------------------------
        while pg.locateOnScreen(FolURL2 + "/SinseiSousin.png",confidence= 0.9) is None:
            time.sleep(1)
            if ImgCheck(FolURL2,"TihouAnsyou.png",0.9,5)[0] == True:
                time.sleep(1)
                ImgClick(FolURL2,"TihouAnsyou.png",0.9,3)
                time.sleep(1)
                pg.write("Ha47K05121", interval=0.01)#直接SENDできないのでpyautoguiで入力
                pg.press('return')
                time.sleep(1)
                pg.press('return')
                time.sleep(1)
            if ImgCheck(FolURL2,"KokuzeiAnsyou.png",0.9,5)[0] == True:
                time.sleep(1)
                ImgClick(FolURL2,"KokuzeiAnsyou.png",0.9,3)
                time.sleep(1)
                pg.write("Ha47K05121", interval=0.01)#直接SENDできないのでpyautoguiで入力
                pg.press('return')
                time.sleep(1)
                pg.press('return')
                time.sleep(1)
        if ImgCheck(FolURL2,"SinseiSousin.png",0.9,5)[0] == True:
            time.sleep(1)
            pg.press('n')
            time.sleep(1)
            FileName = "SumiIcon.png"
            NonImgClickKeep(FolURL2,FileName)
    else:
    #要素クリック----------------------------------------------------------------------------------------------------------
        Hub = "AutomationID"#取得要素種類を指定
        ObjName = "etaxPasswordTextBox"
        DriverClick(Hub,ObjName,driver)#一括電子申告起動ボタン2を押す
        conf = 0.9
        LoopVal = 10000
        FileName = "ZeirisiAnsyou.png"
        ZeiresiAnsyou = ImgCheck(FolURL2,FileName,conf,LoopVal)[0] #== True:
        if ZeiresiAnsyou == True:
            FileName = "ZeirisiAnsyou.png"
            ImgClick(FolURL2,FileName,conf,LoopVal)
            pg.write("Ha47K05121", interval=0.01)#直接SENDできないのでpyautoguiで入力
            pg.press('return')
        time.sleep(5)
        conf = 0.9
        LoopVal = 10000
        FileName = "ZeirisiAnsyouT.png"
        ZeiresiAnsyouT = ImgCheck(FolURL2,FileName,conf,LoopVal)[0] #== True:
        if ZeiresiAnsyouT == True:
            FileName = "ZeirisiAnsyouT.png"
            ImgClick(FolURL2,FileName,conf,LoopVal)
            pg.write("Ha47K05121", interval=0.01)#直接SENDできないのでpyautoguiで入力
            pg.press('return')
        #----------------------------------------------------------------------------------------------------------------------
        #要素クリック----------------------------------------------------------------------------------------------------------
        Hub = "AutomationID"#取得要素種類を指定
        ObjName = "ltaxPasswordTextBox"
        DriverClick(Hub,ObjName,driver)#一括電子申告起動ボタン2を押す
        conf = 0.9
        LoopVal = 10
        FileName = "TihouzeiOK.png"
        if ImgCheck(FolURL2,FileName,conf,LoopVal)[0] == False:
            pg.write("Ha47K05121", interval=0.01)#直接SENDできないのでpyautoguiで入力
            pg.press('return')
        #----------------------------------------------------------------------------------------------------------------------
        #要素クリック----------------------------------------------------------------------------------------------------------
        Hub = "AutomationID"#取得要素種類を指定
        ObjName = "okButton"
        DriverClick(Hub,ObjName,driver)#一括電子申告起動ボタン2を押す
        #----------------------------------------------------------------------------------------------------------------------            
        time.sleep(1)
        FileName = "SousinKanryou.png"
        while pg.locateOnScreen(FolURL2 + "/" + FileName, confidence=0.9) is None:
            time.sleep(1)
        time.sleep(1)
        pg.press('n')
        conf = 0.9
        LoopVal = 10
        FileName = "KanryouHoukokuBtn2.png"
        while pg.locateOnScreen(FolURL2 + "/" + FileName, confidence=0.9) is None:
            time.sleep(1)
        time.sleep(1)
        FileName = "SumiIcon.png"
        NonImgClickKeep(FolURL2,FileName)
#----------------------------------------------------------------------------------------------------------------------
def SinSousin(driver,FolURL2,ItemRowArray):
    #要素クリック----------------------------------------------------------------------------------------------------------
    while pg.locateOnScreen(FolURL2 + "/" + "SinseiLogin.png", confidence=0.9) is None:
        time.sleep(1)
    pg.write("Ha47K05121", interval=0.01)#直接SENDできないのでpyautoguiで入力
    pg.press('return')
    pg.press('return')
    #----------------------------------------------------------------------------------------------------------------------          
    time.sleep(1)
    FileName = "SousinKanryou.png"
    while pg.locateOnScreen(FolURL2 + "/" + FileName, confidence=0.9) is None:
        time.sleep(1)
    time.sleep(1)
    pg.press('n')
    conf = 0.9
    LoopVal = 10
    FileName = "KanryouHoukokuBtn2.png"
    while pg.locateOnScreen(FolURL2 + "/" + FileName, confidence=0.9) is None:
        time.sleep(1)
    time.sleep(1)
    FileName = "SumiIcon.png"
    NonImgClickKeep(FolURL2,FileName)

#----------------------------------------------------------------------------------------------------------------------
def NonImgClickKeep(FolURL2,FileName):
    try:
        while all(pg.locateOnScreen(FolURL2 + "/" + FileName, confidence=0.9)) == True:
            conf = 0.9#画像認識感度
            LoopVal = 10
            xpos = ImgCheck(FolURL2,FileName,conf,LoopVal)[1]
            ypos = ImgCheck(FolURL2,FileName,conf,LoopVal)[2]
            pg.click(xpos, ypos,1, 0,'left') #送信「可」を選択
            time.sleep(1)
    except:
        return True
#----------------------------------------------------------------------------------------------------------------------
def NoBlue(FolURL2):
    try:
        for x in range(5):
            while pg.locateOnScreen(FolURL2 + "/Ka.png", confidence=0.9) is not None:
                ImgClick(FolURL2,"Ka.png",0.9,1)
                time.sleep(1)
            pg.press('pagedown')
        for x in range(5):
            pg.press('pageup')
    except:
        exception
#----------------------------------------------------------------------------------------------------------------------
def MasterLoop(List,FileName,CSVName,CSVChildName,C_Master,C_dfRow,C_dfCol,driver,FolURL2):
    C_forCount = 0
    NoAction = False
    #----------------------------------------------------------------------------------------------------------------------
    #切出MasterCSVをループ処理---------------------------------------------------------------------------------------------
    for x in range(C_dfRow):
        #関与先DB配列をループして識別番号とPassを取得
        if CSVName == 'SinseiMaster':#処理が申請の場合
            C_dfDataRow = C_Master.iloc[x,:]
            C_SCode = C_dfDataRow["関与先コード"]
            C_Name = C_dfDataRow["納税者(関与先)"]
            C_Zeimoku = C_dfDataRow["申請・届出書類名"]
            C_Sousin = C_dfDataRow["送信"]
            C_All =  str(C_SCode) + str(C_Name) 
#元ネタ列名"→"行","事務所コード","関与先コード","納税者(関与先)","決算月","申請・届出書類名","提出先","電子申請データ作成","電子署名(納税者)","電子署名(税理士)","送信","申請受付日時","即時通知","受信通知","送付書","提出期限","報告書","実践報告","監査担当者"
        else:
            C_dfDataRow = C_Master.iloc[x,:]
            C_SCode = C_dfDataRow["関与先コード"]
            C_Name = C_dfDataRow["納税者(関与先)"]
            C_Zeimoku = C_dfDataRow["税目"]
            C_Sousin = C_dfDataRow["送信"]
            C_All =  str(C_SCode) + str(C_Name) 
#元ネタ列名"→行","事務所コード","関与先コード","納税者(関与先)","決算月","税目","申告区分","電子申告データ作成","事業年度／課税期間","電子署名(添付書面)","電子署名(納税者)","電子署名(税理士)","送信","申告受付日時","即時通知","受信通知","送付書","申告期限","完了目標(3日前まで)","期限内","TISC","報告書","実践報告","監査担当者"
        
        
        if not C_SCode == 82:
        
        
            #申請処理----------------------------------------------------------------------------------------------------------
            conf = 0.9#画像認識感度
            LoopVal = 10
            if NoAction == False:#前周で操作した場合ChildCSVを再切出し
                C_Child = TaxHantei(List,FolURL2,FileName,conf,LoopVal,CSVChildName,driver)
            C_CdfRow = np.array(C_Child[0]).shape[0]#配列行数取得
            C_CdfCol = np.array(C_Child[0]).shape[1]#配列列数取得
            C_CforCount = 0
            #-------------------------------------------------------------------------------------------------------------------
            if CSVName == 'SinseiMaster':
                if C_Sousin == "可":
                    ItemRowArray = SortCSVItem(C_Child[0],"関与先コード","納税者(関与先)","申請・届出書類名","送信",C_All)
                    for ItemRow in ItemRowArray:
                        #Target選択の為にページダウンが必要か行数から割り出す-------------------------------------------------------------------------------------------
                        if ItemRow >= 13: #取得した行数が13以上なら
                            Pc = ItemRow/13 #取得した行数を13で除する
                            for p in range(int(Pc)):#13で除した整数分処理
                                pg.press('pagedown')
                                ItemNextRow = (ItemRow - (13*int(Pc)))#ページダウン後のTargetの行数を計算
                        FileName = "AnotherTrigger.png"
                        conf = 0.9#画像認識感度
                        LoopVal = 10
                        xpos = ImgCheck(FolURL2,FileName,conf,LoopVal)[1]
                        ypos = ImgCheck(FolURL2,FileName,conf,LoopVal)[2] + 60
                        if ItemRow >= 13: #取得した行数が13以上なら
                            ypos = ypos + (ItemNextRow*30)
                        else:
                            ypos = ypos + (ItemRow*30)
                        pg.click(xpos, ypos,1, 0,'left') #送信「可」を選択
                        time.sleep(1)
                        if ItemRow >= 13: #取得した行数が13以上なら                        
                            for p in range(int(Pc)):#13で除した整数分処理
                                pg.press('pageup')
                    #要素クリック------------------------------------------------------------------------------------------------
                    Hub = "AutomationID"#取得要素種類を指定
                    ObjName = "soshinButton"
                    DriverClick(Hub,ObjName,driver)#電子申告送信ボタンを押す
                    #------------------------------------------------------------------------------------------------------------
                    #送信エラー画像判定------------------------------------------------------------------------------------------
                    List = ["SousinErr.png","SousinErr2.png"]#送信エラーウィンドウ画像を2つ指定
                    ErrMsg = ""
                    if ImgCheckForList(FolURL2,List,conf)[0] == True:#リスト内の画像があればTrueと画像名を返す
                        pg.press('return')
                        ErrMsg = "送信エラー"
                        time.sleep(1)
                    #------------------------------------------------------------------------------------------------------------
                    if ErrMsg == "送信エラー":
                        FileName = "jimusyoCD.png"#画面左上の事務所コード画像を元に読込判定
                        conf = 0.9#画像認識感度
                        LoopVal = 10#検索回数
                        if ImgCheck(FolURL2,FileName,conf,LoopVal)[0] == True:
                            print("送信エラーをスキップしました。")
                        LoopVal = 10#検索回数
                    else:
                        print("送信エラー無")
                        Sousin(driver,FolURL2,ItemRowArray,CSVName)
                else:
                    NoAction = True
                    print("送信不可")
            else:
                if C_Sousin == "可":
                    ItemRowArray = SortCSVItem(C_Child[0],"関与先コード","納税者(関与先)","税目","送信",C_All)
                    for ItemRow in ItemRowArray:
                        #Target選択の為にページダウンが必要か行数から割り出す-------------------------------------------------------------------------------------------
                        if ItemRow >= 13: #取得した行数が13以上なら
                            Pc = ItemRow/13 #取得した行数を13で除する
                            for p in range(int(Pc)):#13で除した整数分処理
                                pg.press('pagedown')
                                ItemNextRow = (ItemRow - (13*int(Pc)))#ページダウン後のTargetの行数を計算
                        FileName = "AnotherTrigger.png"
                        conf = 0.9#画像認識感度
                        LoopVal = 10
                        xpos = ImgCheck(FolURL2,FileName,conf,LoopVal)[1]
                        ypos = ImgCheck(FolURL2,FileName,conf,LoopVal)[2] + 60
                        if ItemRow >= 13: #取得した行数が13以上なら
                            ypos = ypos + (ItemNextRow*30)
                        else:
                            ypos = ypos + (ItemRow*30)
                        pg.click(xpos, ypos,1, 0,'left') #送信「可」を選択
                        time.sleep(1)
                        if ItemRow >= 13: #取得した行数が13以上なら                        
                            for p in range(int(Pc)):#13で除した整数分処理
                                pg.press('pageup')
                    #要素クリック------------------------------------------------------------------------------------------------
                    Hub = "AutomationID"#取得要素種類を指定
                    ObjName = "soshinButton"
                    DriverClick(Hub,ObjName,driver)#電子申告送信ボタンを押す
                    #------------------------------------------------------------------------------------------------------------
                    #送信エラー画像判定------------------------------------------------------------------------------------------
                    List = ["SousinErr.png","SousinErr2.png"]#送信エラーウィンドウ画像を2つ指定
                    ErrMsg = ""
                    if ImgCheckForList(FolURL2,List,conf)[0] == True:#リスト内の画像があればTrueと画像名を返す
                        pg.press('return')
                        ErrMsg = "送信エラー"
                        time.sleep(1)
                    #------------------------------------------------------------------------------------------------------------
                    if ErrMsg == "送信エラー":
                        FileName = "jimusyoCD.png"#画面左上の事務所コード画像を元に読込判定
                        conf = 0.9#画像認識感度
                        LoopVal = 10#検索回数
                        if ImgCheck(FolURL2,FileName,conf,LoopVal)[0] == True:
                            print("送信エラーをスキップしました。")
                        LoopVal = 10#検索回数
                    else:
                        print("送信エラー無")
                        Sousin(driver,FolURL2,ItemRowArray,CSVName)
                else:
                    NoAction = True
                    print("送信不可")
#メイン処理----------------------------------------------------------------------------------------------------------------------
def MainFlow(FolURL2):
    BatUrl = FolURL2 + "/bat/AWADriverOpen.bat"#4724ポート指定でappiumサーバー起動バッチを開く
    driver = OMSOpen.MainFlow(BatUrl,FolURL2,"RPAPhoto")#OMSを起動しログイン後インスタンス化
    FolURL2 = FolURL2 + "/RPAPhoto/TKC_DensiSinkoku"#画像格納フォルダ
    #----------------------------------------------------------------------------------------------------------------------
    #要素クリック----------------------------------------------------------------------------------------------------------
    Hub = "AutomationID"#取得要素種類を指定
    ObjName = "um12PictureButton"#取得要素Nameを指定
    DriverClick(Hub,ObjName,driver)#一括電子申告ボタンを押す
    #----------------------------------------------------------------------------------------------------------------------
    #要素クリック----------------------------------------------------------------------------------------------------------
    FileName = "DensiSinkokuHub.png"
    conf = 0.9#画像認識感度
    LoopVal = 10#検索回数
    ImgClick(FolURL2,FileName,conf,LoopVal)#電子申告・申請タブを押す
    #----------------------------------------------------------------------------------------------------------------------
    #要素クリック----------------------------------------------------------------------------------------------------------
    Hub = "AutomationID"#取得要素種類を指定
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
    Hub = "AutomationID"#取得要素種類を指定    
    ObjName = "taxAccountantComboBox"#税理士選択コンボボックスをクリック
    DriverClick(Hub,ObjName,driver)
    time.sleep(1)
    pg.press('down')
    pg.press('return')#小林常務を選択
    # # FileName = "KanyoHasegawa.png"#担当税理士所長判定
    # #法人税消費税処理------------------------------------------------------------------------------------------------------
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
    #     NoBlue(FolURL2)
    #     C_Master = C_Master [C_Master['送信']=='可']#送信列「可」のみ抽出
    #     C_Master = C_Master.drop_duplicates(subset='関与先コード')#関与先コードをキーに重複削除
    #     C_dfRow = np.array(C_Master).shape[0]#配列行数取得
    #     C_dfCol = np.array(C_Master).shape[1]#配列列数取得
    #     print(C_Master)
    #     MasterLoop(List,FileName,CSVName,CSVChildName,C_Master,C_dfRow,C_dfCol,driver,FolURL2) 
    # #----------------------------------------------------------------------------------------------------------------------
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
    #    NoBlue(FolURL2)
    #    C_Master = C_Master[C_Master['送信']=='可']#送信列「可」のみ抽出
    #    C_Master = C_Master.drop_duplicates(subset='関与先コード')#関与先コードをキーに重複削除
    #    C_dfRow = np.array(C_Master).shape[0]#配列行数取得
    #    C_dfCol = np.array(C_Master).shape[1]#配列列数取得
    #    MasterLoop(List,FileName,CSVName,CSVChildName,C_Master,C_dfRow,C_dfCol,driver,FolURL2)
    #    
    ##-----------------------------------------------------------------------------------------------------------------------
    # #法定調書給報処理------------------------------------------------------------------------------------------------------
    # FileName = "KanyoZeirisi.png"#担当税理士小林常務判定
    # conf = 0.9#画像認識感度
    # LoopVal = 500
    # CSVName = 'HouteiKyuuhouMaster'
    # CSVChildName = 'HouteiKyuuhouChild'#チャイルドのCSVファイル名を指定
    # List = ["HouteiKyuuhou.png","HouteiKyuuhou2.png"]
    # TaxAns = TaxHantei(List,FolURL2,FileName,conf,LoopVal,CSVName,driver)#pandasにマスターCSVぶっこみ
    # C_Master = TaxAns[0]
    # C_MasterFlag = TaxAns[1]
    # if C_MasterFlag == False:
    #     print("C_Masterは空です")
    # else:
    #     NoBlue(FolURL2)
    #     C_Master = C_Master [C_Master['送信']=='可']#送信列「可」のみ抽出
    #     C_Master = C_Master.drop_duplicates(subset='関与先コード')#関与先コードをキーに重複削除
    #     C_dfRow = np.array(C_Master).shape[0]#配列行数取得
    #     C_dfCol = np.array(C_Master).shape[1]#配列列数取得
    #     print(C_Master)
    #     MasterLoop(List,FileName,CSVName,CSVChildName,C_Master,C_dfRow,C_dfCol,driver,FolURL2)
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
    #     NoBlue(FolURL2)  
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
    #     NoBlue(FolURL2)  
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
    #     NoBlue(FolURL2)  
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
    #     NoBlue(FolURL2)  
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
        NoBlue(FolURL2)
        C_Master = C_Master[C_Master['送信']=='可']#送信列「可」のみ抽出
        C_Master = C_Master.drop_duplicates(subset='関与先コード')#関与先コードをキーに重複削除
        C_dfRow = np.array(C_Master).shape[0]#配列行数取得
        C_dfCol = np.array(C_Master).shape[1]#配列列数取得
        MasterLoop(List,FileName,CSVName,CSVChildName,C_Master,C_dfRow,C_dfCol,driver,FolURL2)     
    #-----------------------------------------------------------------------------------------------------------------------

#RPA用画像フォルダの作成---------------------------------------------------------
FolURL = "//Sv05121a/e/C 作業台/RPA/ALLDataBase/RPAPhoto/TKC_DensiSinkoku"#元
FolURL2 = os.getcwd().replace('\\','/')#先
#--------------------------------------------------------------------------------
try:
    MainFlow(FolURL2)
except:
    traceback.print_exc()