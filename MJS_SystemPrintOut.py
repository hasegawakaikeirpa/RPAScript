# モジュールインポート
import pyautogui as pg
import time
import MJSOpen

# pandasインポート
import pandas as pd

# 配列計算関数numpyインポート
import numpy as np

# osインポート
import os

# datetimeインポート

# 例外処理判定の為のtracebackインポート
import traceback

# pandas(pd)で関与先データCSVを取得
import pyautogui
import pyperclip  # クリップボードへのコピーで使用
import Function.ExcelFileAction as EFA
import Function.CSVOut as FCO
import datetime
import openpyxl
from openpyxl.formatting.rule import Rule
from ctypes import windll

# logger設定------------------------------------------------------------------------------------------------------------
import logging.config

logging.config.fileConfig(r"LogConf\loggingMJSSysUp.conf")
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
def ImgCheckForList(FolURL2, List, conf, LoopVal):  # リスト内の画像があればTrueと画像名を返す
    for x in range(LoopVal):
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


# ------------------------------------------------------------------------------------------------------------------
def ChildFlow(
    FolURL,
    TFolURL,
    CFolURL,
    ExRow,
    Ex,
    Eh,
    ExrcHeader,
    isnItem,
    Title,
    PN,
    driver,
    Rno,
    Rn,
):
    if "会計大将" == Title:
        # Log---------------------------------------------------------------------------------------
        dt_s = datetime.datetime.now()
        dt_s = dt_s.strftime("%Y-%m-%d %H:%M:%S")
        logger.debug(dt_s + "_関与先番号:" + str(Rno) + ":" + str(Rn) + "_会計大将更新処理開始")
        with open(LURL, "a") as f:
            print([dt_s, "関与先番号:" + str(Rno), str(Rn), "会計大将更新処理開始"], file=f)
        # ------------------------------------------------------------------------------------------
        Fname = (
            r"D:\PythonScript\RPAScript\RPAPhoto\MJS_SystemPrintOut\PDF\\" + PN + ".pdf"
        )
        SystemUp = KaikeiUpDate(FolURL, TFolURL, CFolURL, ExRow, driver, PN, Fname)
        # Excel書き込み--------------------------------------------------
        if SystemUp[0] is True:
            dt_now = datetime.datetime.now()
            dt_now = dt_now.strftime("%Y/%m/%d %H:%M:%S")
            WriteEx = openpyxl.load_workbook(XLSURL)
            WriteExSheet = WriteEx[isnItem]
            WriteExSheet.cell(row=Ex + 5, column=Eh + 1).value = dt_now
            print("シート書き込み完了")
            print(WriteEx)
            WriteEx.save(XLSURL)
            WriteEx.close
            # ---------------------------------------------------------------
            # Log---------------------------------------------------------------------------------------
            dt_s = datetime.datetime.now()
            dt_s = dt_s.strftime("%Y-%m-%d %H:%M:%S")
            logger.debug(dt_s + "_関与先番号:" + str(Rno) + ":" + str(Rn) + "_会計大将更新処理終了")
            with open(LURL, "a") as f:
                print([dt_s, "関与先番号:" + str(Rno), str(Rn), "会計大将更新処理終了"], file=f)
            # ------------------------------------------------------------------------------------------
        else:
            # Log---------------------------------------------------------------------------------------
            dt_s = datetime.datetime.now()
            dt_s = dt_s.strftime("%Y-%m-%d %H:%M:%S")
            logger.debug(dt_s + "_関与先番号:" + str(Rno) + ":" + str(Rn) + "_会計大将更新処理エラー中断")
            with open(LURL, "a") as f:
                print([dt_s, "関与先番号:" + str(Rno), str(Rn), "会計大将更新エラー中断"], file=f)
            # ------------------------------------------------------------------------------------------
    elif "決算内訳書" == Title:
        # Log---------------------------------------------------------------------------------------
        dt_s = datetime.datetime.now()
        dt_s = dt_s.strftime("%Y-%m-%d %H:%M:%S")
        logger.debug(dt_s + "_関与先番号:" + str(Rno) + ":" + str(Rn) + "_決算内訳書更新処理開始")
        with open(LURL, "a") as f:
            print([dt_s, "関与先番号:" + str(Rno), str(Rn), "決算内訳書更新処理開始"], file=f)
        # ------------------------------------------------------------------------------------------
        Fname = (
            r"D:\PythonScript\RPAScript\RPAPhoto\MJS_SystemPrintOut\PDF\\" + PN + ".pdf"
        )
        SystemUp = KessanUpDate(FolURL, TFolURL, CFolURL, ExRow, driver, PN, Fname)
        # Excel書き込み--------------------------------------------------
        if SystemUp[0] is True:
            dt_now = datetime.datetime.now()
            dt_now = dt_now.strftime("%Y/%m/%d %H:%M:%S")
            WriteEx = openpyxl.load_workbook(XLSURL)
            WriteExSheet = WriteEx[isnItem]
            WriteExSheet.cell(row=Ex + 5, column=Eh + 1).value = dt_now
            print("シート書き込み完了")
            WriteEx.save(XLSURL)
            WriteEx.close
            # Log---------------------------------------------------------------------------------------
            dt_s = datetime.datetime.now()
            dt_s = dt_s.strftime("%Y-%m-%d %H:%M:%S")
            logger.debug(dt_s + "_関与先番号:" + str(Rno) + ":" + str(Rn) + "_決算内訳書更新処理終了")
            with open(LURL, "a") as f:
                print([dt_s, "関与先番号:" + str(Rno), str(Rn), "決算内訳書更新処理終了"], file=f)
            # ------------------------------------------------------------------------------------------
        elif SystemUp[1] == "Noren":
            dt_now = datetime.datetime.now()
            dt_now = dt_now.strftime("%Y/%m/%d %H:%M:%S")
            WriteEx = openpyxl.load_workbook(XLSURL)
            WriteExSheet = WriteEx[isnItem]
            WriteExSheet.cell(row=Ex + 5, column=Eh + 1).value = dt_now
            print("シート書き込み完了")
            WriteEx.save(XLSURL)
            WriteEx.close
            # Log---------------------------------------------------------------------------------------
            dt_s = datetime.datetime.now()
            dt_s = dt_s.strftime("%Y-%m-%d %H:%M:%S")
            logger.debug(dt_s + "_関与先番号:" + str(Rno) + ":" + str(Rn) + "_決算内訳書更新処理終了")
            with open(LURL, "a") as f:
                print([dt_s, "関与先番号:" + str(Rno), str(Rn), "決算内訳書更新処理終了"], file=f)
            # ------------------------------------------------------------------------------------------
    elif "減価償却" == Title:
        # Log---------------------------------------------------------------------------------------
        dt_s = datetime.datetime.now()
        dt_s = dt_s.strftime("%Y-%m-%d %H:%M:%S")
        logger.debug(dt_s + "_関与先番号:" + str(Rno) + ":" + str(Rn) + "_減価償却更新処理開始")
        with open(LURL, "a") as f:
            print([dt_s, "関与先番号:" + str(Rno), str(Rn), "減価償却更新処理開始"], file=f)
        # ------------------------------------------------------------------------------------------
        Fname = (
            r"D:\PythonScript\RPAScript\RPAPhoto\MJS_SystemPrintOut\PDF\\" + PN + ".pdf"
        )
        SystemUp = GenkasyoukyakuUpdate(
            FolURL, TFolURL, CFolURL, ExRow, driver, PN, Fname
        )
        # Excel書き込み---------------------------------------------------
        if SystemUp[0] is True:
            dt_now = datetime.datetime.now()
            dt_now = dt_now.strftime("%Y/%m/%d %H:%M:%S")
            WriteEx = openpyxl.load_workbook(XLSURL)
            WriteExSheet = WriteEx[isnItem]
            WriteExSheet.cell(row=Ex + 5, column=Eh + 1).value = dt_now
            print("シート書き込み完了")
            WriteEx.save(XLSURL)
            WriteEx.close
            # Log---------------------------------------------------------------------------------------
            dt_s = datetime.datetime.now()
            dt_s = dt_s.strftime("%Y-%m-%d %H:%M:%S")
            logger.debug(dt_s + "_関与先番号:" + str(Rno) + ":" + str(Rn) + "_減価償却更新処理終了")
            with open(LURL, "a") as f:
                print([dt_s, "関与先番号:" + str(Rno), str(Rn), "減価償却更新処理終了"], file=f)
            # ------------------------------------------------------------------------------------------
        elif SystemUp[1] == "Noren":
            dt_now = datetime.datetime.now()
            dt_now = dt_now.strftime("%Y/%m/%d %H:%M:%S")
            WriteEx = openpyxl.load_workbook(XLSURL)
            WriteExSheet = WriteEx[isnItem]
            WriteExSheet.cell(row=Ex + 5, column=Eh + 1).value = dt_now
            print("シート書き込み完了")
            WriteEx.save(XLSURL)
            WriteEx.close
            # Log---------------------------------------------------------------------------------------
            dt_s = datetime.datetime.now()
            dt_s = dt_s.strftime("%Y-%m-%d %H:%M:%S")
            logger.debug(
                dt_s + "_関与先番号:" + str(Rno) + ":" + str(Rn) + "_決算未確定減価償却更新処理終了"
            )
            with open(LURL, "a") as f:
                print(
                    [dt_s, "関与先番号:" + str(Rno), str(Rn), "決算未確定_減価償却更新処理終了"],
                    file=f,
                )
            # ------------------------------------------------------------------------------------------
    elif "法人税申告書" == Title:
        # Log---------------------------------------------------------------------------------------
        dt_s = datetime.datetime.now()
        dt_s = dt_s.strftime("%Y-%m-%d %H:%M:%S")
        logger.debug(dt_s + "_関与先番号:" + str(Rno) + ":" + str(Rn) + "_法人税申告書更新処理開始")
        with open(LURL, "a") as f:
            print([dt_s, "関与先番号:" + str(Rno), str(Rn), "法人税申告書更新処理開始"], file=f)
        # ------------------------------------------------------------------------------------------
        Fname = (
            r"D:\PythonScript\RPAScript\RPAPhoto\MJS_SystemPrintOut\PDF\\" + PN + ".pdf"
        )
        SystemUp = HoujinzeiUpdate(FolURL, TFolURL, CFolURL, ExRow, driver, PN, Fname)
        # Excel書き込み---------------------------------------------------
        if SystemUp[0] is True:
            dt_now = datetime.datetime.now()
            dt_now = dt_now.strftime("%Y/%m/%d %H:%M:%S")
            WriteEx = openpyxl.load_workbook(XLSURL)
            WriteExSheet = WriteEx[isnItem]
            WriteExSheet.cell(row=Ex + 5, column=Eh + 1).value = dt_now
            print("シート書き込み完了")
            WriteEx.save(XLSURL)
            WriteEx.close
            # Log---------------------------------------------------------------------------------------
            dt_s = datetime.datetime.now()
            dt_s = dt_s.strftime("%Y-%m-%d %H:%M:%S")
            logger.debug(dt_s + "_関与先番号:" + str(Rno) + ":" + str(Rn) + "_法人税申告書更新処理終了")
            with open(LURL, "a") as f:
                print([dt_s, "関与先番号:" + str(Rno), str(Rn), "法人税申告書更新処理終了"], file=f)
            # ------------------------------------------------------------------------------------------
        elif SystemUp[1] == "要データ再計算":
            dt_now = datetime.datetime.now()
            dt_now = dt_now.strftime("%Y/%m/%d %H:%M:%S")
            WriteEx = openpyxl.load_workbook(XLSURL)
            WriteExSheet = WriteEx[isnItem]
            WriteExSheet.cell(row=Ex + 5, column=Eh + 1).value = dt_now
            print("シート書き込み完了")
            WriteEx.save(XLSURL)
            WriteEx.close
            # Log---------------------------------------------------------------------------------------
            dt_s = datetime.datetime.now()
            dt_s = dt_s.strftime("%Y-%m-%d %H:%M:%S")
            logger.debug(dt_s + "_関与先番号:" + str(Rno) + ":" + str(Rn) + "_法人税申告書更新処理終了")
            with open(LURL, "a") as f:
                print([dt_s, "関与先番号:" + str(Rno), str(Rn), "法人税申告書更新処理終了"], file=f)
            # ------------------------------------------------------------------------------------------
        elif SystemUp[1] == "要申告指定":
            dt_now = datetime.datetime.now()
            dt_now = dt_now.strftime("%Y/%m/%d %H:%M:%S")
            WriteEx = openpyxl.load_workbook(XLSURL)
            WriteExSheet = WriteEx[isnItem]
            WriteExSheet.cell(row=Ex + 5, column=Eh + 1).value = dt_now
            print("シート書き込み完了")
            WriteEx.save(XLSURL)
            WriteEx.close
            # Log---------------------------------------------------------------------------------------
            dt_s = datetime.datetime.now()
            dt_s = dt_s.strftime("%Y-%m-%d %H:%M:%S")
            logger.debug(
                dt_s + "_関与先番号:" + str(Rno) + ":" + str(Rn) + "_法人税申告書申告指定無しの為中断"
            )
            with open(LURL, "a") as f:
                print(
                    [dt_s, "関与先番号:" + str(Rno), str(Rn), "法人税申告書申告指定無しの為中断"],
                    file=f,
                )
            # ------------------------------------------------------------------------------------------
    elif "電子申告" == Title:
        print("電子申告")
    elif "決算内訳書" == Title:
        print("決算内訳書")
    else:
        print("NoSystem")


