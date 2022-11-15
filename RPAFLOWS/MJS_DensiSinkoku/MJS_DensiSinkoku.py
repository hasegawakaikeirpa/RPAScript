###########################################################################################################
# 稼働設定：解像度 1920*1080 表示スケール125%
###########################################################################################################
# モジュールインポート
import tkinter as tk
import pyautogui as pg
import time
import pandas as pd
import numpy as np
import os
from datetime import datetime as dt
import traceback
import pyautogui
import codecs
import pyperclip  # クリップボードへのコピーで使用
import logging.config
from tkinter import filedialog, messagebox

# 自作モジュールインポート
import MJSOpen
import RPA_Function as RPA
import MyTable

# logger設定------------------------------------------------------------------------------------------------------------
logging.config.fileConfig(r"LogConf\logging_debug.conf")
logger = logging.getLogger(__name__)
# ----------------------------------------------------------------------------------------------------------------------


def DriverUIWaitXPATH(UIPATH, driver):  # XPATH要素を取得するまで待機
    for x in range(10):
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
    for x in range(10):
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
    for x in range(10):
        try:
            driver.find_element_by_Name(UIPATH)
            Flag = 1
            return True
        except:
            Flag = 0
    if Flag == 0:
        return False


# ------------------------------------------------------------r----------------------------------------------------------
def DriverUIWaitclassname(UIPATH, driver):  # XPATH要素を取得するまで待機
    for x in range(10):
        try:
            driver.find_element_by_class_name(UIPATH)
            Flag = 1
            return True
        except:
            Flag = 0
    if Flag == 0:
        return False


# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
def DriverFindClass(UIPATH, driver):  # XPATH要素を取得するまで待機
    for x in range(10):
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
    for x in range(10):
        if Hub == "AutomationID":
            if (
                DriverUIWaitAutomationId(ObjName, driver) is True
            ):  # MJSメニューの年調起動ボタンを判定して初期処理分け
                # 正常待機後処理
                driver.find_element_by_accessibility_id(ObjName)  # 一括電子申告送信ボタン
                return True
            else:
                # 異常待機後処理
                print("要素取得に失敗しました。")
        elif Hub == "XPATH":
            if DriverUIWaitXPATH(ObjName, driver) is True:  # MJSメニューの年調起動ボタンを判定して初期処理分け
                # 正常待機後処理
                driver.find_element_by_xpath(ObjName)  # 一括電子申告送信ボタン
                return True
            else:
                # 異常待機後処理
                print("要素取得に失敗しました。")
        elif Hub == "Name":
            if DriverUIWaitName(ObjName, driver) is True:  # MJSメニューの年調起動ボタンを判定して初期処理分け
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
        ):  # MJSメニューの年調起動ボタンを判定して初期処理分け
            # 正常待機後処理
            MJSObj = driver.find_element_by_accessibility_id(ObjName)  # 一括電子申告送信ボタン
            MJSObj.click()
            return MJSObj
        else:
            # 異常待機後処理
            print("要素取得に失敗しました。")
    elif Hub == "XPATH":
        if DriverUIWaitXPATH(ObjName, driver) is True:  # MJSメニューの年調起動ボタンを判定して初期処理分け
            # 正常待機後処理
            MJSObj = driver.find_element_by_xpath(ObjName)  # 一括電子申告送信ボタン
            MJSObj.click()
            return MJSObj
        else:
            # 異常待機後処理
            print("要素取得に失敗しました。")
    elif Hub == "Name":
        if DriverUIWaitName(ObjName, driver) is True:  # MJSメニューの年調起動ボタンを判定して初期処理分け
            # 正常待機後処理
            MJSObj = driver.find_element_by_Name(ObjName)  # 一括電子申告送信ボタン
            MJSObj.click()
            return MJSObj
        else:
            # 異常待機後処理
            print("要素取得に失敗しました。")
    elif Hub == "class_name":
        if DriverUIWaitclassname(ObjName, driver) is True:  # MJSメニューの年調起動ボタンを判定して初期処理分け
            # 正常待機後処理
            MJSObj = driver.find_element_by_class_name(ObjName)  # 一括電子申告送信ボタン
            MJSObj.click()
            return MJSObj
        else:
            # 異常待機後処理
            print("要素取得に失敗しました。")


# ----------------------------------------------------------------------------------------------------------------------
def ImgCheck(Img_dir_D, FileName, conf, LoopVal):  # 画像があればTrueを返す関数
    ImgURL = Img_dir_D + "/" + FileName
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
def ImgNothingCheck(Img_dir_D, FileName, conf, LoopVal):  # 画像がなければTrueを返す
    ImgURL = Img_dir_D + "/" + FileName
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
def ImgCheckForList(Img_dir_D, List, conf, LoopVal):  # リスト内の画像があればTrueと画像名を返す
    for x in range(LoopVal):
        for ListItem in List:
            ImgURL = Img_dir_D + "/" + ListItem
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
def ImgClick(Img_dir_D, FileName, conf, LoopVal):  # 画像があればクリックしてx,y軸を返す
    ImgURL = Img_dir_D + "/" + FileName
    for x in range(10):
        if (
            ImgCheck(Img_dir_D, FileName, conf, LoopVal)[0] is True
        ):  # MJSメニューの年調起動ボタンを判定して初期処理分け
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
def SortCSVItem(SortURL, SortName, Key):  # CSVと列名を4つ与えて4つの複合と引数Keyが一致する行数を返す
    Sort_url = SortURL.replace("\\", "/") + "/" + SortName + ".CSV"
    with codecs.open(Sort_url, "r", "utf-8", "ignore") as file:
        C_Child = pd.read_table(file, delimiter=",")
    C_CforCount = 0
    for C_ChildItem in C_Child:
        # C_ChildItemName = C_ChildItem['科目名']
        if Key == C_ChildItem:
            return C_CforCount
        else:
            C_CforCount = C_CforCount + 1


