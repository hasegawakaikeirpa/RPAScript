# モジュールインポート
# osインポート
import os
from google.cloud import vision
from google.oauth2 import service_account
import io

# import time
import toml
from collections import OrderedDict
import re

# ﻿from PIL import Image
# import os
# import sys
# import pyocr
# import pyocr.builders
# import pdf2image
import numpy as np
from pathlib import Path
from pdf2image import convert_from_path
import Function.CSVOut as FCSV
import RPAPhoto.PDFeTaxReadForList.CSVSetting as CSVSet  # CSVの設定ファイルの読込

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
def APIRead(FolURL, tar):  # Arg1 = 画像ファイルのdir,Arg2 = 読取画像のテキストを返す
    # GoogleAPI身元証明書のjson読み込み--------------------------------------------------------------------
    try:
        credentials = service_account.Credentials.from_service_account_file(
            os.getcwd() + "/key.json"
        )  # GAPIキーのURL
        client = vision.ImageAnnotatorClient(credentials=credentials)
        # client = vision.ImageAnnotatorClient()PCにPath通してるならこっちでも認証可能
        # 抽出対象の画像からテキスト抽出------------------------------------------------------------------------
        path = FolURL + "\\" + tar
        with io.open(path, "rb") as image_file:
            content = image_file.read()

        image = vision.Image(content=content)

        response = client.text_detection(image=image)
        texts = response.text_annotations
        x = 0
        for text in texts:
            if x == 0:
                OT = '\n"{}"'.format(text.description)
            x = x + 1
        # APIレスポンスエラーならraiseでエラーおこし---------------------------------------------
        if response.error.message:
            raise Exception(
                "{}\nFor more info on error messages, check: "
                "https://cloud.google.com/apis/design/errors".format(
                    response.error.message
                )
            )
        OT = OT.split("\n")
        return True, OT
    except:
        return False, ""


# -------------------------------------------------------------------------------------------------------
def OCRDiff(OT, ET):
    try:
        Final = []
        # 雛形と重複項目を削除してリスト化-----------------------------------------------------
        for OTItem in OT:
            OTTInput = False
            OTT = (
                OTItem.replace(" ", "")
                .replace("\u3000", "")
                .replace("'", "")
                .replace('"', "")
                .replace("|", "")
                .replace("・", "·")
            )
            for ETItem in ET:
                ETT = (
                    ETItem.replace(" ", "")
                    .replace("\u3000", "")
                    .replace("'", "")
                    .replace('"', "")
                    .replace("|", "")
                    .replace("・", "·")
                )
                if OTT == ETT:
                    OTT = OTT.replace(ETT, "")
                    Final.append(OTT)
                    OTTInput = True
                    break
            if OTTInput is False:
                Final.append(OTT)
        remRow = len(Final) - 1
        for FinalItem in reversed(Final):
            if FinalItem == "":
                Final.pop(remRow)
            remRow = remRow - 1
        # ---------------------------------------------------------------------------------
        print(Final)
        return True, Final
    except:
        return False, ""


