# モジュールインポート
import pyautogui as pg
import time

from sqlalchemy import true
import OMSOpen

# pandasインポート
import pandas as pd

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
import pyperclip  # クリップボードへのコピーで使用
import WarekiHenkan  # WarekiHenkan.SeirekiDate("R",4,1,19) = 返り値2022/1/19(str)
from chardet.universaldetector import UniversalDetector

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
def getFileEncoding(file_path):  # .format( getFileEncoding( "sjis.csv" ) )
    detector = UniversalDetector()
    with open(file_path, mode="rb") as f:
        for binary in f:
            detector.feed(binary)
            if detector.done:
                break
    detector.close()
    return detector.result["encoding"]


# ----------------------------------------------------------------------------------------------------------------------
def CSVGet(FileUrl):
    # 出力したCSVを読込み----------------------------------------------------------------------------------------------------------
    try:
        SerchEnc = format(getFileEncoding(FileUrl))
        MasterCSV = pd.read_csv(FileUrl, encoding=SerchEnc)
        return True, MasterCSV
    except:
        return False, ""


# ----------------------------------------------------------------------------------------------------------------------
def ShiftJisCSVGet(FileUrl):
    # 出力したCSVを読込み----------------------------------------------------------------------------------------------------------
    try:
        MasterCSV = pd.read_csv(FileUrl, encoding="SHIFT_JIS")
        return True, MasterCSV
    except:
        return False, ""


# ----------------------------------------------------------------------------------------------------------------------
def CSVCheck(Key, CSVArr, ColName):
    CSVArrRow = np.array(CSVArr).shape[0]  # 配列行数取得
    try:
        for x in range(CSVArrRow):
            CSVRowData = CSVArr.iloc[x, :]
            CSVTarget = CSVRowData[ColName].replace("\u3000", "")
            if Key == CSVTarget:
                return True, x
    except:
        return False, ""


# ----------------------------------------------------------------------------------------------------------------------
def FirstOpen(FolURL2, Tax):
    try:
        time.sleep(1)
        ImgClick(FolURL2, "TMSOpen.png", 0.9, 2)
        while (
            pg.locateOnScreen(FolURL2 + "/GyoumuBunsekiBtn.png", confidence=0.9) is None
        ):
            time.sleep(1)
        time.sleep(1)
        ImgClick(FolURL2, "GyoumuBunsekiBtn.png", 0.9, 2)
        # while pg.locateOnScreen(FolURL2 + "/GyoumuBunsekiWin.png" , confidence=0.9) is None:
        #     time.sleep(1)
        while (
            pg.locateOnScreen(FolURL2 + "/Syuukeityuu.png", confidence=0.9) is not None
        ):
            time.sleep(1)
        time.sleep(1)
        pg.press("f7")
        time.sleep(1)
        while pg.locateOnScreen(FolURL2 + "/SiteiKikanStr.png", confidence=0.9) is None:
            time.sleep(1)
        ImgClick(FolURL2, "SiteiKikanStr.png", 0.9, 2)
        time.sleep(1)
        ImgClick(FolURL2, "SiteiKikanOKBtn.png", 0.9, 2)
        time.sleep(1)
        ImgClick(FolURL2, "TimeBox.png", 0.9, 2)
        time.sleep(1)
        pg.press("return")
        time.sleep(1)
        yPar = str(WarekiHenkan.Wareki.from_ad(dt.today().year).year)
        mPar = str(dt.today().month - 1)
        pg.write(yPar, interval=0.01)
        pg.press("return")
        time.sleep(1)
        pg.write(mPar, interval=0.01)
        pg.press("return")
        time.sleep(1)
        pg.press("return")
        time.sleep(1)
        pg.write(yPar, interval=0.01)
        pg.press("return")
        time.sleep(1)
        pg.write(mPar, interval=0.01)
        pg.press("return")
        time.sleep(1)
        pg.press("return")
        time.sleep(3)
        ImgClick(FolURL2, "GyoumubetuTab.png", 0.9, 2)
        time.sleep(1)
        while (
            pg.locateOnScreen(FolURL2 + "/TyokusetuOpenFlag.png", confidence=0.9)
            is None
        ):
            time.sleep(1)
        time.sleep(1)
        ImgClick(FolURL2, "KansetuTab.png", 0.9, 2)
        Kansetu = TKCCSVOut(FolURL2, "KANSETU")
        if Kansetu is True:
            KansetuList = CSVGet(FolURL2 + "/KANSETU.CSV")
            if KansetuList[0] is True:
                KansetuListRow = CSVCheck("E4移動時間", KansetuList[1], "業務")
                if KansetuListRow[0] is True:
                    time.sleep(1)
                    ImgClick(FolURL2, "1gyouUnderArrow.png", 0.9, 1)
                    for x in range(KansetuListRow[1]):
                        pg.press("down")
                    time.sleep(1)
                    pg.press("return")
                    time.sleep(1)
                    while (
                        pg.locateOnScreen(FolURL2 + "/Syuukeityuu.png", confidence=0.9)
                        is not None
                    ):
                        time.sleep(1)
                    time.sleep(1)
                    while (
                        pg.locateOnScreen(
                            FolURL2 + "/TantoubetuFlag.png", confidence=0.9
                        )
                        is None
                    ):
                        time.sleep(1)
                    time.sleep(1)
                    TKCTimeCSVOut(
                        FolURL2, "移動時間", "//nas-sv/A_共通/A8_ｼｽﾃﾑ資料/RPA/公会計時間分析/担当者別", Tax
                    )
                    time.sleep(1)
                    pg.press("f10")
                    time.sleep(1)
                    while (
                        pg.locateOnScreen(FolURL2 + "/TyokuKanTab.png", confidence=0.9)
                        is None
                    ):
                        time.sleep(1)
                    time.sleep(1)
                    ImgClick(FolURL2, "TyokusetuTab.png", 0.9, 1)
        return True
    except:
        return False


