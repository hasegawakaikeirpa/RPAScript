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
import Function.ImageChange as FIC
import Function.CV2Setting as CV2S
import csv
import pandas as pd

# logger設定------------------------------------------------------------------------------
import logging.config

logging.config.fileConfig(r"LogConf\logging_debug.conf")
logger = logging.getLogger(__name__)
# -------------------------------------------------------------------------------------------------------
def ModelpngDelete(FolURL):
    """
    概要: PDF変換後のpngの削除
    @param FolURL : このpyファイルのフォルダ(str)
    @return : なし
    """
    try:
        for fd_path, sb_folder, sb_file in os.walk(FolURL):
            for fil in sb_file:
                if "OCR" in fil and fil.endswith(".png") is True:
                    os.remove(fd_path + "\\" + fil)
    except:
        print("OCR画像ファイル削除エラー")


# -------------------------------------------------------------------------------------------------------
def pdf_image(pdf_file, img_path, fmtt, dpi, PDFPage):
    """
    概要: popplerでPDFを指定した画像形式に変換
    @param pdf_file : PDFURL(str)
    @param img_path : 画像フォルダURL(str)
    @param fmtt : 変換後の画像形式(str)
    @param dpi : 変換する際の解像度(int)
    @param PDFPage : 変換するPDFのページ番号(str)
    @return : bool
    @return : 変換後画像URLのリスト(list)
    """
    try:
        OCRList = []
        Mydir = os.getcwd()
        pppath = Mydir + r"\poppler-22.01.0\Library\bin"
        # pdf_file、img_pathをPathにする
        pdf_path = Path(pdf_file)
        image_dir = Path(img_path)
        # 線形検出パラメータ設定########################################
        disth = 1.41421356
        canth1 = 50.0
        canth2 = 50.0
        casize = 3
        do = True
        # ############################################################
        # PDFをImage に変換(pdf2imageの関数)
        pages = convert_from_path(pdf_path, dpi, poppler_path=pppath)
        # 画像ファイルを１ページずつ保存
        for i, page in enumerate(pages):
            file_name = "OCR" + str(i) + "." + fmtt
            image_path = image_dir / file_name
            # page.save(image_path, fmtt)
            # 画像が横向きなら縦向きに回転-------------------------------------------
            # if yoko > tate:
            #     img = cv2.imread(image_path._str, 0)
            #     img_rotate_90_clockwise = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
            #     cv2.imwrite(image_path._str, img_rotate_90_clockwise)
            # ---------------------------------------------------------------------
            # FIC.OCRIMGChange(
            #     img_path, image_path._str, disth, canth1, canth2, casize, do
            # )
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
def DiffListCreate(FileURL, KCode, PDFDir, PDFPageTxt, Banktoml):
    """
    概要: GoogleApiで取得した内容を整形
    @param FolURL : このpyファイルのフォルダ(str)
    @param OCRList : 画像フォルダURL(str)
    @param KCode : 受信通知取得失敗リストから取得した関与先コード(str)
    @param PDFDir : 受信通知取得失敗リストから取得したPDFURL(str)
    @param PDFPageTxt : 受信通知取得失敗リストから取得したPDFのページ番号(str)
    @return : bool
    @return : 変換後画像から取得して抽出したカラムリスト(list)
    @return : 変換後画像から取得して抽出した値のリスト(list)
    """
    try:
        COLArray = CV2S.straightlinesetting(FileURL)  # cv2で直線を描き直線軸をリスト化
        with open(
            r"D:\PythonScript\RPAScript\RPAPhoto\PDFeTaxReadForList\StraightListYoko.csv",
            "w",
            newline="",
        ) as file:
            writer = csv.writer(file)
            writer.writerow(COLArray[1])
        with open(
            r"D:\PythonScript\RPAScript\RPAPhoto\PDFeTaxReadForList\StraightListTate.csv",
            "w",
            newline="",
        ) as file:
            writer = csv.writer(file)
            writer.writerow(COLArray[2])

        # COLArray = True, Banktoml["TESTYOKO"]["Y"], Banktoml["TESTTATE"]["T"]
        if COLArray[0] is True:
            GF = GCV.Bankrentxtver(
                FileURL,
                COLArray[1],
                COLArray[2],
            )  # 画像URL,横軸閾値,縦軸閾値,ラベル配置間隔,etax横軸閾値,etax縦軸閾値,etaxラベル配置間隔,ラベル(str),同行として扱う縦間隔
            if GF[0] is True:
                GFTable = GF[1]
                GFRow = len(GFTable)
                # OCR結果を整形----------------------------------------------------------------
                for g in range(GFRow):
                    for c in Banktoml["Momiji"]["MoneyCol"]:
                        strs = ""
                        ints = ""
                        try:
                            S = GFTable[g][c - 1]
                            if len(S) > 0:
                                for y in range(len(S)):
                                    if S[y].isdecimal() is False:
                                        strs += S[y]
                                    else:
                                        ints += S[y]
                                strs = (
                                    strs.replace(",", "")
                                    .replace("*", "")
                                    .replace("'", "")
                                    .replace(",", "")
                                    .replace("○", "")
                                    .replace("×", "")
                                    .replace("✓", "")
                                    .replace("¥", "")
                                    .replace("´", "")
                                    .replace("=", "")
                                    .replace("串", "")
                                    .replace("第", "")
                                    .replace("$", "")
                                    .replace("〒", "")
                                    .replace(".", "")
                                    .replace('"', "")
                                    .replace("(", "")
                                    .replace(")", "")
                                    .replace("#", "")
                                    .replace("-", "")
                                    .replace(":", "")
                                )
                                if len(strs) == 0:
                                    GFTable[g][c - 1] = ints
                                elif len(ints) == 0:
                                    GFTable[g][c - 1] = strs
                                else:
                                    GFTable[g][c - 1] = strs + "::" + ints
                        except:
                            print("Nodata")
                # ----------------------------------------------------------------------------
                # DataFrame作成
                df = pd.DataFrame(GFTable, columns=Banktoml["Momiji"]["ColumnName"])
                FName = str(KCode) + "_TEST.csv"
                df.to_csv(FName, index=False, encoding="cp932")
                print("END")
    except:
        print("ループ内エラー抽出失敗")


