# import GCloudVision as GCV
from GCloudVision import Bankrentxtver
import os
import toml

# import pandas as pd
from pandas import DataFrame, read_csv, concat
from csv import reader, QUOTE_NONNUMERIC

# import numpy as np
from numpy import asarray, array
from difflib import SequenceMatcher
from mojimoji import han_to_zen
import CSVOut as CSVO

# ----------------------------------------------------------------------------
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


# ----------------------------------------------------------------------------
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
def JoinCSV(CSVList):
    """
    概要: 引数リストのURLから連結CSVを作成
    @param CSVList: CSVURLリスト
    @return 連結CSVURL
    """
    try:
        r = 0
        CSVList = set(CSVList)
        for CSVListItem in CSVList:
            enc = CSVO.getFileEncoding(CSVListItem)  # 摘要変換ルールエンコード
            if r == 0:
                m_csv = read_csv(CSVListItem, encoding=enc)
                F_File = CSVListItem.split(".")[0] + "_merge" + ".csv"
                os.remove(CSVListItem)
                G_logger.debug(CSVListItem + "_先頭ページ連結完了")  # Log出力
            else:
                r_csv = read_csv(CSVListItem, encoding=enc)
                os.remove(CSVListItem)
                G_logger.debug(CSVListItem + "_" + str(r) + "ページ連結完了")  # Log出力
                m_csv = concat([m_csv, r_csv])
            r += 1
        try:
            G_logger.debug("ページ連結後dfto_csv開始")  # Log出力
            m_csv.to_csv(F_File, index=False, encoding=enc, quoting=QUOTE_NONNUMERIC)
        except:
            G_logger.debug("GoogleAPI後dfto_csvエラー後開始")  # Log出力
            with open(
                F_File,
                mode="w",
                encoding="cp932",
                errors="ignore",
                newline="",
            ) as f:
                m_csv.to_csv(f, index=False, quoting=QUOTE_NONNUMERIC)
        G_logger.debug("GoogleAPI後csv処理完了")  # Log出力
        return True, F_File
    except:
        G_logger.debug("GoogleAPI後csv処理失敗")  # Log出力
        return False, ""


# ----------------------------------------------------------------------------
def DayCheck(GFTable, DaySet):
    """
    概要: 設定日付列番号に応じて日付書式変換
    @param GFTable: データ配列
    @param DaySet: 設定日付列番号
    """

    # 設定日付列番号に応じて日付書式変換------------------------------
    DS = int(DaySet[0]) - 1
    G_list = array(GFTable)[:, DS]