# ----------------------------------------------------------------------------------------------------------------------
def TKCCSVOut(FolURL2, Title):
    try:
        ImgClick(FolURL2, "ExcelTab.png", 0.9, 2)
        while pg.locateOnScreen(FolURL2 + "/KiridasiFlag.png", confidence=0.9) is None:
            time.sleep(1)
        ImgList = ["KiridasiType.png", "KiridasiType2.png"]
        ImgListAns = ImgCheckForList(FolURL2, ImgList, 0.9)
        ImgClick(FolURL2, ImgListAns[1], 0.9, 2)
        time.sleep(1)
        pg.press(["down", "down", "down"])
        pg.press(["return"])
        time.sleep(1)
        pg.press(["tab", "tab", "tab"])
        pg.press("delete")
        FolURL2 = FolURL2.replace("/", "\\")
        pyperclip.copy(FolURL2)
        pg.hotkey("ctrl", "v")  # pg日本語不可なのでコピペ
        pg.press(["return"])
        time.sleep(1)
        pg.press("delete")
        pg.write(Title, interval=0.01)
        time.sleep(1)
        pg.press(["return"])
        time.sleep(1)
        pg.press(["return"])
        time.sleep(1)
        ImgClick(FolURL2, "KiridasiSave.png", 0.9, 2)
        time.sleep(1)
        if ImgCheck(FolURL2, "OverFileList.png", 0.9, 1)[0] is True:
            time.sleep(1)
            ImgClick(FolURL2, "OverFileListYes.png", 0.9, 2)
        return True
    except:
        return False


# ----------------------------------------------------------------------------------------------------------------------
def TKCB2CSVOut(FolURL2, CSVURL, Title):
    try:
        ImgClick(FolURL2, "ExcelTab.png", 0.9, 2)
        while pg.locateOnScreen(FolURL2 + "/KiridasiFlag.png", confidence=0.9) is None:
            time.sleep(1)
        ImgList = ["KiridasiType.png", "KiridasiType2.png"]
        ImgListAns = ImgCheckForList(FolURL2, ImgList, 0.9)
        ImgClick(FolURL2, ImgListAns[1], 0.9, 2)
        time.sleep(1)
        pg.press(["down", "down", "down"])
        pg.press(["return"])
        time.sleep(1)
        pg.press(["tab", "tab", "tab"])
        pg.press("delete")
        CSVURL = CSVURL.replace("/", "\\")
        pyperclip.copy(CSVURL)
        pg.hotkey("ctrl", "v")  # pg日本語不可なのでコピペ
        pg.press(["return"])
        time.sleep(1)
        pg.press("delete")
        pyperclip.copy(Title)
        pg.hotkey("ctrl", "v")  # pg日本語不可なのでコピペ
        time.sleep(1)
        pg.press(["return"])
        time.sleep(1)
        pg.press(["return"])
        time.sleep(1)
        ImgClick(FolURL2, "KiridasiSave.png", 0.9, 2)
        time.sleep(1)
        if ImgCheck(FolURL2, "OverFileList.png", 0.9, 1)[0] is True:
            time.sleep(1)
            ImgClick(FolURL2, "OverFileListYes.png", 0.9, 2)
        return True
    except:
        return False


