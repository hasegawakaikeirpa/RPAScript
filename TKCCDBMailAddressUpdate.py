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
def CSVOutFind(wsRow,LogList):#登録ログに同一データがないかチェック
    try:
        #行データから変数格納----------------------------------------------------------------------------------------
        wsgyo = wsRow['行']
        wscd = wsRow['コード']
        wsName = wsRow['関与先名']
        wsKa = wsRow['課']
        wsTno = wsRow['No.']
        wsTname = wsRow['監査担当']
        wsSubTno = wsRow['サブNo.']
        wsSubTname = wsRow['会計サブ']
        wsAd = wsRow['アドレス']
        wsHassou = wsRow['発送方法']
        wsNyuu = wsRow['入力日時']
        wsUser = wsRow['入力ユーザー']
        wsDno = wsRow['データNo']
        #----------------------------------------------------------------------------------------------------------
        CSVLenRow = np.array(LogList).shape[0]#dfインスタンスの行数取得
        for x in range(CSVLenRow):
            CSVRow = LogList.iloc[x]#dfインスタンスの行データ
            #行データから変数格納----------------------------------------------------------------------------------------
            CSVgyo = CSVRow['行']
            CSVcd = CSVRow['コード']
            CSVName = CSVRow['関与先名']
            CSVKa = CSVRow['課']
            CSVTno = CSVRow['No.']
            CSVTname = CSVRow['監査担当']
            CSVSubTno = CSVRow['サブNo.']
            CSVSubTname = CSVRow['会計サブ']
            CSVAd = CSVRow['アドレス']
            CSVHassou = CSVRow['発送方法']
            CSVNyuu = CSVRow['入力日時']
            #文字列日付をDate格納----------------------------------------------------------------------------------------
            try:
                CSVNyuu = dt.strptime(CSVNyuu, '%Y/%m/%d %H:%M')
            except:
                try:
                    CSVNyuu = dt.strptime(CSVNyuu, '%Y/%m/%d %H:%M:%S')
                except:
                    try:
                        CSVNyuu = dt.strptime(CSVNyuu, '%Y-%m-%d %H:%M:%S')
                    except:
                        CSVNyuu = dt.strptime(CSVNyuu, '%Y-%m-%d %H:%M')
            #----------------------------------------------------------------------------------------------------------
            CSVUser = CSVRow['入力ユーザー']
            CSVDno = CSVRow['データNo']
            #----------------------------------------------------------------------------------------------------------
            if wscd == CSVcd:#登録済みリストに同一コードがあったら
                if wsAd == CSVAd:#登録済みリストに同一アドレスがあったら
                    if wsNyuu == CSVNyuu:#登録済みリストと同一の登録日時なら
                        return True
                else:
                    if wsNyuu > CSVNyuu:#登録済みリストより後の登録日時なら
                        return False                  
        return False
    except:
        return False