# ----------------------------------------------------------------------------
def DiffListCreate(
    FileURL,
    Yoko,
    Tate,
    Banktoml,
    ColList,
    DaySet,
    MoneySet,
    ReplaceSet,
    ReplaceStr,
    PBAR,
    ChangeVar,
):
    """
    概要: GoogleVisionApiを実行し、結果をCSV化
    @param FileURL : 画像URL(str)
    @param Yoko : 横軸リスト
    @param Tate : 縦軸リスト
    @param Banktoml : toml設定ファイルURL(str)
    @param ColList : 列名リスト(list)
    @param DaySet : 日付列番号リスト(list)
    @param MoneySet : 金額表示列番号リスト(list)
    @param ReplaceSet : 置換対象列番号のリスト(list)
    @param ReplaceStr : 置換対象文字列のリスト(list)
    @return : bool,CSVURL(str)
    """

    # try:
    # dic = {
    #     "FileURL": FileURL,
    #     "Yoko": Yoko,
    #     "Tate": Tate,
    #     "Banktoml": Banktoml,
    #     "ColList": ColList,
    #     "MoneySet": MoneySet,
    #     "ReplaceSet": ReplaceSet,
    #     "ReplaceStr": ReplaceStr,
    # }
    # ####################################################################################
    readcsv1 = Yoko
    readcsv2 = Tate
    COLArray = True, readcsv1, readcsv2
    # ####################################################################################
    if COLArray[0] is True:
        G_logger.debug("Bankrentxtver起動")  # Log出力

        GF = Bankrentxtver(
            FileURL,
            COLArray[1],
            COLArray[2],
        )  # 画像URL,横軸閾値,縦軸閾値,ラベル配置間隔,etax横軸閾値,etax縦軸閾値,etaxラベル配置間隔,ラベル(str),同行として扱う縦間隔
        G_logger.debug("Bankrentxtver完了")  # Log出力
        PBAR._target.step(20)
        print(GF[0])
        if GF[0] is True:
            GFTable = GF[1]
            # 設定日付列番号に応じて日付書式変換------------------------------
            DayCheck(GFTable, DaySet)
            # --------------------------------------------------------------
            GFRow = len(GFTable)
            GFCol = len(GFTable[0])
            ChangeTxtList = []
            PB_v = int(90 / GFRow)
            # OCR結果を整形----------------------------------------------------------------
            for g in range(GFRow):
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
                        # else:
                        #     GFTable[g][c - 1] = strs + "::" + ints
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
                            R_par = ChangeVar / 100
                            if 1.0 - GNV[0] < R_par:
                                ChangeTxtList.append([GFTable[g][c - 1], GNV[1]])
                                GFTable[g][c - 1] = GNV[1]
                PBAR._target.step(PB_v)
                # -------------------------------------------------------------------------
            # 入出金列の数値以外を分別------------------------------------------------------
            Replist = [
                ",",
                "*",
                "'",
                "○",
                "×",
                "✓",
                "¥",
                "´",
                "=",
                "串",
                "第",
                "$",
                "〒",
                ".",
                "|",
                "-",
                "･",
                "!",
                ":",
            ]
            strsList = []
            # Check = [True for i in Replist if strs == i]
            for g in range(GFRow):
                strs = ""
                for c in MoneySet:
                    ints = ""
                    c = int(c)
                    S = GFTable[g][c - 1]
                    for y in range(len(S)):
                        if S[y].isdecimal() is False:
                            strs += S[y]
                        else:
                            ints += S[y]
                    if strs == "":
                        if c == int(MoneySet[len(MoneySet) - 1]):
                            strsList.append("")
                    elif ints != "":
                        Check = [True if strs == i else False for i in Replist]
                        if True not in Check:
                            GFTable[g][c - 1] = ints
                        if c == int(MoneySet[len(MoneySet) - 1]) and strs != "":
                            if True not in Check:
                                strsList.append(strs)
                            else:
                                strsList.append("")
                        else:
                            GFTable[g][c - 1] = ints
                    else:
                        GFTable[g][c - 1] = ""
                        if c == int(MoneySet[len(MoneySet) - 1]) and strs != "":
                            strsList.append(strs)
                # -------------------------------------------------------------------------
            # 入出金列の数値以外を分別------------------------------------------------------
            # intsList = []
            # for g in range(GFRow):
            #     intsList_r = []
            #     for c in MoneySet:
            #         ints = ""
            #         c = int(c)
            #         S = GFTable[g][c - 1]
            #         if S == "":
            #             intsList_r.append(0)
            #         else:
            #             Check = [True if i in S else False for i in Replist]
            #             if True not in Check:
            #                 intsList_r.append(int(S))
            #             else:
            #                 try:
            #                     intsList_r.append(int(S))
            #                 except:
            #                     intsList_r.append(0)
            #     if len(intsList_r) == 1:
            #         intsList_r[g] = ""
            #     else:
            #         Min_S = min(intsList_r)
            #         Min_S_c = [i for i, x in enumerate(intsList_r) if x == Min_S]
            #         Min_S_c = int(MoneySet[int(Min_S_c[0])]) - 1
            #         if True not in Check:
            #             GFTable[g][Min_S_c] = ""
            #         else:
            #             GFTable[g][Min_S_c] = S
            #         if Min_S == 0:
            #             if True not in Check:
            #                 intsList.append("")
            #             else:
            #                 intsList.append(S)
            #         else:
            #             intsList.append(str(Min_S))
            # -------------------------------------------------------------------------
            # -----------------------------------------------------------------------------
            G_logger.debug("GoogleAPI後編集処理完了")  # Log出力
            # DataFrame作成
            # 分割文字列リストを結合---------------------------------------------------------
            if len(strsList) == 0:
                df = DataFrame(GFTable, columns=ColList)
                DiffCheck(df, ColList)  # データフレームの列数にあわせて列名リスト要素数を変更
            else:
                DF_strsList = DataFrame(strsList, columns=["抽出文字列"])
                # DF_intsList = DataFrame(intsList, columns=["抽出数値"])
                GFTable = DataFrame(GFTable)
                GFTable = concat([GFTable, DF_strsList], axis=1)
                # GFTable = concat([GFTable, DF_intsList], axis=1)
                ColList.append("抽出文字列")
                # ColList.append("抽出数値")
                GFTable.columns = ColList
                df = GFTable
            # -----------------------------------------------------------------------------
            FU = FileURL.split("\\")
            FN = FU[len(FU) - 1].replace(".png", ".csv")
            FDir = FileURL.replace(FU[len(FU) - 1], "")
            FileName = FDir + r"\\" + FN
            ChangeTxtUrl = FDir + r"\\OCRChangeList.csv"
            if os.path.isfile(ChangeTxtUrl) is True:
                enc = CSVO.getFileEncoding(ChangeTxtUrl)  # 摘要変換ルールエンコード
            else:
                enc = "cp932"
            if os.path.isfile(FileName) is True:
                enc = CSVO.getFileEncoding(FileName)  # 摘要変換ルールエンコード
            else:
                enc = "cp932"
            try:
                G_logger.debug("GoogleAPI後dfto_csv開始")  # Log出力
                df.to_csv(FileName, index=False, encoding=enc, quoting=QUOTE_NONNUMERIC)
            except:
                G_logger.debug("GoogleAPI後dfto_csvエラー後開始")  # Log出力
                with open(
                    FileName,
                    mode="w",
                    encoding="cp932",
                    errors="ignore",
                    newline="",
                ) as f:
                    df.to_csv(f, index=False, quoting=QUOTE_NONNUMERIC)
                # df.to_csv(FileName, index=False, encoding="utf8")
            G_logger.debug("GoogleAPI後csv処理完了")  # Log出力
            return True, FileName
    # except:
    #     print("ループ内エラー抽出失敗")
    #     return False, ""