# ----------------------------------------------------------------------------------------------------------------------
def TKCTimeCSVOut(FolURL2, Title, FileURL, Tax):
    try:
        ImgClick(FolURL2, "ExcelTab.png", 0.9, 2)
        while pg.locateOnScreen(FolURL2 + "/KiridasiFlag.png", confidence=0.9) is None:
            time.sleep(1)
        ImgList = ["KiridasiType.png", "KiridasiType2.png"]
        ImgListAns = ImgCheckForList(FolURL2, ImgList, 0.9)
        ImgClick(FolURL2, ImgListAns[1], 0.9, 2)
        time.sleep(1)
        pg.press(["down", "down", "down"])
        pg.press(["return"])
        time.sleep(1)
        pg.press(["tab", "tab", "tab"])
        pg.press("delete")
        FileURL = FileURL.replace("/", "\\")
        pyperclip.copy(FileURL)
        pg.hotkey("ctrl", "v")  # pg日本語不可なのでコピペ
        pg.press(["return"])
        time.sleep(1)
        pg.press("delete")
        if Tax != "":
            Title = Title + "_" + Tax
        pyperclip.copy(Title)
        pg.hotkey("ctrl", "v")  # pg日本語不可なのでコピペ
        pg.press(["return"])
        time.sleep(1)
        pg.press(["return"])
        time.sleep(1)
        ImgClick(FolURL2, "KiridasiSave.png", 0.9, 2)
        time.sleep(1)
        if ImgCheck(FolURL2, "OverFileList.png", 0.9, 1)[0] is True:
            time.sleep(1)
            ImgClick(FolURL2, "OverFileListYes.png", 0.9, 2)
        return True
    except:
        return False


# ----------------------------------------------------------------------------------------------------------------------
def KanyoScroll(FolURL2, Tax):  # 関与先毎の時間集計操作
    KCSVO = TKCCSVOut(FolURL2, "KANYOSAKIBETU")
    if KCSVO is True:
        KanyosakibetuList = ShiftJisCSVGet(FolURL2 + "/KANYOSAKIBETU.CSV")
        if KanyosakibetuList[0] is True:
            KArr = KanyosakibetuList[1]
            KArrRow = np.array(KArr).shape[0]  # 配列行数取得
            for y in range(KArrRow):
                if y < KArrRow - 1:
                    KArrRowData = KArr.iloc[y, :]
                    KArrName = KArrRowData["関与先"]
                    KArrListRow = CSVCheck(KArrName, KArr, "関与先")
                    if KArrListRow[0] is True:
                        # GList = ["1gyou.png","1gyou2.png"]
                        # GL = ImgCheckForList(FolURL2,GList,0.99999)
                        # ImgClick(FolURL2,GL[1],0.99999,1)
                        time.sleep(1)
                        ImgClick(FolURL2, "1gyouUnderArrow.png", 0.9, 5)
                        for z in range(KArrListRow[1]):
                            pg.press("down")
                        time.sleep(1)
                        pg.press("return")
                        time.sleep(1)
                        while (
                            pg.locateOnScreen(
                                FolURL2 + "/TantoubetuFlag.png", confidence=0.9
                            )
                            is None
                        ):
                            time.sleep(1)
                        TantouCSVO = TKCCSVOut(FolURL2, "TANTOUBETU")
                        if TantouCSVO is True:
                            TantouList = CSVGet(FolURL2 + "/TANTOUBETU.CSV")
                            if TantouList[0] is True:
                                TanArr = TantouList[1]
                                TanArrRow = np.array(TanArr).shape[0]  # 配列行数取得
                                for z in range(TanArrRow):
                                    TanArrData = TanArr.iloc[z, :]
                                    TanName = TanArrData["担当者"]
                                    TanArrName = TanArrData["担当者"].replace("\u3000", "")
                                    TanArrTime = TanArrData["実\u3000績(A)"]
                                    if not TanArrName == "【合計】":
                                        if TanArrTime is not False:
                                            TanArrRowListRow = CSVCheck(
                                                TanArrName, TanArr, "担当者"
                                            )
                                            if TanArrRowListRow[0] is True:
                                                time.sleep(1)
                                                ImgClick(
                                                    FolURL2,
                                                    "1gyouUnderArrow.png",
                                                    0.9,
                                                    5,
                                                )
                                                for z in range(TanArrRowListRow[1]):
                                                    pg.press("down")
                                                time.sleep(1)
                                                pg.press("return")
                                                time.sleep(1)
                                                while (
                                                    pg.locateOnScreen(
                                                        FolURL2 + "/KatudouTab.png",
                                                        confidence=0.9,
                                                    )
                                                    is None
                                                ):
                                                    time.sleep(1)
                                                FN = KArrName + "_" + TanName
                                                TKCTimeCSVOut(
                                                    FolURL2,
                                                    FN,
                                                    "//nas-sv/A_共通/A8_ｼｽﾃﾑ資料/RPA/公会計時間分析/担当者別",
                                                    Tax,
                                                )
                                                time.sleep(1)
                                                pg.press("f10")
                                                time.sleep(1)
                                                ImgClick(
                                                    FolURL2,
                                                    "1gyouUnderArrow.png",
                                                    0.9,
                                                    5,
                                                )
                                                for z in range(TanArrRowListRow[1]):
                                                    pg.press("up")
                                time.sleep(1)
                                while (
                                    pg.locateOnScreen(
                                        FolURL2 + "/TantoubetuFlag.png", confidence=0.9
                                    )
                                    is None
                                ):
                                    time.sleep(1)
                                time.sleep(1)
                                pg.press("f10")
                                time.sleep(1)
                                # while (
                                #     pg.locateOnScreen(
                                #         FolURL2 + "/KousagyouOpen.png", confidence=0.9
                                #     )
                                #     is None
                                # ):
                                #     time.sleep(1)
                                KouList = [
                                    "KousagyouOpen.png",
                                    "KousagyouOpen2.png",
                                    "KousagyouOpen3.png",
                                    "KousagyouOpen4.png",
                                    "KousagyouOpen5.png",
                                ]
                                while (
                                    ImgCheckForList(FolURL2, KouList, 0.9)[0] is False
                                ):
                                    time.sleep(1)
                                time.sleep(1)
                                ImgClick(FolURL2, "1gyouUnderArrow.png", 0.9, 5)
                                time.sleep(1)
                                for z in range(KArrListRow[1]):
                                    pg.press("up")
                                time.sleep(1)
            pg.press("f10")
            print("")


