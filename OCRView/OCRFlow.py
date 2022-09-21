# import GCloudVision as GCV
from GCloudVision import Bankrentxtver
import os
import toml

# import pandas as pd
from pandas import DataFrame
from csv import reader, QUOTE_NONNUMERIC

# import numpy as np
from numpy import asarray
from difflib import SequenceMatcher
from mojimoji import han_to_zen
import CSVOut as CSVO


def getNearestValue(list, num):
    """
    概要: リストからある値に最も近い値を返却する関数
    @param list: データ配列
    @param num: 対象値
    @return 対象値に最も近い値
    """

    # リスト要素と対象値の差分を計算し最小値のインデックスを取得
    array = asarray(list)
    array = asarray(array[:, 0], dtype="float64")
    idx = (abs(array - num)).argmin()
    return list[idx]


def DiffCheck(GFTable, ColList):
    """
    概要: データフレームの列数にあわせて列名リスト要素数を変更
    @param list: データ配列
    @param num: 対象値
    @return 対象値に最も近い値
    """

    # データフレームの列数にあわせて列名リスト要素数を変更------------------------------
    GC_Diff = len(GFTable[0]) - len(ColList)
    if GC_Diff < 0:
        GC_Diff = GC_Diff * -1
        for GC_d in range(GC_Diff):
            ColList.pop(len(ColList) - 1)
    else:
        for GC_d in range(GC_Diff):
            ColList.append("未設定" + str(GC_d + 1))
    # ----------------------------------------------------------------------------


def DiffListCreate(
    FileURL, Yoko, Tate, Banktoml, ColList, MoneySet, ReplaceSet, ReplaceStr
):
    """
    概要: GoogleVisionApiを実行し、結果をCSV化
    @param FileURL : 画像URL(str)
    @param Yoko : 横軸リスト
    @param Tate : 縦軸リスト
    @param Banktoml : toml設定ファイルURL(str)
    @param ColList : 日付列番号リスト(list)
    @param MoneySet : 金額表示列番号リスト(list)
    @param ReplaceSet : 置換対象列番号のリスト(list)
    @param ReplaceStr : 置換対象文字列のリスト(list)
    @return : bool,CSVURL(str)
    """

    # try:
    dic = {
        "FileURL": FileURL,
        "Yoko": Yoko,
        "Tate": Tate,
        "Banktoml": Banktoml,
        "ColList": ColList,
        "MoneySet": MoneySet,
        "ReplaceSet": ReplaceSet,
        "ReplaceStr": ReplaceStr,
    }
    # ####################################################################################
    readcsv1 = Yoko
    readcsv2 = Tate
    COLArray = True, readcsv1, readcsv2
    # ####################################################################################
    if COLArray[0] is True:
        GF = Bankrentxtver(
            FileURL,
            COLArray[1],
            COLArray[2],
        )  # 画像URL,横軸閾値,縦軸閾値,ラベル配置間隔,etax横軸閾値,etax縦軸閾値,etaxラベル配置間隔,ラベル(str),同行として扱う縦間隔
        if GF[0] is True:
            GFTable = GF[1]
            GFRow = len(GFTable)
            GFCol = len(GFTable[0])
            ChangeTxtList = []
            # OCR結果を整形----------------------------------------------------------------
            for g in range(GFRow):
                if g == 21:
                    print("")
                try:
                    # toml設定の列数以上の列を削除-----------------------------------------------
                    lentoml = len(ColList)
                    lenGT = len(GFTable[g])
                    if lentoml < lenGT:
                        for c in range(lenGT - lentoml):
                            GFTable[g].pop(lenGT + c - 1)
                    # -------------------------------------------------------------------------
                except:
                    print("toml設定の列数以上の列を削除エラー")
                if "," in MoneySet:
                    MoneySet = MoneySet.split(",")
                for c in MoneySet:
                    c = int(c)
                    # 指定列がデータフレーム列数未満なら------------------------------------------
                    if c <= GFCol:
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
                    # -------------------------------------------------------------------------
                # tomlから摘要変換リストを読込一致率50％を超えるものがあれば置換-----------------
                if "," in ReplaceSet:
                    ReplaceSet = ReplaceSet.split(",")
                for c in ReplaceSet:
                    c = int(c)
                    # 指定列がデータフレーム列数未満なら------------------------------------------
                    if c <= GFCol:
                        strs = ""
                        ints = ""
                        S = GFTable[g][c - 1]
                        for y in range(len(S)):
                            if S[y].isdecimal() is False:
                                strs += S[y]
                            else:
                                ints += S[y]
                        CTCount = []
                        if len(ReplaceStr) != 0:
                            if "," in ReplaceStr:
                                ReplaceStr = ReplaceStr.split(",")
                            for CT in ReplaceStr:
                                src, trg = han_to_zen(strs.lower()), han_to_zen(
                                    CT.lower()
                                )
                                r = SequenceMatcher(None, src, trg).ratio()
                                CTCount.append([r, CT])
                            GNV = getNearestValue(CTCount, 1.0)
                            if 1.0 - GNV[0] < 0.5:
                                ChangeTxtList.append([GFTable[g][c - 1], GNV[1]])
                                GFTable[g][c - 1] = GNV[1]

                    # -------------------------------------------------------------------------
            # デコード＆エンコード--------------------------------------------------------------
            # for g in range(GFRow):
            #     for c in range(len(GFTable[g])):
            #         ChangeTxt = GFTable[g][c]
            #         result = ChangeTxt.encode("utf-8")
            #         henkan = result.decode("cp932", errors="ignore")
            #         fukugenhenkan = henkan.encode("cp932")
            #         kekkafukugen = fukugenhenkan.decode("utf-8", errors="ignore")
            #         GFTable[g][c] = kekkafukugen
            # ---------------------------------------------------------------------------------
            # DataFrame作成
            DiffCheck(GFTable, ColList)  # データフレームの列数にあわせて列名リスト要素数を変更
            df = DataFrame(GFTable, columns=ColList)
            FU = FileURL.split("\\")
            FN = FU[len(FU) - 1].replace(".png", ".csv")
            FDir = FileURL.replace(FU[len(FU) - 1], "")
            FileName = FDir + r"\\" + FN
            ChangeTxtUrl = FDir + r"\\OCRChangeList.csv"
            if os.path.isfile(ChangeTxtUrl) is True:
                enc = CSVO.getFileEncoding(ChangeTxtUrl)  # 摘要変換ルールエンコード
            else:
                enc = "cp932"

            # 変換実績リストに要素があれば保存------------------------------------------------
            # if len(ChangeTxtList) > 0:
            #     if os.path.isfile(ChangeTxtUrl) is True:
            #         CTL_df = DataFrame(ChangeTxtList, columns=["OCRテキスト", "元帳テキスト"])
            #         CTL_df.to_csv(
            #             ChangeTxtUrl,
            #             mode="a",
            #             header=False,
            #             index=False,
            #             encoding=enc,
            #         )
            #     else:
            #         CTL_df = DataFrame(ChangeTxtList, columns=["OCRテキスト", "元帳テキスト"])
            #         CTL_df.to_csv(ChangeTxtUrl, index=False, encoding=enc)
            # -------------------------------------------------------------------------------
            if os.path.isfile(FileName) is True:
                enc = CSVO.getFileEncoding(FileName)  # 摘要変換ルールエンコード
            else:
                enc = "cp932"
            try:
                df.to_csv(FileName, index=False, encoding=enc, quoting=QUOTE_NONNUMERIC)
            except:
                with open(
                    FileName,
                    mode="w",
                    encoding="cp932",
                    errors="ignore",
                    newline="",
                ) as f:
                    df.to_csv(f, index=False, quoting=QUOTE_NONNUMERIC)
                # df.to_csv(FileName, index=False, encoding="utf8")
            print("END")
            return True, FileName
    # except:
    #     print("ループ内エラー抽出失敗")
    #     return False, ""


