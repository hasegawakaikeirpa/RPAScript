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
import Function.MJSSPOPDFMarge as PDFM
import datetime
import openpyxl
from openpyxl.formatting.rule import Rule
from ctypes import windll

import os
import sys
import PyPDF2
from pdfminer.high_level import extract_text
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfpage import PDFPage
import WarekiHenkan as WK

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


# ------------------------------------------------------------------------------------------------------------------
def delete_page(file_name, page_nums, PW):
    with open(file_name, "rb") as input_file:
        pdf_reader = PyPDF2.PdfFileReader(input_file, strict=False)
        pdf_writer = PW

        for i in range(pdf_reader.numPages):
            if str(i + 1) in page_nums:
                continue
            pdf_page = pdf_reader.getPage(i)
            pdf_writer.addPage(pdf_page)
            return pdf_writer


def BeppyouPDFSplit(
    path_pdf,
    PDFDir,
):
    output = PyPDF2.PdfFileWriter()
    output2 = PyPDF2.PdfFileWriter()
    output3 = PyPDF2.PdfFileWriter()
    output4 = PyPDF2.PdfFileWriter()
    output5 = PyPDF2.PdfFileWriter()
    op = 0
    op2 = 0
    op3 = 0
    op4 = 0
    op5 = 0
    SPList = []
    fp = open(path_pdf, "rb")  # PDFファイルを読み込み
    parser = PDFParser(fp)  # PDFperserを作成。
    document = PDFDocument(parser)  # PDFperserを格納。
    num_pages = 0  # ページ数格納変数を初期化
    num_pagesList = []
    for page in PDFPage.create_pages(document):  # ページオブジェ分ループ
        num_pages += 1  # ページ数カウント
        num_pagesList.append(num_pages - 1)
    print(num_pages)  # ページ数確認
    # ------------------------------------------------------------------------------------
    try:
        # PDFのページ数分ループ---------------------------------------------------------------------------
        for y in range(num_pages):
            infile = PyPDF2.PdfFileReader(path_pdf, "rb")
            PL = []
            PL.append(y)
            Sbtext = extract_text(
                path_pdf, page_numbers=PL, maxpages=1, codec="utf-8"
            )  # テキストのみ取得できる
            Sbtext = (
                Sbtext.replace("\n", "")
                .replace("\u3000", "")
                .replace("\x0c", "")
                .replace(" ", "")
            )
            if (
                "第六号様式（提出用）" in Sbtext
                or "第六号様式（入力用）" in Sbtext
                or "第六号様式別表九（提出用）" in Sbtext
                or "第六号様式別表九（入力用）" in Sbtext
                or "第二十号様式（提出用）" in Sbtext
                or "第二十号様式（入力用）" in Sbtext
            ):
                print("不要")
            elif "第六号様式（控用）" in Sbtext:
                print(Sbtext)
                p = infile.getPage(y)
                output2.addPage(p)
                op2 += 1
            elif "第六号様式別表九（控用）" in Sbtext:
                print(Sbtext)
                p = infile.getPage(y)
                output3.addPage(p)
                op3 += 1
            elif "第二十号様式（控用）" in Sbtext:
                print(Sbtext)
                p = infile.getPage(y)
                output4.addPage(p)
                op4 += 1
            elif "第二十二号の二様式" in Sbtext:
                print(Sbtext)
                p = infile.getPage(y)
                output5.addPage(p)
                op5 += 1
            elif "個別注記表" in Sbtext:
                print(Sbtext)
                SP = Sbtext.split("個別注記表")
                SP = SP[1].split("Ⅰ.")
                SP = SP[0].replace("自", "").replace("至", "-")
                SP = SP.split("-")
                FD = WK.SeirekiSTRDate(SP[0])
                FD = datetime.datetime.strptime(FD, "%Y/%m/%d")
                SPList.append([y, FD])
                p = infile.getPage(y)
            else:
                print(Sbtext)
                p = infile.getPage(y)
                output.addPage(p)
                op += 1
        if not len(SPList) == 0:
            DcDiff = SPList[0][1] - SPList[1][1]
            if DcDiff.days > 0:
                p = infile.getPage(SPList[0][0])
                output.addPage(p)
                op += 1
            elif DcDiff.days < 0:
                p = infile.getPage(SPList[1][0])
                output.addPage(p)
                op += 1
        splitext = os.path.splitext(path_pdf)
        if not op == 0:
            with open(path_pdf, "wb") as output_file:
                output.write(output_file)
        elif not op2 == 0:
            with open(PDFDir + r"\第6号様式（県）" + splitext[1], "wb") as output_file:
                output2.write(output_file)
        elif not op3 == 0:
            with open(PDFDir + r"\第6号様式別表9（県）" + splitext[1], "wb") as output_file:
                output3.write(output_file)
        elif not op4 == 0:
            with open(PDFDir + r"\第20号様式（市）" + splitext[1], "wb") as output_file:
                output4.write(output_file)
        elif not op5 == 0:
            with open(PDFDir + r"\第22号の2様式" + splitext[1], "wb") as output_file:
                output5.write(output_file)
        return True
    except:
        return False


# RPA用画像フォルダの作成---------------------------------------------------------
FolURL = os.getcwd().replace("\\", "/")  # 先
TFolURL = FolURL + r"\RPAPhoto\MJS_SystemNextCreate"  # 先
CFolURL = FolURL + r"\RPAPhoto\MJS_SystemPrintOut"  # 先
SerchURL = r"\\Sv05121a\e\電子ファイル\(3)法人決算"  # 先
XLSURL = r"\\Sv05121a\e\C 作業台\RPA\RPA_ミロクシステム次年更新\ミロク更新項目.xlsx"
LURL = r"\\Sv05121a\e\C 作業台\RPA\RPA_ミロクシステム次年更新\MJSLog\MJSSysUpLog.txt"  # 処理状況CSVのURL
Title = "490_㈲ムカイハタタイヤ_RPA決算書"
EXNo = 490
EXdir = "R3"
# --------------------------------------------------------------------------------
BeppyouPDFSplit(
    r"D:\TEST.pdf",
    r"D:",
)