# ----------------------------------------------------------------------------------------------------------------------
def EigyouScroll(FolURL2):  # 関与先毎の時間集計操作
    KCSVO = TKCCSVOut(FolURL2, "KANYOSAKIBETU")
    if KCSVO is True:
        KanyosakibetuList = ShiftJisCSVGet(FolURL2 + "/KANYOSAKIBETU.CSV")
        if KanyosakibetuList[0] is True:
            KArr = KanyosakibetuList[1]
            KArrRow = np.array(KArr).shape[0]  # 配列行数取得
            for y in range(KArrRow):
                if y < KArrRow - 1:
                    KArrRowData = KArr.iloc[y, :]
                    KArrName = KArrRowData["関与先"]
                    KArrTime = KArrRowData["実　績(A)"]
                    if KArrTime != KArrTime is False:
                        KArrListRow = CSVCheck(KArrName, KArr, "関与先")
                        if KArrListRow[0] is True:
                            # GList = ["1gyou.png","1gyou2.png"]
                            # GL = ImgCheckForList(FolURL2,GList,0.99999)
                            # ImgClick(FolURL2,GL[1],0.99999,1)
                            time.sleep(1)
                            ImgClick(FolURL2, "1gyouUnderArrow.png", 0.9, 5)
                            for z in range(KArrListRow[1]):
                                pg.press("down")
                            time.sleep(1)
                            pg.press("return")

                            time.sleep(1)
                            while (
                                pg.locateOnScreen(
                                    FolURL2 + "/TantoubetuFlag.png", confidence=0.9
                                )
                                is None
                            ):
                                time.sleep(1)
                            TantouB2CSVO = TKCB2CSVOut(
                                FolURL2,
                                "//nas-sv/A_共通/A8_ｼｽﾃﾑ資料/RPA/公会計時間分析/担当者別",
                                KArrName + "_B2",
                            )
                            if TantouB2CSVO is True:
                                time.sleep(1)
                                pg.press("f10")
                                time.sleep(1)
                                ImgClick(FolURL2, "1gyouUnderArrow.png", 0.9, 5)
                                for z in reversed(range(KArrListRow[1])):
                                    pg.press("up")
                                time.sleep(1)
                            else:
                                print("B2CSV出力失敗")