#----------------------------------------------------------------------------------------------------------------------
def CDBOpen(FolURL2,Lday,driver,ws,XlsmURL):
    try:
        #CDB開始ボタンクリック-------------------------------------------------------------------------------------------
        Hub = "AutomationID"
        ObjName = "um8PictureButton"
        DriverClick(Hub,ObjName,driver)
        #--------------------------------------------------------------------------------------------------------------
        while pg.locateOnScreen(FolURL2 + "/CDBMenuBar.png", confidence=0.9) is None:#CDBのメニューバー検知まで待機
            time.sleep(1)
        #--------------------------------------------------------------------------------------------------------------
        LenRow = np.array(ws).shape[0]#dfインスタンスの行数取得
        for x in range(LenRow):
            CSVURL = "\\Sv05121a\e\C 作業台\RPA\ALLDataBase\m_kfmsrireki.csv"
            CSVURL = CSVURL.replace("\\","/")#URLリネーム
            CSVURL = "/" + CSVURL
            LogList = CSVOut.CsvRead(CSVURL)
            wsRow = ws.iloc[x]#dfインスタンスの行データ
            #行データから変数格納----------------------------------------------------------------------------------------
            wscd = wsRow['コード']
            wsName = wsRow['個人名']
            wsKName = wsRow['関与先名']
            wsHassou = wsRow['発送方法']
            wsSousin = wsRow['送信方法']
            wsAd = wsRow['アドレス']
            wsKano = wsRow['課No']
            wsKa = wsRow['課']
            wsTno = wsRow['監査担当No']
            wsTname = wsRow['監査担当']
            wsSubTno = wsRow['サブNo']
            wsSubTname = wsRow['サブ']
            wsSubTno2 = wsRow['サブ2No']
            wsSubTname2 = wsRow['サブ2']            
            wsSousin2 = wsRow['送信方法2']
            wsAd2 = wsRow['アドレス2']
            wsSousin3 = wsRow['送信方法3']
            wsAd3 = wsRow['アドレス3']
            wsSousin4 = wsRow['送信方法4']
            wsAd4 = wsRow['アドレス4']
            wsSousin5 = wsRow['送信方法5']
            wsAd5 = wsRow['アドレス5']
            #,ParList,0
            #,ParList,"",'m_kfmsrireki')
            wsNyuu = wsRow['入力日時']
            wsUser = wsRow['入力ユーザー']
            wsDno = wsRow['変更前アドレス']
            #----------------------------------------------------------------------------------------------------------
            ImgClick(FolURL2,"JimusyoCD.png",0.9,5)#事務所コードボックスをクリック
            time.sleep(1)
            #所内コードに応じて処理分け-----------------------------------------------------------------------------------
            if int(wscd) >= 0 and int(wscd) < 1000:
                #----------------------------------------------------------------------------------------------------------
                NList = ["05121.png","05121b.png"]
                ICFL = ImgCheckForList(FolURL2,NList,0.9)
                if ICFL[0] == True:
                    ImgClick(FolURL2,ICFL[1],0.9,1)
                    if int(wscd) < 100:
                        wscd = f'{wscd:03}' 
                #----------------------------------------------------------------------------------------------------------
            elif int(wscd) >= 4000 and int(wscd) < 5000:
                NList = ["05371.png","05371b.png"]
                ICFL = ImgCheckForList(FolURL2,NList,0.9)
                if ICFL[0] == True:
                    ImgClick(FolURL2,ICFL[1],0.9,1)
                    wscd = int(wscd)-4000
                    if int(wscd) < 100:
                        wscd = f'{wscd:03}' 
                #----------------------------------------------------------------------------------------------------------
            elif int(wscd) >= 1000 and int(wscd) < 4000:
                NList = ["15180.png","15180b.png"]
                ICFL = ImgCheckForList(FolURL2,NList,0.9)
                if ICFL[0] == True:
                    ImgClick(FolURL2,ICFL[1],0.9,1)
                    wscd = int(wscd)-1000
                    if int(wscd) < 100:
                        wscd = f'{wscd:03}' 
                #----------------------------------------------------------------------------------------------------------
            elif int(wscd) >= 9000 and int(wscd) < 9999:
                NList = ["99999.png","99999b.png"]
                ICFL = ImgCheckForList(FolURL2,NList,0.9)
                if ICFL[0] == True:
                    ImgClick(FolURL2,ICFL[1],0.9,1)
                    wscd = int(wscd)-9000
                    if int(wscd) < 100:
                        wscd = f'{wscd:03}' 
                #----------------------------------------------------------------------------------------------------------
            elif int(wscd) >= 10000:
                NList = ["05121.png","05121b.png"]
                ICFL = ImgCheckForList(FolURL2,NList,0.9)
                if ICFL[0] == True:
                    ImgClick(FolURL2,ICFL[1],0.9,1)
            #--------------------------------------------------------------------------------------------------------------
            time.sleep(2)
            pg.write(str(wscd))#TKC用に変換した関与先コードを入力
            pg.press('return')#確定
            time.sleep(1)
            while pg.locateOnScreen(FolURL2 + "/CDBAddBtn.png",0.9) is None:#追加・修正ボタン表示まで待機
                time.sleep(1)
            time.sleep(1)
            ImgClick(FolURL2,"CDBAddBtn.png",0.9,5)#追加・修正ボタンクリック
            time.sleep(1)
            while pg.locateOnScreen(FolURL2 + "/InputEnd.png",0.9) is None:#入力終了ボタン表示まで待機
                time.sleep(1)
            time.sleep(1)
            if int(wscd) >= 10000:
                EMI = ImgCheck(FolURL2,"EMailIconK.png",0.9,5)#EMAILテキストボックス画像を判定
            else:
                EMI = ImgCheck(FolURL2,"EMailIcon.png",0.9,5)#EMAILテキストボックス画像を判定
            if EMI[0] == True:
                pg.click(EMI[1] + 100,EMI[2])#EMAILテキストボックス画像中央より右+100座標をクリック
                time.sleep(1)
                #変更前アドレスを保存して削除--------------------
                pyperclip.copy("")#クリップクリア
                pg.hotkey('ctrl','a')#テキスト全選択
                pg.hotkey('ctrl','c')#クリップにコピー
                LostAdd = pyperclip.paste()#変更前アドレスを保管
                pg.press('delete')#CDBのアドレスを削除
                #--------------------------------------------
                time.sleep(1)
                #アドレスがnanか判定して処理分け--------------------------------------------
                try:
                    if np.isnan(wsAd) == True:
                        print('nan')
                    else:
                        pyperclip.copy(wsAd)#クリップに変更後アドレスをコピー
                        pg.hotkey('ctrl','v')#CDBにペースト
                        pg.press('return')#確定
                        time.sleep(1)
                except:
                    pyperclip.copy(wsAd)#クリップに変更後アドレスをコピー
                    pg.hotkey('ctrl','v')#CDBにペースト
                    pg.press('return')#確定
                    time.sleep(1)
                #------------------------------------------------------------------------                    
                ImgClick(FolURL2,"InputEnd.png",0.9,5)#入力終了ボタンをクリック
                time.sleep(1)
                while pg.locateOnScreen(FolURL2 + "/CDBAddBtn.png",0.9) is None:
                    time.sleep(1)
                time.sleep(1)
                #CSVログに追加------------------------------------------------------------------------------------------------
                USQL = "UPDATE m_kfmsrireki SET vc_gyou = 'CDB' WHERE vc_FMSKnrCd = '" + wscd + "';"
                SQ.MySQLAct('ws77','SYSTEM','SYSTEM',3306,'test_db','utf8',USQL)
                SQC.MailRirekiUp()
                SQC.MailListUp()					
                # LogMSG = ['CDB',wscd,wsName,wsKa,wsTno,wsTname,wsSubTno,wsSubTname,wsAd,wsHassou,wsNyuu,wsUser,wsDno,LostAdd]
                # CSVOut.CsvPlus(CSVURL,LogList[1],LogMSG)#引数指定のCSV最終行に行データ追加
                time.sleep(1)
                return True
            else:
                print(wscd + "エラー") 
                return True
    except:
        print(x + "エラー") 
        return False