def SortPDF(PDFName):
    Fol = str(dt.today().year) + "-" + str(dt.today().month)
    pt = "\\\\nas-sv\\B_監査etc\\B2_電子ﾌｧｲﾙ\\ﾒｯｾｰｼﾞﾎﾞｯｸｽ\\" + Fol + "\\送信分受信通知"
    # path = path.replace('\\','/')#先
    PDFFileList = os.listdir(pt)
    Cou = 1
    for PDFItem in PDFFileList:
        PDFName = PDFName.replace("\u3000", "").replace(".PDF", "").replace(".pdf", "")
        PDFItem = PDFItem.replace("\u3000", "").replace(".PDF", "").replace(".pdf", "")
        if PDFName in PDFItem:
            Cou = Cou + 1
    return str(Cou), pt


# ------------------------------------------------------------------------------------------------------------------
def FolCre(C_SCode, C_Name, C_Nendo, C_Zeimoku, C_Syurui):
    Fol = str(dt.today().year) + "-" + str(dt.today().month)
    pt = r"\\nas-sv\B_監査etc\B2_電子ﾌｧｲﾙ\ﾒｯｾｰｼﾞﾎﾞｯｸｽ\\" + Fol
    try:
        # ---------------------------------------------------------
        if os.path.exists(pt) is False:
            os.mkdir(pt)
            pt = pt + r"\\送信分受信通知"
            if os.path.exists(pt) is False:  # 1
                os.mkdir(pt)
                C_Fol = pt + r"\\" + str(C_SCode)
                if os.path.exists(C_Fol) is False:  # 2
                    os.mkdir(C_Fol)
                    C_F = C_Fol + r"\\" + "ミロク送信分"
                    if os.path.exists(C_F) is False:  # 3
                        os.mkdir(C_F)
                        return True, C_F
                    else:
                        return True, C_F
                else:
                    C_F = C_Fol + r"\\" + "ミロク送信分"
                    if os.path.exists(C_F) is False:  # 3
                        os.mkdir(C_F)
                        return True, C_F
                    else:
                        return True, C_F
            else:
                C_Fol = pt + r"\\" + str(C_SCode)
                if os.path.exists(C_Fol) is False:  # 2
                    os.mkdir(C_Fol)
                    C_F = C_Fol + r"\\" + "ミロク送信分"
                    if os.path.exists(C_F) is False:  # 3
                        os.mkdir(C_F)
                        return True, C_F
                    else:
                        return True, C_F
                else:
                    C_F = C_Fol + r"\\" + "ミロク送信分"
                    if os.path.exists(C_F) is False:  # 3
                        os.mkdir(C_F)
                        return True, C_F
                    else:
                        return True, C_F
        else:
            pt = pt + r"\\送信分受信通知"
            if os.path.exists(pt) is False:  # 1
                os.mkdir(pt)
                C_Fol = pt + r"\\" + str(C_SCode)
                if os.path.exists(C_Fol) is False:  # 2
                    os.mkdir(C_Fol)
                    C_F = C_Fol + r"\\" + "ミロク送信分"
                    if os.path.exists(C_F) is False:  # 3
                        os.mkdir(C_F)
                        return True, C_F
                    else:
                        return True, C_F
                else:
                    C_F = C_Fol + r"\\" + "ミロク送信分"
                    if os.path.exists(C_F) is False:  # 3
                        os.mkdir(C_F)
                        return True, C_F
                    else:
                        return True, C_F
            else:
                C_Fol = pt + r"\\" + str(C_SCode)
                if os.path.exists(C_Fol) is False:  # 2
                    os.mkdir(C_Fol)
                    C_F = C_Fol + r"\\" + "ミロク送信分"
                    if os.path.exists(C_F) is False:  # 3
                        os.mkdir(C_F)
                        return True, C_F
                    else:
                        return False, ""
                else:
                    C_F = C_Fol + r"\\" + "ミロク送信分"
                    if os.path.exists(C_F) is False:  # 3
                        os.mkdir(C_F)
                        return True, C_F
                    else:
                        return True, C_F
        # ---------------------------------------------------------
    except:
        return False, ""


