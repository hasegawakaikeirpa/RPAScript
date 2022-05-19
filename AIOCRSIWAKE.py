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

        # PDFをImage に変換(pdf2imageの関数)
        pages = convert_from_path(pdf_path, dpi, poppler_path=pppath)
        # 画像ファイルを１ページずつ保存
        for i, page in enumerate(pages):
            file_name = "OCR" + str(i) + "." + fmtt
            image_path = image_dir / file_name
            page.save(image_path, fmtt)
            yoko = page.size[0]  # 画像の幅
            tate = page.size[1]  # 画像の高さ
            # 画像が横向きなら縦向きに回転-------------------------------------------
            if yoko > tate:
                img = cv2.imread(image_path._str, 0)
                img_rotate_90_clockwise = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
                cv2.imwrite(image_path._str, img_rotate_90_clockwise)
            # ---------------------------------------------------------------------
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
        for OCRListItem in OCRList:
            try:
                FileURL = OCRListItem[0] + "\\" + OCRListItem[1]
                if "eLTAX受信通知" in PDFDir:
                    Flag = "eltax"
                else:
                    Flag = ""
                GF = GCV.rentxtver(
                    FileURL, 2000, 15, 100, 2000, 15, 500, "::", 10, Flag
                )  # 画像URL,横軸閾値,縦軸閾値,ラベル配置間隔,etax横軸閾値,etax縦軸閾値,etaxラベル配置間隔,ラベル(str),同行として扱う縦間隔
                if GF[0] is True:
                    GFTable = GF[1]
                    GFRow = len(GFTable)
                    GFTColList = []
                    GFTParList = []
                    # OCR結果を整形----------------------------------------------------------------
                    for g in reversed(range(GFRow)):
                        if "::" not in GFTable[g]:  # OCR結果行に区切り文字がない場合
                            if GFTable[g].endswith("円") is True:  # OCR結果行が円で終わる場合
                                if Flag == "eltax":  # eltax処理の場合
                                    Koumoku = GFTable[g]  # 項目を代入
                                    Money = int(re.sub(r"\D", "", GFTable[g]))  # 数値のみ取得
                                    Money = "{:,}".format(Money)  # 取り出した数値をカンマ区切りにする
                                    Money = Money + "円"  # 末尾に円をつける
                                    Koumoku = Koumoku.replace(
                                        Money, ""
                                    )  # 金額と項目名を置換で切り分け
                                    if Koumoku.endswith("-") is True:
                                        GFTable[g] = (
                                            Koumoku.replace("-", "") + "::-" + Money
                                        )  # 区切り文字を挿入
                                    else:
                                        GFTable[g] = Koumoku + "::" + Money  # 区切り文字を挿入
                                    Money = ""
                                    Koumoku = ""
                                else:
                                    GFTable.pop(g)
                            else:
                                GFTable.pop(g)
                    # ----------------------------------------------------------------------------
                    GFTCount = 0
                    for GFTableItem in GFTable:
                        strGF = str(GFTableItem).replace("給額", "総額").replace("稅", "税")
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
# -----------------------------------------------------------
CDict = CSVSet.CSVIndexSortFuncArray  # 外部よりdict変数取得
MyURL = os.getcwd() + r"\RPAPhoto\PDFeTaxReadForList"  # このスクリプトの配下の設定フォルダ
# CSVURL = r"\\Sv05121a\e\電子ファイル\メッセージボックス\TEST2022-3\受信通知CSV\受信通知取得失敗リスト.csv"  # 取得対象のURLが記載されたCSV
CSVURL = r"\\Sv05121a\e\電子ファイル\メッセージボックス\TEST\AIOCRTEST.csv"  # 取得対象のURLが記載されたCSV
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
            ModelpngDelete(MyURL)  # PDF変換pngの削除
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
