# モジュールインポート
import pyautogui as pg
import time
import OMSOpen

# 配列計算関数numpyインポート
import numpy as np

# osインポート
import os

# datetimeインポート
from datetime import datetime as dt

# 例外処理判定の為のtracebackインポート
import traceback

# pandas(pd)で関与先データCSVを取得
import pyautogui
import Function.CSVOut as FCSV
import Function.ExcelFileAction as EF
import calendar
import pyperclip  # クリップボードへのコピーで使用
import Function.SQLConnect as SQ
import Function.SQLCSVOUTFunction as SQC

# logger設定------------------------------------------------------------------------------------------------------------
import logging.config

logging.config.fileConfig(r"LogConf\logging_debug.conf")
logger = logging.getLogger(__name__)
# ----------------------------------------------------------------------------------------------------------------------
def DriverUIWaitXPATH(UIPATH, driver):  # XPATH要素を取得するまで待機
    for x in range(1000):
        try:
            driver.find_element_by_xpath(UIPATH)
            Flag = 1
            return True
        except:
            Flag = 0
    if Flag == 0:
        return False


# ----------------------------------------------------------------------------------------------------------------------
def DriverUIWaitAutomationId(UIPATH, driver):  # XPATH要素を取得するまで待機
    for x in range(1000):
        try:
            driver.find_element_by_accessibility_id(UIPATH)
            Flag = 1
            return True
        except:
            Flag = 0
    if Flag == 0:
        return False


# ----------------------------------------------------------------------------------------------------------------------
def DriverUIWaitName(UIPATH, driver):  # XPATH要素を取得するまで待機
    for x in range(1000):
        try:
            driver.find_element_by_Name(UIPATH)
            Flag = 1
            return True
        except:
            Flag = 0
    if Flag == 0:
        return False


# ----------------------------------------------------------------------------------------------------------------------
def DriverUIWaitclassname(UIPATH, driver):  # XPATH要素を取得するまで待機
    for x in range(10000):
        try:
            driver.find_element_by_class_name(UIPATH)
            Flag = 1
            return True
        except:
            Flag = 0
    if Flag == 0:
        return False


# ----------------------------------------------------------------------------------------------------------------------
def DriverFindClass(UIPATH, driver):  # XPATH要素を取得するまで待機
    for x in range(10000):
        try:
            elList = driver.find_elements_by_class_name(UIPATH)
            Flag = 1
            return True, elList
        except:
            Flag = 0
    if Flag == 0:
        return False


# ----------------------------------------------------------------------------------------------------------------------
def DriverCheck(Hub, ObjName, driver):  # XPATH要素を取得するまで待機
    for x in range(1000):
        if Hub == "AutomationID":
            if (
                DriverUIWaitAutomationId(ObjName, driver) is True
            ):  # OMSメニューの年調起動ボタンを判定して初期処理分け
                # 正常待機後処理
                driver.find_element_by_accessibility_id(ObjName)  # 一括電子申告送信ボタン
                return True
            else:
                # 異常待機後処理
                print("要素取得に失敗しました。")
        elif Hub == "XPATH":
            if DriverUIWaitXPATH(ObjName, driver) is True:  # OMSメニューの年調起動ボタンを判定して初期処理分け
                # 正常待機後処理
                driver.find_element_by_xpath(ObjName)  # 一括電子申告送信ボタン
                return True
            else:
                # 異常待機後処理
                print("要素取得に失敗しました。")
        elif Hub == "Name":
            if DriverUIWaitName(ObjName, driver) is True:  # OMSメニューの年調起動ボタンを判定して初期処理分け
                # 正常待機後処理
                driver.find_element_by_Name(ObjName)  # 一括電子申告送信ボタン
                return True
            else:
                # 異常待機後処理
                print("要素取得に失敗しました。")