# ------------------------------------------------------------------------------------------------------------------
def HoujinzeiUpdateSinkokuItiran(
    FolURL, TFolURL, CFolURL, ExRow, driver, PN, Fname, ThisNo, ThisYear, ThisMonth
):
    # 申告税一覧表印刷処理----------------------------------------------------
    OP = ImgCheckForList(
        CFolURL,
        [
            r"\Houjinzei\01SinkokuNyuuryoku.png",
            r"\Houjinzei\01SinkokuNyuuryoku2.png",
        ],
        0.9,
        10,
    )
    if OP[0] is True:
        ImgClick(CFolURL, OP[1], 0.9, 10)
        # 法人税メニューが表示されるまで待機------------------------------------
        while (
            pg.locateOnScreen(CFolURL + r"\Houjinzei\HoujinOpen.png", confidence=0.9)
            is None
        ):
            time.sleep(1)
        # --------------------------------------------------------------------
        if PN == "申告税一覧表":
            ImgClick(CFolURL, r"\Houjinzei\DownPrint.png", 0.9, 10)
            time.sleep(1)
            pg.press("n")
            # 一覧表メニューが表示されるまで待機------------------------------------
            while (
                pg.locateOnScreen(
                    CFolURL + r"\Houjinzei\ItiranFlag.png", confidence=0.9
                )
                is None
            ):
                time.sleep(1)
            # --------------------------------------------------------------------
            ImgClick(CFolURL, r"\Houjinzei\Print.png", 0.9, 10)
            # 一覧表出力項目指定が表示されるまで待機---------------------------------
            while (
                pg.locateOnScreen(
                    CFolURL + r"\Houjinzei\ItiranSyutuQ.png", confidence=0.9
                )
                is None
            ):
                time.sleep(1)
            # --------------------------------------------------------------------
            pg.press("return")
            # 一覧表出力項目指定が表示されるまで待機---------------------------------
            while (
                pg.locateOnScreen(CFolURL + r"\Houjinzei\PrintBar.png", confidence=0.9)
                is None
            ):
                time.sleep(1)
            # --------------------------------------------------------------------
            # 申告税一覧表印刷処理----------------------------------------------------
            FO = ImgCheckForList(
                CFolURL,
                [
                    r"\Houjinzei\FileOut.png",
                    r"\Houjinzei\FileOut2.png",
                ],
                0.9,
                10,
            )
            if FO[0] is True:
                ImgClick(CFolURL, FO[1], 0.9, 10)
            ImgClick(CFolURL, r"\Houjinzei\PDFBar.png", 0.9, 10)
            pg.press("return")
            pg.press("delete")
            pyperclip.copy(Fname)
            pg.hotkey("ctrl", "v")
            pg.press("return")
            time.sleep(1)
            ImgClick(CFolURL, r"\Houjinzei\PrintOut.png", 0.9, 10)
            # 印刷中が表示されるまで待機---------------------------------
            while (
                pg.locateOnScreen(CFolURL + r"\Houjinzei\NowPrint.png", confidence=0.9)
                is None
            ):
                time.sleep(1)
                FO = ImgCheck(CFolURL, r"\Houjinzei\FileOver.png", 0.9, 10)
                if FO[0] is True:
                    pg.press("y")
                    while (
                        pg.locateOnScreen(
                            CFolURL + r"\Houjinzei\NowPrint.png",
                            confidence=0.9,
                        )
                        is None
                    ):
                        time.sleep(1)
            # --------------------------------------------------------------------
            # 印刷中が表示されなくなるまで待機---------------------------------
            while (
                pg.locateOnScreen(CFolURL + r"\Houjinzei\NowPrint.png", confidence=0.9)
                is not None
            ):
                time.sleep(1)
            # --------------------------------------------------------------------
            time.sleep(1)
            pg.keyDown("alt")
            pg.press("x")
            pg.keyUp("alt")
            time.sleep(3)
            ImgClick(CFolURL, r"\Houjinzei\MenuEnd.png", 0.9, 10)
            # 終了確認が表示されるまで待機---------------------------------
            while (
                pg.locateOnScreen(
                    CFolURL + r"\Houjinzei\SinkokuEndQ.png", confidence=0.9
                )
                is None
            ):
                time.sleep(1)
            # --------------------------------------------------------------------
            pg.press("y")
            while (
                ImgCheckForList(
                    CFolURL,
                    [
                        r"\Houjinzei\01SinkokuNyuuryoku.png",
                        r"\Houjinzei\01SinkokuNyuuryoku2.png",
                    ],
                    0.9,
                    10,
                )[0]
                is False
            ):
                time.sleep(1)
                SEQ = ImgCheck(CFolURL, r"\Houjinzei\SinkokuEndQ2.png", 0.9, 10)
                if SEQ[0] is True:
                    ImgClick(CFolURL, r"\Houjinzei\SinkokuEndQ2Btn.png", 0.9, 10)
            # 閉じる処理--------------------------
            pg.keyDown("alt")
            pg.press("f4")
            pg.keyUp("alt")
            # -----------------------------------
            # 法人税フラグが表示されるまで待機-------------------------------------
            while (
                pg.locateOnScreen(TFolURL + r"\HoujinFlag.png", confidence=0.9) is None
            ):
                time.sleep(1)
            # --------------------------------------------------------------------
            # 初期画面で開封された法人税項目を閉じる----------------------------------
            HoujinList = [
                r"\FastMenuHoujinzei.png",
                r"\FastMenuHoujinzei2.png",
            ]
            HLI = ImgCheckForList(TFolURL, HoujinList, 0.9, 10)
            if HLI[0] is True:
                ImgClick(TFolURL, HLI[1], 0.9, 10)
            # --------------------------------------------------------------------
            return True, ThisNo, ThisYear, ThisMonth
        elif (
            PN == "第6号様式（県）"
            or PN == "第6号様式別表9（県）"
            or PN == "第20号様式（市）"
            or PN == "別表１　緑色"
        ):
            ImgClick(CFolURL, r"\Houjinzei\HoujinzeiSelecter.png", 0.9, 10)
            # 申告書印刷メニューが表示されるまで待機------------------------------------
            while (
                pg.locateOnScreen(
                    CFolURL + r"\Houjinzei\BeppyouIcon.png", confidence=0.9
                )
                is None
            ):
                time.sleep(1)
            # --------------------------------------------------------------------
            if PN == "第6号様式（県）":
                pg.press("end")
                pg.press(["up", "up"])
                pg.press("return")
            elif PN == "第6号様式別表9（県）":
                pg.press("end")
                pg.press("up")
                pg.press("return")
            elif PN == "第20号様式（市）":
                pg.press("end")
                pg.press("return")
            elif PN == "別表１　緑色":
                pg.press("home")
                pg.press("return")
            time.sleep(1)
            ImgClick(CFolURL, r"\Houjinzei\PreviewIcon.png", 0.9, 10)
            # プレビュー画面が表示されるまで待機------------------------------------
            while (
                pg.locateOnScreen(
                    CFolURL + r"\Houjinzei\HoujinOpen.png", confidence=0.9
                )
                is None
            ):
                time.sleep(1)
            # --------------------------------------------------------------------
            time.sleep(3)
            # ロード完了まで待機----------------------------------------------------
            while (
                pg.locateOnScreen(
                    CFolURL + r"\Houjinzei\PreviewLoad.png", confidence=0.9
                )
                is not None
            ):
                time.sleep(1)
            # --------------------------------------------------------------------
            TPI = ImgCheckForList(
                CFolURL,
                [r"\Houjinzei\ThisPIcon.png", r"\Houjinzei\ThisPIcon2.png"],
                0.9,
                10,
            )  # 現在項印刷アイコンを探す
            if TPI[0] is True:  # 現在項印刷アイコンがあれば
                # pg.keydown("alt")
                # pg.press("c")
                # pg.keyup("alt")
                ImgClick(CFolURL, TPI[1], 0.9, 10)  # 現在項印刷アイコンをクリック
                # 印刷ダイアログ待機----------------------------------------------------
                while (
                    pg.locateOnScreen(
                        CFolURL + r"\Houjinzei\ThisPMenu.png", confidence=0.9
                    )
                    is None
                ):
                    time.sleep(1)
                # --------------------------------------------------------------------
                pyperclip.copy(Fname.replace("\\\\", "\\"))
                pg.hotkey("ctrl", "v")
                pg.press("return")
                # 印刷完了まで待機----------------------------------------------------
                while (
                    pg.locateOnScreen(
                        CFolURL + r"\Houjinzei\ThisPMenu2.png", confidence=0.9
                    )
                    is not None
                ):
                    time.sleep(1)
                    TPOQ = ImgCheck(
                        CFolURL, r"\Houjinzei\ThisPOverQ.png", 0.9, 10
                    )  # 上書き確認
                    if TPOQ[0] is True:
                        pg.press("y")  # yで上書き
                # -------------------------------------------------------------------
                # 印刷完了まで待機----------------------------------------------------
                while (
                    pg.locateOnScreen(
                        CFolURL + r"\Houjinzei\NowPrint.png", confidence=0.9
                    )
                    is not None
                ):
                    time.sleep(1)
                # --------------------------------------------------------------------
                ImgClick(CFolURL, r"\Houjinzei\MenuEnd.png", 0.9, 10)
                # 終了確認が表示されるまで待機---------------------------------
                while (
                    pg.locateOnScreen(
                        CFolURL + r"\Houjinzei\SinkokuEndQ.png", confidence=0.9
                    )
                    is None
                ):
                    time.sleep(1)
                # --------------------------------------------------------------------
                pg.press("y")
                while (
                    ImgCheckForList(
                        CFolURL,
                        [
                            r"\Houjinzei\01SinkokuNyuuryoku.png",
                            r"\Houjinzei\01SinkokuNyuuryoku2.png",
                        ],
                        0.9,
                        10,
                    )[0]
                    is False
                ):
                    time.sleep(1)
                    SEQ = ImgCheck(CFolURL, r"\Houjinzei\SinkokuEndQ2.png", 0.9, 10)
                    if SEQ[0] is True:
                        ImgClick(CFolURL, r"\Houjinzei\SinkokuEndQ2Btn.png", 0.9, 10)
                # 閉じる処理--------------------------
                pg.keyDown("alt")
                pg.press("f4")
                pg.keyUp("alt")
                # -----------------------------------
                # 法人税フラグが表示されるまで待機-------------------------------------
                while (
                    pg.locateOnScreen(TFolURL + r"\HoujinFlag.png", confidence=0.9)
                    is None
                ):
                    time.sleep(1)
                # --------------------------------------------------------------------
                # 初期画面で開封された法人税項目を閉じる----------------------------------
                HoujinList = [
                    r"\FastMenuHoujinzei.png",
                    r"\FastMenuHoujinzei2.png",
                ]
                HLI = ImgCheckForList(TFolURL, HoujinList, 0.9, 10)
                if HLI[0] is True:
                    ImgClick(TFolURL, HLI[1], 0.9, 10)
                # --------------------------------------------------------------------
                return True, ThisNo, ThisYear, ThisMonth