# ------------------------------------------------------------------------------------------------------------------
def PrintAct(Img_dir_D, C_SCode, C_Name, C_Nendo, C_Zeimoku, C_Syurui):
    # 画像が出現するまで待機してクリック------------------------------------------------------------------------------------
    List = ["FileOut.png", "FileOut2.png"]
    conf = 0.9  # 画像認識感度
    LoopVal = 10  # 検索回数
    ListCheck = ImgCheckForList(Img_dir_D, List, conf, LoopVal)  # 画像検索関数
    if ListCheck[0] is True:
        ImgClick(Img_dir_D, ListCheck[1], conf, LoopVal)
        time.sleep(1)
    # ----------------------------------------------------------------------------------------------------------------------
    # 画像が出現するまで待機してクリック------------------------------------------------------------------------------------
    List = ["PDFIcon.png", "CSVIcon.png"]
    conf = 0.9  # 画像認識感度
    LoopVal = 10  # 検索回数
    ListCheck = ImgCheckForList(Img_dir_D, List, conf, LoopVal)  # 画像検索関数
    if ListCheck[0] is True:
        ImgClick(Img_dir_D, ListCheck[1], conf, LoopVal)
        time.sleep(1)
        pg.press(["down", "down", "down", "down", "down"])
        pg.press(["return"])
    # ----------------------------------------------------------------------------------------------------------------------
    FC = FolCre(C_SCode, C_Name, C_Nendo, C_Zeimoku, C_Syurui)
    Tyouhuku = SortPDF(C_SCode + "_" + C_Name)
    if FC[0] is True:
        if Tyouhuku[0] == str(1):
            FileURL = (
                FC[1]
                + "\\"
                + C_SCode
                + "_"
                + C_Name
                + "_"
                + C_Nendo
                + "_"
                + C_Zeimoku
                + "_"
                + C_Syurui
                + ".pdf"
            )
        else:
            FileURL = (
                FC[1]
                + "\\"
                + C_SCode
                + "_"
                + C_Name
                + "_"
                + C_Nendo
                + "_"
                + C_Zeimoku
                + "_"
                + C_Syurui
                + Tyouhuku[0]
                + ".pdf"
            )
        time.sleep(1)
        FileURL
        pyperclip.copy(FileURL)
        pg.hotkey("ctrl", "v")  # pg日本語不可なのでコピペ
        time.sleep(1)
        pg.press(["return"])
        time.sleep(1)
        # ----------------------------------------------------------------------------------------------------------------------
        # ----------------------------------------------------------------------------------------------------------------------
        ImgClick(Img_dir_D, "FileOutPutBtn.png", conf, LoopVal)
        time.sleep(1)
        while (
            pg.locateOnScreen(Img_dir_D + "/" + "UnderArrow.png", confidence=0.9)
            is None
        ):
            time.sleep(1)
            FO = ImgCheck(Img_dir_D, "FIleOver.png", 0.9, 10)
            if FO[0] is True:
                pg.press(["y"])
        time.sleep(3)
        ImgClick(Img_dir_D, "FallEnd.png", 0.9, 10)
        time.sleep(3)
        while (
            pg.locateOnScreen(Img_dir_D + "/" + "DensiSyomei.png", confidence=0.9)
            is not None
        ):
            while (
                pg.locateOnScreen(Img_dir_D + "/" + "Kanryou.png", confidence=0.9)
                is not None
            ):
                time.sleep(1)
                ImgClick(Img_dir_D, "SyousaiIcon.png", 0.9, 1)
                while (
                    pg.locateOnScreen(
                        Img_dir_D + "/" + "PrintSyousai.png", confidence=0.9
                    )
                    is None
                ):
                    time.sleep(1)
                PList = ["PrintSyousai.png", "PrintSyousaiWhite.png"]
                ICFL = ImgCheckForList(Img_dir_D, PList, 0.9, 1)
                ImgClick(Img_dir_D, ICFL[1], 0.9, 1)
                ICFLCount = 0
                while (
                    pg.locateOnScreen(
                        Img_dir_D + "/" + "SouRireList.png", confidence=0.9
                    )
                    is None
                ):
                    time.sleep(1)
                    ICFL = ImgCheckForList(Img_dir_D, PList, 0.9, 1)
                    ImgClick(Img_dir_D, ICFL[1], 0.9, 1)
                    if ICFLCount == 5:
                        break
                    else:
                        ICFLCount = ICFLCount + 1
                if ICFLCount == 5:
                    ImgClick(Img_dir_D, "DensiSyomei.png", 0.9, 1)  # 電子申告・申請タブを押す
                    time.sleep(3)
                    time.sleep(1)
                    ImgClick(Img_dir_D, "FindIcon.png", 0.9, 1)
                    time.sleep(1)
                    while (
                        pg.locateOnScreen(
                            Img_dir_D + "/" + "JyoukenBar.png", confidence=0.9
                        )
                        is None
                    ):
                        time.sleep(1)
                    time.sleep(1)
                    pg.press("r")
                else:
                    time.sleep(1)
                    pg.press("x")
                    time.sleep(1)
                    # ------------------------------------------------------------------------------------------------------------------------------------------
                    # 画像が出現するまで待機してクリック------------------------------------------------------------------------------------
                    List = ["FileOut.png", "FileOut2.png"]
                    conf = 0.9  # 画像認識感度
                    LoopVal = 10  # 検索回数
                    ListCheck = ImgCheckForList(
                        Img_dir_D, List, conf, LoopVal
                    )  # 画像検索関数
                    if ListCheck[0] is True:
                        ImgClick(Img_dir_D, ListCheck[1], conf, LoopVal)
                        time.sleep(1)
                    # ----------------------------------------------------------------------------------------------------------------------
                    # 画像が出現するまで待機してクリック------------------------------------------------------------------------------------
                    List = ["PDFIcon.png", "CSVIcon.png"]
                    conf = 0.9  # 画像認識感度
                    LoopVal = 10  # 検索回数
                    ListCheck = ImgCheckForList(
                        Img_dir_D, List, conf, LoopVal
                    )  # 画像検索関数
                    if ListCheck[0] is True:
                        ImgClick(Img_dir_D, ListCheck[1], conf, LoopVal)
                        time.sleep(1)
                        pg.press(["down", "down", "down", "down", "down"])
                        pg.press(["return"])
                    # ----------------------------------------------------------------------------------------------------------------------
                    time.sleep(2)
                    FC = FolCre(C_SCode, C_Name, C_Nendo, C_Zeimoku, C_Syurui)
                    Tyouhuku = SortPDF(C_SCode + "_" + C_Name)
                    if FC[0] is True:
                        if Tyouhuku[0] == str(1):
                            FileURL = (
                                FC[1]
                                + "\\"
                                + C_SCode
                                + "_"
                                + C_Name
                                + "_"
                                + C_Nendo
                                + "_"
                                + C_Zeimoku
                                + "_"
                                + C_Syurui
                                + "申告等送信票(兼送付書).pdf"
                            )
                        else:
                            FileURL = (
                                FC[1]
                                + "\\"
                                + C_SCode
                                + "_"
                                + C_Name
                                + "_"
                                + C_Nendo
                                + "_"
                                + C_Zeimoku
                                + "_"
                                + C_Syurui
                                + Tyouhuku[0]
                                + "申告等送信票(兼送付書).pdf"
                            )

                        pyperclip.copy(FileURL)
                        time.sleep(1)
                        pg.hotkey("ctrl", "v")  # pg日本語不可なのでコピペ
                        time.sleep(1)
                        pg.press(["return"])
                        time.sleep(1)
                        # ----------------------------------------------------------------------------------------------------------------------
                        # ----------------------------------------------------------------------------------------------------------------------
                        ImgClick(Img_dir_D, "FileOutPutBtn.png", conf, LoopVal)
                        time.sleep(1)
                    else:
                        if Tyouhuku[0] == str(1):
                            FileURL = (
                                FC[1]
                                + "\\"
                                + C_SCode
                                + "_"
                                + C_Name
                                + "_"
                                + C_Nendo
                                + "_"
                                + C_Zeimoku
                                + "_"
                                + C_Syurui
                                + "申告等送信票(兼送付書).pdf"
                            )
                        else:
                            FileURL = (
                                FC[1]
                                + "\\"
                                + C_SCode
                                + "_"
                                + C_Name
                                + "_"
                                + C_Nendo
                                + "_"
                                + C_Zeimoku
                                + "_"
                                + C_Syurui
                                + Tyouhuku[0]
                                + "申告等送信票(兼送付書).pdf"
                            )
                        pyperclip.copy(FileURL)
                        time.sleep(1)
                        pg.hotkey("ctrl", "v")  # pg日本語不可なのでコピペ
                        time.sleep(1)
                        pg.press(["return"])
                        time.sleep(1)
                        # ----------------------------------------------------------------------------------------------------------------------
                        # ----------------------------------------------------------------------------------------------------------------------
                        ImgClick(Img_dir_D, "FileOutPutBtn.png", conf, LoopVal)
                        time.sleep(1)
                    # ------------------------------------------------------------------------------------------------------------------------------------------
                    ImgClick(Img_dir_D, "DensiSyomei.png", 0.9, 1)  # 電子申告・申請タブを押す
                    time.sleep(3)
        time.sleep(1)
        ImgClick(Img_dir_D, "FindIcon.png", 0.9, 1)
        time.sleep(1)
        while (
            pg.locateOnScreen(Img_dir_D + "/" + "JyoukenBar.png", confidence=0.9)
            is None
        ):
            time.sleep(1)
        time.sleep(1)
        pg.press("r")
    else:
        print("フォルダ作成エラー")