# ----------------------------------------------------------------------------------------------------------------------
def DriverClick(Hub, ObjName, driver):
    if Hub == "AutomationID":
        if (
            DriverUIWaitAutomationId(ObjName, driver) is True
        ):  # OMSメニューの年調起動ボタンを判定して初期処理分け
            # 正常待機後処理
            OMSObj = driver.find_element_by_accessibility_id(ObjName)  # 一括電子申告送信ボタン
            OMSObj.click()
            return OMSObj
        else:
            # 異常待機後処理
            print("要素取得に失敗しました。")
    elif Hub == "XPATH":
        if DriverUIWaitXPATH(ObjName, driver) is True:  # OMSメニューの年調起動ボタンを判定して初期処理分け
            # 正常待機後処理
            OMSObj = driver.find_element_by_xpath(ObjName)  # 一括電子申告送信ボタン
            OMSObj.click()
            return OMSObj
        else:
            # 異常待機後処理
            print("要素取得に失敗しました。")
    elif Hub == "Name":
        if DriverUIWaitName(ObjName, driver) is True:  # OMSメニューの年調起動ボタンを判定して初期処理分け
            # 正常待機後処理
            OMSObj = driver.find_element_by_Name(ObjName)  # 一括電子申告送信ボタン
            OMSObj.click()
            return OMSObj
        else:
            # 異常待機後処理
            print("要素取得に失敗しました。")
    elif Hub == "class_name":
        if DriverUIWaitclassname(ObjName, driver) is True:  # OMSメニューの年調起動ボタンを判定して初期処理分け
            # 正常待機後処理
            OMSObj = driver.find_element_by_class_name(ObjName)  # 一括電子申告送信ボタン
            OMSObj.click()
            return OMSObj
        else:
            # 異常待機後処理
            print("要素取得に失敗しました。")


# ----------------------------------------------------------------------------------------------------------------------
def ImgCheck(FolURL2, FileName, conf, LoopVal):  # 画像があればTrueを返す関数
    ImgURL = FolURL2 + "/" + FileName
    for x in range(LoopVal):
        try:
            p = pyautogui.locateOnScreen(ImgURL, confidence=conf)
            x, y = pyautogui.center(p)
            return True, x, y
        except:
            Flag = 0
    if Flag == 0:
        return False, "", ""


# ----------------------------------------------------------------------------------------------------------------------
def ImgNothingCheck(FolURL2, FileName, conf, LoopVal):  # 画像がなければTrueを返す
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


# ----------------------------------------------------------------------------------------------------------------------
def ImgCheckForList(FolURL2, List, conf):  # リスト内の画像があればTrueと画像名を返す
    for x in range(10):
        for ListItem in List:
            ImgURL = FolURL2 + "/" + ListItem
            try:
                p = pyautogui.locateOnScreen(ImgURL, confidence=conf)
                x, y = pyautogui.center(p)
                return True, ListItem
                break
            except:
                Flag = 0
    if Flag == 0:
        return False, ""


# ----------------------------------------------------------------------------------------------------------------------
def ImgClick(FolURL2, FileName, conf, LoopVal):  # 画像があればクリックしてx,y軸を返す
    ImgURL = FolURL2 + "/" + FileName
    for x in range(10):
        if (
            ImgCheck(FolURL2, FileName, conf, LoopVal)[0] is True
        ):  # OMSメニューの年調起動ボタンを判定して初期処理分け
            # 正常待機後処理
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
            # 異常待機後処理
            print("要素取得に失敗しました。")