# ------------------------------------------------------------------------------------------------------------------
def HoujinzeiUpdateZeimuDairi(
    FolURL, TFolURL, CFolURL, ExRow, driver, PN, Fname, ThisNo, ThisYear, ThisMonth
):
    # 税務代理権限証書印刷処理----------------------------------------------------
    OP = ImgCheckForList(
        CFolURL,
        [
            r"\Houjinzei\15Zeimudairi.png",
            r"\Houjinzei\15Zeimudairi2.png",
        ],
        0.9,
        10,
    )
    if OP[0] is True:
        ImgClick(CFolURL, OP[1], 0.9, 10)
        # 法人税メニューが表示されるまで待機------------------------------------
        while (
            pg.locateOnScreen(CFolURL + r"\Houjinzei\HoujinOpen.png", confidence=0.9)
            is None
        ):
            time.sleep(1)
        # --------------------------------------------------------------------
        ImgClick(CFolURL, r"\Houjinzei\ZeimuPrint.png", 0.9, 10)
        time.sleep(1)
        # 一覧表出力項目指定が表示されるまで待機---------------------------------
        while (
            pg.locateOnScreen(CFolURL + r"\Houjinzei\PrintBar.png", confidence=0.9)
            is None
        ):
            time.sleep(1)
        # --------------------------------------------------------------------
        # 申告税一覧表印刷処理----------------------------------------------------
        FO = ImgCheckForList(
            CFolURL,
            [
                r"\Houjinzei\FileOut.png",
                r"\Houjinzei\FileOut2.png",
            ],
            0.9,
            10,
        )
        if FO[0] is True:
            ImgClick(CFolURL, FO[1], 0.9, 10)
        ImgClick(CFolURL, r"\Houjinzei\PDFBar.png", 0.9, 10)
        pg.press("return")
        pg.press("delete")
        pyperclip.copy(Fname)
        pg.hotkey("ctrl", "v")
        pg.press("return")
        time.sleep(1)
        ImgClick(CFolURL, r"\Houjinzei\PrintOut.png", 0.9, 10)
        # 印刷中が表示されるまで待機---------------------------------
        while (
            pg.locateOnScreen(CFolURL + r"\Houjinzei\NowPrint.png", confidence=0.9)
            is None
        ):
            time.sleep(1)
            FO = ImgCheck(CFolURL, r"\Houjinzei\FileOver.png", 0.9, 10)
            if FO[0] is True:
                pg.press("y")
                while (
                    pg.locateOnScreen(
                        CFolURL + r"\Houjinzei\NowPrint.png",
                        confidence=0.9,
                    )
                    is None
                ):
                    time.sleep(1)
        # --------------------------------------------------------------------
        # 印刷中が表示されなくなるまで待機---------------------------------
        while (
            pg.locateOnScreen(CFolURL + r"\Houjinzei\NowZeimuPrint.png", confidence=0.9)
            is not None
        ):
            time.sleep(1)
        # --------------------------------------------------------------------
        time.sleep(1)
        ImgClick(CFolURL, r"\Houjinzei\ZeimuMEnd.png", 0.9, 10)
        # 終了確認が表示されるまで待機---------------------------------
        while (
            ImgCheckForList(
                CFolURL,
                [
                    r"\Houjinzei\15Zeimudairi.png",
                    r"\Houjinzei\15Zeimudairi2.png",
                ],
                0.9,
                10,
            )[0]
            is False
        ):
            time.sleep(1)
            SEQ = ImgCheck(CFolURL, r"\Houjinzei\SinkokuEndQ2.png", 0.9, 10)
            if SEQ[0] is True:
                ImgClick(CFolURL, r"\Houjinzei\SinkokuEndQ2Btn.png", 0.9, 10)
        # 閉じる処理--------------------------
        pg.keyDown("alt")
        pg.press("f4")
        pg.keyUp("alt")
        # -----------------------------------
        # 法人税フラグが表示されるまで待機-------------------------------------
        while pg.locateOnScreen(TFolURL + r"\HoujinFlag.png", confidence=0.9) is None:
            time.sleep(1)
        # --------------------------------------------------------------------
        # 初期画面で開封された法人税項目を閉じる----------------------------------
        HoujinList = [
            r"\FastMenuHoujinzei.png",
            r"\FastMenuHoujinzei2.png",
        ]
        HLI = ImgCheckForList(TFolURL, HoujinList, 0.9, 10)
        if HLI[0] is True:
            ImgClick(TFolURL, HLI[1], 0.9, 10)
        # --------------------------------------------------------------------
        return True, ThisNo, ThisYear, ThisMonth


# ------------------------------------------------------------------------------------------------------------------
def HoujinzeiUpdateSyomen(
    FolURL, TFolURL, CFolURL, ExRow, driver, PN, Fname, ThisNo, ThisYear, ThisMonth
):
    # 税務代理権限証書印刷処理----------------------------------------------------
    OP = ImgCheckForList(
        CFolURL,
        [
            r"\Houjinzei\16TenpuSyomen.png",
            r"\Houjinzei\16TenpuSyomen2.png",
        ],
        0.9,
        10,
    )
    if OP[0] is True:
        ImgClick(CFolURL, OP[1], 0.9, 10)
        # 法人税メニューが表示されるまで待機------------------------------------
        while (
            pg.locateOnScreen(CFolURL + r"\Houjinzei\HoujinOpen.png", confidence=0.9)
            is None
        ):
            time.sleep(1)
        # --------------------------------------------------------------------
        ImgClick(CFolURL, r"\Houjinzei\ZeimuPrint.png", 0.9, 10)
        time.sleep(1)
        # 用紙選択が表示されるまで待機---------------------------------
        while (
            pg.locateOnScreen(CFolURL + r"\Houjinzei\YousiSentaku.png", confidence=0.9)
            is None
        ):
            time.sleep(1)
        # --------------------------------------------------------------------
        ImgClick(CFolURL, r"\Houjinzei\YousiOK.png", 0.9, 10)
        # 申告税一覧表印刷処理----------------------------------------------------
        FO = ImgCheckForList(
            CFolURL,
            [
                r"\Houjinzei\FileOut.png",
                r"\Houjinzei\FileOut2.png",
            ],
            0.9,
            10,
        )
        if FO[0] is True:
            ImgClick(CFolURL, FO[1], 0.9, 10)
        ImgClick(CFolURL, r"\Houjinzei\PDFBar.png", 0.9, 10)
        pg.press("return")
        pg.press("delete")
        pyperclip.copy(Fname)
        pg.hotkey("ctrl", "v")
        pg.press("return")
        time.sleep(1)
        ImgClick(CFolURL, r"\Houjinzei\PrintOut.png", 0.9, 10)
        # 印刷中が表示されるまで待機---------------------------------
        while (
            pg.locateOnScreen(CFolURL + r"\Houjinzei\NowPrint.png", confidence=0.9)
            is None
        ):
            time.sleep(1)
            FO = ImgCheck(CFolURL, r"\Houjinzei\FileOver.png", 0.9, 10)
            if FO[0] is True:
                pg.press("y")
                while (
                    pg.locateOnScreen(
                        CFolURL + r"\Houjinzei\NowPrint.png",
                        confidence=0.9,
                    )
                    is None
                ):
                    time.sleep(1)
        # --------------------------------------------------------------------
        # 印刷中が表示されなくなるまで待機---------------------------------
        while (
            pg.locateOnScreen(
                CFolURL + r"\Houjinzei\NowSyomenPrint.png", confidence=0.9
            )
            is not None
        ):
            time.sleep(1)
        # --------------------------------------------------------------------
        time.sleep(1)
        ImgClick(CFolURL, r"\Houjinzei\ZeimuMEnd.png", 0.9, 10)
        # 終了確認が表示されるまで待機---------------------------------
        while (
            ImgCheckForList(
                CFolURL,
                [
                    r"\Houjinzei\16TenpuSyomen.png",
                    r"\Houjinzei\16TenpuSyomen2.png",
                ],
                0.9,
                10,
            )[0]
            is False
        ):
            time.sleep(1)
            SEQ = ImgCheck(CFolURL, r"\Houjinzei\SinkokuEndQ2.png", 0.9, 10)
            if SEQ[0] is True:
                ImgClick(CFolURL, r"\Houjinzei\SinkokuEndQ2Btn.png", 0.9, 10)
        # 閉じる処理--------------------------
        pg.keyDown("alt")
        pg.press("f4")
        pg.keyUp("alt")
        # -----------------------------------
        # 法人税フラグが表示されるまで待機-------------------------------------
        while pg.locateOnScreen(TFolURL + r"\HoujinFlag.png", confidence=0.9) is None:
            time.sleep(1)
        # --------------------------------------------------------------------
        # 初期画面で開封された法人税項目を閉じる----------------------------------
        HoujinList = [
            r"\FastMenuHoujinzei.png",
            r"\FastMenuHoujinzei2.png",
        ]
        HLI = ImgCheckForList(TFolURL, HoujinList, 0.9, 10)
        if HLI[0] is True:
            ImgClick(TFolURL, HLI[1], 0.9, 10)
        # --------------------------------------------------------------------
        return True, ThisNo, ThisYear, ThisMonth


# ------------------------------------------------------------------------------------------------------------------
def HoujinzeiUpdateBeppyou(
    FolURL, TFolURL, CFolURL, ExRow, driver, PN, Fname, ThisNo, ThisYear, ThisMonth
):
    # 別表2-16印刷処理--------------------------------------------------------
    OP = ImgCheckForList(
        CFolURL,
        [
            r"\Houjinzei\01SinkokuNyuuryoku.png",
            r"\Houjinzei\01SinkokuNyuuryoku2.png",
        ],
        0.9,
        10,
    )
    if OP[0] is True:
        ImgClick(CFolURL, OP[1], 0.9, 10)
        # 法人税メニューが表示されるまで待機------------------------------------
        while (
            pg.locateOnScreen(CFolURL + r"\Houjinzei\HoujinOpen.png", confidence=0.9)
            is None
        ):
            time.sleep(1)
        # --------------------------------------------------------------------
        ImgClick(CFolURL, r"\Houjinzei\DownPrint.png", 0.9, 10)
        time.sleep(1)
        pg.press("s")
        # 一覧表メニューが表示されるまで待機------------------------------------
        while (
            pg.locateOnScreen(CFolURL + r"\Houjinzei\SItiranFlag.png", confidence=0.9)
            is None
        ):
            time.sleep(1)
            HEQ = ImgCheck(CFolURL, r"\Houjinzei\HNoEntryQ.png", 0.9, 10)
            if HEQ[0] is True:  # 法人番号未登録ダイアログが表示されていたら
                pg.press("y")  # yで確定
        # --------------------------------------------------------------------
        ImgClick(CFolURL, r"\Houjinzei\SPrint.png", 0.9, 10)
        # 一覧表出力項目指定が表示されるまで待機---------------------------------
        while (
            pg.locateOnScreen(CFolURL + r"\Houjinzei\PrintBar.png", confidence=0.9)
            is None
        ):
            time.sleep(1)
        # --------------------------------------------------------------------
        # 申告税一覧表印刷処理----------------------------------------------------
        FO = ImgCheckForList(
            CFolURL,
            [
                r"\Houjinzei\FileOut.png",
                r"\Houjinzei\FileOut2.png",
            ],
            0.9,
            10,
        )
        if FO[0] is True:
            ImgClick(CFolURL, FO[1], 0.9, 10)
        ImgClick(CFolURL, r"\Houjinzei\PDFBar.png", 0.9, 10)
        pg.press("return")
        pg.press("delete")
        pyperclip.copy(Fname)
        pg.hotkey("ctrl", "v")
        pg.press("return")
        time.sleep(1)
        ImgClick(CFolURL, r"\Houjinzei\PrintOut.png", 0.9, 10)
        # 印刷中が表示されるまで待機---------------------------------
        while (
            pg.locateOnScreen(CFolURL + r"\Houjinzei\NowPrint.png", confidence=0.9)
            is None
        ):
            time.sleep(1)
            FO = ImgCheck(CFolURL, r"\Houjinzei\FileOver.png", 0.9, 10)
            if FO[0] is True:
                pg.press("y")
                while (
                    pg.locateOnScreen(
                        CFolURL + r"\Houjinzei\NowPrint.png",
                        confidence=0.9,
                    )
                    is None
                ):
                    time.sleep(1)
        # --------------------------------------------------------------------
        # 印刷中が表示されなくなるまで待機---------------------------------
        while (
            pg.locateOnScreen(CFolURL + r"\Houjinzei\NowPrint.png", confidence=0.9)
            is not None
        ):
            time.sleep(1)
        # --------------------------------------------------------------------
        time.sleep(1)
        pg.keyDown("alt")
        pg.press("x")
        pg.keyUp("alt")
        time.sleep(3)
        ImgClick(CFolURL, r"\Houjinzei\MenuEnd.png", 0.9, 10)
        # 終了確認が表示されるまで待機---------------------------------
        while (
            pg.locateOnScreen(CFolURL + r"\Houjinzei\SinkokuEndQ.png", confidence=0.9)
            is None
        ):
            time.sleep(1)
        # --------------------------------------------------------------------
        pg.press("y")
        while (
            ImgCheckForList(
                CFolURL,
                [
                    r"\Houjinzei\01SinkokuNyuuryoku.png",
                    r"\Houjinzei\01SinkokuNyuuryoku2.png",
                ],
                0.9,
                10,
            )[0]
            is False
        ):
            time.sleep(1)
            SEQ = ImgCheck(CFolURL, r"\Houjinzei\SinkokuEndQ2.png", 0.9, 10)
            if SEQ[0] is True:
                ImgClick(CFolURL, r"\Houjinzei\SinkokuEndQ2Btn.png", 0.9, 10)
        # 閉じる処理--------------------------
        pg.keyDown("alt")
        pg.press("f4")
        pg.keyUp("alt")
        # -----------------------------------
        # 法人税フラグが表示されるまで待機-------------------------------------
        while pg.locateOnScreen(TFolURL + r"\HoujinFlag.png", confidence=0.9) is None:
            time.sleep(1)
        # --------------------------------------------------------------------
        # 初期画面で開封された法人税項目を閉じる----------------------------------
        HoujinList = [
            r"\FastMenuHoujinzei.png",
            r"\FastMenuHoujinzei2.png",
        ]
        HLI = ImgCheckForList(TFolURL, HoujinList, 0.9, 10)
        if HLI[0] is True:
            ImgClick(TFolURL, HLI[1], 0.9, 10)
        # --------------------------------------------------------------------
        return True, ThisNo, ThisYear, ThisMonth


