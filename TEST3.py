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

import datetime
import openpyxl

from ctypes import windll

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


# RPA用画像フォルダの作成---------------------------------------------------------
FolURL = os.getcwd().replace("\\", "/")  # 先
TFolURL = FolURL + r"\RPAPhoto\MJS_SystemNextCreate"  # 先
XLSDir = r"\\NAS-SV\B_監査etc\B2_電子ﾌｧｲﾙ\RPA_ミロクシステム次年更新\一括更新申請"
LURL = r"\\NAS-SV\B_監査etc\B2_電子ﾌｧｲﾙ\RPA_ミロクシステム次年更新\一括更新申請\MJSLog\MJSSysUpLog.txt"  # 処理状況CSVのURL

def KomonUpdate(TFolURL,ExRow):

    # 関与先コード入力ボックスをクリック------------------------------------
    ImgClick(TFolURL, r"\Komonsaki_Icon.png", 0.9, 10)
    while (
        pg.locateOnScreen(TFolURL + r"\Komonsaki_Open.png", confidence=0.9)
        is None
    ):
        time.sleep(1)

    p = pyautogui.locateOnScreen(TFolURL + r"\Komonsaki_CodeTxt.png", confidence=0.9)
    x, y = pyautogui.center(p)
    pyautogui.click(x + 100, y)
    pg.press("delete")
    pyperclip.copy(str(ExRow["関与先番号"]))
    pg.hotkey("ctrl", "v")
    pg.press(["return", "return"])

    time.sleep(1)

    p = pyautogui.locateOnScreen(TFolURL + r"\RensaouMeisyou.png", confidence=0.9)
    x, y = pyautogui.center(p)
    pyautogui.click(x + 100, y)
    pg.press("up")
    pg.press("down")
    pg.press("delete")
    pyperclip.copy(str(ExRow["関与先番号"]))
    pg.hotkey("ctrl", "v")
    pg.press(["return", "return"])

    pg.keyDown("alt")
    pg.press("u")
    pg.keyUp("alt")

    time.sleep(1)

    pg.keyDown("alt")
    pg.press("x")
    pg.keyUp("alt")

    while (
        pg.locateOnScreen(TFolURL + r"\SyonaiKanri.png", confidence=0.9)
        is None
    ):
        time.sleep(1)

    pg.keyDown("alt")
    pg.press("f4")
    pg.keyUp("alt")
    time.sleep(1)


# -----------------------------------------------------------------------


ImgClick(TFolURL, r"\PrintOutTab.png", 0.9, 10)  # 2印刷タブクリック
# 6月次締めが表示されるまで待機--------------------------
while (
    pg.locateOnScreen(TFolURL + r"\SimeIcon.png", confidence=0.9)
    is None
):
    time.sleep(1)
ImgClick(TFolURL, r"\SimeIcon.png", 0.9, 10)  # その他メニュ-のアイコンをクリック
while (
    pg.locateOnScreen(TFolURL + r"\GetujiIcon.png", confidence=0.9)
    is None
):
    time.sleep(1)
ImgClick(TFolURL, r"\GetujiIcon.png", 0.9, 10)  # 月次処理アイコンをクリック
# 月次確定済みか判定して処理分け-------------------------------------------------------
# 月次処理解除-----------------------------------------------------------------------
KUL = ImgCheck(TFolURL, r"\KakuteUnLock.png", 0.9, 10)  # 月次処理解除アイコンを検索
if KUL[0] is True:
    ImgClick(TFolURL, r"\KakuteUnLock.png", 0.9, 10)  # 月次処理アイコンをクリック
    time.sleep(2)
    pg.press("y")
    while (
        pg.locateOnScreen(TFolURL + r"\GetusjiKakutei.png", confidence=0.9)
        is None
    ):
        time.sleep(1)
    pg.press("return")
    time.sleep(1)
# ---------------------------------------------------------------------------------
pg.keyDown("alt")
pg.press("x")
pg.keyUp("alt")
while (
    pg.locateOnScreen(TFolURL + r"\M_Sonota.png", confidence=0.9)
    is None
):
    time.sleep(1)
ImgClick(TFolURL, r"\D_TourokuTAB.png", 0.9, 10)  # 6導入・登録タブクリック
# 会社基本情報アイコンが表示されるまで待機--------------------------------------
while (
    pg.locateOnScreen(TFolURL + r"\CamIcon.png", confidence=0.9)
    is None
):
    time.sleep(1)      
ImgClick(TFolURL, r"\CamIcon.png", 0.9, 10)  # 会社基本情報アイコンをクリック
# 顧問先情報取り込みアイコンが表示されるまで待機--------------------------------
while (
    pg.locateOnScreen(TFolURL + r"\DataInIcon.png", confidence=0.9)
    is None
):
    time.sleep(1)         
ImgClick(TFolURL, r"\DataInIcon.png", 0.9, 10)  # 顧問先情報取り込みアイコンをクリック
while (
    pg.locateOnScreen(TFolURL + r"\DataInOK.png", confidence=0.9)
    is None
):
    time.sleep(1)
ImgClick(TFolURL, r"\DataInOK.png", 0.9, 10)  #取り込むボタンをクリック
time.sleep(1)
pg.keyDown("alt")
pg.press("x")
pg.keyUp("alt")
time.sleep(1)
# --------------------------------------------------------------------------------
ImgClick(TFolURL, r"\PrintOutTab.png", 0.9, 10)  # 2印刷タブクリック
# 6月次締めが表示されるまで待機--------------------------
while (
    pg.locateOnScreen(TFolURL + r"\AfterGetujiKakutei.png", confidence=0.9)
    is None
):
    time.sleep(1)
ImgClick(TFolURL, r"\AfterGetujiKakutei.png", 0.9, 10)  # 2印刷タブクリック
# 月次確定--------------------------------------------------------------------------
KL = ImgCheck(TFolURL, r"\KakuteiLock.png", 0.9, 10)  # 月次処理確定アイコンを検索
if KL[0] is True:
    ImgClick(TFolURL, r"\KakuteiLock.png", 0.9, 10)  # 月次処理確定アイコンをクリック
    time.sleep(1)
    pg.press("y")
    while (
        pg.locateOnScreen(TFolURL + r"\KessanKQ.png", confidence=0.9)
        is None
    ):
        time.sleep(1)
    pg.press("y")
    while (
        pg.locateOnScreen(TFolURL + r"\GetusjiKakutei.png", confidence=0.9)
        is None
    ):
        time.sleep(1)
    pg.press("return")