#---------------------------------------------------------------------------------------------------------------------- 
def SQLIn(ws):#Excelデータを履歴テーブルにインサート
    try:
        LenRow = np.array(ws).shape[0]#dfインスタンスの行数取得
        ColNS = SQ.MysqlColumnPic('ws77','SYSTEM','SYSTEM',3306,'test_db','utf8','m_kfmsrireki')
        LenColNRow = np.array(ColNS).shape[0]#dfインスタンスの行数取得
        ColN = []
        #テーブルのカラム情報より列名リスト作成-------------------------------------------------------------------------
        for ColNSItem in ColNS[1]:
            ColN.append(ColNSItem[0])
        ParList = []
        #-----------------------------------------------------------------------------------------------------------
        for x in range(LenRow):
            wsRow = ws.iloc[x]#dfインスタンスの行データ
            wscd = wsRow['コード']
            if int(wscd) < 100:
                wscd = f'{wscd:03}'  
            #WHERE社内コードでDBよりMAX(履歴No)を抽出-------------------------------------------------------------------------
            Maxsql = "SELECT MAX(in_RrkNo_pk) FROM m_kfmsrireki WHERE vc_FMSKnrCd = '" + wscd + "';" 
            MaxRrkNo = SQ.MySQLGet('ws77','SYSTEM','SYSTEM',3306,'test_db','utf8',Maxsql)
            if MaxRrkNo[0] == True:
                print(MaxRrkNo[1])
                if MaxRrkNo[1] == ((None,),):
                    MaxRrkNo = 1
                else:
                    Mstr = str(MaxRrkNo[1]).replace('((','').replace(',),)','')
                    MaxRrkNo = int(Mstr) + 1
            else:
                MaxRrkNo = 1
            #テーブルのデータ型に合わせて値を格納したリストを作成---------------------------------------------------------------
            SQ.ChangeData('vc_gyou',ParList,"",'m_kfmsrireki')
            ParList.append(MaxRrkNo)
            SQ.ChangeData('vc_FMSKnrCd',ParList,wscd,'m_kfmsrireki')
            SQ.ChangeData('vc_Name',ParList,wsRow['個人名'],'m_kfmsrireki')
            SQ.ChangeData('vc_KName',ParList,wsRow['関与先名'],'m_kfmsrireki')
            SQ.ChangeData('vc_Hakkou',ParList,wsRow['発送方法'],'m_kfmsrireki')
            SQ.ChangeData('vc_SousinK',ParList,wsRow['送信方法'],'m_kfmsrireki')
            SQ.ChangeData('vc_Mail',ParList,wsRow['アドレス'],'m_kfmsrireki')    
            SQ.ChangeData('vc_BmnCd_pk',ParList,wsRow['課No'] ,'m_kfmsrireki')
            SQ.ChangeData('vc_BmnNm',ParList,wsRow['課'],'m_kfmsrireki')
            SQ.ChangeData('vc_KansaTantouNo',ParList,wsRow['監査担当No'],'m_kfmsrireki')
            SQ.ChangeData('vc_KansaTantou',ParList,wsRow['監査担当'],'m_kfmsrireki')
            SQ.ChangeData('vc_SubTantouNo',ParList,wsRow['サブNo'],'m_kfmsrireki')
            SQ.ChangeData('vc_SubTantou',ParList,wsRow['サブ'],'m_kfmsrireki')
            SQ.ChangeData('vc_Sub_SubTantouNo',ParList,wsRow['サブ2No'],'m_kfmsrireki')
            SQ.ChangeData('vc_Sub_SubTantou',ParList,wsRow['サブ2'],'m_kfmsrireki')
            SQ.ChangeData('vc_SousinK2',ParList,wsRow['送信方法2'],'m_kfmsrireki')
            SQ.ChangeData('vc_Mail2',ParList,wsRow['アドレス2'],'m_kfmsrireki')
            SQ.ChangeData('vc_SousinK3',ParList,wsRow['送信方法3'],'m_kfmsrireki')
            SQ.ChangeData('vc_Mail3',ParList,wsRow['アドレス3'],'m_kfmsrireki')
            SQ.ChangeData('vc_SousinK4',ParList,wsRow['送信方法4'],'m_kfmsrireki')
            SQ.ChangeData('vc_Mail4',ParList,wsRow['アドレス4'],'m_kfmsrireki')
            SQ.ChangeData('vc_SousinK5',ParList,wsRow['送信方法5'],'m_kfmsrireki')
            SQ.ChangeData('vc_Mail5',ParList,wsRow['アドレス5'],'m_kfmsrireki')
            SQ.ChangeData('cr_RecKbn',ParList,0,'m_kfmsrireki')
            SQ.ChangeData('dt_InstDT',ParList,wsRow['入力日時'],'m_kfmsrireki')
            SQ.ChangeData('dt_UpdtDT',ParList,"",'m_kfmsrireki')
            SQ.ChangeData('vc_inputuser',ParList,wsRow['入力ユーザー'],'m_kfmsrireki')
            SQ.ChangeData('vc_beforeadd',ParList,wsRow['変更前アドレス'],'m_kfmsrireki')
            #----------------------------------------------------------------------------------------------------------
            ParList = str(ParList).replace('[','').replace(']','').replace('nan','')
            ColN = str(ColN).replace('[','').replace(']','').replace("'",'')
            sql = "INSERT INTO m_kfmsrireki (" + ColN + ") VALUES(" + ParList + ");"
            SQ.MySQLAct('ws77','SYSTEM','SYSTEM',3306,'test_db','utf8',sql)
            SQC.MailRirekiUp()
            SQC.MailListUp()
            ParList = []
        return True
    except:
        return False