# ------------------------------------------------------------------------------------------------------------------
def HoujinzeiUpdateGaikyou(
    FolURL, TFolURL, CFolURL, ExRow, driver, PN, Fname, ThisNo, ThisYear, ThisMonth
):
    # 事業概況説明書印刷処理--------------------------------------------------------
    OP = ImgCheckForList(
        CFolURL,
        [
            r"\Houjinzei\02JigyouGaikyou.png",
            r"\Houjinzei\02JigyouGaikyou2.png",
        ],
        0.9,
        10,
    )
    if OP[0] is True:
        ImgClick(CFolURL, OP[1], 0.9, 10)
        # 法人税メニューが表示されるまで待機------------------------------------
        while (
            pg.locateOnScreen(CFolURL + r"\Houjinzei\HoujinOpen.png", confidence=0.9)
            is None
        ):
            time.sleep(1)
        # --------------------------------------------------------------------
        ImgClick(CFolURL, r"\Houjinzei\GaikyouPrint.png", 0.9, 10)
        # 一覧表出力項目指定が表示されるまで待機---------------------------------
        while (
            pg.locateOnScreen(CFolURL + r"\Houjinzei\PrintBar.png", confidence=0.9)
            is None
        ):
            time.sleep(1)
            # 印刷条件設定----------------------------------------------------------
            GP = ImgCheck(CFolURL, r"\Houjinzei\GPMenu.png", 0.9, 10)
            if GP[0] is True:
                # 白紙チェックボックス確認
                HP = ImgCheck(CFolURL, r"\Houjinzei\HPCheck.png", 0.9, 10)
                if HP[0] is True:
                    # 白紙チェックボックスが未指定ならクリック
                    ImgClick(CFolURL, r"\Houjinzei\HPCheck.png", 0.9, 10)
                    # 両面チェックボックス確認
                    RM = ImgCheck(CFolURL, r"\Houjinzei\Ryoumen.png", 0.9, 10)
                    if RM[0] is True:
                        # 両面チェックボックスが未指定ならクリック
                        ImgClick(CFolURL, r"\Houjinzei\Ryoumen.png", 0.9, 10)
                        # 印刷ボタンクリック
                        ImgClick(CFolURL, r"\Houjinzei\GPPrint.png", 0.9, 10)
                    else:
                        # 両面チェックボックスが指定済の場合
                        # 印刷ボタンクリック
                        ImgClick(CFolURL, r"\Houjinzei\GPPrint.png", 0.9, 10)
                else:
                    # 白紙チェックボックスが指定済の場合
                    # 両面チェックボックス確認
                    RM = ImgCheck(CFolURL, r"\Houjinzei\Ryoumen.png", 0.9, 10)
                    if RM[0] is True:
                        # 両面チェックボックスが未指定ならクリック
                        ImgClick(CFolURL, r"\Houjinzei\Ryoumen.png", 0.9, 10)
                        # 印刷ボタンクリック
                        ImgClick(CFolURL, r"\Houjinzei\GPPrint.png", 0.9, 10)
                    else:
                        # 両面チェックボックスが指定済の場合
                        # 印刷ボタンクリック
                        ImgClick(CFolURL, r"\Houjinzei\GPPrint.png", 0.9, 10)
        # --------------------------------------------------------------------------
        # 申告税一覧表印刷処理----------------------------------------------------
        FO = ImgCheckForList(
            CFolURL,
            [
                r"\Houjinzei\FileOut.png",
                r"\Houjinzei\FileOut2.png",
            ],
            0.9,
            10,
        )
        if FO[0] is True:
            ImgClick(CFolURL, FO[1], 0.9, 10)
        ImgClick(CFolURL, r"\Houjinzei\PDFBar.png", 0.9, 10)
        pg.press("return")
        pg.press("delete")
        pyperclip.copy(Fname)
        pg.hotkey("ctrl", "v")
        pg.press("return")
        time.sleep(1)
        ImgClick(CFolURL, r"\Houjinzei\PrintOut.png", 0.9, 10)
        # 印刷中が表示されるまで待機---------------------------------
        while (
            pg.locateOnScreen(CFolURL + r"\Houjinzei\NowPrint.png", confidence=0.9)
            is None
        ):
            time.sleep(1)
            FO = ImgCheck(CFolURL, r"\Houjinzei\FileOver.png", 0.9, 10)
            if FO[0] is True:
                pg.press("y")
                while (
                    pg.locateOnScreen(
                        CFolURL + r"\Houjinzei\NowPrint.png",
                        confidence=0.9,
                    )
                    is None
                ):
                    time.sleep(1)
        # --------------------------------------------------------------------
        # 印刷中が表示されなくなるまで待機---------------------------------
        while (
            pg.locateOnScreen(CFolURL + r"\Houjinzei\NowPrint.png", confidence=0.9)
            is not None
        ):
            time.sleep(1)
        # --------------------------------------------------------------------
        time.sleep(1)
        pg.keyDown("alt")
        pg.press("x")
        pg.keyUp("alt")
        time.sleep(3)
        ImgClick(CFolURL, r"\Houjinzei\MenuEnd.png", 0.9, 10)
        # 終了確認が表示されるまで待機---------------------------------
        while (
            pg.locateOnScreen(CFolURL + r"\Houjinzei\GaikyouEndQ.png", confidence=0.9)
            is None
        ):
            time.sleep(1)
        # --------------------------------------------------------------------
        pg.press("y")
        while (
            ImgCheckForList(
                CFolURL,
                [
                    r"\Houjinzei\02JigyouGaikyou.png",
                    r"\Houjinzei\02JigyouGaikyou2.png",
                ],
                0.9,
                10,
            )[0]
            is False
        ):
            time.sleep(1)
            SEQ = ImgCheck(CFolURL, r"\Houjinzei\SinkokuEndQ2.png", 0.9, 10)
            if SEQ[0] is True:
                ImgClick(CFolURL, r"\Houjinzei\SinkokuEndQ2Btn.png", 0.9, 10)
        # 閉じる処理--------------------------
        pg.keyDown("alt")
        pg.press("f4")
        pg.keyUp("alt")
        # -----------------------------------
        # 法人税フラグが表示されるまで待機-------------------------------------
        while pg.locateOnScreen(TFolURL + r"\HoujinFlag.png", confidence=0.9) is None:
            time.sleep(1)
        # --------------------------------------------------------------------
        # 初期画面で開封された法人税項目を閉じる----------------------------------
        HoujinList = [
            r"\FastMenuHoujinzei.png",
            r"\FastMenuHoujinzei2.png",
        ]
        HLI = ImgCheckForList(TFolURL, HoujinList, 0.9, 10)
        if HLI[0] is True:
            ImgClick(TFolURL, HLI[1], 0.9, 10)
        # --------------------------------------------------------------------
        return True, ThisNo, ThisYear, ThisMonth


# ------------------------------------------------------------------------------------------------------------------
def HoujinzeiUpdate(FolURL, TFolURL, CFolURL, ExRow, driver, PN, Fname):
    """
    概要: 法人税更新処理
    @param FolURL : ミロク起動関数のフォルダ(str)
    @param TFolURL : このpyファイルのフォルダ(str)
    @param ExRow : Excel抽出行(obj)
    @param driver : 画面操作ドライバー(obj)
    @return : bool,ミロク入力関与先コード, ミロク入力処理年, ミロク入力処理月
    """
    try:
        ErrStr = ""  # Rpaエラー判別変数
        # 法人税のアイコンを探す-------------------------------------------------
        ImgList = [r"\Houjinzei.png", r"\Houjinzei2.png"]
        ICFL = ImgCheckForList(TFolURL, ImgList, 0.9, 10)
        # -----------------------------------------------------------------------
        if ICFL[0] is True:  # 法人税のアイコンがあれば
            ImgClick(TFolURL, ICFL[1], 0.9, 10)  # 法人税のアイコンをクリック
            # 法人税フラグが表示されるまで待機------------------------------------
            while (
                pg.locateOnScreen(TFolURL + r"\HoujinFlag.png", confidence=0.9) is None
            ):
                time.sleep(1)
            # ------------------------------------------------------------------
            time.sleep(1)
            # 他システムとメニューが違う-------------------------------------------------------
            # 年度を最新に指定----------------------------------------------------
            IC = ImgCheck(TFolURL, r"\Nendo_Saisin.png", 0.9, 10)
            if IC[0] is False:
                IC2 = ImgCheck(TFolURL, r"\Nendo_All.png", 0.9, 10)
                if IC2[0] is False:
                    print("年度選択がない")
                else:
                    ImgClick(TFolURL, r"\Nendo_All.png", 0.9, 10)
                    pg.press("home")
                    time.sleep(1)
                    pg.press("down")
                    time.sleep(1)
                    pg.press("return")
                    time.sleep(1)
            # ------------------------------------------------------------------
            # 関与先コード入力ボックスをクリック------------------------------------
            ImgClick(TFolURL, r"\K_NoBox.png", 0.9, 10)
            while (
                pg.locateOnScreen(TFolURL + r"\K_AfterNoBox.png", confidence=0.9)
                is None
            ):
                time.sleep(1)
            pg.write(str(ExRow["関与先番号"]))
            pg.press(["return", "return"])
            # -----------------------------------
            if ImgCheck(TFolURL, r"\NotData.png", 0.9, 10)[0] is True:
                # 入力した関与先コードを取得------------
                pg.press(["return", "return"])
                pg.keyDown("shift")
                pg.press(["tab", "tab", "tab", "tab"])
                pg.keyUp("shift")
                if windll.user32.OpenClipboard(None):
                    windll.user32.EmptyClipboard()
                    windll.user32.CloseClipboard()
                pg.hotkey("ctrl", "c")
                ThisNo = pyperclip.paste()
                pg.press("return")
                # クリップボードをクリア----------------
                if windll.user32.OpenClipboard(None):
                    windll.user32.EmptyClipboard()
                    windll.user32.CloseClipboard()
                # ------------------------------------
                # 表示された年度を取得-----------------
                if windll.user32.OpenClipboard(None):
                    windll.user32.EmptyClipboard()
                    windll.user32.CloseClipboard()
                pg.hotkey("ctrl", "c")
                ThisYear = pyperclip.paste()
                # -----------------------------------
                pg.press("return")
                # 表示された申告種類を取得---------------
                if windll.user32.OpenClipboard(None):
                    windll.user32.EmptyClipboard()
                    windll.user32.CloseClipboard()
                pg.hotkey("ctrl", "c")
                ThisMonth = pyperclip.paste()
                pg.press("return")
                # -----------------------------------
            else:
                # 入力した関与先コードを取得------------
                pg.press(["return", "return"])
                pg.keyDown("shift")
                pg.press(["tab", "tab", "tab", "tab"])
                pg.keyUp("shift")
                if windll.user32.OpenClipboard(None):
                    windll.user32.EmptyClipboard()
                    windll.user32.CloseClipboard()
                pg.hotkey("ctrl", "c")
                ThisNo = pyperclip.paste()
                pg.press("return")
                # 表示された年度を取得-----------------
                if windll.user32.OpenClipboard(None):
                    windll.user32.EmptyClipboard()
                    windll.user32.CloseClipboard()
                pg.hotkey("ctrl", "c")
                ThisYear = pyperclip.paste()
                # -----------------------------------
                pg.press("return")
                # 表示された申告種類を取得---------------
                if windll.user32.OpenClipboard(None):
                    windll.user32.EmptyClipboard()
                    windll.user32.CloseClipboard()
                pg.hotkey("ctrl", "c")
                ThisMonth = pyperclip.paste()
                pg.press("return")
                # -----------------------------------
            # 他システムとメニューが違う-------------------------------------------------------
            if str(ExRow["関与先番号"]) == ThisNo:
                print("関与先あり")
                pg.press(["return", "return", "return"])
                # 法人税メニューが表示されるまで待機------------------------------------
                while (
                    pg.locateOnScreen(TFolURL + r"\HoujinzeiMenu.png", confidence=0.9)
                    is None
                ):
                    time.sleep(1)
                    HQ = ImgCheck(TFolURL, r"\HoujinOpenQ.png", 0.9, 10)
                    if HQ[0] is True:
                        ImgClick(TFolURL, r"\HoujinOpenQCansel.png", 0.9, 10)
                # 指示内容で処理分け----------------------------------------------------------
                if (
                    PN == "申告税一覧表"
                    or PN == "第6号様式（県）"
                    or PN == "第6号様式別表9（県）"
                    or PN == "第20号様式（市）"
                    or PN == "別表１　緑色"
                ):
                    PNFlow = HoujinzeiUpdateSinkokuItiran(
                        FolURL,
                        TFolURL,
                        ExRow,
                        driver,
                        PN,
                        Fname,
                        ThisNo,
                        ThisYear,
                        ThisMonth,
                    )
                    return PNFlow[0], PNFlow[1], PNFlow[2], PNFlow[3]
                elif PN == "税務代理権限書":
                    PNFlow = HoujinzeiUpdateZeimuDairi(
                        FolURL,
                        TFolURL,
                        ExRow,
                        driver,
                        PN,
                        Fname,
                        ThisNo,
                        ThisYear,
                        ThisMonth,
                    )
                    return PNFlow[0], PNFlow[1], PNFlow[2], PNFlow[3]
                elif PN == "書面添付　法人税":
                    PNFlow = HoujinzeiUpdateSyomen(
                        FolURL,
                        TFolURL,
                        ExRow,
                        driver,
                        PN,
                        Fname,
                        ThisNo,
                        ThisYear,
                        ThisMonth,
                    )
                    return PNFlow[0], PNFlow[1], PNFlow[2], PNFlow[3]
                elif PN == "別表2-16":
                    PNFlow = HoujinzeiUpdateBeppyou(
                        FolURL,
                        TFolURL,
                        ExRow,
                        driver,
                        PN,
                        Fname,
                        ThisNo,
                        ThisYear,
                        ThisMonth,
                    )
                    return PNFlow[0], PNFlow[1], PNFlow[2], PNFlow[3]
                elif PN == "法人事業概況説明書":
                    PNFlow = HoujinzeiUpdateGaikyou(
                        FolURL,
                        TFolURL,
                        ExRow,
                        driver,
                        PN,
                        Fname,
                        ThisNo,
                        ThisYear,
                        ThisMonth,
                    )
                    return PNFlow[0], PNFlow[1], PNFlow[2], PNFlow[3]
                elif ErrStr == "ReCalc":
                    # 閉じる処理--------------------------
                    pg.keyDown("alt")
                    pg.press("f4")
                    pg.keyUp("alt")
                    # -----------------------------------
                    # 法人税フラグが表示されるまで待機-------------------------------------
                    while (
                        pg.locateOnScreen(TFolURL + r"\HoujinFlag.png", confidence=0.9)
                        is None
                    ):
                        time.sleep(1)
                    # --------------------------------------------------------------------
                    # 初期画面で開封された法人税項目を閉じる----------------------------------
                    HoujinList = [r"\FastMenuHoujinzei.png", r"\FastMenuHoujinzei2.png"]
                    HLI = ImgCheckForList(TFolURL, HoujinList, 0.9, 10)
                    if HLI[0] is True:
                        ImgClick(TFolURL, HLI[1], 0.9, 10)
                    # --------------------------------------------------------------------
                    return False, "要データ再計算", "", ""
            else:
                print("関与先なし")
                return False, "関与先なし", "", ""
        else:
            return False, "法人税起動失敗", "", ""
    except:
        return False, "exceptエラー", "", ""


