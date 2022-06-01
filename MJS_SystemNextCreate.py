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
from datetime import datetime as dt

# 例外処理判定の為のtracebackインポート
import traceback

# pandas(pd)で関与先データCSVを取得
import pyautogui
import codecs
import pyperclip  # クリップボードへのコピーで使用
import Function.ExcelFileAction as EFA
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
        Exrc = np.array(ExDf).shape[1]  # 行数
        for Ex in range(Exrc):
            ExRow = ExDf.iloc[Ex]
            if ExRow["関与先番号"] == ExRow["関与先番号"]:  # nan判定
                # nanでない場合
                OpenSystem(FolURL, TFolURL, ExRow, ExrcHeader, isnItem, driver)
            else:
                # nanの場合
                print("nan")
    except:
        return False, ""


# ------------------------------------------------------------------------------------------------------------------
def OpenSystem(FolURL, TFolURL, ExRow, ExrcHeader, isnItem, driver):
    try:
        for ExrcHeaderItem in ExrcHeader:
            if "_繰越対象" in ExrcHeaderItem:
                SysN = ExrcHeaderItem.split("_")
                if ExRow[SysN[0] + "_繰越対象"] == ExRow[SysN[0] + "_繰越対象"]:
                    # nanでない場合
                    if ExRow[SysN[0] + "_繰越処理日"] == ExRow[SysN[0] + "_繰越処理日"]:
                        # nanでない場合
                        print(ExRow[SysN[0] + "_繰越処理日"])
                    else:
                        # nanの場合
                        print("nan")
                else:
                    # nanの場合
                    print("スタート")
                    if "会計大将" == SysN[0]:
                        SystemUp = KaikeiUpDate(FolURL, TFolURL, ExRow, driver)
                        if SystemUp[0] is True:
                            dt_now = datetime.datetime.now()
                            WriteEx = openpyxl.load_workbook(XLSURL)
                            WriteExSheet = WriteEx[isnItem]
                            c = int(ExRow[str(SysN[0]) + "_列"])
                            r = int(ExRow[str(SysN[0]) + "_行"])
                            WriteExSheet.cell(row=r, column=c).value = dt_now
                            WriteExSheet.cell(row=(r), column=(c - 3)).value = "*"
                            print("シート書き込み完了")
                            WriteEx.save(XLSURL)
                    elif "決算内訳書" == SysN[0]:
                        SystemUp = KessanUpDate(FolURL, TFolURL, ExRow, driver)
                        if SystemUp[0] is True:
                            dt_now = datetime.datetime.now()
                            WriteEx = openpyxl.load_workbook(XLSURL)
                            WriteExSheet = WriteEx[isnItem]
                            c = int(ExRow[str(SysN[0]) + "_列"])
                            r = int(ExRow[str(SysN[0]) + "_行"])
                            WriteExSheet.cell(row=r, column=c).value = dt_now
                            WriteExSheet.cell(row=(r), column=(c - 3)).value = "*"
                            print("シート書き込み完了")
                            WriteEx.save(XLSURL)
                    elif "減価償却" == SysN[0]:
                        print("減価償却")
                    elif "法人税申告書" == SysN[0]:
                        print("法人税申告書")
                    elif "財産評価明細書" == SysN[0]:
                        print("財産評価明細書")
                    elif "年末調整" == SysN[0]:
                        print("年末調整")
                    elif "法定調書" == SysN[0]:
                        print("法定調書")
                    elif "所得税確定申告" == SysN[0]:
                        print("所得税確定申告")
                    else:
                        print("NoSystem")
    except:
        print("TEST")


# ------------------------------------------------------------------------------------------------------------------
def KessanUpDate(FolURL, TFolURL, ExRow, driver):
    """
    00:"関与先番号"
    01:"関与先名"
    02:"担当者_ｺｰﾄﾞ"
    03:"担当者_担当者名"
    04:"会計大将_繰越対象"
    05:"会計大将_列"
    06:"会計大将_行"
    07:"会計大将_繰越処理日"
    08:"決算内訳書_繰越対象"
    09:"決算内訳書_列"
    10:"決算内訳書_行"
    11:"決算内訳書_繰越処理日"
    12:"減価償却_繰越対象"
    13:"減価償却_列"
    14:"減価償却_行"
    15:"減価償却_繰越処理日"
    16:"法人税申告書_繰越対象"
    17:"法人税申告書_列"
    18:"法人税申告書_行"
    19:"法人税申告書_繰越処理日"
    20:"財産評価明細書_繰越対象"
    21:"財産評価明細書_列"
    22:"財産評価明細書_行"
    23:"財産評価明細書_繰越処理日"
    24:"財産評価明細書"
    25:"年末調整"
    26:"法定調書"
    27:"所得税確定申告"
    """
    try:
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
                time.sleep(3)
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
                return True, ThisNo, ThisYear, ThisMonth
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
                time.sleep(3)
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
                Exrc = np.array(ExSheet).shape[0]  # 列数
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