#----------------------------------------------------------------------------------------------------------------------     
def MainFlow(FolURL2):
    BatUrl = FolURL2 + "/bat/AWADriverOpen.bat"#4724ポート指定でappiumサーバー起動バッチを開く
    driver = OMSOpen.MainFlow(BatUrl,FolURL2,"RPAPhoto")#OMSを起動しログイン後インスタンス化
    # driver = ""
    FolURL2 = FolURL2 + "/RPAPhoto/TKCCDBMailAddressUpdate"#RPA用画像保管フォルダを指定
    XlsmURL = "\\Sv05121a\e\C 作業台\請求書メールアドレス収集\アドレス新規登録シート.xlsm"#アドレス登録シートを指定
    XlsmURL = XlsmURL.replace("\\","/")#URLリネーム
    XlsmURL = "/" + XlsmURL#URLリネーム
    #エクセルブックを読込------------------------------------------------------------------------------------------------
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
    ws = ws.sort_values('入力日時', ascending=False)#入力日時順に並び替え
    ws = ws.drop_duplicates(subset='コード')#コードで重複削除
    print(ws)
    SQI = SQLIn(ws)
    #---------------------------------------------------------------------------------------------------------------------- 
    if SQI == True:
        CDBO = CDBOpen(FolURL2,Lday,driver,ws,XlsmURL)#CDBアクション開始
        if CDBO == True:
            print('CDBログインOK')
        else:
            print('CDBログイン失敗')
    else:
        print('履歴テーブル登録失敗')
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
import SQLConnect as SQ
import SQLCSVOUTFunction as SQC
#RPA用画像フォルダの作成-----------------------------------------------------------
Lday = calendar.monthrange(dt.today().year,dt.today().month)
FolURL = "//Sv05121a/e/C 作業台/RPA/ALLDataBase/RPAPhoto/TKC_DensiSinkoku"#元
FolURL2 = os.getcwd().replace('\\','/')#先
#--------------------------------------------------------------------------------
try:
    MainFlow(FolURL2)
except:
    traceback.print_exc()