# ------------------------------------------------------------------------------------------------------------------
def GenkasyoukyakuUpdate(FolURL, TFolURL, CFolURL, ExRow, driver, PN, Fname):
    """
    概要: 減価償却更新処理
    @param FolURL : ミロク起動関数のフォルダ(str)
    @param TFolURL : このpyファイルのフォルダ(str)
    @param ExRow : Excel抽出行(obj)
    @param driver : 画面操作ドライバー(obj)
    @return : bool,ミロク入力関与先コード, ミロク入力処理年, ミロク入力処理月
    """
    try:
        ErrStr = ""  # Rpaエラー判別変数
        # 減価償却のアイコンを探す-------------------------------------------------
        ImgList = [r"\G_Syoukyaku.png", r"\G_Syoukyaku2.png"]
        ICFL = ImgCheckForList(TFolURL, ImgList, 0.9, 10)
        # -----------------------------------------------------------------------
        if ICFL[0] is True:  # 減価償却のアイコンがあれば
            ImgClick(TFolURL, ICFL[1], 0.9, 10)  # 減価償却のアイコンをクリック
            # 減価償却フラグが表示されるまで待機------------------------------------
            while (
                pg.locateOnScreen(TFolURL + r"\G_SyoukyakuFlag.png", confidence=0.9)
                is None
            ):
                time.sleep(1)
            # ------------------------------------------------------------------
            time.sleep(1)
            # 年度を最新に指定----------------------------------------------------
            IC = ImgCheck(TFolURL, r"\Nendo_Saisin.png", 0.9, 10)
            if IC[0] is False:
                IC2 = ImgCheck(TFolURL, r"\Nendo_All.png", 0.9, 10)
                if IC2[0] is False:
                    print("年度選択がない")
                else:
                    ImgClick(TFolURL, r"\Nendo_All.png", 0.9, 10)
                    pg.press("home")
                    time.sleep(1)
                    pg.press("down")
                    time.sleep(1)
                    pg.press("return")
                    time.sleep(1)
            # ------------------------------------------------------------------
            # 関与先コード入力ボックスをクリック------------------------------------
            ImgClick(TFolURL, r"\K_NoBox.png", 0.9, 10)
            while (
                pg.locateOnScreen(TFolURL + r"\K_AfterNoBox.png", confidence=0.9)
                is None
            ):
                time.sleep(1)
            pg.write(str(ExRow["関与先番号"]))
            pg.press(["return", "return", "return"])
            # 入力した関与先コードを取得------------
            pg.keyDown("shift")
            pg.press(["tab", "tab", "tab"])
            pg.keyUp("shift")
            if windll.user32.OpenClipboard(None):
                windll.user32.EmptyClipboard()
                windll.user32.CloseClipboard()
            pg.hotkey("ctrl", "c")
            ThisNo = pyperclip.paste()
            # -----------------------------------
            pg.press("return")
            # 表示された年度を取得-----------------
            if windll.user32.OpenClipboard(None):
                windll.user32.EmptyClipboard()
                windll.user32.CloseClipboard()
            pg.hotkey("ctrl", "c")
            ThisYear = pyperclip.paste()
            # -----------------------------------
            pg.press("return")
            # 表示された月を取得-------------------
            if windll.user32.OpenClipboard(None):
                windll.user32.EmptyClipboard()
                windll.user32.CloseClipboard()
            pg.hotkey("ctrl", "c")
            ThisMonth = pyperclip.paste()
            # -----------------------------------
            time.sleep(1)
            if str(ExRow["関与先番号"]) == ThisNo:
                print("関与先あり")
                pg.press(["return", "return", "return"])
                # 減価償却メニューが表示されるまで待機------------------------------------
                while (
                    pg.locateOnScreen(TFolURL + r"\G_SyoukyakuMenu.png", confidence=0.9)
                    is None
                ):
                    time.sleep(1)
                    # アップデート情報画面が出たら閉じる-------------------------------
                    GSUM = ImgCheck(TFolURL, r"\G_SyoukyakuUpMsg.png", 0.9, 10)
                    if GSUM[0] is True:
                        ImgClick(TFolURL, r"\G_SyoukyakuUpMsgCansel.png", 0.9, 10)
                # --------------------------------------------------------------------
                ImgClick(TFolURL, r"\G_SyoukyakuMenu.png", 0.9, 10)  # 一括更新のアイコンをクリック
                ImgClick(TFolURL, r"\M_G_Sonota.png", 0.9, 10)  # 5.その他処理アイコンをクリック
                # 一括更新メニューが表示されるまで待機------------------------------------
                while (
                    pg.locateOnScreen(
                        TFolURL + r"\IkkatsuGenkaKousin.png", confidence=0.9
                    )
                    is None
                ):
                    time.sleep(1)
                # --------------------------------------------------------------------
                ImgClick(
                    TFolURL, r"\IkkatsuGenkaKousin.png", 0.9, 10
                )  # 一括更新メニューのアイコンをクリック
                # 一括更新メニューが表示されるまで待機------------------------------------
                while (
                    pg.locateOnScreen(
                        TFolURL + r"\IkkatuOpenGenkaFlag.png", confidence=0.9
                    )
                    is None
                ):
                    time.sleep(1)
                # --------------------------------------------------------------------
                ImgClick(
                    TFolURL, r"\IkkatuOpenGenkaFlag.png", 0.9, 10
                )  # 一括更新メニューのアイコンをクリック
                time.sleep(1)
                ImgClick(TFolURL, r"\IkkatuGenakStart.png", 0.9, 10)  # 一括更新開始のアイコンをクリック
                # 確認ウィンドウが表示されるまで待機-------------------------------------
                while (
                    pg.locateOnScreen(TFolURL + r"\SakuseiGenkaQ.png", confidence=0.9)
                    is None
                ):
                    time.sleep(1)
                # --------------------------------------------------------------------
                pg.press("y")  # yで決定(nがキャンセル)
                # 処理終了ウィンドウが表示されるまで待機----------------------------------
                while (
                    pg.locateOnScreen(TFolURL + r"\SakuseiGenkaEnd.png", confidence=0.9)
                    is None
                ):
                    time.sleep(1)
                    Noren = ImgCheck(TFolURL, r"\No_Rendou.png", 0.9, 10)
                    if Noren[0] is True:
                        ErrStr = "Noren"
                        pg.press("y")  # yで決定(nがキャンセル)
                # --------------------------------------------------------------------
                pg.press("return")  # 決定
                # 一括更新のアイコンが表示されるまで待機----------------------------------
                while (
                    pg.locateOnScreen(TFolURL + r"\G_SyoukyakuMenu.png", confidence=0.9)
                    is None
                ):
                    time.sleep(1)
                # --------------------------------------------------------------------
                # 閉じる処理--------------------------
                pg.keyDown("alt")
                pg.press("f4")
                pg.keyUp("alt")
                # -----------------------------------
                # 減価償却フラグが表示されるまで待機-------------------------------------
                while (
                    pg.locateOnScreen(TFolURL + r"\G_SyoukyakuFlag.png", confidence=0.9)
                    is None
                ):
                    time.sleep(1)
                    al4c = ImgCheck(TFolURL, r"\altf4Q.png", 0.9, 10)  # 終了確認が表示されたら
                    if al4c[0] is True:
                        pg.press("y")  # yで決定(nがキャンセル)
                # --------------------------------------------------------------------
                print("更新完了")
                if ErrStr == "":
                    return True, ThisNo, ThisYear, ThisMonth
                elif ErrStr == "Noren":
                    return False, ErrStr, "", ""
            else:
                print("関与先なし")
                return False, "関与先なし", "", ""
        else:
            return False, "減価償却起動失敗", "", ""
    except:
        return False, "exceptエラー", "", ""


