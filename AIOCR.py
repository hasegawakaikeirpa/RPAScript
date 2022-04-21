# モジュールインポート
# osインポート
import os
import Function.GCloudVision as GCV
import toml
from collections import OrderedDict
import re
import numpy as np
from pathlib import Path
from pdf2image import convert_from_path
import Function.CSVOut as FCSV
import RPAPhoto.PDFeTaxReadForList.CSVSetting as CSVSet  # CSVの設定ファイルの読込
import cv2

# logger設定------------------------------------------------------------------------------
import logging.config

logging.config.fileConfig(r"LogConf\logging_debug.conf")
logger = logging.getLogger(__name__)
# -------------------------------------------------------------------------------------------------------
def ModelpngDelte(FolURL):
    # PDF変換pngの削除-----------------------------------------------------------------
    try:
        for fd_path, sb_folder, sb_file in os.walk(FolURL):
            for fil in sb_file:
                if "OCR" in fil and fil.endswith(".png") is True:
                    os.remove(fd_path + "\\" + fil)
    except:
        print("OCR画像ファイル削除エラー")
    # --------------------------------------------------------------------------------


# -------------------------------------------------------------------------------------------------------
def pdf_image(pdf_file, img_path, fmtt, dpi, PDFPage):
    try:
        OCRList = []
        Mydir = os.getcwd()
        pppath = Mydir + r"\poppler-22.01.0\Library\bin"
        # pdf_file、img_pathをPathにする
        pdf_path = Path(pdf_file)
        image_dir = Path(img_path)

        # PDFをImage に変換(pdf2imageの関数)
        pages = convert_from_path(pdf_path, dpi, poppler_path=pppath)

        # 画像ファイルを１ページずつ保存
        for i, page in enumerate(pages):
            file_name = "OCR" + str(i) + "." + fmtt
            image_path = image_dir / file_name
            page.save(image_path, fmtt)

            # グレースケールに変換
            src = cv2.imread(image_path._str, 0)
            cv2.imwrite(image_path._str, src)

        for fd_path, sb_folder, sb_file in os.walk(image_dir):
            for fil in sb_file:
                # if "OCR" in fil and fil.endswith(".png") is True:
                SerchName = "OCR" + PDFPage + ".png"
                if SerchName == fil:
                    OCRList.append([fd_path, fil])
        return True, OCRList
    except:
        return False, ""


# -------------------------------------------------------------------------------------------------------
def DiffListCreate(FolURL, OCRList, KCode, PDFDir, PDFPageTxt):
    try:
        for OCRListItem in OCRList:
            try:
                FileURL = OCRListItem[0] + "\\" + OCRListItem[1]
                GF = GCV.rentxtver(
                    FileURL, 2000, 15, 300, 1100, 5, 500, "::", 10
                )  # 画像URL,横軸閾値,縦軸閾値,ラベル配置間隔,etax横軸閾値,etax縦軸閾値,etaxラベル配置間隔,ラベル(str),同行として扱う縦間隔
                if GF[0] is True:
                    GFTable = GF[1]
                    GFRow = len(GFTable)
                    GFTColList = []
                    GFTParList = []
                    for g in reversed(range(GFRow)):
                        if "::" not in GFTable[g]:
                            GFTable.pop(g)
                    GFTCount = 0
                    for GFTableItem in GFTable:
                        strGF = str(GFTableItem).replace("給額", "総額").replace("稅", "税")
                        if strGF.endswith("円") is True:
                            strGF = strGF.replace("円", "")
                        SGF = strGF.split("::")
                        if GFTCount == 0:
                            GFTColList.append("URL")
                            GFTParList.append(str(PDFDir))
                            GFTColList.append("ページ")
                            GFTParList.append(str(PDFPageTxt))
                        if "氏名又は名称" in strGF:
                            GFTColList.append("コード")
                            GFTParList.append(str(KCode))
                            GFTColList.append(SGF[0].replace(",", ""))
                            GFTParList.append(SGF[1])
                        else:
                            GFTColList.append(SGF[0].replace(",", ""))
                            GFTParList.append(SGF[1])
                        GFTCount += 1
                    print(GFTColList)
                    print(GFTParList)
                    return True, GFTColList, GFTParList
            except:
                print("ループ内エラー抽出失敗")
                logger.debug(FolURL + "ループ内エラー抽出失敗")
                return False, "", ""
    except:
        print("エラー抽出失敗")
        logger.debug(FolURL + "ループ内エラー抽出失敗")
        return False, "", ""


