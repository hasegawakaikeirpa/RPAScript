# モジュールインポート
from matplotlib.colors import cnames
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
from datetime import datetime as dt

# 例外処理判定の為のtracebackインポート
import traceback

# pandas(pd)で関与先データCSVを取得
import pyautogui
import codecs
import pyperclip  # クリップボードへのコピーで使用
import Function.ExcelFileAction as EFA
import Function.CSVOut as FCO
import datetime
import openpyxl

# logger設定------------------------------------------------------------------------------------------------------------
import logging.config

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
def FolCre(C_SCode, C_Name, C_Nendo, C_Zeimoku, C_Syurui):
    Fol = str(dt.today().year) + "-" + str(dt.today().month)
    pt = "\\\\Sv05121a\\e\\電子ファイル\\メッセージボックス\\" + Fol + "\\送信分受信通知"
    try:
        if os.path.exists(pt) is False:
            os.mkdir(pt)
        C_Fol = pt + "\\" + str(C_SCode)
        if os.path.exists(C_Fol) is False:
            os.mkdir(C_Fol)
        C_F = C_Fol + "\\" + "ミロク送信分"
        if os.path.exists(C_F) is False:
            os.mkdir(C_F)
        return True, C_F
    except:
        return False, ""


def MainStarter(FolURL, TFolURL, ExSheet, ExrcHeader, isnItem, driver):
    try:
        print(ExSheet[3 : len(ExSheet)])
        li = np.array(ExSheet[3 : len(ExSheet)])
        ExDf = pd.DataFrame(li, columns=ExrcHeader)
        print(ExDf)
        # FCO.CsvSave(
        #     r"D:\PythonScript\RPAScript\RPAPhoto\MJS_SystemNextCreate\TEST.csv", ExDf
        # )
        Exrc = np.array(ExDf).shape[1]  # 行数
        for Ex in range(Exrc):
            ExRow = ExDf.iloc[Ex]
            if ExRow["関与先番号"] == ExRow["関与先番号"]:  # nan判定
                # nanでない場合
                OpenSystem(FolURL, TFolURL, ExRow, Ex, ExrcHeader, isnItem, driver)
            else:
                # nanの場合
                print("nan")
    except:
        return False, ""


# ------------------------------------------------------------------------------------------------------------------
def OpenSystem(FolURL, TFolURL, ExRow, Ex, ExrcHeader, isnItem, driver):
    try:
        Eh = 0
        for ExrcHeaderItem in ExrcHeader:
            if "_繰越対象" in ExrcHeaderItem:
                SysN = ExrcHeaderItem.split("_")
                Title = str(SysN[0])
                if ExRow[Title + "_繰越対象"] == ExRow[Title + "_繰越対象"]:
                    # nanでない場合
                    if ExRow[Title + "_繰越処理日"] == ExRow[Title + "_繰越処理日"]:
                        # nanでない場合
                        print(ExRow[Title + "_繰越処理日"])
                    else:
                        # nanの場合
                        ChildFlow(
                            FolURL,
                            TFolURL,
                            ExRow,
                            Ex,
                            Eh,
                            ExrcHeader,
                            isnItem,
                            Title,
                            driver,
                        )
                else:
                    # nanでない場合
                    if ExRow[Title + "_繰越処理日"] == ExRow[Title + "_繰越処理日"]:
                        # nanでない場合
                        print("スタート")
                    else:
                        # nanの場合
                        ChildFlow(
                            FolURL,
                            TFolURL,
                            ExRow,
                            Ex,
                            Eh,
                            ExrcHeader,
                            isnItem,
                            Title,
                            driver,
                        )
            Eh += 1
    except:
        print("TEST")