# ------------------------------------------------------------------------------------------------------------------
def KessanUpDate(FolURL, TFolURL, CFolURL, ExRow, driver):
    """
    概要: 決算内訳書更新処理
    @param FolURL : ミロク起動関数のフォルダ(str)
    @param TFolURL : このpyファイルのフォルダ(str)
    @param ExRow : Excel抽出行(obj)
    @param driver : 画面操作ドライバー(obj)
    @return : bool,ミロク入力関与先コード, ミロク入力処理年, ミロク入力処理月
    """
    try:
        ErrStr = ""  # Rpaエラー判別変数
        # 決算内訳書のアイコンを探す-------------------------------------------------
        ImgList = [r"\K_Uchiwake.png", r"\K_Uchiwake2.png"]
        ICFL = ImgCheckForList(TFolURL, ImgList, 0.9, 10)
        # -----------------------------------------------------------------------
        if ICFL[0] is True:  # 決算内訳書のアイコンがあれば
            ImgClick(TFolURL, ICFL[1], 0.9, 10)  # 決算内訳書のアイコンをクリック
            # 決算内訳書フラグが表示されるまで待機------------------------------------
            while (
                pg.locateOnScreen(TFolURL + r"\Kessan_CFlag.png", confidence=0.9)
                is None
            ):
                time.sleep(1)
            # ------------------------------------------------------------------
            time.sleep(1)
            # 年度を最新に指定----------------------------------------------------
            IC = ImgCheck(TFolURL, r"\Nendo_Saisin.png", 0.9, 10)
            if IC[0] is False:
                IC2 = ImgCheck(TFolURL, r"\Nendo_All.png", 0.9, 10)
                if IC2[0] is False:
                    print("年度選択がない")
                else:
                    ImgClick(TFolURL, r"\Nendo_All.png", 0.9, 10)
                    pg.press("home")
                    time.sleep(1)
                    pg.press("down")
                    time.sleep(1)
                    pg.press("return")
                    time.sleep(1)
            # ------------------------------------------------------------------
            # 関与先コード入力ボックスをクリック------------------------------------
            ImgClick(TFolURL, r"\K_NoBox.png", 0.9, 10)
            while (
                pg.locateOnScreen(TFolURL + r"\K_AfterNoBox.png", confidence=0.9)
                is None
            ):
                time.sleep(1)
            pg.write(str(ExRow["関与先番号"]))
            pg.press(["return", "return", "return"])
            # 入力した関与先コードを取得------------
            pg.keyDown("shift")
            pg.press(["tab", "tab", "tab"])
            pg.keyUp("shift")
            if windll.user32.OpenClipboard(None):
                windll.user32.EmptyClipboard()
                windll.user32.CloseClipboard()
            pg.hotkey("ctrl", "c")
            ThisNo = pyperclip.paste()
            # -----------------------------------
            pg.press("return")
            # 表示された年度を取得-----------------
            if windll.user32.OpenClipboard(None):
                windll.user32.EmptyClipboard()
                windll.user32.CloseClipboard()
            pg.hotkey("ctrl", "c")
            ThisYear = pyperclip.paste()
            # -----------------------------------
            pg.press("return")
            # 表示された月を取得-------------------
            if windll.user32.OpenClipboard(None):
                windll.user32.EmptyClipboard()
                windll.user32.CloseClipboard()
            pg.hotkey("ctrl", "c")
            ThisMonth = pyperclip.paste()
            # -----------------------------------
            time.sleep(1)
            if str(ExRow["関与先番号"]) == ThisNo:
                print("関与先あり")
                pg.press(["return", "return", "return"])
                # 決算内訳書メニューが表示されるまで待機------------------------------------
                while (
                    pg.locateOnScreen(TFolURL + r"\KessanMenu.png", confidence=0.9)
                    is None
                ):
                    time.sleep(1)
                # --------------------------------------------------------------------
                # 一括更新のアイコンが表示されるまで待機----------------------------------
                while (
                    pg.locateOnScreen(
                        TFolURL + r"\IkkatsuKessanKousin.png", confidence=0.9
                    )
                    is None
                ):
                    time.sleep(1)
                # --------------------------------------------------------------------
                ImgClick(
                    TFolURL, r"\IkkatsuKessanKousin.png", 0.9, 10
                )  # 一括更新のアイコンをクリック
                # 一括更新メニューが表示されるまで待機------------------------------------
                while (
                    pg.locateOnScreen(
                        TFolURL + r"\IkkatuKessanOpenFlag.png", confidence=0.9
                    )
                    is None
                ):
                    time.sleep(1)
                # --------------------------------------------------------------------
                ImgClick(
                    TFolURL, r"\IkkatuKessanOpenFlag.png", 0.9, 10
                )  # 一括更新メニューのアイコンをクリック
                time.sleep(1)
                ImgClick(
                    TFolURL, r"\IkkatuKessanStart.png", 0.9, 10
                )  # 一括更新開始のアイコンをクリック
                # 確認ウィンドウが表示されるまで待機-------------------------------------
                while (
                    pg.locateOnScreen(TFolURL + r"\SakuseiKessanQ.png", confidence=0.9)
                    is None
                ):
                    time.sleep(1)
                # --------------------------------------------------------------------
                pg.press("y")  # yで決定(nがキャンセル)
                # 処理終了ウィンドウが表示されるまで待機----------------------------------
                while (
                    pg.locateOnScreen(
                        TFolURL + r"\IkkatuKessanEndFlag.png", confidence=0.9
                    )
                    is None
                ):
                    time.sleep(1)
                    Noren = ImgCheck(TFolURL, r"\No_Rendou.png", 0.9, 10)
                    if Noren[0] is True:
                        ErrStr = "Noren"
                        ImgClick(TFolURL, r"\No_Rendou_Cansel.png", 0.9, 10)
                # --------------------------------------------------------------------
                pg.press("return")  # 決定
                # 一括更新のアイコンが表示されるまで待機----------------------------------
                while (
                    pg.locateOnScreen(
                        TFolURL + r"\IkkatsuKessanKousin.png", confidence=0.9
                    )
                    is None
                ):
                    time.sleep(1)
                    ME = ImgCheckForList(
                        TFolURL, [r"\MenuEnd.png", r"\MenuEnd2.png"], 0.9, 10
                    )
                    if ME[0] is True:
                        ImgClick(TFolURL, ME[1], 0.9, 10)  # 終了アイコンをクリック
                # --------------------------------------------------------------------
                # 閉じる処理--------------------------
                pg.keyDown("alt")
                pg.press("f4")
                pg.keyUp("alt")
                # -----------------------------------
                # 決算内訳書フラグが表示されるまで待機-------------------------------------
                while (
                    pg.locateOnScreen(TFolURL + r"\Kessan_CFlag.png", confidence=0.9)
                    is None
                ):
                    time.sleep(1)
                    al4c = ImgCheck(TFolURL, r"\altf4Q.png", 0.9, 10)  # 終了確認が表示されたら
                    if al4c[0] is True:
                        pg.press("y")  # yで決定(nがキャンセル)
                # --------------------------------------------------------------------
                print("更新完了")
                if ErrStr == "":
                    return True, ThisNo, ThisYear, ThisMonth
                elif ErrStr == "Noren":
                    return False, ErrStr, "", ""
            else:
                print("関与先なし")
                return False, "関与先なし", "", ""
        else:
            return False, "決算内訳書起動失敗", "", ""
    except:
        return False, "exceptエラー", "", ""