def MainStarter():
    # 画像が出現するまで待機してクリック------------------------------------------------------------------------------------
    List = ["DensiSinkokuIcon.png", "DensiSinkokuIcon2.png"]
    conf = 0.9  # 画像認識感度
    LoopVal = 10  # 検索回数
    ListCheck = ImgCheckForList(Img_dir_D, List, conf, LoopVal)  # 画像検索関数
    if ListCheck[0] is True:
        ImgClick(Img_dir_D, ListCheck[1], conf, LoopVal)
        time.sleep(1)
        pg.keyDown("alt")
        pg.press("a")
        pg.keyUp("alt")
    time.sleep(1)
    # ----------------------------------------------------------------------------------------------------------------------
    # 画像が出現するまで待機してクリック------------------------------------------------------------------------------------
    List = ["DensiKaiteiClose.png", "DensiKaiteiClose2.png"]
    conf = 0.9  # 画像認識感度
    LoopVal = 10  # 検索回数
    ListCheck = ImgCheckForList(Img_dir_D, List, conf, LoopVal)  # 画像検索関数
    if ListCheck[0] is True:
        ImgClick(Img_dir_D, ListCheck[1], conf, LoopVal)
        time.sleep(1)
    time.sleep(1)
    # ----------------------------------------------------------------------------------------------------------------------
    # 画像が出現するまで待機してクリック------------------------------------------------------------------------------------
    List = ["DensiKidouIcon.png", "DensiKidouIcon2.png"]
    conf = 0.9  # 画像認識感度
    LoopVal = 10  # 検索回数
    ListCheck = ImgCheckForList(Img_dir_D, List, conf, LoopVal)  # 画像検索関数
    if ListCheck[0] is True:
        ImgClick(Img_dir_D, ListCheck[1], conf, LoopVal)
        time.sleep(1)
    time.sleep(1)
    # ----------------------------------------------------------------------------------------------------------------------
    ImgClick(Img_dir_D, "DensiSyomei.png", 0.9, 1)  # 電子申告・申請タブを押す
    # 画像が出現するまで待機してクリック------------------------------------------------------------------------------------
    List = ["DensiSyomeiOpen.png", "DensiSyomeiOpen2.png"]
    while ImgCheckForList(Img_dir_D, List, conf, LoopVal)[0] is False:  # 画像検索関数
        time.sleep(1)
        ImgClick(Img_dir_D, "DensiSyomei.png", 0.9, 1)  # 電子申告・申請タブを押す


# ----------------------------------------------------------------------------------------------------------------------
def MasterCSVGet(URL):
    try:
        # ----------------------------------------------------------------------------------------------------------------------
        pg.keyDown("alt")
        pg.press("p")
        pg.keyUp("alt")
        time.sleep(1)
        # 画像が出現するまで待機してクリック------------------------------------------------------------------------------------
        List = ["FileOut.png", "FileOut2.png"]
        conf = 0.9  # 画像認識感度
        LoopVal = 10  # 検索回数
        ListCheck = ImgCheckForList(Img_dir_D, List, conf, LoopVal)  # 画像検索関数
        if ListCheck[0] is True:
            ImgClick(Img_dir_D, ListCheck[1], conf, LoopVal)
            time.sleep(1)
        time.sleep(1)
        # ----------------------------------------------------------------------------------------------------------------------
        # 画像が出現するまで待機してクリック------------------------------------------------------------------------------------
        List = ["PDFIcon.png", "CSVIcon.png"]
        conf = 0.9  # 画像認識感度
        LoopVal = 10  # 検索回数
        ListCheck = ImgCheckForList(Img_dir_D, List, conf, LoopVal)  # 画像検索関数
        if ListCheck[0] is True:
            ImgClick(Img_dir_D, ListCheck[1], conf, LoopVal)
            time.sleep(1)
        time.sleep(1)
        pg.press(["up", "up", "up", "up", "up"])
        pg.press(["return"])
        # ----------------------------------------------------------------------------------------------------------------------
        FileURL = URL + r"\SyomeiMaster.csv"
        FileURL = FileURL.replace("*", ":")
        pg.write(FileURL, interval=0.01)  # 直接SENDできないのでpyautoguiで入力
        pg.press(["return"])
        # ----------------------------------------------------------------------------------------------------------------------
        ImgClick(Img_dir_D, "FileOutPutBtn.png", conf, LoopVal)
        time.sleep(2)
        FO = ImgCheck(Img_dir_D, "FIleOver.png", 0.9, 10)
        if FO[0] is True:
            pg.press(["y"])
        time.sleep(1)
        pg.keyDown("alt")
        pg.press("f4")
        pg.keyUp("alt")
        while (
            pg.locateOnScreen(Img_dir_D + "/" + "EndCheck.png", confidence=0.9) is None
        ):
            time.sleep(1)
        pg.press("y")
        time.sleep(1)
        pg.keyDown("alt")
        pg.press("f4")
        pg.keyUp("alt")
        while (
            pg.locateOnScreen(Img_dir_D + "/" + "NX-EndCheck.png", confidence=0.9)
            is None
        ):
            time.sleep(1)
        pg.press("y")
        time.sleep(1)
        return True
    except:
        return False
    # # #出力したCSVを読込み----------------------------------------------------------------------------------------------------------
    # CSVURL = Img_dir_D
    # CSVName = "/SyomeiMaster"
    # # C_url = CSVURL.replace("\\","/") + '/' + CSVName + '.CSV'
    # C_url = CSVURL + "/" + CSVName + ".CSV"
    # with codecs.open(C_url, "r", "Shift-JIS", "ignore") as file:
    #     C_df = pd.read_table(file, delimiter=",")
    #     ColLister = ["顧問先コード", "年度", "税目", "申告種類"]
    #     C_df = C_df.drop_duplicates(subset=ColLister)
    # print(C_df)
    # return C_df