# ----------------------------------------------------------------------------------------------------------------------
def CSVOutFind(wsRow, LogList):  # 登録ログに同一データがないかチェック
    try:
        # 行データから変数格納----------------------------------------------------------------------------------------
        wscd = wsRow["コード"]
        wsAd = wsRow["アドレス"]
        wsNyuu = wsRow["入力日時"]

        # ----------------------------------------------------------------------------------------------------------
        CSVLenRow = np.array(LogList).shape[0]  # dfインスタンスの行数取得
        for x in range(CSVLenRow):
            CSVRow = LogList.iloc[x]  # dfインスタンスの行データ
            # 行データから変数格納----------------------------------------------------------------------------------------
            CSVcd = CSVRow["コード"]
            CSVAd = CSVRow["アドレス"]
            CSVNyuu = CSVRow["入力日時"]
            # 文字列日付をDate格納----------------------------------------------------------------------------------------
            try:
                CSVNyuu = dt.strptime(CSVNyuu, "%Y/%m/%d %H:%M")
            except:
                try:
                    CSVNyuu = dt.strptime(CSVNyuu, "%Y/%m/%d %H:%M:%S")
                except:
                    try:
                        CSVNyuu = dt.strptime(CSVNyuu, "%Y-%m-%d %H:%M:%S")
                    except:
                        CSVNyuu = dt.strptime(CSVNyuu, "%Y-%m-%d %H:%M")
            # ----------------------------------------------------------------------------------------------------------
            if wscd == CSVcd:  # 登録済みリストに同一コードがあったら
                if wsAd == CSVAd:  # 登録済みリストに同一アドレスがあったら
                    if wsNyuu == CSVNyuu:  # 登録済みリストと同一の登録日時なら
                        return True
                else:
                    if wsNyuu > CSVNyuu:  # 登録済みリストより後の登録日時なら
                        return False
        return False
    except:
        return False