# ------------------------------------------------------------------------------------------------------------------
def KaikeiUpDate(FolURL, TFolURL, CFolURL, ExRow, driver, PN, Fname):
    """
    概要: 会計大将更新処理
    @param FolURL : ミロク起動関数のフォルダ(str)
    @param TFolURL : このpyファイルのフォルダ(str)
    @param ExRow : Excel抽出行(obj)
    @param driver : 画面操作ドライバー(obj)
    @return : bool,ミロク入力関与先コード, ミロク入力処理年, ミロク入力処理月
    """
    try:
        ErrStr = ""  # Rpaエラー判別変数
        # 会計大将のアイコンを探す-------------------------------------------------
        ImgList = [r"\K_TaisyouIcon.png", r"\K_TaisyouIcon2.png"]
        ICFL = ImgCheckForList(TFolURL, ImgList, 0.9, 10)
        # -----------------------------------------------------------------------
        if ICFL[0] is True:  # 会計大将のアイコンがあれば
            ImgClick(TFolURL, ICFL[1], 0.9, 10)  # 会計大将のアイコンをクリック
            # 会計大将フラグが表示されるまで待機------------------------------------
            while (
                pg.locateOnScreen(TFolURL + r"\Kaikei_CFlag.png", confidence=0.9)
                is None
            ):
                time.sleep(1)
            # ------------------------------------------------------------------
            time.sleep(1)
            # 年度を最新に指定----------------------------------------------------
            IC = ImgCheck(TFolURL, r"\Nendo_Saisin.png", 0.9, 10)
            if IC[0] is False:
                IC2 = ImgCheck(TFolURL, r"\Nendo_All.png", 0.9, 10)
                if IC2[0] is False:
                    print("年度選択がない")
                else:
                    ImgClick(TFolURL, r"\Nendo_All.png", 0.9, 10)
                    pg.press("home")
                    time.sleep(1)
                    pg.press("down")
                    time.sleep(1)
                    pg.press("return")
                    time.sleep(1)
            # ------------------------------------------------------------------
            # 関与先コード入力ボックスをクリック------------------------------------
            ImgClick(TFolURL, r"\K_NoBox.png", 0.9, 10)
            while (
                pg.locateOnScreen(TFolURL + r"\K_AfterNoBox.png", confidence=0.9)
                is None
            ):
                time.sleep(1)
            pg.write(str(ExRow["関与先番号"]))
            pg.press(["return", "return", "return"])
            # 入力した関与先コードを取得------------
            pg.keyDown("shift")
            pg.press(["tab", "tab", "tab"])
            pg.keyUp("shift")
            if windll.user32.OpenClipboard(None):
                windll.user32.EmptyClipboard()
                windll.user32.CloseClipboard()
            pg.hotkey("ctrl", "c")
            ThisNo = pyperclip.paste()
            # -----------------------------------
            pg.press("return")
            # 表示された年度を取得-----------------
            if windll.user32.OpenClipboard(None):
                windll.user32.EmptyClipboard()
                windll.user32.CloseClipboard()
            pg.hotkey("ctrl", "c")
            ThisYear = pyperclip.paste()
            # -----------------------------------
            pg.press("return")
            # 表示された月を取得-------------------
            if windll.user32.OpenClipboard(None):
                windll.user32.EmptyClipboard()
                windll.user32.CloseClipboard()
            pg.hotkey("ctrl", "c")
            ThisMonth = pyperclip.paste()
            # -----------------------------------
            time.sleep(1)
            if str(ExRow["関与先番号"]) == ThisNo:
                print("関与先あり")
                pg.press(["return", "return", "return"])
                # 会計大将メニューが表示されるまで待機------------------------------------
                while (
                    pg.locateOnScreen(TFolURL + r"\K_TaisyouMenu.png", confidence=0.9)
                    is None
                ):
                    time.sleep(1)
                # --------------------------------------------------------------------
                # 指示内容で処理分け----------------------------------------------------------
                if PN == "消費税確定申告書":
                    ImgClick(
                        CFolURL, r"\KTaisyou\KessanSinkoku.png", 0.9, 10
                    )  # 決算申告書アイコンをクリック
                    # 決算申告書が表示されるまで待機----------------------------------
                    while (
                        pg.locateOnScreen(
                            CFolURL + r"\KTaisyou\KessanFlag.png", confidence=0.9
                        )
                        is None
                    ):
                        time.sleep(1)
                    # サイドメニューより消費税申告書を確認------------------------------------------
                    SSM = ImgCheckForList(
                        CFolURL,
                        [r"\KTaisyou\Syouhizei.png", r"\KTaisyou\Syouhizei2.png"],
                        0.9,
                        10,
                    )
                    if SSM[0] is True:  # 消費税申告書があれば
                        ImgClick(CFolURL, SSM[1], 0.9, 10)  # 消費税申告書アイコンをクリック
                        time.sleep(2)
                    # 申告書・付表入力を確認------------------------------------------------
                    SFI = ImgCheckForList(
                        CFolURL,
                        [r"\KTaisyou\SFIcon.png", r"\KTaisyou\SFIcon2.png"],
                        0.9,
                        10,
                    )
                    if SFI[0] is True:  # 申告書・付表入力があれば
                        ImgClick(CFolURL, SFI[1], 0.9, 10)  # 申告書・付表入力アイコンをクリック
                    # 申告選択ウィンドウが表示されるまで待機-------------------------------------
                    while (
                        pg.locateOnScreen(
                            CFolURL + r"\KTaisyou\SinkokuSentaku.png", confidence=0.9
                        )
                        is None
                    ):
                        time.sleep(1)
                        # 申告回数設定ウィンドウがひょうじされたら
                        SCQ = ImgCheck(CFolURL, r"\KTaisyou\ScountQ.png", 0.9, 10)
                        if SCQ[0] is True:
                            pg.press("n")  # nでいいえ
                    # 申告種で処理分け----------------------------------------------------------------------------------
                    SL = ImgCheck(
                        CFolURL, r"\KTaisyou\SinkokuList.png", 0.9, 10
                    )  # 申告種類選択ボックスが開かれてるか確認
                    if SL[0] is True:
                        if ExRow["会計大将_消費税確定申告書"] == "1":  # Excel数値が確定申告なら
                            while (
                                pg.locateOnScreen(
                                    CFolURL + r"\KTaisyou\Kakutei.png", confidence=0.9
                                )
                                is None
                            ):
                                pg.press("down")
                            pg.press("return")
                        elif ExRow["会計大将_消費税確定申告書"] == "2":  # Excel数値が修正確定なら
                            while (
                                pg.locateOnScreen(
                                    CFolURL + r"\KTaisyou\Syuusei.png", confidence=0.9
                                )
                                is None
                            ):
                                pg.press("down")
                            pg.press("return")
                        elif ExRow["会計大将_消費税確定申告書"] == "3":  # Excel数値が中間申告なら
                            while (
                                pg.locateOnScreen(
                                    CFolURL + r"\KTaisyou\Cyuukan.png", confidence=0.9
                                )
                                is None
                            ):
                                pg.press("down")
                            pg.press("return")
                        elif ExRow["会計大将_消費税確定申告書"] == "4":  # Excel数値が修正中間なら
                            while (
                                pg.locateOnScreen(
                                    CFolURL + r"\KTaisyou\SCyuukan.png", confidence=0.9
                                )
                                is None
                            ):
                                pg.press("down")
                            pg.press("return")
                        elif ExRow["会計大将_消費税確定申告書"] == "5":  # Excel数値が予定申告なら
                            while (
                                pg.locateOnScreen(
                                    CFolURL + r"\KTaisyou\Yotei.png", confidence=0.9
                                )
                                is None
                            ):
                                pg.press("down")
                            pg.press("return")
                    else:
                        SA = ImgCheck(
                            CFolURL, r"\KTaisyou\SinkokuArrow.png", 0.9, 10
                        )  # 申告区分ドロップボックスが開けるか確認
                        if SA[0] is True:
                            ImgClick(
                                CFolURL, r"\KTaisyou\SinkokuArrow.png", 0.9, 10
                            )  # 一括更新開始のアイコンをクリック
                            if ExRow["会計大将_消費税確定申告書"] == "1":  # Excel数値が確定申告なら
                                while (
                                    pg.locateOnScreen(
                                        CFolURL + r"\KTaisyou\Kakutei.png",
                                        confidence=0.9,
                                    )
                                    is None
                                ):
                                    pg.press("down")
                                pg.press("return")
                            elif ExRow["会計大将_消費税確定申告書"] == "2":  # Excel数値が修正確定なら
                                while (
                                    pg.locateOnScreen(
                                        CFolURL + r"\KTaisyou\Syuusei.png",
                                        confidence=0.9,
                                    )
                                    is None
                                ):
                                    pg.press("down")
                                pg.press("return")
                            elif ExRow["会計大将_消費税確定申告書"] == "3":  # Excel数値が中間申告なら
                                while (
                                    pg.locateOnScreen(
                                        CFolURL + r"\KTaisyou\Cyuukan.png",
                                        confidence=0.9,
                                    )
                                    is None
                                ):
                                    pg.press("down")
                                pg.press("return")
                            elif ExRow["会計大将_消費税確定申告書"] == "4":  # Excel数値が修正中間なら
                                while (
                                    pg.locateOnScreen(
                                        CFolURL + r"\KTaisyou\SCyuukan.png",
                                        confidence=0.9,
                                    )
                                    is None
                                ):
                                    pg.press("down")
                                pg.press("return")
                            elif ExRow["会計大将_消費税確定申告書"] == "5":  # Excel数値が予定申告なら
                                while (
                                    pg.locateOnScreen(
                                        CFolURL + r"\KTaisyou\Yotei.png", confidence=0.9
                                    )
                                    is None
                                ):
                                    pg.press("down")
                                pg.press("return")
                        else:
                            # 現在の申告回数を取得
                            pg.hotkey("ctrl", "c")
                            SinNo = pyperclip.paste()
                            NextSinNo = int(SinNo) + 1
                            pg.write(str(NextSinNo))
                            pg.press("return")
                            if ExRow["会計大将_消費税確定申告書"] == "1":  # Excel数値が確定申告なら
                                while (
                                    pg.locateOnScreen(
                                        CFolURL + r"\KTaisyou\Kakutei.png",
                                        confidence=0.9,
                                    )
                                    is None
                                ):
                                    pg.press("down")
                                pg.press("return")
                            elif ExRow["会計大将_消費税確定申告書"] == "2":  # Excel数値が修正確定なら
                                while (
                                    pg.locateOnScreen(
                                        CFolURL + r"\KTaisyou\Syuusei.png",
                                        confidence=0.9,
                                    )
                                    is None
                                ):
                                    pg.press("down")
                                pg.press("return")
                            elif ExRow["会計大将_消費税確定申告書"] == "3":  # Excel数値が中間申告なら
                                while (
                                    pg.locateOnScreen(
                                        CFolURL + r"\KTaisyou\Cyuukan.png",
                                        confidence=0.9,
                                    )
                                    is None
                                ):
                                    pg.press("down")
                                pg.press("return")
                            elif ExRow["会計大将_消費税確定申告書"] == "4":  # Excel数値が修正中間なら
                                while (
                                    pg.locateOnScreen(
                                        CFolURL + r"\KTaisyou\SCyuukan.png",
                                        confidence=0.9,
                                    )
                                    is None
                                ):
                                    pg.press("down")
                                pg.press("return")
                            elif ExRow["会計大将_消費税確定申告書"] == "5":  # Excel数値が予定申告なら
                                while (
                                    pg.locateOnScreen(
                                        CFolURL + r"\KTaisyou\Yotei.png", confidence=0.9
                                    )
                                    is None
                                ):
                                    pg.press("down")
                                pg.press("return")
                            time.sleep(1)
                            pg.press("return")
                            time.sleep(1)
                            pg.press("return")
                            time.sleep(1)
                            # 申告回数変更を求められた場合--------------------------------------------
                            SCQ = ImgCheck(CFolURL, r"\KTaisyou\S_CountQ.png", 0.9, 10)
                            if SCQ[0] is True:
                                pg.press("N")  # 申告回数変更しない
                                time.sleep(1)
                                pg.write(str(SinNo))  # 取得していた現在申告区分Noを入力
                                pg.press("return")
                                ImgClick(CFolURL, r"\KTaisyou\S_Delete.png", 0.9, 10)
                                # 申告データ削除ダイアログ表示まで待機----------------------------------
                                while (
                                    pg.locateOnScreen(
                                        CFolURL + r"\KTaisyou\S_DeleteQ.png",
                                        confidence=0.9,
                                    )
                                    is None
                                ):
                                    time.sleep(1)
                                pg.press("y")
                                # ---------------------------------------------------------------------
                                # 申告データ削除完了まで待機----------------------------------
                                while (
                                    pg.locateOnScreen(
                                        CFolURL + r"\KTaisyou\S_DeleteQ2.png",
                                        confidence=0.9,
                                    )
                                    is None
                                ):
                                    time.sleep(1)
                                pg.press("return")
                                # ---------------------------------------------------------------------
                                time.sleep(1)
                                pg.press("return")
                                time.sleep(1)
                                pg.press("home")
                                time.sleep(1)
                                SL = ImgCheck(
                                    CFolURL, r"\KTaisyou\SinkokuList.png", 0.9, 10
                                )  # 申告種類選択ボックスが開かれてるか確認
                                if SL[0] is True:
                                    if ExRow["会計大将_消費税確定申告書"] == "1":  # Excel数値が確定申告なら
                                        while (
                                            pg.locateOnScreen(
                                                CFolURL + r"\KTaisyou\Kakutei.png",
                                                confidence=0.9,
                                            )
                                            is None
                                        ):
                                            pg.press("down")
                                        pg.press("return")
                                    elif (
                                        ExRow["会計大将_消費税確定申告書"] == "2"
                                    ):  # Excel数値が修正確定なら
                                        while (
                                            pg.locateOnScreen(
                                                CFolURL + r"\KTaisyou\Syuusei.png",
                                                confidence=0.9,
                                            )
                                            is None
                                        ):
                                            pg.press("down")
                                        pg.press("return")
                                    elif (
                                        ExRow["会計大将_消費税確定申告書"] == "3"
                                    ):  # Excel数値が中間申告なら
                                        while (
                                            pg.locateOnScreen(
                                                CFolURL + r"\KTaisyou\Cyuukan.png",
                                                confidence=0.9,
                                            )
                                            is None
                                        ):
                                            pg.press("down")
                                        pg.press("return")
                                    elif (
                                        ExRow["会計大将_消費税確定申告書"] == "4"
                                    ):  # Excel数値が修正中間なら
                                        while (
                                            pg.locateOnScreen(
                                                CFolURL + r"\KTaisyou\SCyuukan.png",
                                                confidence=0.9,
                                            )
                                            is None
                                        ):
                                            pg.press("down")
                                        pg.press("return")
                                    elif (
                                        ExRow["会計大将_消費税確定申告書"] == "5"
                                    ):  # Excel数値が予定申告なら
                                        while (
                                            pg.locateOnScreen(
                                                CFolURL + r"\KTaisyou\Yotei.png",
                                                confidence=0.9,
                                            )
                                            is None
                                        ):
                                            pg.press("down")
                                        pg.press("return")
                    # ----------------------------------------------------------------------------------------------------
                    time.sleep(1)
                    # OKボタンにフォーカスするまでエンター押下-------------------------------
                    while (
                        pg.locateOnScreen(
                            CFolURL + r"\KTaisyou\SinkokuAllOK.png", confidence=0.9
                        )
                        is None
                    ):
                        pg.press("return")
                    # ---------------------------------------------------------------------
                    pg.press("return")  # 確定
                    # 確認ウィンドウが表示されるまで待機-------------------------------------
                    while (
                        pg.locateOnScreen(
                            CFolURL + r"\KTaisyou\SinkokuWin.png", confidence=0.9
                        )
                        is None
                    ):
                        time.sleep(1)
                    # --------------------------------------------------------------------
                    time.sleep(1)
                    SKQ = ImgCheck(CFolURL, r"\KTaisyou\KakuninQ.png", 0.9, 10)
                    if SKQ[0] is True:
                        pg.press("return")
                    time.sleep(1)
                    ImgClick(CFolURL, r"\KTaisyou\SyouhiPrint.png", 0.9, 10)
                    # 確認ウィンドウが表示されるまで待機-------------------------------------
                    while (
                        pg.locateOnScreen(
                            CFolURL + r"\KTaisyou\S_Huhyou.png", confidence=0.9
                        )
                        is None
                    ):
                        time.sleep(1)
                    # --------------------------------------------------------------------
                    pg.press("p")  # 決定
                    time.sleep(1)
                    # 法人番号未登録確認が表示されているか確認
                    SAL = ImgCheck(CFolURL, r"\KTaisyou\S_Alert.png", 0.9, 10)
                    if SAL[0] is True:  # 法人番号未登録確認が表示された場合
                        pg.press("y")  # yで確定
                    # 一覧表出力項目指定が表示されるまで待機---------------------------------
                    while (
                        pg.locateOnScreen(
                            CFolURL + r"\Houjinzei\PrintBar.png", confidence=0.9
                        )
                        is None
                    ):
                        time.sleep(1)
                    # --------------------------------------------------------------------
                    # 申告税一覧表印刷処理----------------------------------------------------
                    FO = ImgCheckForList(
                        CFolURL,
                        [
                            r"\Houjinzei\FileOut.png",
                            r"\Houjinzei\FileOut2.png",
                        ],
                        0.9,
                        10,
                    )
                    if FO[0] is True:
                        ImgClick(CFolURL, FO[1], 0.9, 10)
                    ImgClick(CFolURL, r"\Houjinzei\PDFBar.png", 0.9, 10)
                    pg.press("return")
                    pg.press("delete")
                    pyperclip.copy(Fname)
                    pg.hotkey("ctrl", "v")
                    pg.press("return")
                    time.sleep(1)
                    ImgClick(CFolURL, r"\Houjinzei\PrintOut.png", 0.9, 10)
                    # 印刷中が表示されるまで待機---------------------------------
                    while (
                        pg.locateOnScreen(
                            CFolURL + r"\KTaisyou\NowSyouhiPrint.png", confidence=0.9
                        )
                        is None
                    ):
                        time.sleep(1)
                        FO = ImgCheck(CFolURL, r"\Houjinzei\FileOver.png", 0.9, 10)
                        if FO[0] is True:
                            pg.press("y")
                            while (
                                pg.locateOnScreen(
                                    CFolURL + r"\KTaisyou\NowSyouhiPrint.png",
                                    confidence=0.9,
                                )
                                is None
                            ):
                                time.sleep(1)
                    # --------------------------------------------------------------------
                    # 印刷中が表示されなくなるまで待機---------------------------------
                    while (
                        pg.locateOnScreen(
                            CFolURL + r"\KTaisyou\NowSyouhiPrint.png", confidence=0.9
                        )
                        is not None
                    ):
                        time.sleep(1)
                    # --------------------------------------------------------------------
                    time.sleep(1)
                    pg.keyDown("alt")
                    pg.press("x")
                    pg.keyUp("alt")
                    time.sleep(3)
                    ImgClick(CFolURL, r"\KTaisyou\MenuEnd.png", 0.9, 10)
                    # 終了確認が表示されるまで待機---------------------------------
                    while (
                        pg.locateOnScreen(
                            CFolURL + r"\KTaisyou\KTaisyouEndQ.png", confidence=0.9
                        )
                        is None
                    ):
                        time.sleep(1)
                    # --------------------------------------------------------------------
                    pg.press("y")
                    while (
                        ImgCheckForList(
                            CFolURL,
                            [r"\KTaisyou\Syouhizei.png", r"\KTaisyou\Syouhizei2.png"],
                            0.9,
                            10,
                        )[0]
                        is False
                    ):
                        time.sleep(1)
                    # 閉じる処理--------------------------
                    pg.keyDown("alt")
                    pg.press("f4")
                    pg.keyUp("alt")
                    # -----------------------------------
                    # 会計大将フラグが表示されるまで待機------------------------------------
                    while (
                        pg.locateOnScreen(
                            TFolURL + r"\Kaikei_CFlag.png", confidence=0.9
                        )
                        is None
                    ):
                        time.sleep(1)
                    # ------------------------------------------------------------------
                    return True, ThisNo, ThisYear, ThisMonth
                elif PN == "書面添付　消費税":
                    ImgClick(
                        CFolURL, r"\KTaisyou\KessanSinkoku.png", 0.9, 10
                    )  # 決算申告書アイコンをクリック
                    # 決算申告書が表示されるまで待機----------------------------------
                    while (
                        pg.locateOnScreen(
                            CFolURL + r"\KTaisyou\KessanFlag.png", confidence=0.9
                        )
                        is None
                    ):
                        time.sleep(1)
                    # サイドメニューより消費税申告書を確認------------------------------------------
                    SSM = ImgCheckForList(
                        CFolURL,
                        [r"\KTaisyou\Syouhizei.png", r"\KTaisyou\Syouhizei2.png"],
                        0.9,
                        10,
                    )
                    if SSM[0] is True:  # 消費税申告書があれば
                        ImgClick(CFolURL, SSM[1], 0.9, 10)  # 消費税申告書アイコンをクリック
                        time.sleep(2)
                    # 添付書面を確認------------------------------------------------
                    SFI = ImgCheckForList(
                        CFolURL,
                        [r"\KTaisyou\14Tenpu.png", r"\KTaisyou\14Tenpu2.png"],
                        0.9,
                        10,
                    )
                    if SFI[0] is True:  # 添付書面があれば
                        ImgClick(CFolURL, SFI[1], 0.9, 10)  # 添付書面アイコンをクリック
                    # 添付書面申告種類選択ウィンドウが表示されるまで待機--------------------------
                    while (
                        pg.locateOnScreen(
                            CFolURL + r"\KTaisyou\TenpuBar.png", confidence=0.9
                        )
                        is None
                    ):
                        time.sleep(1)
                    pg.press(["return", "return"])
                    # 添付書面印刷ウィンドウが表示されるまで待機---------------------------------
                    while (
                        pg.locateOnScreen(
                            CFolURL + r"\KTaisyou\TenpuFlag.png", confidence=0.9
                        )
                        is None
                    ):
                        time.sleep(1)
                    ImgClick(CFolURL, r"\KTaisyou\TenpuFlagPrint.png", 0.9, 10)
                    # 添付書面印刷サイズ選択が表示されるまで待機---------------------------------
                    while (
                        pg.locateOnScreen(
                            CFolURL + r"\KTaisyou\TenpuPrintType.png", confidence=0.9
                        )
                        is None
                    ):
                        time.sleep(1)
                    A4T = ImgCheck(CFolURL, r"\KTaisyou\A4Box.png", 0.99999, 10)
                    if A4T[0] is True:
                        ImgClick(CFolURL, r"\KTaisyou\A4Box.png", 0.99999, 10)
                    ImgClick(CFolURL, r"\KTaisyou\A4BoxOK.png", 0.9, 10)
                    # 一覧表出力項目指定が表示されるまで待機---------------------------------
                    while (
                        pg.locateOnScreen(
                            CFolURL + r"\Houjinzei\PrintBar.png", confidence=0.9
                        )
                        is None
                    ):
                        time.sleep(1)
                    # --------------------------------------------------------------------
                    # 申告税一覧表印刷処理----------------------------------------------------
                    FO = ImgCheckForList(
                        CFolURL,
                        [
                            r"\Houjinzei\FileOut.png",
                            r"\Houjinzei\FileOut2.png",
                        ],
                        0.9,
                        10,
                    )
                    if FO[0] is True:
                        ImgClick(CFolURL, FO[1], 0.9, 10)
                    ImgClick(CFolURL, r"\Houjinzei\PDFBar.png", 0.9, 10)
                    pg.press("return")
                    pg.press("delete")
                    pyperclip.copy(Fname)
                    pg.hotkey("ctrl", "v")
                    pg.press("return")
                    time.sleep(1)
                    ImgClick(CFolURL, r"\Houjinzei\PrintOut.png", 0.9, 10)
                    # 印刷中が表示されるまで待機---------------------------------
                    while (
                        pg.locateOnScreen(
                            CFolURL + r"\KTaisyou\TenpuPBar.png", confidence=0.9
                        )
                        is not None
                    ):
                        time.sleep(1)
                        FO = ImgCheck(CFolURL, r"\Houjinzei\FileOver.png", 0.9, 10)
                        if FO[0] is True:
                            pg.press("y")
                    # --------------------------------------------------------------------
                    time.sleep(2)
                    ImgClick(CFolURL, r"\KTaisyou\MenuEnd.png", 0.9, 10)
                    # 終了確認が表示されるまで待機---------------------------------
                    while (
                        ImgCheckForList(
                            CFolURL,
                            [r"\KTaisyou\14Tenpu.png", r"\KTaisyou\14Tenpu2.png"],
                            0.9,
                            10,
                        )[0]
                        is False
                    ):
                        time.sleep(1)
                    # 閉じる処理--------------------------
                    pg.keyDown("alt")
                    pg.press("f4")
                    pg.keyUp("alt")
                    # -----------------------------------
                    # 会計大将フラグが表示されるまで待機------------------------------------
                    while (
                        pg.locateOnScreen(
                            TFolURL + r"\Kaikei_CFlag.png", confidence=0.9
                        )
                        is None
                    ):
                        time.sleep(1)
                    # ------------------------------------------------------------------
                    return True, ThisNo, ThisYear, ThisMonth
            else:
                print("関与先なし")
                return False, "関与先なし", "", ""
        else:
            return False, "会計大将起動失敗", "", ""
    except:
        return False, "exceptエラー", "", ""