# ---------------------------------------------------------------------------------------------------------------------------------
def MainFirstAction(Img_dir_D, C_SCode, C_Name, C_Nendo, C_Zeimoku, C_Syurui):
    conf = 0.9  # 画像認識感度
    LoopVal = 10
    IMGD = False
    time.sleep(1)
    while (
        pg.locateOnScreen(Img_dir_D + "/" + "SousinKekka.png", confidence=0.9) is None
    ):
        time.sleep(1)
        if ImgCheck(Img_dir_D, "DoujiSousin.png", conf, LoopVal)[0] is True:
            ImgClick(Img_dir_D, "DoujiSousinPrint.png", conf, LoopVal)
            IMGD = True
            break
        if ImgCheck(Img_dir_D, "ErrJyouhou.png", conf, LoopVal)[0] is True:
            time.sleep(1)
            pg.press("return")
            break
    conf = 0.9  # 画像認識感度
    LoopVal = 10  # 検索回数
    time.sleep(1)
    if IMGD is False:
        if ImgCheck(Img_dir_D, "SousinAfterErr.png", conf, LoopVal)[0] is True:
            pg.press("x")
            conf = 0.9  # 画像認識感度
            LoopVal = 20  # 検索回数
            FileName = "MSGNokori.png"
            time.sleep(1)
            if ImgCheck(Img_dir_D, FileName, conf, LoopVal)[0] is True:
                pg.press("n")
                time.sleep(1)
                while (
                    pg.locateOnScreen(
                        Img_dir_D + "/" + "UnderArrow.png", confidence=0.9
                    )
                    is None
                ):
                    time.sleep(1)
                time.sleep(1)
                ImgClick(Img_dir_D, "UnderArrow.png", conf, LoopVal)
                time.sleep(1)
                pg.press("q")
                # ----------------------------------------------------------------------------------------------------------------------
                conf = 0.9  # 画像認識感度
                LoopVal = 20  # 検索回数
                FileName = "EturanCheck.png"
                if ImgCheck(Img_dir_D, FileName, conf, LoopVal)[0] is True:
                    pg.press("return")
                FileName = "MSGSyousaiErr.png"
                if ImgCheck(Img_dir_D, FileName, conf, LoopVal)[0] is True:
                    pg.press("return")
                PrintAct(Img_dir_D, C_SCode, C_Name, C_Nendo, C_Zeimoku, C_Syurui)
            else:
                print("送信エラー")
                time.sleep(1)
                ImgClick(Img_dir_D, "DensiSyomeiXXX.png", conf, LoopVal)  # 電子申告・申請タブを押す
                # 画像が出現するまで待機してクリック------------------------------------------------------------------------------------
                List = ["DensiSyomeiOpenXXX.png", "DensiSyomeiOpenXXX2.png"]
                conf = 0.9  # 画像認識感度
                LoopVal = 10  # 検索回数
                ImgCheckForList(Img_dir_D, List, conf, LoopVal)  # 画像検索関数
                time.sleep(1)
                ImgClick(Img_dir_D, "DensiSyomei.png", 0.9, 1)  # 電子申告・申請タブを押す
                # 画像が出現するまで待機してクリック------------------------------------------------------------------------------------
                List = ["DensiSyomeiOpen.png", "DensiSyomeiOpen2.png"]
                conf = 0.9  # 画像認識感度
                LoopVal = 10  # 検索回数
                while ImgCheckForList(Img_dir_D, List, conf, LoopVal) is True:
                    time.sleep(1)
                time.sleep(1)
                ImgClick(Img_dir_D, "FindIcon.png", 0.9, 1)
                time.sleep(1)
                while (
                    pg.locateOnScreen(
                        Img_dir_D + "/" + "JyoukenBar.png", confidence=0.9
                    )
                    is None
                ):
                    time.sleep(1)
                time.sleep(1)
                pg.press("r")
        else:
            time.sleep(1)
            while (
                pg.locateOnScreen(Img_dir_D + "/" + "UnderArrow.png", confidence=0.9)
                is None
            ):
                time.sleep(1)
            time.sleep(1)
            ImgClick(Img_dir_D, "UnderArrow.png", conf, LoopVal)
            time.sleep(1)
            pg.press("q")
            # ----------------------------------------------------------------------------------------------------------------------
            conf = 0.9  # 画像認識感度
            LoopVal = 20  # 検索回数
            FileName = "EturanCheck.png"
            if ImgCheck(Img_dir_D, FileName, conf, LoopVal)[0] is True:
                pg.press("return")
            FileName = "MSGSyousaiErr.png"
            if ImgCheck(Img_dir_D, FileName, conf, LoopVal)[0] is True:
                pg.press("return")
            PrintAct(Img_dir_D, C_SCode, C_Name, C_Nendo, C_Zeimoku, C_Syurui)
    else:
        DSEL = ImgCheck(Img_dir_D, "DensiSyomei.png", conf, LoopVal)
        if DSEL[0] is True:
            ImgClick(Img_dir_D, "DensiSyomei.png", 0.9, 1)  # 電子申告・申請タブを押す
        # 画像が出現するまで待機してクリック------------------------------------------------------------------------------------
        time.sleep(1)
        ImgClick(Img_dir_D, "FindIcon.png", 0.9, 1)
        time.sleep(1)
        while (
            pg.locateOnScreen(Img_dir_D + "/" + "JyoukenBar.png", confidence=0.9)
            is None
        ):
            time.sleep(1)
        time.sleep(1)
        pg.press("r")