def Main(FileURL, Yoko, Tate, Banktoml, ColList, MoneySet, ReplaceSet, ReplaceStr):
    """
    概要: 呼出関数
    @param FileURL : 画像URL(str)
    @param Yoko : 横軸リスト
    @param Tate : 縦軸リスト
    @param Banktoml : toml設定ファイルURL(str)
    @param ColList : 日付列番号リスト(list)
    @param MoneySet : 金額表示列番号リスト(list)
    @param ReplaceSet : 置換対象列番号のリスト(list)
    @param ReplaceStr : 置換対象文字列のリスト(list)
    @return : bool,CSVURL(str)
    """
    # # toml読込------------------------------------------------------------------------------
    # with open(os.getcwd() + r"/TKInterGUI/BankSetting.toml", encoding="utf-8") as f:
    #     Banktoml = toml.load(f)
    #     print(Banktoml)
    # # -----------------------------------------------------------
    DLC = DiffListCreate(
        FileURL, Yoko, Tate, Banktoml, ColList, MoneySet, ReplaceSet, ReplaceStr
    )
    if DLC[0] is True:
        return DLC
    else:
        return False, ""


if __name__ == "__main__":
    # toml読込------------------------------------------------------------------------------
    with open(os.getcwd() + r"/TKInterGUI/BankSetting.toml", encoding="utf-8") as f:
        Banktoml = toml.load(f)
        print(Banktoml)
    # -----------------------------------------------------------
    URL = os.getcwd()
    readcsv1 = []
    with open(
        URL + r"\TKInterGUI\StraightListYoko.csv",
        "r",
        newline="",
    ) as inputfile:
        for row in reader(inputfile):
            for rowItem in row:
                rsp = (
                    rowItem.replace("[", "")
                    .replace("]", "")
                    .replace(" ", "")
                    .split(",")
                )
                readcsv1.append([int(rsp[0]), int(rsp[1]), int(rsp[2]), int(rsp[3])])
    readcsv2 = []
    with open(
        URL + r"\TKInterGUI\StraightListTate.csv",
        "r",
        newline="",
    ) as inputfile:
        for row in reader(inputfile):
            for rowItem in row:
                rsp = (
                    rowItem.replace("[", "")
                    .replace("]", "")
                    .replace(" ", "")
                    .split(",")
                )
                readcsv2.append([int(rsp[0]), int(rsp[1]), int(rsp[2]), int(rsp[3])])
    for fd_path, sb_folder, sb_file in os.walk(r"D:\Souzoku_JAPng"):
        si = 0
        for sb_fileItem in sb_file:
            if si >= 14:
                imgurl = fd_path + "\\" + sb_fileItem
                DiffListCreate(imgurl, readcsv1, readcsv2, Banktoml, "JASouzoku")
            si += 1