# ----------------------------------------------------------------------------------------------------------------------
def MainFlow(FolURL2):
    BatUrl = FolURL2 + "/bat/AWADriverOpen.bat"  # 4724ポート指定でappiumサーバー起動バッチを開く
    OMSOpen.MainFlow(BatUrl, FolURL2, "RPAPhoto")  # OMSを起動しログイン後インスタンス化
    FolURL2 = FolURL2 + "/RPAPhoto/TKC_KoukaikeiTimetabulation"
    Tax = ""
    FMO = FirstOpen(FolURL2, Tax)
    if FMO is True:
        TCSVO = TKCCSVOut(FolURL2, "TGYOUMULIST")
        if TCSVO is True:
            TgyoumuList = CSVGet(FolURL2 + "/TGYOUMULIST.CSV")
            if TgyoumuList[0] is True:
                # TgyoumuListRow = CSVCheck("B2公会計営業", TgyoumuList[1], "業務")
                # if TgyoumuListRow[0] is True:
                #     Tax = "B2"
                #     # GList = ["1gyou.png","1gyou2.png"]
                #     # GL = ImgCheckForList(FolURL2,GList,0.99999)
                #     # ImgClick(FolURL2,GL[1],0.99999,1)
                #     time.sleep(1)
                #     ImgClick(FolURL2, "1gyouUnderArrow.png", 0.9, 5)
                #     for x in range(TgyoumuListRow[1]):
                #         pg.press("down")
                #     time.sleep(1)
                #     pg.press("return")
                #     time.sleep(1)
                #     while (
                #         pg.locateOnScreen(FolURL2 + "/Syuukeityuu.png", confidence=0.9)
                #         is not None
                #     ):
                #         time.sleep(1)
                #     while (
                #         pg.locateOnScreen(FolURL2 + "/KanyoTab.png", confidence=0.9)
                #         is None
                #     ):
                #         time.sleep(1)
                #     ImgClick(FolURL2, "KanyoTab.png", 0.9, 5)
                #     time.sleep(1)
                #     KanyoScroll(FolURL2, Tax)  # 関与先毎の時間集計操作
                #     ImgClick(FolURL2, "1gyouUnderArrow.png", 0.9, 5)
                #     for x in range(TgyoumuListRow[1]):
                #         pg.press("up")
                # ------------------------------------------------------------------------------
                # TgyoumuListRow = CSVCheck("A8公会計作業（固定資産台帳）", TgyoumuList[1], "業務")
                # if TgyoumuListRow[0] is True:
                #     Tax = "A8"
                #     # GList = ["1gyou.png","1gyou2.png"]
                #     # GL = ImgCheckForList(FolURL2,GList,0.99999)
                #     # ImgClick(FolURL2,GL[1],0.99999,1)
                #     time.sleep(1)
                #     ImgClick(FolURL2, "1gyouUnderArrow.png", 0.9, 5)
                #     for x in range(TgyoumuListRow[1]):
                #         pg.press("down")
                #     time.sleep(1)
                #     pg.press("return")
                #     time.sleep(1)
                #     while (
                #         pg.locateOnScreen(FolURL2 + "/Syuukeityuu.png", confidence=0.9)
                #         is not None
                #     ):
                #         time.sleep(1)
                #     while (
                #         pg.locateOnScreen(FolURL2 + "/KanyoTab.png", confidence=0.9)
                #         is None
                #     ):
                #         time.sleep(1)
                #     ImgClick(FolURL2, "KanyoTab.png", 0.9, 5)
                #     time.sleep(1)
                #     KanyoScroll(FolURL2, Tax)  # 関与先毎の時間集計操作
                #     ImgClick(FolURL2, "1gyouUnderArrow.png", 0.9, 5)
                #     for x in range(TgyoumuListRow[1]):
                #         pg.press("up")
                # ------------------------------------------------------------------------------
                # TgyoumuListRow = CSVCheck("A9公会計作業（財務書類）", TgyoumuList[1], "業務")
                # if TgyoumuListRow[0] is True:
                #     Tax = "A9"
                #     # GList = ["1gyou.png","1gyou2.png"]
                #     # GL = ImgCheckForList(FolURL2,GList,0.99999)
                #     # ImgClick(FolURL2,GL[1],0.99999,1)
                #     time.sleep(1)
                #     ImgClick(FolURL2, "1gyouUnderArrow.png", 0.9, 5)
                #     for x in range(TgyoumuListRow[1]):
                #         pg.press("down")
                #     time.sleep(1)
                #     pg.press("return")
                #     time.sleep(1)
                #     while (
                #         pg.locateOnScreen(FolURL2 + "/Syuukeityuu.png", confidence=0.9)
                #         is not None
                #     ):
                #         time.sleep(1)
                #     while (
                #         pg.locateOnScreen(FolURL2 + "/KanyoTab.png", confidence=0.9)
                #         is None
                #     ):
                #         time.sleep(1)
                #     ImgClick(FolURL2, "KanyoTab.png", 0.9, 5)
                #     time.sleep(1)
                #     KanyoScroll(FolURL2, Tax)  # 関与先毎の時間集計操作
                #     ImgClick(FolURL2, "1gyouUnderArrow.png", 0.9, 5)
                #     for x in range(TgyoumuListRow[1]):
                #         pg.press("up")
                # # ------------------------------------------------------------------------------
                # TgyoumuListRow = CSVCheck("A10公会計作業（その他）", TgyoumuList[1], "業務")
                # if TgyoumuListRow[0] is True:
                #     Tax = "A10"
                #     # GList = ["1gyou.png","1gyou2.png"]
                #     # GL = ImgCheckForList(FolURL2,GList,0.99999)
                #     # ImgClick(FolURL2,GL[1],0.99999,1)
                #     time.sleep(1)
                #     ImgClick(FolURL2, "1gyouUnderArrow.png", 0.9, 5)
                #     for x in range(TgyoumuListRow[1]):
                #         pg.press("down")
                #     time.sleep(1)
                #     pg.press("return")
                #     time.sleep(1)
                #     while (
                #         pg.locateOnScreen(FolURL2 + "/Syuukeityuu.png", confidence=0.9)
                #         is not None
                #     ):
                #         time.sleep(1)
                #     while (
                #         pg.locateOnScreen(FolURL2 + "/KanyoTab.png", confidence=0.9)
                #         is None
                #     ):
                #         time.sleep(1)
                #     ImgClick(FolURL2, "KanyoTab.png", 0.9, 5)
                #     time.sleep(1)
                #     KanyoScroll(FolURL2, Tax)  # 関与先毎の時間集計操作
                #     ImgClick(FolURL2, "1gyouUnderArrow.png", 0.9, 5)
                #     for x in range(TgyoumuListRow[1]):
                #         pg.press("up")
                # # ------------------------------------------------------------------------------
                TgyoumuListRow = CSVCheck("A11公営作業", TgyoumuList[1], "業務")
                if TgyoumuListRow[0] is True:
                    Tax = "A11"
                    # GList = ["1gyou.png","1gyou2.png"]
                    # GL = ImgCheckForList(FolURL2,GList,0.99999)
                    # ImgClick(FolURL2,GL[1],0.99999,1)
                    time.sleep(1)
                    ImgClick(FolURL2, "1gyouUnderArrow.png", 0.9, 5)
                    for x in range(TgyoumuListRow[1]):
                        pg.press("down")
                    time.sleep(1)
                    pg.press("return")
                    time.sleep(1)
                    while (
                        pg.locateOnScreen(FolURL2 + "/Syuukeityuu.png", confidence=0.9)
                        is not None
                    ):
                        time.sleep(1)
                    while (
                        pg.locateOnScreen(FolURL2 + "/KanyoTab.png", confidence=0.9)
                        is None
                    ):
                        time.sleep(1)
                    ImgClick(FolURL2, "KanyoTab.png", 0.9, 5)
                    time.sleep(1)
                    KanyoScroll(FolURL2, Tax)  # 関与先毎の時間集計操作
                    ImgClick(FolURL2, "1gyouUnderArrow.png", 0.9, 5)
                    for x in range(TgyoumuListRow[1]):
                        pg.press("up")
                # ------------------------------------------------------------------------------
    else:
        time.sleep(1)


# ----------------------------------------------------------------------------------------------------------------------
# RPA用画像フォルダの作成---------------------------------------------------------
FolURL = (
    "//nas-sv/A_共通/A8_ｼｽﾃﾑ資料/RPA/ALLDataBase/RPAPhoto/TKC_KoukaikeiTimetabulation"  # 元
)
# FolURL2 = os.getcwd().replace('\\','/') + "/TKC_DensiSinkoku"#先
FolURL2 = os.getcwd().replace("\\", "/")  # 先
# --------------------------------------------------------------------------------
try:
    MainFlow(FolURL2)
except:
    traceback.print_exc()
