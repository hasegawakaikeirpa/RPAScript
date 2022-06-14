# ----------------------------------------------------------------------------------------------------------------------
# モジュールインポート
import pyautogui as pg
import time

# pandasインポート
import pandas as pd

# import tkinter
import tkinter.filedialog

# osインポート
import os

# pandas(pd)で関与先データCSVを取得
import pyautogui
import pyperclip  # クリップボードへのコピーで使用
import PyPDF2
from PyPDF2 import PdfFileWriter, PdfFileReader
from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, portrait
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

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
def insert_text_output_pdf_PyPDF2(pdf_file_path, insert_text, output_name):
    """
    既存のPDFファイルに文字を挿入し、別名で出力します
    :param pdf_file_path:       既存のPDFファイルパス
    :param insert_text:         挿入するテキスト
    :return:
    """

    # ファイルの指定
    template_file = pdf_file_path  # 既存のテンプレートPDF
    output_file = output_name  # 完成したPDFの保存先
    tmp_file = "./__tmp.pdf"  # 一時ファイル

    # A4縦のCanvasを作成 -- (*1)
    w, h = portrait(A4)
    cv = canvas.Canvas(tmp_file, pagesize=(w, h))

    # フォントを登録しCanvasに設定 --- (*2)
    font_size = 10
    ttf_file = os.getcwd() + r"\IPAexfont00401\ipaexg.ttf"
    pdfmetrics.registerFont(TTFont("IPAexGothic", ttf_file))
    cv.setFont("IPAexGothic", font_size)

    # 文字列を描画する --- (*3)
    cv.setFillColorRGB(0, 0, 0.4)
    cv.drawString(30 * mm, h - 10 * mm, insert_text)

    # 一時ファイルに保存 --- (*4)
    cv.showPage()
    cv.save()

    # テンプレートとなるPDFを読む --- (*5)
    template_pdf = PdfFileReader(template_file)
    num_pages = template_pdf.getNumPages()  # ページ数の取得
    template_page = template_pdf.getPage(0)
    merger = PyPDF2.PdfFileMerger()
    output = PdfFileWriter()

    # 一時ファイルを読んで合成する --- (*6)
    tmp_pdf = PdfFileReader(tmp_file)
    for x in range(num_pages):
        if x == 0:
            template_page.mergePage(tmp_pdf.getPage(0))
            output.addPage(template_page)
            # merger.append(tmp_file)
        else:
            output.addPage(template_pdf.getPage(x))
            # merger.append(template_file, pages=(x))

    # 書き込み先PDFを用意 --- (*7)
    with open(output_file, "wb") as fp:
        output.write(fp)


def ChangeDir():

    List = []
    idir = TFolURL
    file_path = tkinter.filedialog.askdirectory(initialdir=idir)
    # file_path = file_path.replace("\u3000","\　")
    for fd_path, sb_folder, sb_file in os.walk(file_path):
        for fil in sb_file:
            List.append([fd_path + "\\" + fil, fil.replace(".pdf", "")])
    for ListItem in List:
        SPName = ListItem[1]
        ReSPName = ListItem[0].replace(".pdf", "") + "(印字).pdf"
        insert_text_output_pdf_PyPDF2(
            ListItem[0],
            SPName,
            ReSPName,
        )


# RPA用画像フォルダの作成---------------------------------------------------------
FolURL = os.getcwd().replace("\\", "/")  # 先
TFolURL = FolURL + r"\RPAPhoto\TKC_TekikakuPrintOut"  # 先
CSVURL = TFolURL + r"\List.CSV"
# --------------------------------------------------------------------------------
# with open(CSVURL, "r", encoding="cp932") as f:
#     LM = csv.reader(f)
#     Line = [row for row in LM]
"""
コード,関与先名・納税者名,税務署,課税方式区分,書類作成,電子申請ﾃﾞｰﾀ作成,担当者
"""
Call = ChangeDir()
# CSVF = pd.read_csv(CSVURL, encoding="cp932")
# CSVR = len(CSVF)
# PV = ImgCheck(TFolURL, r"\Preview.png", 0.9, 10)
# PVx = PV[1]
# PVy = PV[2] + 45
# SPos = PV[2] + 45
# CRCount = 1
# for CR in range(CSVR):
#     CSVRow = CSVF.iloc[CR]
#     Title = CSVRow["コード"] + "_" + CSVRow["担当者"] + ".pdf"
#     Title = Title.replace("/", "_")
#     Fname = TFolURL.replace("/", "\\") + "\\" + Title
#     if int(CSVRow["行"]) >= 183:
#         pyautogui.click(PVx, PVy)
#         while pg.locateOnScreen(TFolURL + r"\PrintTitle.png", confidence=0.9) is None:
#             time.sleep(1)
#         ImgClick(TFolURL, r"\PrintTitle.png", 0.9, 10)
#         pg.keyDown("ctrl")
#         pg.press("p")
#         pg.keyUp("ctrl")
#         while pg.locateOnScreen(TFolURL + r"\PrintBtn.png", confidence=0.9) is None:
#             time.sleep(1)
#         ImgClick(TFolURL, r"\PrintBtn.png", 0.9, 10)
#         time.sleep(1)
#         pyperclip.copy(Fname)
#         pg.hotkey("ctrl", "v")
#         pg.press("return")
#         while pg.locateOnScreen(TFolURL + r"\PrintTitle.png", confidence=0.9) is None:
#             if ImgCheck(TFolURL, r"\RepFile.png", 0.9, 10)[0] is True:
#                 pg.press("y")
#         time.sleep(1)
#         ImgClick(TFolURL, r"\PrintTitle.png", 0.9, 10)
#         pg.keyDown("alt")
#         pg.press("f4")
#         pg.keyUp("alt")
#         time.sleep(1)
#     if CRCount == 14:
#         pyautogui.click(PVx, PV[2])
#         pg.press("pagedown")
#         CRCount = 1
#         PVy = SPos
#     else:
#         pyautogui.click(PVx, PV[2])
#         CRCount += 1
#         PVy += 30