# ------------------------------------------------------------------------------------------------------------------
def ChildFlow(FolURL, TFolURL, ExRow, Ex, Eh, ExrcHeader, isnItem, Title, driver):
    if "会計大将" == Title:
        SystemUp = KaikeiUpDate(FolURL, TFolURL, ExRow, driver)
        # Excel書き込み--------------------------------------------------
        if SystemUp[0] is True:
            dt_now = datetime.datetime.now()
            WriteEx = openpyxl.load_workbook(XLSURL)
            WriteExSheet = WriteEx[isnItem]
            WriteExSheet.cell(row=Ex + 5, column=Eh + 2).value = dt_now
            WriteExSheet.cell(row=Ex + 5, column=Eh + 1).value = "○"
            print("シート書き込み完了")
            WriteEx.save(XLSURL)
            WriteEx.close
        # ---------------------------------------------------------------
    elif "決算内訳書" == Title:
        SystemUp = KessanUpDate(FolURL, TFolURL, ExRow, driver)
        # Excel書き込み--------------------------------------------------
        if SystemUp[0] is True:
            dt_now = datetime.datetime.now()
            WriteEx = openpyxl.load_workbook(XLSURL)
            WriteExSheet = WriteEx[isnItem]
            WriteExSheet.cell(row=Ex + 5, column=Eh + 2).value = dt_now
            WriteExSheet.cell(row=Ex + 5, column=Eh + 1).value = "○"
            print("シート書き込み完了")
            WriteEx.save(XLSURL)
            WriteEx.close
        elif SystemUp[1] == "Noren":
            dt_now = datetime.datetime.now()
            WriteEx = openpyxl.load_workbook(XLSURL)
            WriteExSheet = WriteEx[isnItem]
            WriteExSheet.cell(row=Ex + 5, column=Eh + 2).value = dt_now
            WriteExSheet.cell(row=Ex + 5, column=Eh + 1).value = "連動対象無エラー"
            print("シート書き込み完了")
            WriteEx.save(XLSURL)
            WriteEx.close
        # ---------------------------------------------------------------
    elif "減価償却" == Title:
        SystemUp = GenkasyoukyakuUpdate(FolURL, TFolURL, ExRow, driver)
        # Excel書き込み---------------------------------------------------
        if SystemUp[0] is True:
            dt_now = datetime.datetime.now()
            WriteEx = openpyxl.load_workbook(XLSURL)
            WriteExSheet = WriteEx[isnItem]
            WriteExSheet.cell(row=Ex + 5, column=Eh + 2).value = dt_now
            WriteExSheet.cell(row=Ex + 5, column=Eh + 1).value = "○"
            print("シート書き込み完了")
            WriteEx.save(XLSURL)
            WriteEx.close
        # ---------------------------------------------------------------
    elif "法人税申告書" == Title:
        SystemUp = HoujinzeiUpdate(FolURL, TFolURL, ExRow, driver)
        # Excel書き込み---------------------------------------------------
        if SystemUp[0] is True:
            dt_now = datetime.datetime.now()
            WriteEx = openpyxl.load_workbook(XLSURL)
            WriteExSheet = WriteEx[isnItem]
            WriteExSheet.cell(row=Ex + 5, column=Eh + 2).value = dt_now
            WriteExSheet.cell(row=Ex + 5, column=Eh + 1).value = "○"
            print("シート書き込み完了")
            WriteEx.save(XLSURL)
            WriteEx.close
        elif SystemUp[1] == "要データ再計算":
            dt_now = datetime.datetime.now()
            WriteEx = openpyxl.load_workbook(XLSURL)
            WriteExSheet = WriteEx[isnItem]
            WriteExSheet.cell(row=Ex + 5, column=Eh + 2).value = dt_now
            WriteExSheet.cell(row=Ex + 5, column=Eh + 1).value = "要データ再計算"
            print("シート書き込み完了")
            WriteEx.save(XLSURL)
            WriteEx.close
        # ---------------------------------------------------------------
    elif "財産評価明細書" == Title:
        SystemUp = ZaisanUpdate(FolURL, TFolURL, ExRow, driver)
        # Excel書き込み---------------------------------------------------
        if SystemUp[0] is True:
            dt_now = datetime.datetime.now()
            WriteEx = openpyxl.load_workbook(XLSURL)
            WriteExSheet = WriteEx[isnItem]
            WriteExSheet.cell(row=Ex + 5, column=Eh + 2).value = dt_now
            WriteExSheet.cell(row=Ex + 5, column=Eh + 1).value = "○"
            print("シート書き込み完了")
            WriteEx.save(XLSURL)
            WriteEx.close
        # ---------------------------------------------------------------
    elif "年末調整" == Title:
        print("年末調整")
    elif "法定調書" == Title:
        print("法定調書")
    elif "所得税確定申告" == Title:
        print("所得税確定申告")
    else:
        print("NoSystem")


