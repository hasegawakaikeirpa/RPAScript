import Function.GCloudVision as GCV
import re
import os
from dateutil.parser import parse
import toml
import pandas as pd
import Function.ImageChange as FIC
import Function.CV2Setting as CV2S
import csv
import numpy as np
from difflib import SequenceMatcher


def getNearestValue(list, num):
    """
    概要: リストからある値に最も近い値を返却する関数
    @param list: データ配列
    @param num: 対象値
    @return 対象値に最も近い値
    """

    # リスト要素と対象値の差分を計算し最小値のインデックスを取得
    array = np.asarray(list)
    array = np.asarray(array[:, 0], dtype="float64")
    idx = (np.abs(array - num)).argmin()
    return list[idx]


def DiffListCreate(KCode, PDFDir, PDFPageTxt, Banktoml):
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
        # ####################################################################################
        # COLArray = CV2S.straightlinesetting(FileURL)  # cv2で直線を描き直線軸をリスト化
        # with open(
        #     r"D:\PythonScript\RPAScript\RPAPhoto\PDFeTaxReadForList\StraightListYoko.csv",
        #     "w",
        #     newline="",
        # ) as file:
        #     writer = csv.writer(file)
        #     writer.writerow(COLArray[1])
        # with open(
        #     r"D:\PythonScript\RPAScript\RPAPhoto\PDFeTaxReadForList\StraightListTate.csv",
        #     "w",
        #     newline="",
        # ) as file:
        #     writer = csv.writer(file)
        #     writer.writerow(COLArray[2])
        # ####################################################################################
        # ####################################################################################
        readcsv1 = []
        with open(
            r"D:\PythonScript\RPAScript\RPAPhoto\PDFeTaxReadForList\StraightListYoko.csv",
            "r",
            newline="",
        ) as inputfile:
            for row in csv.reader(inputfile):
                for rowItem in row:
                    rsp = (
                        rowItem.replace("[", "")
                        .replace("]", "")
                        .replace(" ", "")
                        .split(",")
                    )
                    readcsv1.append(
                        [int(rsp[0]), int(rsp[1]), int(rsp[2]), int(rsp[3])]
                    )
        readcsv2 = []
        with open(
            r"D:\PythonScript\RPAScript\RPAPhoto\PDFeTaxReadForList\StraightListTate.csv",
            "r",
            newline="",
        ) as inputfile:
            for row in csv.reader(inputfile):
                for rowItem in row:
                    rsp = (
                        rowItem.replace("[", "")
                        .replace("]", "")
                        .replace(" ", "")
                        .split(",")
                    )
                    readcsv2.append(
                        [int(rsp[0]), int(rsp[1]), int(rsp[2]), int(rsp[3])]
                    )
        COLArray = True, readcsv1, readcsv2
        # ####################################################################################
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
                    if g == 21:
                        print("")
                    for c in Banktoml["HiroginSouzoku"]["MoneyCol"]:
                        strs = ""
                        ints = ""
                        S = GFTable[g][c - 1]
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
                            .replace("|", "")
                            .replace("-", "")
                            .replace("･", "")
                            .replace("!", "")
                        )
                        if len(strs) == 0:
                            GFTable[g][c - 1] = ints
                        elif len(ints) == 0:
                            GFTable[g][c - 1] = strs
                        else:
                            GFTable[g][c - 1] = strs + "::" + ints
                    # tomlから摘要変換リストを読込一致率50％を超えるものがあれば置換-----------------
                    for c in Banktoml["HiroginSouzoku"]["ChangeTextCol"]:
                        strs = ""
                        ints = ""
                        S = GFTable[g][c - 1]
                        for y in range(len(S)):
                            if S[y].isdecimal() is False:
                                strs += S[y]
                            else:
                                ints += S[y]
                        CTCount = []
                        for CT in Banktoml["HiroginSouzoku"]["ChangeText"]:
                            src, trg = strs, CT
                            r = SequenceMatcher(None, src, trg).ratio()
                            CTCount.append([r, CT])
                        GNV = getNearestValue(CTCount, 1.0)
                        if 1.0 - GNV[0] < 0.5:
                            GFTable[g][c - 1] = GNV[1]
                # ----------------------------------------------------------------------------
                # DataFrame作成
                df = pd.DataFrame(
                    GFTable, columns=Banktoml["HiroginSouzoku"]["ColumnName"]
                )
                FileName = (
                    r"D:\PythonScript\RPAScript\RPAPhoto\PDFeTaxReadForList\Kekka.csv"
                )

                # with open(
                #     r"D:\PythonScript\RPAScript\RPAPhoto\PDFeTaxReadForList\XYList.csv",
                #     mode="w",
                #     encoding="shiftjis",
                #     errors="ignore",
                #     newline="",
                # ) as f:
                # pandasでファイルオブジェクトに書き込む
                df.to_csv(FileName, index=False, encoding="cp932")

                print("END")
    except:
        print("ループ内エラー抽出失敗")


# toml読込------------------------------------------------------------------------------
with open(
    os.getcwd() + r"/RPAPhoto/PDFeTaxReadForList/BankSetting.toml", encoding="utf-8"
) as f:
    Banktoml = toml.load(f)
    print(Banktoml)
# -----------------------------------------------------------

FileURL = r"D:\PythonScript\RPAScript\RPAPhoto\PDFeTaxReadForList\OCR0.png"
PDFDir = r"D:\PythonScript\RPAScript\RPAPhoto\PDFeTaxReadForList\OCR0.png"
KCode = "0"
DiffListCreate(KCode, PDFDir, "1", Banktoml)