# ------------------------------------------------------------------------------------------------------------------
def MainStarter(FolURL, TFolURL, CFolURL, NameDF, ExSheet, ExrcHeader, isnItem, driver):
    try:
        print(ExSheet[3 : len(ExSheet)])
        li = np.array(ExSheet[3 : len(ExSheet)])
        ExDf = pd.DataFrame(li, columns=ExrcHeader)
        print(ExDf)
        Exrc = np.array(ExDf).shape[1]  # 行数
        for Ex in range(Exrc):
            ExRow = ExDf.iloc[Ex]
            if ExRow["関与先番号"] == ExRow["関与先番号"]:  # nan判定
                # nanでない場合
                OpenSystem(
                    FolURL,
                    TFolURL,
                    CFolURL,
                    NameDF,
                    ExRow,
                    Ex,
                    ExrcHeader,
                    isnItem,
                    driver,
                )
            else:
                # nanの場合
                print("nan")
    except:
        return False, ""


# ------------------------------------------------------------------------------------------------------------------
def NameSearch(NameDF, Rno):
    try:
        Nr = len(NameDF)
        for Nrx in range(Nr):
            NameDFRow = NameDF.iloc[Nrx]
            print(NameDFRow["コード"])
            if Rno == NameDFRow["コード"]:
                return NameDFRow["顧問先名称"]
    except:
        return "NameErr"


# ------------------------------------------------------------------------------------------------------------------
def OpenSystem(
    FolURL, TFolURL, CFolURL, NameDF, ExRow, Ex, ExrcHeader, isnItem, driver
):
    try:
        Eh = 0
        # 列名からMJSシステムリストを作成------------------------------------------------
        SystemList = []
        CountList = []
        for ExrcHeaderItem in ExrcHeader:
            if "_" in ExrcHeaderItem:
                SP = ExrcHeaderItem.split("_")
                SystemList.append(SP[0])
        for SystemListItem in SystemList:
            CountList.append(int(SystemList.count(SystemListItem)))
        SL = np.array(SystemList)
        CL = np.array(CountList)
        FMaxSystemList = SL[CL.argsort(axis=0)[::-1]]
        FMaxSystemList = list(dict.fromkeys(FMaxSystemList))
        print(FMaxSystemList)
        # ----------------------------------------------------------------------------
        for ExrcHeaderItem in ExrcHeader:
            for FMaxSystemListItem in FMaxSystemList:
                if FMaxSystemListItem in ExrcHeaderItem:
                    Title = FMaxSystemListItem  # MJSSytem名
                    PN = ExrcHeaderItem.split("_")[1]  # MJS出力帳表名
                    # nanの場合
                    # Log--------------------------------------------
                    dt_s = datetime.datetime.now()
                    dt_s = dt_s.strftime("%Y-%m-%d %H:%M:%S")
                    Rno = ExRow["関与先番号"]
                    Rn = NameSearch(NameDF, Rno)
                    Rn = Rn.replace("\u3000", " ")
                    NumList = [1, 2, 3, 4, 5]
                    strNumList = ["1", "2", "3", "4", "5"]
                    if (
                        ExRow[ExrcHeaderItem] in NumList
                        or ExRow[ExrcHeaderItem] in strNumList
                    ):
                        logger.debug(
                            dt_s + "_関与先番号:" + str(Rno) + ":" + str(Rn) + "_プリントメイン処理開始"
                        )
                        with open(LURL, "a") as f:
                            print(
                                [dt_s, "関与先番号:" + str(Rno), str(Rn), "プリントメイン処理開始"],
                                file=f,
                            )
                        # -----------------------------------------------
                        if not Title == "なし" or not Title == "決算フォルダ":
                            ChildFlow(
                                FolURL,
                                TFolURL,
                                CFolURL,
                                ExRow,
                                Ex,
                                Eh,
                                ExrcHeader,
                                isnItem,
                                Title,
                                PN,
                                driver,
                                Rno,
                                Rn,
                            )
            Eh += 1
    except:
        print("TEST")


# ------------------------------------------------------------------------------------------------------------------
def MainFlow(FolURL, TFolURL, CFolURL, Exlsx):
    """
    概要: プリントメイン処理
    @param FolURL : ミロク起動関数のフォルダ(str)
    @param TFolURL : このpyファイルのフォルダ(str)
    @param Exlsx : Excel指示シート(obj)
    @return : bool
    """
    try:
        # Log--------------------------------------------
        dt_s = datetime.datetime.now()
        dt_s = dt_s.strftime("%Y-%m-%d %H:%M:%S")
        logger.debug(dt_s + "_MJSシステム更新開始")
        # -----------------------------------------------
        BatUrl = FolURL + "/bat/AWADriverOpen.bat"  # 4724ポート指定でappiumサーバー起動バッチを開く
        driver = MJSOpen.MainFlow(
            BatUrl, FolURL, "RPAPhoto/MJS_DensiSinkoku"
        )  # MJSを起動しログイン後インスタンス化
        # driver = []
        FolURL = FolURL + "/RPAPhoto/MJS_DensiSinkoku"
        # ----------------------------------------------------------------------------------------------------------------------
        logger.debug("xlsxをDataFrameに")
        # sheet_namesメソッドでExcelブック内の各シートの名前をリストで取得できる
        input_sheet_name = Exlsx.sheet_names
        # lenでシートの総数を確認
        num_sheet = len(input_sheet_name)
        # シートの数とシートの名前のリストの表示
        print("Sheet の数:", num_sheet)
        print(input_sheet_name)
        for isnItem in input_sheet_name:
            # DataFrameとしてsheetのデータ読込み
            if isnItem == "印刷申請":
                ExSheet = Exlsx.parse(isnItem, skiprows=0)
                NameSheet = Exlsx.parse("顧問先別システム採用一覧表")
                print(ExSheet)
                # 初回読込時の保存--------------------------
                dt_s = datetime.datetime.now()
                dt_s = dt_s.strftime("%Y-%m-%d %H-%M-%S")
                DF = pd.DataFrame(ExSheet)
                NameDF = pd.DataFrame(NameSheet)
                DF.to_csv(
                    r"\\Sv05121a\e\C 作業台\RPA\RPA_ミロクシステム次年更新\MJSLog\初回起動_プリント"
                    + dt_s
                    + ".csv",
                    encoding="cp932",
                    index=False,
                )
                # ----------------------------------------
                Exrc = np.array(ExSheet).shape[1]  # 列数
                ExrcHeader = []
                for Ex in range(Exrc):
                    ExRow = ExSheet.iloc[1]
                    print(ExRow)
                    ExSecondRow = ExSheet.iloc[2]
                    print(ExSecondRow)
                    if ExRow[Ex] == ExRow[Ex]:  # nan判定
                        # nanでない場合
                        if ExSecondRow[Ex] == ExSecondRow[Ex]:  # nan判定
                            # nanでない場合
                            ExrcHeader.append(ExRow[Ex] + "_" + ExSecondRow[Ex])
                        else:
                            # nanの場合
                            ExrcHeader.append(ExRow[Ex])
                    else:
                        # nanの場合
                        ExrcHeader.append(ExSecondRow[Ex])
                # Log--------------------------------------------
                dt_s = datetime.datetime.now()
                dt_s = dt_s.strftime("%Y-%m-%d %H:%M:%S")
                logger.debug(dt_s + "_Excelシート読込完了")
                with open(LURL, "a") as f:
                    print([dt_s, "Excelシート読込完了"], file=f)
                # -----------------------------------------------
                MainStarter(
                    FolURL,
                    TFolURL,
                    CFolURL,
                    NameDF,
                    ExSheet,
                    ExrcHeader,
                    isnItem,
                    driver,
                )  # データ送信画面までの関数
    except Exception as e:
        logger.debug(e)


# RPA用画像フォルダの作成---------------------------------------------------------
FolURL = os.getcwd().replace("\\", "/")  # 先
TFolURL = FolURL + r"\RPAPhoto\MJS_SystemNextCreate"  # 先
CFolURL = FolURL + r"\RPAPhoto\MJS_SystemPrintOut"  # 先
XLSURL = r"\\Sv05121a\e\C 作業台\RPA\RPA_ミロクシステム次年更新\ミロク更新項目.xlsx"
LURL = r"\\Sv05121a\e\C 作業台\RPA\RPA_ミロクシステム次年更新\MJSLog\MJSSysUpLog.txt"  # 処理状況CSVのURL
# --------------------------------------------------------------------------------
open(LURL, "w").close()
Exlsx = EFA.XlsmRead(XLSURL)
if Exlsx[0] is True:
    try:
        MainFlow(FolURL, TFolURL, CFolURL, Exlsx[1])
    except:
        traceback.print_exc()
else:
    print("Excel読み込みエラー")
    logger.debug("Excel読み込みエラー")