# ----------------------------------------------------------------------------------------------------------------------
def CDBOpen(FolURL2, Lday, driver, ws, XlsmURL):
    try:
        # CDB開始ボタンクリック-------------------------------------------------------------------------------------------
        Hub = "AutomationID"
        ObjName = "um8PictureButton"
        DriverClick(Hub, ObjName, driver)
        # --------------------------------------------------------------------------------------------------------------
        while (
            pg.locateOnScreen(FolURL2 + "/CDBMenuBar.png", confidence=0.9) is None
        ):  # CDBのメニューバー検知まで待機
            time.sleep(1)
        # --------------------------------------------------------------------------------------------------------------
        LenRow = np.array(ws).shape[0]  # dfインスタンスの行数取得
        for x in range(LenRow):
            CSVURL = r"\\Sv05121a\e\C 作業台\RPA\ALLDataBase\m_kfmsrireki.csv"
            CSVURL = CSVURL.replace("\\", "/")  # URLリネーム
            FCSV.CsvRead(CSVURL)
            wsRow = ws.iloc[x]  # dfインスタンスの行データ
            # 行データから変数格納----------------------------------------------------------------------------------------
            wscd = wsRow["コード"]
            wsUpcd = wsRow["コード"]
            wsAd = wsRow["アドレス"]
            # ----------------------------------------------------------------------------------------------------------
            ImgClick(FolURL2, "JimusyoCD.png", 0.9, 5)  # 事務所コードボックスをクリック
            time.sleep(1)
            # 所内コードに応じて処理分け-----------------------------------------------------------------------------------
            KFlag = False  # 個人判定フラグ
            if int(wscd) >= 0 and int(wscd) < 1000:
                # ----------------------------------------------------------------------------------------------------------
                NList = ["05121.png", "05121b.png"]
                ICFL = ImgCheckForList(FolURL2, NList, 0.9)
                if ICFL[0] is True:
                    ImgClick(FolURL2, ICFL[1], 0.9, 1)
                    if int(wscd) < 100:
                        try:
                            wscd = f"{wscd:03}"
                        except:
                            print("wscdエラー")
                # ----------------------------------------------------------------------------------------------------------
            elif int(wscd) >= 4000 and int(wscd) < 5000:
                NList = ["05371.png", "05371b.png"]
                ICFL = ImgCheckForList(FolURL2, NList, 0.9)
                if ICFL[0] is True:
                    ImgClick(FolURL2, ICFL[1], 0.9, 1)
                    wscd = int(wscd) - 4000
                    if int(wscd) < 100:
                        try:
                            wscd = f"{wscd:03}"
                        except:
                            print("wscdエラー")
                # ----------------------------------------------------------------------------------------------------------
            elif int(wscd) >= 1000 and int(wscd) < 2000:
                if len(wscd) == 5:
                    KFlag = True
                    NList = ["05121.png", "05121b.png"]
                    ICFL = ImgCheckForList(FolURL2, NList, 0.9)
                    if ICFL[0] is True:
                        ImgClick(FolURL2, ICFL[1], 0.9, 1)
                    time.sleep(1)
                else:
                    NList = ["15180.png", "15180b.png"]
                    ICFL = ImgCheckForList(FolURL2, NList, 0.9)
                    if ICFL[0] is True:
                        ImgClick(FolURL2, ICFL[1], 0.9, 1)
                        wscd = int(wscd) - 1000
                        if int(wscd) < 100:
                            try:
                                wscd = f"{wscd:03}"
                            except:
                                print("wscdエラー")
                # ----------------------------------------------------------------------------------------------------------
            elif int(wscd) >= 9000 and int(wscd) < 9999:
                NList = ["99999.png", "99999b.png"]
                ICFL = ImgCheckForList(FolURL2, NList, 0.9)
                if ICFL[0] is True:
                    ImgClick(FolURL2, ICFL[1], 0.9, 1)
                    wscd = int(wscd) - 9000
                    if int(wscd) < 100:
                        try:
                            wscd = f"{wscd:03}"
                        except:
                            print("wscdエラー")
                # ----------------------------------------------------------------------------------------------------------
            elif int(wscd) >= 10000:
                KFlag = True
                if len(wscd) == 5:
                    NList = ["05121.png", "05121b.png"]
                    ICFL = ImgCheckForList(FolURL2, NList, 0.9)
                    if ICFL[0] is True:
                        ImgClick(FolURL2, ICFL[1], 0.9, 1)
                        wscd = str(wscd)
                        wscdL = wscd[3] + wscd[4]
                        wscd = wscd[0] + wscd[1] + wscd[2]
                        wscd = wscd + wscdL
                else:
                    wscd = str(wscd)
                    wscdL = wscd[4] + wscd[5]
                    wscd = wscd[1] + wscd[2] + wscd[3]
                    if int(wscd) >= 4000 and int(wscd) < 5000:
                        NList = ["05371.png", "05371b.png"]
                        ICFL = ImgCheckForList(FolURL2, NList, 0.9)
                    elif int(wscd) >= 1000 and int(wscd) < 2000:
                        NList = ["15180.png", "15180b.png"]
                        ICFL = ImgCheckForList(FolURL2, NList, 0.9)
                    elif int(wscd) >= 9000 and int(wscd) < 9999:
                        NList = ["99999.png", "99999b.png"]
                        ICFL = ImgCheckForList(FolURL2, NList, 0.9)
                    wscd = wscd + wscdL
            # --------------------------------------------------------------------------------------------------------------
            time.sleep(2)
            pg.write(str(wscd))  # TKC用に変換した関与先コードを入力
            pg.press("return")  # 確定
            time.sleep(1)
            while (
                pg.locateOnScreen(FolURL2 + "/CDBAddBtn.png", 0.9) is None
            ):  # 追加・修正ボタン表示まで待機
                time.sleep(1)
            time.sleep(1)
            ImgClick(FolURL2, "CDBAddBtn.png", 0.9, 5)  # 追加・修正ボタンクリック
            time.sleep(1)
            while (
                pg.locateOnScreen(FolURL2 + "/InputEnd.png", 0.9) is None
            ):  # 入力終了ボタン表示まで待機
                time.sleep(1)
            time.sleep(1)
            if KFlag is True:
                EMI = ImgCheck(FolURL2, "EMailIconK.png", 0.9, 5)  # EMAILテキストボックス画像を判定
            else:
                EMI = ImgCheck(FolURL2, "EMailIcon.png", 0.9, 5)  # EMAILテキストボックス画像を判定
            if EMI[0] is True:
                pg.click(EMI[1] + 100, EMI[2])  # EMAILテキストボックス画像中央より右+100座標をクリック
                time.sleep(1)
                # 変更前アドレスを保存して削除--------------------
                pyperclip.copy("")  # クリップクリア
                pg.hotkey("ctrl", "a")  # テキスト全選択
                pg.hotkey("ctrl", "c")  # クリップにコピー
                pyperclip.paste()  # 変更前アドレスを保管
                pg.press("delete")  # CDBのアドレスを削除
                # --------------------------------------------
                time.sleep(1)
                # アドレスがnanか判定して処理分け--------------------------------------------
                try:
                    if np.isnan(wsAd) is True:
                        print("nan")
                    else:
                        pyperclip.copy(wsAd)  # クリップに変更後アドレスをコピー
                        pg.hotkey("ctrl", "v")  # CDBにペースト
                        pg.press("return")  # 確定
                        time.sleep(1)
                except:
                    pyperclip.copy(wsAd)  # クリップに変更後アドレスをコピー
                    pg.hotkey("ctrl", "v")  # CDBにペースト
                    pg.press("return")  # 確定
                    time.sleep(1)
                # ------------------------------------------------------------------------
                ImgClick(FolURL2, "InputEnd.png", 0.9, 5)  # 入力終了ボタンをクリック
                time.sleep(1)
                while pg.locateOnScreen(FolURL2 + "/CDBAddBtn.png", 0.9) is None:
                    time.sleep(1)
                time.sleep(1)
                # CSVログに追加------------------------------------------------------------------------------------------------
                Maxsql = (
                    "SELECT MAX(in_RrkNo_pk) FROM m_kfmsrireki WHERE vc_FMSKnrCd = "
                    + str(wsUpcd)
                    + ";"
                )
                MaxRrkNo = SQ.MySQLGet(
                    "ws77", "SYSTEM", "SYSTEM", 3306, "test_db", "utf8", Maxsql
                )
                if MaxRrkNo[0] is True:
                    print(MaxRrkNo[1])
                    if MaxRrkNo[1] == ((None,),):
                        MaxRrkNo = 1
                    else:
                        Mstr = str(MaxRrkNo[1]).replace("((", "").replace(",),)", "")
                        MaxRrkNo = int(Mstr)
                else:
                    MaxRrkNo = 1

                USQL = (
                    "UPDATE m_kfmsrireki SET vc_gyou = 'CDB' WHERE vc_FMSKnrCd = "
                    + str(wsUpcd)
                    + " AND in_RrkNo_pk = "
                    + str(MaxRrkNo).replace("'", "")
                    + ";"
                )
                SQ.MySQLAct("ws77", "SYSTEM", "SYSTEM", 3306, "test_db", "utf8", USQL)
                SQC.MailRirekiUp()
                SQC.MailListUp()
                # LogMSG = ['CDB',wscd,wsName,wsKa,wsTno,wsTname,wsSubTno,wsSubTname,wsAd,wsHassou,wsNyuu,wsUser,wsDno,LostAdd]
                # FCSV.CsvPlus(CSVURL,LogList[1],LogMSG)#引数指定のCSV最終行に行データ追加
                time.sleep(1)
            else:
                print(str(wscd) + "エラー")
        return True
    except:
        print(str(x) + "エラー")
        return False