# -------------------------------------------------------------------------------------------------------
def DiffListPlus(ColList, ScrList):
    """
    概要: 取得した情報を各リストに格納
    @param ColList: PDFから取得したヘッダー情報(list)
    @param ScrList: PDFから取得した情報(list)
    @return bool
    @return 代入したリスト名(str)
    """
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
    """
    概要: CSV書出し
    @param ListURL: CSVファイル保存フォルダ(str)
    @param ColN: 格納したlist変数名(str)
    @return なし
    """
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
# toml読込------------------------------------------------------------------------------
with open(
    os.getcwd() + r"/RPAPhoto/PDFeTaxReadForList/BankSetting.toml", encoding="utf-8"
) as f:
    Banktoml = toml.load(f)
    print(Banktoml)
# ---------------------------------------------------------------------------------------
CDict = CSVSet.CSVIndexSortFuncArray  # 外部よりdict変数取得
MyURL = os.getcwd() + r"\RPAPhoto\PDFeTaxReadForList"  # このスクリプトの配下の設定フォルダ
# CSVURL = r"\\Sv05121a\e\電子ファイル\メッセージボックス\TEST2022-3\受信通知CSV\受信通知取得失敗リスト.csv"  # 取得対象のURLが記載されたCSV
CSVURL = r"D:\PythonScript\RPAScript\RPAPhoto\PDFeTaxReadForList\AIOCRTEST.csv"  # 取得対象のURLが記載されたCSV
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
            # ModelpngDelete(MyURL)  # PDF変換pngの削除
            PI = pdf_image(PDFDir, MyURL, "png", 500, PDFPage)  # 対象のPDFをpng変換
            if PI[0] is True:  # png変換に成功したら
                OCRList = PI[1]  # PDFから変換したpngを全て取得
                FileURL = str(OCRList[0][0]) + r"\\" + str(OCRList[0][1])
                DLC = DiffListCreate(
                    FileURL, KCode, PDFDir, PDFPageTxt, Banktoml
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