# -------------------------------------------------------------------------------------------------------
def DiffListPlus(ColList, ScrList):
    try:
        LNList = Settingtoml["MASTER"]["ListNameList"]  # tomlから各種設定リスト名を抽出
        NewColList = []
        for LNListItem in LNList:
            NewColList = Settingtoml["AIOCR"][LNListItem]
            SColA = set(ColList) - set(NewColList)
            SColB = set(NewColList) - set(ColList)
            if len(SColA) == 0 and len(SColB) == 0:
                CDict[LNListItem].append(ScrList)
                return True, LNListItem
        print("指定列名での設定項目がありませんでした。")
        CDict["エラーリスト"].append(ScrList)
        return False, "エラーリスト"
    except:
        CDict["エラーリスト"].append(ScrList)
        return False, "エラーリスト"


# -------------------------------------------------------------------------------------------------------
def DiffListCSVOUT(ListURL, ColN):
    ListURL = ListURL.replace("\\", "/")
    FCSV.CsvSaveEnc(
        ListURL + "/" + ColN + ".csv",
        CDict[ColN],
        "cp932",
        Settingtoml["AIOCR"][ColN],
    )


# -------------------------------------------------------------------------------------------------------

# 各種設定------------------------------------------------------------------------------------------------
# toml読込------------------------------------------------------------------------------
with open(
    os.getcwd() + r"/RPAPhoto/PDFeTaxReadForList/Setting.toml", encoding="utf-8"
) as f:
    Settingtoml = toml.load(f)
    print(Settingtoml)
# -----------------------------------------------------------
CDict = CSVSet.CSVIndexSortFuncArray  # 外部よりdict変数取得
MyURL = os.getcwd() + r"\RPAPhoto\PDFeTaxReadForList"  # このスクリプトの配下の設定フォルダ
# CSVURL = r"\\Sv05121a\e\電子ファイル\メッセージボックス\TEST2022-3\受信通知CSV\受信通知取得失敗リスト.csv"  # 取得対象のURLが記載されたCSV
CSVURL = r"\\Sv05121a\e\電子ファイル\メッセージボックス\TEST\3月受信通知取得失敗リスト.csv"  # 取得対象のURLが記載されたCSV
# --------------------------------------------------------------------------------
try:
    CSVList = FCSV.CsvRead(CSVURL)  # 自作関数でCSVをDataFrameに変換
    CSVRow = np.array(CSVList[1]).shape[0]  # DataFrameの行数
    DLCList = []  # 書出しCSVリスト
    for x in range(CSVRow):  # DataFrameのループ
        try:
            CSVRowData = CSVList[1].iloc[x]  # DataFrameの行データ
            PDFDir = CSVRowData["URL"]  # DataFrameから抽出対象のPDFを取得
            KCode = CSVRowData["コード"]  # DataFrameから抽出対象のPDFを取得
            PDFPageTxt = CSVRowData["ページ"]
            PDFPage = str(int(re.findall(r"\d", CSVRowData["ページ"])[0]) - 1)  # 対象のページを取得
            ModelpngDelte(MyURL)  # PDF変換pngの削除
            PI = pdf_image(PDFDir, MyURL, "png", 500, PDFPage)  # 対象のPDFをpng変換
            if PI[0] is True:  # png変換に成功したら
                OCRList = PI[1]  # PDFから変換したpngを全て取得
                DLC = DiffListCreate(
                    MyURL, OCRList, KCode, PDFDir, PDFPageTxt
                )  # APIで画像テキスト抽出
                if DLC[0] is True:  # 画像テキスト抽出成功なら
                    DLP = DiffListPlus(DLC[1], DLC[2])  # 抽出リストに格納
                    if DLP[0] is True:
                        DLCList.append(DLP[1])  # できあがった抽出リストを保管
        except:
            continue
    DLCDiplicated = list(OrderedDict.fromkeys(DLCList))  # 抽出リストの重複削除
    for DItem in DLCDiplicated:
        try:
            DiffListCSVOUT(MyURL, DItem)  # 抽出リストをCSV書出し
        except:
            continue
except:
    print("エラー")