# ----------------------------------------------------------------------------------------------------------------------
def SQLIn(ws):  # Excelデータを履歴テーブルにインサート
    try:
        LenRow = np.array(ws).shape[0]  # dfインスタンスの行数取得
        ColNS = SQ.MysqlColumnPic(
            "ws77", "SYSTEM", "SYSTEM", 3306, "test_db", "utf8", "m_kfmsrireki"
        )
        ColN = []
        # テーブルのカラム情報より列名リスト作成-------------------------------------------------------------------------
        for ColNSItem in ColNS[1]:
            ColN.append(ColNSItem[0])
        ParList = []
        # -----------------------------------------------------------------------------------------------------------
        for x in range(LenRow):
            wsRow = ws.iloc[x]  # dfインスタンスの行データ
            wscd = str(wsRow["コード"])
            wscdFlag = False
            if int(wscd) < 100:
                wscdFlag = True
                try:
                    wscd = f"{wscd:03}"
                except:
                    print("wscdエラー")
            # WHERE社内コードでDBよりMAX(履歴No)を抽出-------------------------------------------------------------------------
            if wscdFlag is False:
                Maxsql = (
                    "SELECT MAX(in_RrkNo_pk) FROM m_kfmsrireki WHERE vc_FMSKnrCd = "
                    + str(wscd)
                    + ";"
                )
            else:
                Maxsql = (
                    "SELECT MAX(in_RrkNo_pk) FROM m_kfmsrireki WHERE vc_FMSKnrCd = "
                    + wscd
                    + ";"
                )
            MaxRrkNo = SQ.MySQLGet(
                "ws77", "SYSTEM", "SYSTEM", 3306, "test_db", "utf8", Maxsql
            )
            if MaxRrkNo[0] is True:
                print(MaxRrkNo[1])
                if MaxRrkNo[1] == ((None,),):
                    MaxRrkNo = 1
                else:
                    Mstr = str(MaxRrkNo[1]).replace("((", "").replace(",),)", "")
                    MaxRrkNo = int(Mstr) + 1
            else:
                MaxRrkNo = 1
            # テーブルのデータ型に合わせて値を格納したリストを作成---------------------------------------------------------------
            SQ.ChangeData("vc_gyou", ParList, "", "m_kfmsrireki")
            ParList.append(MaxRrkNo)
            SQ.ChangeData("vc_FMSKnrCd", ParList, wscd, "m_kfmsrireki")
            SQ.ChangeData("vc_Name", ParList, wsRow["個人名"], "m_kfmsrireki")
            SQ.ChangeData("vc_KName", ParList, wsRow["関与先名"], "m_kfmsrireki")
            SQ.ChangeData("vc_Hakkou", ParList, wsRow["発送方法"], "m_kfmsrireki")
            SQ.ChangeData("vc_SousinK", ParList, wsRow["送信方法"], "m_kfmsrireki")
            SQ.ChangeData("vc_Mail", ParList, wsRow["アドレス"], "m_kfmsrireki")
            SQ.ChangeData("vc_BmnCd_pk", ParList, wsRow["課No"], "m_kfmsrireki")
            SQ.ChangeData("vc_BmnNm", ParList, wsRow["課"], "m_kfmsrireki")
            SQ.ChangeData("vc_KansaTantouNo", ParList, wsRow["監査担当No"], "m_kfmsrireki")
            SQ.ChangeData("vc_KansaTantou", ParList, wsRow["監査担当"], "m_kfmsrireki")
            SQ.ChangeData("vc_SubTantouNo", ParList, wsRow["サブNo"], "m_kfmsrireki")
            SQ.ChangeData("vc_SubTantou", ParList, wsRow["サブ"], "m_kfmsrireki")
            SQ.ChangeData("vc_Sub_SubTantouNo", ParList, wsRow["サブ2No"], "m_kfmsrireki")
            SQ.ChangeData("vc_Sub_SubTantou", ParList, wsRow["サブ2"], "m_kfmsrireki")
            SQ.ChangeData("vc_SousinK2", ParList, wsRow["送信方法2"], "m_kfmsrireki")
            SQ.ChangeData("vc_Mail2", ParList, wsRow["アドレス2"], "m_kfmsrireki")
            SQ.ChangeData("vc_SousinK3", ParList, wsRow["送信方法3"], "m_kfmsrireki")
            SQ.ChangeData("vc_Mail3", ParList, wsRow["アドレス3"], "m_kfmsrireki")
            SQ.ChangeData("vc_SousinK4", ParList, wsRow["送信方法4"], "m_kfmsrireki")
            SQ.ChangeData("vc_Mail4", ParList, wsRow["アドレス4"], "m_kfmsrireki")
            SQ.ChangeData("vc_SousinK5", ParList, wsRow["送信方法5"], "m_kfmsrireki")
            SQ.ChangeData("vc_Mail5", ParList, wsRow["アドレス5"], "m_kfmsrireki")
            SQ.ChangeData("cr_RecKbn", ParList, 0, "m_kfmsrireki")
            SQ.ChangeData("dt_InstDT", ParList, wsRow["入力日時"], "m_kfmsrireki")
            SQ.ChangeData("dt_UpdtDT", ParList, "", "m_kfmsrireki")
            SQ.ChangeData("vc_inputuser", ParList, wsRow["入力ユーザー"], "m_kfmsrireki")
            SQ.ChangeData("vc_beforeadd", ParList, wsRow["変更前アドレス"], "m_kfmsrireki")
            # ----------------------------------------------------------------------------------------------------------
            ParList = str(ParList).replace("[", "").replace("]", "").replace("nan", "")
            ColN = str(ColN).replace("[", "").replace("]", "").replace("'", "")
            sql = "INSERT INTO m_kfmsrireki (" + ColN + ") VALUES(" + ParList + ");"
            SQ.MySQLAct("ws77", "SYSTEM", "SYSTEM", 3306, "test_db", "utf8", sql)
            SQC.MailRirekiUp()
            SQC.MailListUp()
            ParList = []
        return True
    except:
        return False