# -------------------------------------------------------------------------------------------------------------------------------
def MainFlow(Img_dir, NG_List):
    try:
        driver = MJSOpen.MainFlow("BatUrl", FolURL, Img_dir)  # MJSを起動しログイン後インスタンス化
        # ----------------------------------------------------------------------------------------------------------------------
        logger.debug("MJS操作画面へ偏移")
        MainStarter()  # データ送信画面までの関数
        time.sleep(1)
        logger.debug("FindIcon.pngをクリック")
        ImgClick(Img_dir_D, "FindIcon.png", 0.9, 1)
        time.sleep(1)
        logger.debug("JyoukenBar.pngを待機")
        while (
            pg.locateOnScreen(Img_dir_D + "/" + "JyoukenBar.png", confidence=0.9)
            is None
        ):
            time.sleep(1)
        CSVURL = Img_dir_D
        CSVName = "/SyomeiMaster"
        C_url = CSVURL + "/" + CSVName + ".CSV"
        with codecs.open(C_url, "r", "Shift-JIS", "ignore") as file:
            C_df = pd.read_table(file, delimiter=",")
        C_dfRow = np.array(C_df).shape[0]  # 配列行数取得
        time.sleep(1)
        logger.debug("CSVループ開始")
        # クラス要素クリック----------------------------------------------------------------------------------------------------------
        for y in range(C_dfRow):

            # time.sleep(1)
            # ImgClick(Img_dir_D,"FindIcon.png",0.9,1)
            # time.sleep(1)
            # time.sleep(1)
            logger.debug("CSV行データから値格納")
            # CSV要素取得-------------------------------------------------------------------------------------------------------------
            C_dfDataRow = C_df.iloc[y, :]
            C_SCode = str(int(C_dfDataRow["顧問先コード"]))
            C_Name = str(C_dfDataRow["顧問先名称"])
            C_Name = C_Name.replace("\u3000", " ")
            C_Nendo = str(C_dfDataRow["年度"]).replace("\\", "-")
            C_Zeimoku = str(C_dfDataRow["税目"])
            C_Syurui = str(C_dfDataRow["申告種類"])
            # NG_Listとの突合---------------------------------------------------------------------------------------------------------
            NG_r = 0
            NG_Flag = False
            for NG_ListItem in NG_List:
                for NG_r in range(len(NG_ListItem[1])):
                    NG_ListRow = NG_ListItem[1].iloc[NG_r]
                    NG_SCode = NG_ListRow["関与先コード"]
                    if NG_SCode == C_SCode:
                        NG_Flag = True
                        break
                    NG_r += 1
            if NG_Flag is False:
                # --------------------------------------------------------------------------------------------------------------------
                conf = 0.9
                LoopVal = 1
                logger.debug("SinkokuTuuti.pngを元に処理分岐")
                if ImgCheck(Img_dir_D, "SinkokuTuuti.png", conf, LoopVal)[0] is True:
                    DSEL = ImgCheck(Img_dir_D, "DensiSyomei.png", conf, LoopVal)
                    if DSEL[0] is True:
                        ImgClick(Img_dir_D, "DensiSyomei.png", 0.9, 1)  # 電子申告・申請タブを押す
                    # 画像が出現するまで待機してクリック------------------------------------------------------------------------------------
                    List = ["DensiSyomeiOpen.png", "DensiSyomeiOpen2.png"]
                    conf = 0.9  # 画像認識感度
                    LoopVal = 10  # 検索回数
                    while ImgCheckForList(Img_dir_D, List, conf, LoopVal) is True:
                        time.sleep(1)
                    time.sleep(1)
                    ImgClick(Img_dir_D, "FindIcon.png", 0.9, 1)
                    time.sleep(1)
                    while (
                        pg.locateOnScreen(
                            Img_dir_D + "/" + "JyoukenBar.png", confidence=0.9
                        )
                        is None
                    ):
                        time.sleep(1)
                    time.sleep(1)
                    pg.press("r")
                # ------------------------------------------------------------------------------------------------------------------------
                conf = 0.9  # 画像認識感度
                LoopVal = 10  # 検索回数
                FileName = "Tantousya.png"
                logger.debug("Tantousya.pngを元に処理分岐")
                if ImgCheck(Img_dir_D, FileName, conf, LoopVal)[0] is True:
                    ImgClick(Img_dir_D, FileName, conf, LoopVal)
                    pg.press("Home")
                    pg.press("return")
                time.sleep(1)
                # ----------------------------------------------------------------------------------------------------------------------
                logger.debug("KCodeBox.pngにコード入力")
                ImgClick(Img_dir_D, "KCodeBox.png", 0.9, 5)  # 関与先コードボックス
                pg.write(C_SCode, interval=0.01)  # 直接SENDできないのでpyautoguiで入力
                pg.press(["return"])
                # クラス要素クリック----------------------------------------------------------------------------------------------------------
                time.sleep(1)
                logger.debug("NendoBox.pngに年度入力")
                ImgClick(Img_dir_D, "NendoBox.png", conf, LoopVal)  # 電子申告・申請タブを押す
                pg.write(C_Nendo, interval=0.01)  # 直接SENDできないのでpyautoguiで入力
                pg.press(["return"])
                pg.write(C_Nendo, interval=0.01)  # 直接SENDできないのでpyautoguiで入力
                pg.press(["return"])
                # ----------------------------------------------------------------------------------------------------------------------
                conf = 0.9  # 画像認識感度
                LoopVal = 10  # 検索回数
                FileName = "ZeimokuRadio.png"
                logger.debug("税目処理分け")
                if ImgCheck(Img_dir_D, FileName, conf, LoopVal)[0] is True:
                    pg.press(["tab"])
                else:
                    pg.press(["right"])
                    pg.press(["right"])
                    pg.press(["tab"])
                time.sleep(1)
                # ----------------------------------------------------------------------------------------------------------------------
                SortURL = Img_dir_D + "/ミロク税目分岐"
                ZeimokuRow = SortCSVItem(SortURL, "Master", C_Zeimoku)
                for x in range(ZeimokuRow):
                    pg.press(["down"])
                pg.press(["space"])
                pg.press(["down"])
                time.sleep(1)
                try:
                    SortURL = Img_dir_D + "/ミロク税目分岐"
                    ZeimokuRow = SortCSVItem(SortURL, C_Zeimoku, C_Syurui)
                    for x in range(ZeimokuRow):
                        pg.press(["down"])
                    pg.press(["space"])
                    time.sleep(1)
                except:
                    logger.debug("補助税目無し")
                logger.debug("検索開始")
                # クラス要素クリック----------------------------------------------------------------------------------------------------------
                ImgClick(Img_dir_D, "FindOK.png", conf, LoopVal)  # 電子申告・申請タブを押す
                # ----------------------------------------------------------------------------------------------------------------------
                time.sleep(3)
                logger.debug("チェックボックスクリックを開始")
                # 画像が出現するまで待機してクリック------------------------------------------------------------------------------------
                List = [
                    "FindCheckBox.png",
                    "FindCheckBox2.png",
                    "FindCheckBox3.png",
                    "FindCheckBox4.png",
                ]
                conf = 0.9  # 画像認識感度
                LoopVal = 10  # 検索回数
                ListCheck = ImgCheckForList(Img_dir_D, List, conf, LoopVal)  # 画像検索関数
                conf = 0.9  # 画像認識感度
                LoopVal = 10  # 検索回数
                if ListCheck[0] is True:
                    for x in range(100):
                        ListCheck = ImgCheckForList(
                            Img_dir_D, List, conf, LoopVal
                        )  # 画像検索関数
                        if ListCheck[0] is True:
                            LoopVal = 10  # 検索回数
                            ImgClick(Img_dir_D, ListCheck[1], conf, LoopVal)
                            time.sleep(1)
                        else:
                            time.sleep(1)
                        if (
                            ImgCheck(Img_dir_D, "FindCheckBoxNext.png", conf, LoopVal)[
                                0
                            ]
                            is False
                        ):
                            break
                    time.sleep(1)
                    pg.press("left")
                    time.sleep(1)
                    ImgClick(Img_dir_D, "SousinBtn.png", 0.9, 3)
                    time.sleep(3)
                    if ImgCheck(Img_dir_D, "Tetuduki.png", conf, LoopVal)[0] is False:
                        time.sleep(1)
                        if (
                            ImgCheck(
                                Img_dir_D, "TihouTourokuKakunin.png", conf, LoopVal
                            )[0]
                            is False
                        ):
                            # クラス要素クリック----------------------------------------------------------------------------------------------------------
                            time.sleep(1)
                            Hub = "AutomationID"
                            ObjName = "DropDown"
                            DriverClick(Hub, ObjName, driver)
                            pg.press(["up", "up", "up"])
                            pg.press("return")
                            # クラス要素クリック----------------------------------------------------------------------------------------------------------
                            ImgClick(Img_dir_D, "SetuzokuOK.png", 0.9, 5)
                            # ----------------------------------------------------------------------------------------------------------------------
                            time.sleep(3)
                            MainFirstAction(
                                Img_dir_D, C_SCode, C_Name, C_Nendo, C_Zeimoku, C_Syurui
                            )
                            time.sleep(1)
                        else:
                            time.sleep(1)
                            conf = 0.9  # 画像認識感度
                            LoopVal = 10  # 検索回数
                            if (
                                ImgCheck(Img_dir_D, "Tetuduki.png", conf, LoopVal)[0]
                                is True
                            ):
                                pg.press("return")
                                time.sleep(1)
                                pg.press("o")
                                print("手続き未登録")
                                time.sleep(1)
                            else:
                                pg.press("o")
                                print("手続き未登録")
                                time.sleep(1)
                            # クラス要素クリック----------------------------------------------------------------------------------------------------------
                            time.sleep(1)
                            Hub = "AutomationID"
                            ObjName = "DropDown"
                            DriverClick(Hub, ObjName, driver)
                            pg.press(["up", "up", "up"])
                            pg.press("return")
                            # クラス要素クリック----------------------------------------------------------------------------------------------------------
                            ImgClick(Img_dir_D, "SetuzokuOK.png", 0.9, 5)
                            # ----------------------------------------------------------------------------------------------------------------------
                            logger.debug("メイン処理開始")
                            MainFirstAction(
                                Img_dir_D, C_SCode, C_Name, C_Nendo, C_Zeimoku, C_Syurui
                            )
                    else:
                        time.sleep(1)
                        conf = 0.9  # 画像認識感度
                        LoopVal = 10  # 検索回数
                        if (
                            ImgCheck(Img_dir_D, "Tetuduki.png", conf, LoopVal)[0]
                            is True
                        ):
                            pg.press("return")
                            time.sleep(1)
                            pg.press("o")
                            print("手続き未登録")
                            time.sleep(1)
                        else:
                            pg.press("o")
                            print("手続き未登録")
                            time.sleep(1)
                        # クラス要素クリック----------------------------------------------------------------------------------------------------------
                        time.sleep(1)
                        Hub = "AutomationID"
                        ObjName = "DropDown"
                        DriverClick(Hub, ObjName, driver)
                        pg.press(["up", "up", "up"])
                        pg.press("return")
                        # クラス要素クリック----------------------------------------------------------------------------------------------------------
                        ImgClick(Img_dir_D, "SetuzokuOK.png", 0.9, 5)
                        # ----------------------------------------------------------------------------------------------------------------------
                        logger.debug("メイン処理開始")
                        MainFirstAction(
                            Img_dir_D, C_SCode, C_Name, C_Nendo, C_Zeimoku, C_Syurui
                        )
                else:
                    logger.debug("検索結果なしの処理開始")
                    print("検索結果なし")
                    time.sleep(1)
                    ImgClick(
                        Img_dir_D, "DensiSyomeiXXX.png", conf, LoopVal
                    )  # 電子申告・申請タブを押す
                    # 画像が出現するまで待機してクリック------------------------------------------------------------------------------------
                    List = ["DensiSyomeiOpenXXX.png", "DensiSyomeiOpenXXX2.png"]
                    conf = 0.9  # 画像認識感度
                    LoopVal = 10  # 検索回数
                    ListCheck = ImgCheckForList(
                        Img_dir_D, List, conf, LoopVal
                    )  # 画像検索関数
                    time.sleep(1)
                    ImgClick(Img_dir_D, "DensiSyomei.png", 0.9, 1)  # 電子申告・申請タブを押す
                    # 画像が出現するまで待機してクリック------------------------------------------------------------------------------------
                    List = ["DensiSyomeiOpen.png", "DensiSyomeiOpen2.png"]
                    conf = 0.9  # 画像認識感度
                    LoopVal = 10  # 検索回数
                    while ImgCheckForList(Img_dir_D, List, conf, LoopVal) is True:
                        time.sleep(1)
                    time.sleep(1)
                    ImgClick(Img_dir_D, "FindIcon.png", 0.9, 1)
                    time.sleep(1)
                    while (
                        pg.locateOnScreen(
                            Img_dir_D + "/" + "JyoukenBar.png", confidence=0.9
                        )
                        is None
                    ):
                        time.sleep(1)
                    time.sleep(1)
                    pg.press("r")
            # else:
            #     print("決算なのでキャンセル")
    except Exception as e:
        logger.debug(e)