# ------------------------------------------------------------------------------------------------------------------
def ZaisanUpdate(FolURL, TFolURL, ExRow, driver):
    """
    00:"関与先番号"
    01:"関与先名"
    02:"担当者_ｺｰﾄﾞ"
    03:"担当者_担当者名"
    04:"会計大将_繰越対象"
    07:"会計大将_繰越処理日"
    08:"決算内訳書_繰越対象"
    11:"決算内訳書_繰越処理日"
    12:"減価償却_繰越対象"
    15:"減価償却_繰越処理日"
    16:"法人税申告書_繰越対象"
    19:"法人税申告書_繰越処理日"
    20:"財産評価明細書_繰越対象"
    23:"財産評価明細書_繰越処理日"
    24:"財産評価明細書"
    25:"年末調整"
    26:"法定調書"
    27:"所得税確定申告"
    """
    """
    概要: 財産評価更新処理
    @param FolURL : ミロク起動関数のフォルダ(str)
    @param TFolURL : このpyファイルのフォルダ(str)
    @param ExRow : Excel抽出行(obj)
    @param driver : 画面操作ドライバー(obj)
    @return : bool,ミロク入力関与先コード, ミロク入力処理年, ミロク入力処理月
    """
    try:
        ErrStr = ""  # Rpaエラー判別変数
        # 財産評価のアイコンを探す-------------------------------------------------
        ImgList = [r"\Zaisanhyouka.png", r"\Zaisanhyouka2.png"]
        ICFL = ImgCheckForList(TFolURL, ImgList, 0.9, 10)
        # -----------------------------------------------------------------------
        if ICFL[0] is True:  # 財産評価のアイコンがあれば
            ImgClick(TFolURL, ICFL[1], 0.9, 10)  # 財産評価のアイコンをクリック
            # 財産評価フラグが表示されるまで待機------------------------------------
            while (
                pg.locateOnScreen(TFolURL + r"\ZaisanhyoukaFlag.png", confidence=0.9)
                is None
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
            pg.press("return")
            # 入力した関与先コードを取得------------
            pg.keyDown("shift")
            pg.press("tab")
            pg.keyUp("shift")
            pg.hotkey("ctrl", "c")
            ThisNo = pyperclip.paste()
            # -----------------------------------
            pg.press("return")
            # 表示された年度を取得-----------------
            pg.hotkey("ctrl", "c")
            ThisYear = pyperclip.paste()
            # -----------------------------------
            pg.press("return")
            #####################################
            # [ここは税目種類のドロップボックス]
            #####################################
            pg.press("return")
            # 表示された申告種類を取得---------------
            pg.hotkey("ctrl", "c")
            ThisMonth = pyperclip.paste()
            # -----------------------------------
            time.sleep(1)
            # 他システムとメニューが違う-------------------------------------------------------
            if str(ExRow["関与先番号"]) == ThisNo:
                print("関与先あり")
                pg.press(["return", "return", "return"])
                # 財産評価更新アイコンが表示されるまで待機--------------------------------
                while (
                    pg.locateOnScreen(TFolURL + r"\ZaisanKousin.png", confidence=0.9)
                    is None
                ):
                    time.sleep(1)
                    HQ = ImgCheck(TFolURL, r"\ZaisanOpenQ.png", 0.9, 10)
                    if HQ[0] is True:
                        ImgClick(TFolURL, r"\ZaisanOpenQCansel.png", 0.9, 10)
                # --------------------------------------------------------------------
                ImgClick(TFolURL, r"\ZaisanKousin.png", 0.9, 10)  # 一括更新のアイコンをクリック
                # 財産評価メニューが表示されるまで待機------------------------------------
                while (
                    pg.locateOnScreen(TFolURL + r"\ZaisanOpenFlag.png", confidence=0.9)
                    is None
                ):
                    time.sleep(1)
                # --------------------------------------------------------------------
                time.sleep(3)
                # 更新区分を次年繰越に変更---------------------------------------------
                ImgClick(TFolURL, r"\Kousinkubun.png", 0.9, 10)
                pg.press("home")
                pg.press("return")
                # 更新区分フラグが表示されるまで待機------------------------------------
                while (
                    pg.locateOnScreen(TFolURL + r"\KousinkubunFlag.png", confidence=0.9)
                    is None
                ):
                    time.sleep(1)
                # --------------------------------------------------------------------
                if ErrStr == "":
                    pg.press(["return", "return", "return"])
                    pg.press("space")
                    # チェックマークが表示されるまで待機-------------------------------------
                    while (
                        pg.locateOnScreen(TFolURL + r"\ZaisanCheck.png", confidence=0.9)
                        is None
                    ):
                        time.sleep(1)
                    # --------------------------------------------------------------------
                    time.sleep(1)
                    ImgClick(TFolURL, r"\ZaisanStart.png", 0.9, 10)  # 更新開始のアイコンをクリック
                    # 確認ウィンドウが表示されるまで待機-------------------------------------
                    while (
                        pg.locateOnScreen(
                            TFolURL + r"\ZaisanStartQ.png", confidence=0.9
                        )
                        is None
                    ):
                        time.sleep(1)
                    # --------------------------------------------------------------------
                    pg.press("y")  # yで決定(nがキャンセル)
                    # 処理終了ウィンドウが表示されるまで待機----------------------------------
                    while (
                        pg.locateOnScreen(TFolURL + r"\ZaisanEnd.png", confidence=0.9)
                        is None
                    ):
                        time.sleep(1)
                    # --------------------------------------------------------------------
                    # チェックマークが表示されなくなるまで待機-------------------------------
                    while (
                        pg.locateOnScreen(TFolURL + r"\IkkatuCheck.png", confidence=0.9)
                        is not None
                    ):
                        time.sleep(1)
                    # --------------------------------------------------------------------
                    ImgClick(TFolURL, r"\MenuEnd.png", 0.9, 10)  # 終了アイコンをクリック
                    # 一括更新のアイコンが表示されるまで待機----------------------------------
                    while (
                        pg.locateOnScreen(
                            TFolURL + r"\ZaisanKousin.png", confidence=0.9
                        )
                        is None
                    ):
                        time.sleep(1)
                    # --------------------------------------------------------------------
                    # 閉じる処理--------------------------
                    pg.keyDown("alt")
                    pg.press("f4")
                    pg.keyUp("alt")
                    # -----------------------------------
                    # 財産評価フラグが表示されるまで待機-------------------------------------
                    while (
                        pg.locateOnScreen(
                            TFolURL + r"\ZaisanhyoukaFlag.png", confidence=0.9
                        )
                        is None
                    ):
                        time.sleep(1)
                    # --------------------------------------------------------------------
                    # 初期画面で開封された財産評価項目を閉じる----------------------------------
                    HoujinList = [r"\Zaisanhyouka.png", r"\Zaisanhyouka2.png"]
                    HLI = ImgCheckForList(TFolURL, HoujinList, 0.9, 10)
                    if HLI[0] is True:
                        ImgClick(TFolURL, HLI[1], 0.9, 10)
                    # --------------------------------------------------------------------
                    print("更新完了")
                    if ErrStr == "":
                        return True, ThisNo, ThisYear, ThisMonth
            else:
                print("関与先なし")
                return False, "関与先なし", "", ""
        else:
            return False, "財産評価起動失敗", "", ""
    except:
        return False, "exceptエラー", "", ""


# ------------------------------------------------------------------------------------------------------------------
def HoujinzeiUpdate(FolURL, TFolURL, ExRow, driver):
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
            pg.press("return")
            # 入力した関与先コードを取得------------
            pg.keyDown("shift")
            pg.press("tab")
            pg.keyUp("shift")
            pg.hotkey("ctrl", "c")
            ThisNo = pyperclip.paste()
            # -----------------------------------
            pg.press("return")
            # 表示された年度を取得-----------------
            pg.hotkey("ctrl", "c")
            ThisYear = pyperclip.paste()
            # -----------------------------------
            pg.press("return")
            #####################################
            # [ここは申告種類のドロップボックス]
            #####################################
            pg.press("return")
            # 表示された申告Noを取得---------------
            pg.hotkey("ctrl", "c")
            ThisMonth = pyperclip.paste()
            # -----------------------------------
            time.sleep(1)
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
                # --------------------------------------------------------------------
                ImgClick(
                    TFolURL, r"\IkkatsuHoujinKousin.png", 0.9, 10
                )  # 一括更新のアイコンをクリック
                # 法人税メニューが表示されるまで待機------------------------------------
                while (
                    pg.locateOnScreen(TFolURL + r"\HoujinzeiMenu.png", confidence=0.9)
                    is None
                ):
                    time.sleep(1)
                # --------------------------------------------------------------------
                # 再計算ウィンドウが表示されていないかチェック-----------------------------
                DRC = ImgCheck(TFolURL, r"\DataReCalc.png", 0.9, 10)
                if DRC[0] is True:
                    pg.press("return")
                    ErrStr = "ReCalc"  # Rpaエラー判別変数
                # ------------------------------------------------------------------
                if ErrStr == "":
                    ListCheck = False  # 申告種類判定変数
                    # Excelの値から申告種類を判定------------------------------------
                    ExPar = int(ExRow["法人税申告書_繰越対象"])
                    if ExPar == 31:
                        TaxPngName = r"\KakuteiNext.png"
                    elif ExPar == 41:
                        TaxPngName = r"\CyuukanNext.png"
                    elif ExPar == 51:
                        TaxPngName = r"\YoteiNext.png"
                    elif ExPar == 61:
                        TaxPngName = r"\SyuuseiThis.png"
                    else:
                        TaxPngName = r"\Err"
                    time.sleep(1)
                    # 申告種類に応じたリスト画像までループ----------------------------
                    while ListCheck is False:
                        pg.press("down")
                        TPN = ImgCheck(TFolURL, TaxPngName, 0.9, 10)
                        if TPN[0] is True:
                            ListCheck = True
                            pg.press("return")
                    # ------------------------------------------------------------
                    time.sleep(1)
                    ImgClick(TFolURL, r"\HoujinStart.png", 0.9, 10)  # 更新開始のアイコンをクリック
                    # 確認ウィンドウが表示されるまで待機-------------------------------------
                    while (
                        pg.locateOnScreen(TFolURL + r"\HoujinQ.png", confidence=0.9)
                        is None
                    ):
                        time.sleep(1)
                    # --------------------------------------------------------------------
                    pg.press("y")  # yで決定(nがキャンセル)
                    # 処理終了ウィンドウが表示されるまで待機----------------------------------
                    while (
                        pg.locateOnScreen(TFolURL + r"\HoujinEnd.png", confidence=0.9)
                        is None
                    ):
                        time.sleep(1)
                    # --------------------------------------------------------------------
                    pg.press("return")  # 決定
                    # 一括更新のアイコンが表示されるまで待機----------------------------------
                    while (
                        pg.locateOnScreen(
                            TFolURL + r"\IkkatsuHoujinKousin.png", confidence=0.9
                        )
                        is None
                    ):
                        time.sleep(1)
                    # --------------------------------------------------------------------
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
                    print("更新完了")
                    if ErrStr == "":
                        return True, ThisNo, ThisYear, ThisMonth
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
def GenkasyoukyakuUpdate(FolURL, TFolURL, ExRow, driver):
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
            pg.press("return")
            # 入力した関与先コードを取得------------
            pg.keyDown("shift")
            pg.press("tab")
            pg.keyUp("shift")
            pg.hotkey("ctrl", "c")
            ThisNo = pyperclip.paste()
            # -----------------------------------
            pg.press("return")
            # 表示された年度を取得-----------------
            pg.hotkey("ctrl", "c")
            ThisYear = pyperclip.paste()
            # -----------------------------------
            pg.press("return")
            # 表示された月を取得-------------------
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
                pg.press("tab")
                time.sleep(1)
                pg.press("space")
                # チェックマークが表示されるまで待機-------------------------------------
                while (
                    pg.locateOnScreen(TFolURL + r"\IkkatuCheck.png", confidence=0.9)
                    is None
                ):
                    time.sleep(1)
                # --------------------------------------------------------------------
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
                        ImgClick(TFolURL, r"\No_Rendou_Cansel.png", 0.9, 10)
                # --------------------------------------------------------------------
                pg.press("return")  # 決定
                # チェックマークが表示されなくなるまで待機-------------------------------
                while (
                    pg.locateOnScreen(TFolURL + r"\IkkatuCheck.png", confidence=0.9)
                    is not None
                ):
                    time.sleep(1)
                # --------------------------------------------------------------------
                ImgClick(TFolURL, r"\MenuEnd.png", 0.9, 10)  # 終了アイコンをクリック
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
def KessanUpDate(FolURL, TFolURL, ExRow, driver):
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
            pg.press("return")
            # 入力した関与先コードを取得------------
            pg.keyDown("shift")
            pg.press("tab")
            pg.keyUp("shift")
            pg.hotkey("ctrl", "c")
            ThisNo = pyperclip.paste()
            # -----------------------------------
            pg.press("return")
            # 表示された年度を取得-----------------
            pg.hotkey("ctrl", "c")
            ThisYear = pyperclip.paste()
            # -----------------------------------
            pg.press("return")
            # 表示された月を取得-------------------
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
                pg.press(["tab", "tab"])
                time.sleep(1)
                pg.press("space")
                # チェックマークが表示されるまで待機-------------------------------------
                while (
                    pg.locateOnScreen(TFolURL + r"\IkkatuCheck.png", confidence=0.9)
                    is None
                ):
                    time.sleep(1)
                # --------------------------------------------------------------------
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
                # チェックマークが表示されなくなるまで待機-------------------------------
                while (
                    pg.locateOnScreen(TFolURL + r"\IkkatuCheck.png", confidence=0.9)
                    is not None
                ):
                    time.sleep(1)
                # --------------------------------------------------------------------
                ImgClick(TFolURL, r"\MenuEnd.png", 0.9, 10)  # 終了アイコンをクリック
                # 一括更新のアイコンが表示されるまで待機----------------------------------
                while (
                    pg.locateOnScreen(
                        TFolURL + r"\IkkatsuKessanKousin.png", confidence=0.9
                    )
                    is None
                ):
                    time.sleep(1)
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
def KaikeiUpDate(FolURL, TFolURL, ExRow, driver):
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
            pg.press("return")
            # 入力した関与先コードを取得------------
            pg.keyDown("shift")
            pg.press("tab")
            pg.keyUp("shift")
            pg.hotkey("ctrl", "c")
            ThisNo = pyperclip.paste()
            # -----------------------------------
            pg.press("return")
            # 表示された年度を取得-----------------
            pg.hotkey("ctrl", "c")
            ThisYear = pyperclip.paste()
            # -----------------------------------
            pg.press("return")
            # 表示された月を取得-------------------
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
                ImgClick(TFolURL, r"\M_Sonota.png", 0.9, 10)  # その他メニュ-のアイコンをクリック
                # 一括更新のアイコンが表示されるまで待機----------------------------------
                while (
                    pg.locateOnScreen(TFolURL + r"\IkkatsuKousin.png", confidence=0.9)
                    is None
                ):
                    time.sleep(1)
                # --------------------------------------------------------------------
                ImgClick(TFolURL, r"\IkkatsuKousin.png", 0.9, 10)  # その他メニュ-のアイコンをクリック
                # 一括更新メニューが表示されるまで待機------------------------------------
                while (
                    pg.locateOnScreen(TFolURL + r"\IkkatuOpenFlag.png", confidence=0.9)
                    is None
                ):
                    time.sleep(1)
                # --------------------------------------------------------------------
                ImgClick(TFolURL, r"\IkkatuOpenFlag.png", 0.9, 10)  # 一括更新メニューのアイコンをクリック
                pg.press("tab")
                time.sleep(1)
                pg.press("space")
                # チェックマークが表示されるまで待機-------------------------------------
                while (
                    pg.locateOnScreen(TFolURL + r"\IkkatuCheck.png", confidence=0.9)
                    is None
                ):
                    time.sleep(1)
                # --------------------------------------------------------------------
                time.sleep(1)
                ImgClick(TFolURL, r"\IkkatuStart.png", 0.9, 10)  # 一括更新開始のアイコンをクリック
                # 確認ウィンドウが表示されるまで待機-------------------------------------
                while (
                    pg.locateOnScreen(TFolURL + r"\SakuseiQ.png", confidence=0.9)
                    is None
                ):
                    time.sleep(1)
                # --------------------------------------------------------------------
                pg.press("y")  # yで決定(nがキャンセル)
                # 確認ウィンドウが表示されるまで待機-------------------------------------
                while (
                    pg.locateOnScreen(TFolURL + r"\SakuseiQ2.png", confidence=0.9)
                    is None
                ):
                    time.sleep(1)
                # --------------------------------------------------------------------
                pg.press("return")  # 決定
                # 処理終了ウィンドウが表示されるまで待機----------------------------------
                while (
                    pg.locateOnScreen(TFolURL + r"\IkkatuEndFlag.png", confidence=0.9)
                    is None
                ):
                    time.sleep(1)
                # --------------------------------------------------------------------
                pg.press("return")  # 決定
                # チェックマークが表示されなくなるまで待機-------------------------------
                while (
                    pg.locateOnScreen(TFolURL + r"\IkkatuCheck.png", confidence=0.9)
                    is not None
                ):
                    time.sleep(1)
                # --------------------------------------------------------------------
                ImgClick(TFolURL, r"\MenuEnd.png", 0.9, 10)  # 終了アイコンをクリック
                # 一括更新のアイコンが表示されるまで待機----------------------------------
                while (
                    pg.locateOnScreen(TFolURL + r"\IkkatsuKousin.png", confidence=0.9)
                    is None
                ):
                    time.sleep(1)
                # --------------------------------------------------------------------
                # 閉じる処理--------------------------
                pg.keyDown("alt")
                pg.press("f4")
                pg.keyUp("alt")
                # -----------------------------------
                # 会計大将フラグが表示されるまで待機-------------------------------------
                while (
                    pg.locateOnScreen(TFolURL + r"\Kaikei_CFlag.png", confidence=0.9)
                    is None
                ):
                    time.sleep(1)
                    al4c = ImgCheck(TFolURL, r"\altf4Q.png", 0.9, 10)  # 終了確認が表示されたら
                    if al4c[0] is True:
                        pg.press("y")  # yで決定(nがキャンセル)
                # --------------------------------------------------------------------
                print("更新完了")
                return True, ThisNo, ThisYear, ThisMonth
            else:
                print("関与先なし")
                return False, "関与先なし", "", ""
        else:
            return False, "会計大将起動失敗", "", ""
    except:
        return False, "exceptエラー", "", ""


# ------------------------------------------------------------------------------------------------------------------
def MainFlow(FolURL, TFolURL, Exlsx):
    """
    概要: メイン処理
    @param FolURL : ミロク起動関数のフォルダ(str)
    @param TFolURL : このpyファイルのフォルダ(str)
    @param Exlsx : Excel指示シート(obj)
    @return : bool
    """
    try:
        BatUrl = FolURL + "/bat/AWADriverOpen.bat"  # 4724ポート指定でappiumサーバー起動バッチを開く
        driver = MJSOpen.MainFlow(
            BatUrl, FolURL, "RPAPhoto/MJS_DensiSinkoku"
        )  # OMSを起動しログイン後インスタンス化
        # driver = []
        FolURL = FolURL + "/RPAPhoto/MJS_DensiSinkoku"
        # ----------------------------------------------------------------------------------------------------------------------
        logger.debug("MJS操作画面へ偏移")
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
            if isnItem == "更新申請":
                ExSheet = Exlsx.parse(isnItem, skiprows=0)
                print(ExSheet)
                Exrc = np.array(ExSheet).shape[1]  # 列数
                ExrcHeader = []
                for Ex in range(Exrc):
                    ExRow = ExSheet.iloc[0]
                    ExSecondRow = ExSheet.iloc[1]
                    if ExRow[Ex] == ExRow[Ex]:  # nan判定
                        # nanでない場合
                        Txt = ExRow[Ex]
                        if ExSecondRow[Ex] == ExSecondRow[Ex]:  # nan判定
                            # nanでない場合
                            ExrcHeader.append(ExRow[Ex] + "_" + ExSecondRow[Ex])
                        else:
                            # nanの場合
                            ExrcHeader.append(ExRow[Ex])
                    else:
                        # nanの場合
                        if ExSecondRow[Ex] == ExSecondRow[Ex]:  # nan判定
                            # nanでない場合
                            ExrcHeader.append(Txt + "_" + ExSecondRow[Ex])
                        else:
                            # nanの場合
                            ExrcHeader.append(Txt)
                MainStarter(
                    FolURL, TFolURL, ExSheet, ExrcHeader, isnItem, driver
                )  # データ送信画面までの関数
    except Exception as e:
        logger.debug(e)


# RPA用画像フォルダの作成---------------------------------------------------------
FolURL = os.getcwd().replace("\\", "/")  # 先
TFolURL = FolURL + r"\RPAPhoto\MJS_SystemNextCreate"  # 先
XLSURL = TFolURL + r"\ミロク更新項目.xlsx"
# --------------------------------------------------------------------------------
Exlsx = EFA.XlsmRead(XLSURL)
if Exlsx[0] is True:
    try:
        MainFlow(FolURL, TFolURL, Exlsx[1])
    except:
        traceback.print_exc()
else:
    print("Excel読み込みエラー")
    logger.debug("Excel読み込みエラー")