# ----------------------------------------------------------------------------------------------------------------------
def MainFlow(FolURL2, Lday):
    BatUrl = FolURL2 + "/bat/AWADriverOpen.bat"  # 4724ポート指定でappiumサーバー起動バッチを開く
    driver = OMSOpen.MainFlow(BatUrl, FolURL2, "RPAPhoto")  # OMSを起動しログイン後インスタンス化
    # driver = ""
    FolURL2 = FolURL2 + "/RPAPhoto/TKCCDBMailAddressUpdate"  # RPA用画像保管フォルダを指定
    XlsmURL = r"\\Sv05121a\e\C 作業台\請求書メールアドレス収集\アドレス新規登録シート.xlsm"  # アドレス登録シートを指定
    XlsmURL = XlsmURL.replace("\\", "/")  # URLリネーム
    # エクセルブックを読込------------------------------------------------------------------------------------------------
    logger.debug("エクセルブックを読込")
    XlsmList = EF.XlsmRead(XlsmURL)
    input_book = XlsmList[1]
    # sheet_namesメソッドでExcelブック内の各シートの名前をリストで取得できる
    input_sheet_name = input_book.sheet_names
    # lenでシートの総数を確認
    num_sheet = len(input_sheet_name)
    # シートの数とシートの名前のリストの表示
    print("Sheet の数:", num_sheet)
    print(input_sheet_name)
    x = 0
    for isnItem in input_sheet_name:
        if isnItem == "アドレス登録":
            ws = input_book.parse(input_sheet_name[x], dtype=str)
            print(ws)
            break
        x = x + 1
    ws = ws.sort_values("入力日時", ascending=False)  # 入力日時順に並び替え
    ws = ws.drop_duplicates(subset="コード")  # コードで重複削除
    print(ws)
    logger.debug("Excelデータを履歴テーブルにインサート")
    SQI = SQLIn(ws)
    # ----------------------------------------------------------------------------------------------------------------------
    if SQI is True:
        logger.debug("CDBアクション開始")
        CDBO = CDBOpen(FolURL2, Lday, driver, ws, XlsmURL)  # CDBアクション開始
        if CDBO is True:
            logger.debug("CDBログインOK")
            print("CDBログインOK")
            ImgClick(FolURL2, "F10End.png", 0.9, 10)
            while pg.locateOnScreen(FolURL2 + "/OMSTitle.png", 0.9) is None:
                time.sleep(1)
            return driver
        else:
            logger.debug("CDBログイン失敗")
            print("CDBログイン失敗")
    else:
        logger.debug("履歴テーブル登録失敗")
        print("履歴テーブル登録失敗")


# ----------------------------------------------------------------------------------------------------------------------
def AllMain():
    # RPA用画像フォルダの作成-----------------------------------------------------------
    Lday = calendar.monthrange(dt.today().year, dt.today().month)
    FolURL2 = os.getcwd().replace("\\", "/")  # 先
    # --------------------------------------------------------------------------------
    try:
        MF = MainFlow(FolURL2, Lday)
        return True, MF
    except:
        traceback.print_exc()
        return False, ""