def Main(
    FileURL,
    Yoko,
    Tate,
    Banktoml,
    ColList,
    DaySet,
    MoneySet,
    ReplaceSet,
    ReplaceStr,
    logger,
    PBAR,
    ChangeVar,
):
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
    global G_logger

    G_logger = logger
    # # toml読込------------------------------------------------------------------------------
    # with open(os.getcwd() + r"/TKInterGUI/BankSetting.toml", encoding="utf-8") as f:
    #     Banktoml = toml.load(f)
    #     print(Banktoml)
    # # -----------------------------------------------------------
    DLC = DiffListCreate(
        FileURL,
        Yoko,
        Tate,
        Banktoml,
        ColList,
        DaySet,
        MoneySet,
        ReplaceSet,
        ReplaceStr,
        PBAR,
        ChangeVar,
    )
    if DLC[0] is True:
        return DLC
    else:
        return False, ""


if __name__ == "__main__":
    # toml読込------------------------------------------------------------------------------
    with open(os.getcwd() + r"/BankSetting.toml", encoding="utf-8") as f:
        Banktoml = toml.load(f)
        print(Banktoml)
    # -----------------------------------------------------------
    URL = os.getcwd()
    readcsv1 = []
    with open(
        URL + r"\StraightListYoko.csv",
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
        URL + r"\StraightListTate.csv",
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