# -------------------------------------------------------------------------------------------------------
def DiffListCreate(FolURL, OCRList):
    try:
        for OCRListItem in OCRList:
            try:
                APR = APIRead(FolURL, OCRListItem[1])
                Model = ""
                if APR[0] is True:
                    SiteName = ""
                    FileName = ""
                    for APRItem in APR[1]:
                        # サイト判定--------------------------------------
                        if (
                            "国税電子申告·納税システム(e-Tax)" in APRItem
                            or "国税電子申告納税システム-SU00S240 申告のお知らせ" in APRItem
                        ):
                            SiteName = "eTax"
                        elif "送信されたデータを受け付けました。なお、後日、内容の確認のため、担当職員からご連絡" in APRItem:
                            SiteName = "MJS"
                        # -----------------------------------------------
                        # 税目判定----------------------------------------
                        if SiteName == "eTax":
                            if "第3期分の税額" in APRItem:
                                FileName = "源泉所得税及復興特別所得税2"
                            elif (
                                "所得税及び復興特別所得税" in APRItem
                                and not FileName == "源泉所得税及復興特別所得税2"
                            ):
                                FileName = "源泉所得税及復興特別所得税"
                            elif "課税期間分の中間申告について" in APRItem:
                                FileName = "消費税中間申告用"
                        elif SiteName == "MJS":
                            if "手続名" in APRItem:
                                FileName = "所得税2"
                            elif "第3期分の税額納める税金" in APRItem and not FileName == "所得税2":
                                FileName = "所得税"
                            elif "消費税及び地方消費税の合計(納" in APRItem:
                                if FileName == "所得税2":
                                    FileName = "消費税2"
                                else:
                                    FileName = "消費税"
                        # -----------------------------------------------
                    Model = SiteName + FileName + ".png"  # 雛形のpngを指定
                    EPR = APIRead(SettingDir, Model)  # 雛形をOCR読込
                    ScrList = []  # 最終リスト
                    if EPR[0] is True:
                        DiffList = OCRDiff(APR[1], EPR[1])  # 雛形と重複項目を削除してリスト化
                        DeleteList = Settingtoml["AIOCR"][
                            SiteName + FileName + "削除対象項目"
                        ]  # 重複項目削除リストからの削除対象項目
                        DiffRow = len(DiffList[1]) - 1  # 削除対象項目リストのデータ数
                        # 重複項目削除リストから削除対象項目を削除------------------------
                        for DiffListItem in reversed(DiffList[1]):
                            for DeleteListItem in DeleteList:
                                if DiffListItem == DeleteListItem:
                                    DiffList[1].pop(DiffRow)
                                    break
                            DiffRow = DiffRow - 1
                        # -------------------------------------------------------------
                        tomlList = Settingtoml["AIOCR"][
                            SiteName + FileName
                        ]  # tomlのサイト課目判定一致リスト
                        print(DiffList[1])
                        print(tomlList)
                        # ------------------------------------------------------------
                        DiffRow = 0  # 削除対象項目リストのデータ数
                        # 重複項目削除リストから削除対象項目を削除------------------------
                        for DiffListItem in DiffList[1]:
                            # print(DiffListItem.startswith("自"))
                            # print(DiffListItem.startswith("至"))
                            # OCR取得文字の置換対象を置換--------------------------------
                            DiffPar = DiffListItem
                            if DiffPar.startswith("A"):
                                DiffPar = DiffPar.replace("A", "△")
                            if DiffPar.endswith("A"):
                                DiffPar = DiffPar.replace("A", "円")
                            if DiffPar.endswith("I"):
                                DiffPar = DiffPar.replace("I", "円")
                            # ------------------------------------------------------------
                            if (
                                "課税期間" in tomlList[DiffRow]
                                and DiffListItem.startswith("自") is True
                            ) or (
                                "課税期間" in tomlList[DiffRow]
                                and DiffListItem.startswith("至") is True
                            ):
                                ScrList.append([tomlList[DiffRow], DiffPar])
                            elif "申告区分" in tomlList[DiffRow] and (
                                DiffListItem.startswith("自") is False
                                and DiffListItem.startswith("至") is False
                            ):
                                ScrList.append([tomlList[DiffRow], DiffPar])
                            elif "申告区分" not in tomlList[DiffRow]:
                                ScrList.append([tomlList[DiffRow], DiffPar])
                            else:
                                DiffRow = DiffRow + 1
                                ScrList.append([tomlList[DiffRow], DiffPar])
                            DiffRow = DiffRow + 1
                        print("抽出成功")
                        return True, SiteName + FileName, ScrList
                        # -------------------------------------------------------------
                    else:
                        print("抽出失敗")
                        logger.debug(FolURL + "抽出失敗")
                        return False, "", ""
                else:
                    print("抽出失敗")
                    logger.debug(FolURL + "抽出失敗")
                    return False, "", ""
            except:
                print("ループ内エラー抽出失敗")
                logger.debug(FolURL + "ループ内エラー抽出失敗")
                return False, "", ""
    except:
        print("エラー抽出失敗")
        logger.debug(FolURL + "ループ内エラー抽出失敗")
        return False, "", ""


# -------------------------------------------------------------------------------------------------------
def DiffListPlus(ColN, ScrList):
    NewScrList = []
    ColList = []
    for ScrListItem in ScrList:
        ColList.append(ScrListItem[0])
        NewScrList.append(ScrListItem[1])
    CDict[ColN].append(NewScrList)
    return ColList, CDict[ColN]


# -------------------------------------------------------------------------------------------------------
def DiffListCSVOUT(ListURL, ColN):
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
CSVURL = r"\\Sv05121a\e\電子ファイル\メッセージボックス\TEST2022-3\受信通知CSV\受信通知取得失敗リスト.csv"  # 取得対象のURLが記載されたCSV
SettingDir = os.getcwd() + r"\RPAPhoto\PDFeTaxReadForList\Settingpng"  # 差分検出用のpng保管フォルダ
# --------------------------------------------------------------------------------
try:
    CSVList = FCSV.CsvRead(CSVURL)  # 自作関数でCSVをDataFrameに変換
    CSVRow = np.array(CSVList[1]).shape[0]  # DataFrameの行数
    DLCList = []  # 書出しCSVリスト
    for x in range(CSVRow):  # DataFrameのループ
        try:
            CSVRowData = CSVList[1].iloc[x]  # DataFrameの行データ
            PDFDir = CSVRowData["URL"]  # DataFrameから抽出対象のPDFを取得
            PDFPage = str(int(re.findall(r"\d", CSVRowData["ページ"])[0]) - 1)  # 対象のページを取得
            ModelpngDelte(MyURL)  # PDF変換pngの削除
            PI = pdf_image(PDFDir, MyURL, "png", 200, PDFPage)  # 対象のPDFをpng変換
            if PI[0] is True:  # png変換に成功したら
                OCRList = PI[1]  # PDFから変換したpngを全て取得
                DLC = DiffListCreate(MyURL, OCRList)
                if DLC[0] is True:
                    DLP = DiffListPlus(DLC[1], DLC[2])
                    DLCList.append(DLC[1])
                    # DiffListCSVOUT(MyURL, DLC[1], DLP[0], DLP[1])
        except:
            continue
    DLCDiplicated = list(OrderedDict.fromkeys(DLCList))
    for DItem in DLCDiplicated:
        try:
            DiffListCSVOUT(MyURL, DItem)
        except:
            continue
except:
    print("エラー")