def main():
    try:
        List = []
        NG_List = []
        for fd_path, sb_folder, sb_file in os.walk(NG_Dir):
            if "処理済" not in sb_folder:
                for file in os.listdir(NG_Dir):
                    if os.path.isfile(os.path.join(NG_Dir, file)):
                        List = pd.read_csv(fd_path + r"\\" + file, encoding="shiftjis")
                        NG_List.append([fd_path, file, List])
        MainFlow(Img_dir, NG_List)
        for NG_ListItem in NG_List:
            os.rename(
                NG_ListItem[0] + r"\\" + NG_ListItem[1],
                NG_ListItem[0] + r"\\処理済\\" + NG_ListItem[1],
            )
    # ------------------------------------------------------------------------------
    except:
        traceback.print_exc()


class GUI(tk.Frame):
    def __init__(self, root):
        self.w = int(root.winfo_screenwidth() / 2)
        self.h = int(root.winfo_screenheight() / 2)
        self.x = int(root.winfo_screenwidth() / 4)
        self.y = int(root.winfo_screenheight() / 4)
        super().__init__(root)
        # フレーム
        self.fra = tk.Frame(root, bd=5)
        self.fra.pack(fill=tk.BOTH, expand=True)

        # インナーフレーム
        self.inner_upfra = tk.Frame(
            self.fra, width=self.w, height=(self.h / 2), bd=5, relief=tk.RAISED
        )
        self.inner_upfra.pack(side=tk.TOP, fill=tk.X, expand=True)

        # インナーフレーム要素
        # self.lb = tk.Label(self.inner_upfra, text="TEST")
        # self.lb.pack(side=tk.TOP)
        self.bt = tk.Button(self.inner_upfra, text="指示CSVダウンロード", command=self.csv_get)
        self.bt.grid(row=0, padx=5, sticky=tk.W + tk.E)

        self.txt = tk.Entry(self.inner_upfra, width=100)
        self.txt.grid(row=0, column=1, padx=5, sticky=tk.W + tk.E)

        # self.lb2 = tk.Label(self.inner_upfra, text="TEST")
        # self.lb2.pack(side=tk.TOP)
        self.bt2 = tk.Button(self.inner_upfra, text="指示CSV選択", command=self.csv_open)
        self.bt2.grid(row=1, padx=5, sticky=tk.W + tk.E)

        # インナーフレーム2
        self.inner_lowerfra = tk.Frame(self.fra, width=self.w, bd=5, relief=tk.RAISED)
        self.inner_lowerfra.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
        # テーブル
        self.table = MyTable.MyTable(self.inner_lowerfra, width=self.w)

    def csv_open(self):
        typ = [("CSVファイル", "*.csv")]
        self.csv_name = filedialog.askopenfilename(
            filetypes=typ,
            title="指示CSVを開く",
            initialdir=Img_dir_D,
        )
        self.enc = RPA.getFileEncoding(self.csv_name)
        self.table.importCSV(self.csv_name, encoding=self.enc)
        self.table.show()

    def csv_get(self):
        self.csv_dir = filedialog.askdirectory(
            title="指示CSV保存場所を選択",
            initialdir=Img_dir_D,
        )
        self.master.withdraw()
        tk.messagebox.showinfo(
            "注意",
            "これよりNX-PROを起動し、\n電子申告データ送信可能CSVリストをダウンロードします。\n処理が完了するまで[必ず]PC操作を中断して下さい。",
        )
        # MJSを起動しログイン後インスタンス化
        MJSOpen.MainFlow("BatUrl", FolURL, Img_dir)
        # ----------------------------------------------------------------------------------------------------------------------
        logger.debug("MJS操作画面へ偏移")
        MainStarter()  # データ送信画面までの関数
        logger.debug("CSVを保存")
        if MasterCSVGet(self.csv_dir) is True:
            tk.messagebox.showinfo(
                "完了",
                "電子申告データ送信可能CSVリストをダウンロードしました。",
            )
            Fileurl = self.csv_dir + r"\SyomeiMaster.csv"
            self.enc = RPA.getFileEncoding(Fileurl)
            self.table.importCSV(Fileurl, encoding=self.enc)
            self.table.show()
            self.master.deiconify()
        else:
            tk.messagebox.showinfo(
                "失敗",
                "電子申告データ送信可能CSVリストダウンロードに失敗しました。",
            )
            self.master.deiconify()


if __name__ == "__main__":
    global dir, Img_dir, Img_dir_D, FolURL, NG_Dir
    # RPA用画像フォルダの作成---------------------------------------------------------
    dir = RPA.My_Dir("MJS_DensiSinkoku")
    Img_dir = dir + r"\\img"
    Img_dir_D = Img_dir + r"/MJS_DensiSinkoku"
    FolURL = os.getcwd().replace("\\", "/")  # 先
    NG_Dir = r"\\NAS-SV\B_監査etc\B2_電子ﾌｧｲﾙ\ﾒｯｾｰｼﾞﾎﾞｯｸｽ\申請CSV"
    # ------------------------------------------------------------------------------
    # ルート設定#################################
    root = tk.Tk()
    w = root.winfo_screenwidth() / 2
    h = root.winfo_screenheight() / 2
    x = root.winfo_screenwidth() / 4
    y = root.winfo_screenheight() / 4
    # 画面中央に表示。
    root.geometry("%dx%d+%d+%d" % (w, h, x, y))
    ############################################
    GuiFrame = GUI(root)
    root.mainloop()
