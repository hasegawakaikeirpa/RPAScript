import numpy as np
from datetime import datetime as dt
import WarekiHenkan as wh

# from datetime import timedelta

from tkinter import messagebox

import os

import toml

# ----------------------------------------------------------------------------
def nearestList(data, value):
    """
    引数Listを近似値で並び替え
    data:List
    value:int
    return bool,List
    """
    try:
        indicesArr = []
        for i in reversed(range(len(data))):
            # リスト要素と対象値の差分を計算し最小値のインデックスを取得
            nar = np.array(data)
            lis = np.array(nar[:, 1])  # 金額Listを整数に
            lis = list(lis)  # 金額をListに
            idx = np.argmin(np.abs(np.array(lis) - value))
            print(data[idx])
            indicesArr.append(data[idx])
            data.pop(idx)
        return True, indicesArr
    except:
        return False, ""


# ----------------------------------------------------------------------------
def ColumCheck(MJS_data, cstr):
    """
    引数列名から列番号を調べる
    MJS_data:Numpy配列
    cstr:検索列名
    return bool,index
    """
    try:
        index = np.where(MJS_data == cstr)
        print(index[0])
        if index[0].size == 0:
            return False, ""
        else:
            return True, index
    except:
        return False, ""


# ----------------------------------------------------------------------------
def TextCheck(MJS_data, Txt, stALL):
    """
    テキストから曖昧一致抽出
    MJS_data:Numpy配列
    Txt:検索テキスト
    return bool,np.array(一致率表)
    """
    try:
        M_r = MJS_data.shape[0]  # 行数
        lTxt = len(Txt)  # 文字数
        InTotalList = []  # 完成リスト
        for r in range(M_r):
            if r != 0:
                M_Txt = MJS_data[r][0]  # 検索対象の文字列
                NoList = []  # インデックス格納用リスト
                InList = []  # 一致パラメータ格納リスト
                NoList.append(r)  # 現在のインデックスを格納
                # 検索文字列を一文字ずつ対象に含まれるかチェック--------------------
                for T in range(lTxt):  # 現在のインデックスを格納
                    if Txt[T] in M_Txt:
                        InList.append(1)  # 含まれる場合
                    else:
                        InList.append(0)  # 含まれない場合
                # ---------------------------------------------------------------
                if sum(InList) != 0:  # 一致パラメータ合計値が0以外なら
                    InList.append(
                        round((sum(InList) / len(InList)) * 100, 1)
                    )  # 一致率を計算し格納
                    NoList.extend(InList)  # インデックス格納と一致パラメータ格納リストを結合
                    InTotalList.append(NoList)  # 完成リストに格納
        InTotalList = np.array(InTotalList)  # np配列に変換
        index = np.argsort(InTotalList[:, InTotalList.shape[1] - 1])[
            ::-1
        ]  # np配列を一致率降順ソート
        InTotalList = InTotalList[index]  # 変数格納
        InTotalList = InTotalList[
            :, 0 : InTotalList.shape[1] : InTotalList.shape[1] - 1
        ]
        print(InTotalList)
        return True, InTotalList
    except:
        if stALL != "ALL":
            MB = messagebox.askquestion(
                "確認",
                "摘要項目あいまい一致での自動仕訳抽出結果がありません。直前の結果を表示しますか？",
                icon="warning",
            )
            if MB == "yes":  # If関数
                return MB, MJS_data
            else:
                return False, ""
        else:
            return False, ""


# ----------------------------------------------------------------------------
def TextDateCheck(MJS_data, Txt, stALL):
    """
    テキストから曖昧一致抽出
    MJS_data:Numpy配列
    Txt:検索テキスト
    return bool,np.array(一致率表)
    """
    try:
        D_Txt = ""
        M_Txt = ""
        D_Txt = ChangeD_Txt(Txt)  # 日付西暦和暦変換
        if D_Txt[0] is True:
            D_Txt = D_Txt[1]
            M_r = MJS_data.shape[0]  # 行数
            InTotalList = []  # 完成リスト
            # NoList = []  # インデックス格納用リスト
            InList = []  # 一致パラメータ格納リスト
            for r in range(M_r):
                if r != 0:
                    M_Txt = MJS_data[r][0]  # 検索対象の文字列
                    M_Txt = ChangeD_Txt(M_Txt)  # 日付西暦和暦変換
                    if M_Txt[0] is True:
                        M_Txt = M_Txt[1]
                        # NoList.append(r)  # 現在のインデックスを格納
                        # 日付差を計算--------------------
                        print(type(D_Txt))
                        if type(D_Txt) != dt:
                            D_Txt = dt.strptime(D_Txt, "%Y/%m/%d")
                        if type(M_Txt) != dt:
                            M_Txt = dt.strptime(M_Txt, "%Y/%m/%d")
                        M_s = (
                            str(D_Txt.year)
                            + "/"
                            + str(M_Txt.month)
                            + "/"
                            + str(M_Txt.day)
                        )
                        M_s = dt.strptime(M_s, "%Y/%m/%d")
                        D_M_Diff = (D_Txt - M_s).days
                        print(D_M_Diff)
                        # ---------------------------------------------------------------
                        InList.append([r, D_M_Diff])  # 一致率を計算し格納
            # NoList.extend([InList])  # インデックス格納と一致パラメータ格納リストを結合
            # InTotalList.append(NoList)  # 完成リストに格納
            InTotalList = np.array(InList)  # np配列に変換
            index = np.argsort(
                InTotalList[:, InTotalList.shape[1] - 1]
            )  # np配列を一致率昇順ソート
            InTotalList = InTotalList[index]  # 変数格納
            InTotalList = InTotalList[
                :, 0 : InTotalList.shape[1] : InTotalList.shape[1] - 1
            ]
            print(InTotalList)
            return True, InTotalList
    except:
        if stALL != "ALL":
            MB = messagebox.askquestion(
                "確認",
                "日付あいまい一致での自動仕訳抽出結果がありません。直前の結果を表示しますか？",
                icon="warning",
            )
            if MB == "yes":  # If関数
                return MB, MJS_data
            else:
                return False, ""
        else:
            return False, ""


# ----------------------------------------------------------------------------
def ChangeD_Txt(Txt):
    """
    日付西暦和暦変換
    """
    try:
        # 日付文字列の変換-----------------------------------------------------
        if "-" in Txt:
            TxtSP = Txt.split("-")
            T_Nen = len(TxtSP[0])
            if T_Nen <= 2:
                print("和暦")
                D_str = (
                    "令和"
                    + str(TxtSP[0])
                    + "年"
                    + str(TxtSP[1])
                    + "月"
                    + str(TxtSP[2])
                    + "日"
                )
                D_str = wh.SeirekiSTRDate(D_str)
            elif T_Nen <= 4:
                print("西暦")
                D_str = TxtSP[0] + "/" + TxtSP[1] + "/" + TxtSP[2]
            else:
                print("西暦")
        elif "/" in Txt:
            TxtSP = Txt.split("/")
            T_Nen = len(TxtSP[0])
            if T_Nen <= 2:
                print("和暦")
                D_str = (
                    "令和"
                    + str(TxtSP[0])
                    + "年"
                    + str(TxtSP[1])
                    + "月"
                    + str(TxtSP[2])
                    + "日"
                )
                D_str = wh.SeirekiSTRDate(D_str)
            elif T_Nen <= 4:
                print("西暦")
                D_str = TxtSP[0] + "/" + TxtSP[1] + "/" + TxtSP[2]
            else:
                print("西暦")
        elif "_" in Txt:
            TxtSP = Txt.split("_")
            T_Nen = len(TxtSP[0])
            if T_Nen <= 2:
                print("和暦")
                D_str = (
                    "令和"
                    + str(TxtSP[0])
                    + "年"
                    + str(TxtSP[1])
                    + "月"
                    + str(TxtSP[2])
                    + "日"
                )
                D_str = wh.SeirekiSTRDate(D_str)
            elif T_Nen <= 4:
                print("西暦")
                D_str = TxtSP[0] + "/" + TxtSP[1] + "/" + TxtSP[2]
            else:
                print("西暦")
        elif "." in Txt:
            TxtSP = Txt.split(".")
            T_Nen = len(TxtSP[0])
            if T_Nen <= 2:
                print("和暦")
                D_str = (
                    "令和"
                    + str(TxtSP[0])
                    + "年"
                    + str(TxtSP[1])
                    + "月"
                    + str(TxtSP[2])
                    + "日"
                )
                D_str = wh.SeirekiSTRDate(D_str)
            elif T_Nen <= 4:
                print("西暦")
                D_str = TxtSP[0] + "/" + TxtSP[1] + "/" + TxtSP[2]
            else:
                print("西暦")
        return True, D_str
    except:
        return False, ""


# ---------------------------------------------------------------------


def IntCheck(MJS_data, Int):
    """
    テキストから曖昧一致抽出
    MJS_data:Numpy配列
    Txt:検索テキスト
    return bool,np.array(一致率表)
    """
    try:
        Int = int(Int)
        M_r = MJS_data.shape[0]  # 行数
        InTotalList = []  # 完成リスト
        NoList = []  # インデックス格納用リスト
        for r in range(M_r):
            if r != 0:
                # M_s = MJS_data[r].shape[0] - 1
                M_Txt = MJS_data[r]  # [M_s]  # 検索対象の文字列
                try:
                    NoList.append([r, Int - int(M_Txt)])  # 含まれる場合
                except:
                    NoList.append([r, 999999999])  # 含まれる場合
            # ---------------------------------------------------------------
        InTotalList.append(NoList)  # 完成リストに格納
        nl = nearestList(NoList, 0)
        if nl[0] is True:
            return True, nl[1]
    except:
        return False, ""


# ----------------------------------------------------------------------------
def npCreate(MJS_data, Txt, ColTxt, stALL):
    """
    引数1データの引数3列に引数2の文字が何%含まれるかを計算し、
    np.arrayで返す
    """
    try:
        MJS_Column = MJS_data[0, :]
        int(ColTxt)
        TC = TextCheck(MJS_data[:, int(ColTxt)], Txt, stALL)  # 検索文字列から一致率リストを作成
        if TC[0] is True:
            TCL = np.floor(TC[1][:, 0]).astype(int)  # インデックスを丸めて整数に
            Pac = TC[1][:, 1]  # 一致率列のみ取り出す
            Pac = Pac.reshape(Pac.shape[0], -1)  # 一致率リストを多次元に変換
            Pac = Pac.astype(int)
            MJS_Column = MJS_Column.reshape(-1, MJS_Column.shape[0])  # 列名リストを多次元に変換
            MJS_Column = np.insert(MJS_Column, MJS_Column.shape[1], "", axis=1)
            index = list(TCL)  # 丸めたインデックスnparrayをリストに
            MJS_data = MJS_data[index, :]  # インデックス一致のリスト作成
            MJS_data = np.hstack((MJS_data, Pac))  # 一致率リストを横連結
            MJS_Column[0][MJS_Column.shape[1] - 1] = "一致率"
            MJS_data = np.vstack((MJS_Column, MJS_data))  # 列名リストを縦連結
            print(MJS_data)
            return True, MJS_data
        elif TC[0] == "yes" and stALL != "ALL":
            return True, MJS_data
        else:
            return False, MJS_data
    except:
        try:
            CC = ColumCheck(MJS_data, ColTxt)  # 元帳CSVから列名番号を検出
            if CC[0] is True:
                TC = TextCheck(MJS_data[:, CC[1][1]], Txt, stALL)  # 検索文字列から一致率リストを作成
                if TC[0] is True:
                    TCL = np.floor(TC[1][:, 0]).astype(int)  # インデックスを丸めて整数に
                    Pac = TC[1][:, 1]  # 一致率列のみ取り出す
                    Pac = Pac.reshape(Pac.shape[0], -1)  # 一致率リストを多次元に変換
                    Pac = Pac.astype(int)
                    MJS_Column = MJS_Column.reshape(
                        -1, MJS_Column.shape[0]
                    )  # 列名リストを多次元に変換
                    MJS_Column = np.insert(MJS_Column, MJS_Column.shape[1], "", axis=1)
                    index = list(TCL)  # 丸めたインデックスnparrayをリストに
                    MJS_data = MJS_data[index, :]  # インデックス一致のリスト作成
                    MJS_data = np.hstack((MJS_data, Pac))  # 一致率リストを横連結
                    MJS_Column[0][MJS_Column.shape[1] - 1] = "一致率"
                    MJS_data = np.vstack((MJS_Column, MJS_data))  # 列名リストを縦連結
                    print(MJS_data)
                    return True, MJS_data
                elif TC[0] == "yes" and stALL != "ALL":
                    return True, MJS_data
                else:
                    return False, MJS_data
            else:
                return False, MJS_data
        except:
            print("npCreate下処理エラー")
            return False, MJS_data


# ----------------------------------------------------------------------------
def DayCheck(MJS_data, Txt, ColTxt, stALL):
    """
    引数1データの引数3列の日付データから
    引数2の日付間の日数を計算しnp.arrayで返す
    """
    try:
        MJS_Column = MJS_data[0, :]
        int(ColTxt)
        TC = TextDateCheck(MJS_data[:, int(ColTxt)], Txt, stALL)  # 検索文字列から一致率リストを作成
        if TC[0] is True:
            TCL = np.floor(TC[1][:, 0]).astype(int)  # インデックスを丸めて整数に
            Pac = TC[1][:, 1]  # 一致率列のみ取り出す
            Pac = Pac.reshape(Pac.shape[0], -1)  # 一致率リストを多次元に変換
            MJS_Column = MJS_Column.reshape(-1, MJS_Column.shape[0])  # 列名リストを多次元に変換
            MJS_Column = np.insert(MJS_Column, MJS_Column.shape[1], "", axis=1)
            index = list(TCL)  # 丸めたインデックスnparrayをリストに
            MJS_data = MJS_data[index, :]  # インデックス一致のリスト作成
            MJS_data = np.hstack((MJS_data, Pac))  # 一致率リストを横連結
            MJS_Column[0][MJS_Column.shape[1] - 1] = "日付一致率"
            MJS_data = np.vstack((MJS_Column, MJS_data))  # 列名リストを縦連結
            print(MJS_data)
            return True, MJS_data
        elif TC[0] == "yes" and stALL != "ALL":
            return True, MJS_data
        else:
            return False, MJS_data
    except:
        try:
            CC = ColumCheck(MJS_data, ColTxt)  # 元帳CSVから列名番号を検出
            if CC[0] is True:
                TC = TextDateCheck(
                    MJS_data[:, CC[1][1]], Txt, stALL
                )  # 検索文字列から一致率リストを作成
                if TC[0] is True:
                    TCL = np.floor(TC[1][:, 0]).astype(int)  # インデックスを丸めて整数に
                    Pac = TC[1][:, 1]  # 一致率列のみ取り出す
                    Pac = Pac.reshape(Pac.shape[0], -1)  # 一致率リストを多次元に変換
                    MJS_Column = MJS_Column.reshape(
                        -1, MJS_Column.shape[0]
                    )  # 列名リストを多次元に変換
                    MJS_Column = np.insert(MJS_Column, MJS_Column.shape[1], "", axis=1)
                    index = list(TCL)  # 丸めたインデックスnparrayをリストに
                    MJS_data = MJS_data[index, :]  # インデックス一致のリスト作成
                    MJS_data = np.hstack((MJS_data, Pac))  # 一致率リストを横連結
                    MJS_Column[0][MJS_Column.shape[1] - 1] = "日付一致率"
                    MJS_data = np.vstack((MJS_Column, MJS_data))  # 列名リストを縦連結
                    print(MJS_data)
                    return True, MJS_data
                elif TC[0] == "yes" and stALL != "ALL":
                    return True, MJS_data
                else:
                    return False, MJS_data
            else:
                return False, MJS_data
        except:
            print("DayCheck下処理エラー")
            return False, MJS_data


# ----------------------------------------------------------------------------
def MoneyCheck(MJS_data, Int, ColTxt, stALL):
    """
    引数1データの引数3列の金額データから
    引数2の金額の差額を計算しnp.arrayで返す
    """
    try:
        MJS_Column = MJS_data[0, :]
        int(ColTxt)
        TC = IntCheck(MJS_data[:, int(ColTxt)], Int)  # 検索文字列から一致率リストを作成
        if TC[0] is True:
            Pac = np.array(TC[1])  # 一致率列のみ取り出す
            index = list(Pac[:, 0])
            Pac = Pac[:, 1]
            Pac = Pac.reshape(Pac.shape[0], -1)  # 一致率リストを多次元に変換
            MJS_Column = MJS_Column.reshape(-1, MJS_Column.shape[0])  # 列名リストを多次元に変換
            MJS_Column = np.insert(MJS_Column, MJS_Column.shape[1], "", axis=1)
            MJS_data = MJS_data[index, :]  # インデックス一致のリスト作成
            MJS_data = np.hstack((MJS_data, Pac))  # 一致率リストを横連結
            MJS_Column[0][MJS_Column.shape[1] - 1] = "仕訳金額差額"
            MJS_data = np.vstack((MJS_Column, MJS_data))  # 列名リストを縦連結
            print(MJS_data)
            return True, MJS_data
        elif TC[0] == "yes" and stALL != "ALL":
            return True, MJS_data
        else:
            return False, MJS_data
    except:
        CC = ColumCheck(MJS_data, ColTxt)  # 元帳CSVから列名番号を検出
        if CC[0] is True:
            TC = IntCheck(MJS_data[:, CC[1][1]], Int)  # 検索文字列から一致率リストを作成
            if TC[0] is True:
                Pac = np.array(TC[1])  # 一致率列のみ取り出す
                index = list(Pac[:, 0])
                Pac = Pac[:, 1]
                Pac = Pac.reshape(Pac.shape[0], -1)  # 一致率リストを多次元に変換
                MJS_Column = MJS_Column.reshape(-1, MJS_Column.shape[0])  # 列名リストを多次元に変換
                MJS_Column = np.insert(MJS_Column, MJS_Column.shape[1], "", axis=1)
                MJS_data = MJS_data[index, :]  # インデックス一致のリスト作成
                MJS_data = np.hstack((MJS_data, Pac))  # 一致率リストを横連結
                MJS_Column[0][MJS_Column.shape[1] - 1] = "仕訳金額差額"
                MJS_data = np.vstack((MJS_Column, MJS_data))  # 列名リストを縦連結
                print(MJS_data)
                return True, MJS_data
            elif TC[0] == "yes" and stALL != "ALL":
                return True, MJS_data
            else:
                return False, MJS_data
        else:
            return False, MJS_data


# ----------------------------------------------------------------------------
def npTidyUp(MJS_data):
    """
    引数1データの「一致率」列を基準に
    降順で並び替え
    """
    try:
        MJS_Column = MJS_data[0, :]
        Just = ColumCheck(MJS_data, "一致率")
        npJust = MJS_data[1:, Just[1][1]]
        npMJSList = MJS_data[1:, :]
        npJust = npJust[:, 0]
        npJust = npJust.astype(int)  # インデックスを丸めて整数に
        index = np.argsort(npJust)[::-1]  # np配列を一致率降順ソート
        InTotalList = npMJSList[index]  # 変数格納
        MJS_data = np.vstack((MJS_Column, InTotalList))  # 列名リストを縦連結
        return True, MJS_data
    except:
        print("npTidyUpエラー")
        return False, MJS_data


# ----------------------------------------------------------------------------
def mainListUp(ColTxt, SerchTxt, imgurl, Roolrul, Banktoml, tomltitle):
    MJS_data = np.genfromtxt(Roolrul, dtype=None, delimiter=",")  # 元帳CSVをnp配列に変換
    NPC = npCreate(MJS_data, SerchTxt, ColTxt, "NOALL")
    if NPC[0] is True:
        return NPC[1]


# ----------------------------------------------------------------------------
def ColumCheckListUp(MJS_data, cstr):
    """
    引数列名から列番号を調べる
    MJS_data:Numpy配列
    cstr:検索列名
    return bool,index
    """
    try:
        indexList = []
        MJS_data = list(MJS_data)
        M_r = 0
        for MJS_Item in MJS_data:
            if MJS_Item == cstr:
                indexList.append(M_r)
            M_r += 1
        return True, indexList
    except:
        print("ColumCheckListUpエラー")
        return False, ""


# ----------------------------------------------------------------------------
def ForInReversed(MJS_data, npw, NGList, colT):
    """
    引数列名から列番号を調べる
    MJS_data:Numpy配列
    cstr:検索列名
    return bool,index
    """
    try:
        c_npw = list(npw)
        for c_r in reversed(range((len(c_npw)))):
            npwItem = c_npw[c_r][colT[1]]
            npwItem = npwItem[0]
            if c_r != 0 and "現金" not in npwItem and "預金" not in npwItem:
                NGList.append(c_npw[c_r])
                c_npw.pop(c_r)
        Lastap = np.array(c_npw)
        if len(Lastap) == 1:
            MB = messagebox.askquestion(
                "確認",
                "自動仕訳抽出結果がありません。入出金条件不一致を表示しますか？",
                icon="warning",
            )
            if MB == "yes":  # If関数
                MB = messagebox.askquestion(
                    "確認",
                    "はい=入出金条件不一致表示\nいいえ=元帳全体表示",
                    icon="warning",
                )
                if MB == "yes":  # If関数
                    Lastap = np.array(NGList)
                    return Lastap
                else:
                    return MJS_data
            else:
                return Lastap
        else:
            return Lastap
    except:
        print("ForInReversedエラー")
        return "エラー"


# ----------------------------------------------------------------------------
def main(
    SerchTxt,
    ColName,
    D_var,
    D_coltxt,
    M_var,
    M_coltxt,
    IO,
    Kari,
    Kashi,
    imgurl,
    Roolrul,
    Banktoml,
    tomltitle,
):
    try:
        NGList = []
        MJS_data = np.genfromtxt(Roolrul, dtype=None, delimiter=",")  # 元帳CSVをnp配列に変換
        NPC = npCreate(MJS_data, SerchTxt, ColName, "NOALL")
        if NPC[0] is True:
            # 日付文字列データの変換------------------------------------------
            if (
                "." in D_var
                or "|" in D_var
                or "\\" in D_var
                or ":" in D_var
                or "^" in D_var
                or "~" in D_var
            ):
                D_var = (
                    D_var.replace(".", "/")
                    .replace("|", "")
                    .replace("\\", "")
                    .replace(":", "")
                    .replace("^", "")
                    .replace("~", "")
                )
            # 日付文字列データの変換------------------------------------------
            DC = DayCheck(NPC[1], D_var, D_coltxt, "NoALL")
            if DC[0] is True:
                MC = MoneyCheck(DC[1], M_var, M_coltxt, "NoALL")
                if MC[0] is True:
                    NNPC = npTidyUp(MC[1])
                    if NNPC[0] is True:
                        npw = NNPC[1]
                        npw_Column = npw[0, :]
                        NGList.append(list(npw_Column))
                        if IO == "入金":
                            colT = ColumCheckListUp(npw_Column, Kari)
                            if colT[0] is True:
                                c_npw = list(npw)
                                # for c_r in reversed(range((len(c_npw)))):
                                #     npwItem = c_npw[c_r][colT[1]]
                                #     npwItem = npwItem[0]
                                #     if (
                                #         c_r != 0
                                #         and "現金" not in npwItem
                                #         and "預金" not in npwItem
                                #     ):
                                #         NGList.append(c_npw[c_r])
                                #         c_npw.pop(c_r)
                                # Lastap = np.array(c_npw)
                                # if len(Lastap) == 1:
                                #     MB = messagebox.askquestion(
                                #         "確認",
                                #         "自動仕訳抽出結果がありません。入出金条件不一致を表示しますか？",
                                #         icon="warning",
                                #     )
                                #     if MB == "yes":  # If関数
                                #         MB = messagebox.askquestion(
                                #             "確認",
                                #             "はい=入出金条件不一致表示\nいいえ=元帳全体表示",
                                #             icon="warning",
                                #         )
                                #         if MB == "yes":  # If関数
                                #             Lastap = np.array(NGList)
                                #             return Lastap
                                #         else:
                                #             return MJS_data
                                #     else:
                                #         return Lastap
                                # else:
                                #     return Lastap
                        elif IO == "出金":
                            colT = ColumCheckListUp(npw_Column, Kashi)
                            if colT[0] is True:
                                c_npw = list(npw)
                                for c_r in reversed(range((len(c_npw)))):
                                    npwItem = c_npw[c_r][colT[1]]
                                    npwItem = npwItem[0]
                                    if (
                                        c_r != 0
                                        and "現金" not in npwItem
                                        and "預金" not in npwItem
                                    ):
                                        NGList.append(c_npw[c_r])
                                        c_npw.pop(c_r)
                                Lastap = np.array(c_npw)
                                if len(Lastap) == 1:
                                    MB = messagebox.askquestion(
                                        "確認",
                                        "自動仕訳抽出結果がありません。入出金条件不一致を表示しますか？",
                                        icon="warning",
                                    )
                                    if MB == "yes":  # If関数
                                        MB = messagebox.askquestion(
                                            "確認",
                                            "はい=入出金条件不一致表示\nいいえ=元帳全体表示",
                                            icon="warning",
                                        )
                                        if MB == "yes":  # If関数
                                            Lastap = np.array(NGList)
                                            return Lastap
                                        else:
                                            return MJS_data
                                    else:
                                        return Lastap
                                else:
                                    return Lastap
                    else:
                        npw = NNPC[1]
                        npw_Column = npw[0, :]
                        NGList.append(list(npw_Column))
                        if IO == "入金":
                            colT = ColumCheckListUp(npw_Column, Kari)
                            if colT[0] is True:
                                c_npw = list(npw)
                                for c_r in reversed(range((len(c_npw)))):
                                    npwItem = c_npw[c_r][colT[1]]
                                    npwItem = npwItem[0]
                                    if (
                                        c_r != 0
                                        and "現金" not in npwItem
                                        and "預金" not in npwItem
                                    ):
                                        NGList.append(c_npw[c_r])
                                        c_npw.pop(c_r)
                                Lastap = np.array(c_npw)
                                if len(Lastap) == 1:
                                    MB = messagebox.askquestion(
                                        "確認",
                                        "自動仕訳抽出結果がありません。入出金条件不一致を表示しますか？",
                                        icon="warning",
                                    )
                                    if MB == "yes":  # If関数
                                        MB = messagebox.askquestion(
                                            "確認",
                                            "はい=入出金条件不一致表示\nいいえ=元帳全体表示",
                                            icon="warning",
                                        )
                                        if MB == "yes":  # If関数
                                            Lastap = np.array(NGList)
                                            return Lastap
                                        else:
                                            return MJS_data
                                    else:
                                        return Lastap
                                else:
                                    return Lastap
                        elif IO == "出金":
                            colT = ColumCheckListUp(npw_Column, Kashi)
                            if colT[0] is True:
                                c_npw = list(npw)
                                for c_r in reversed(range((len(c_npw)))):
                                    npwItem = c_npw[c_r][colT[1]]
                                    npwItem = npwItem[0]
                                    if (
                                        c_r != 0
                                        and "現金" not in npwItem
                                        and "預金" not in npwItem
                                    ):
                                        NGList.append(c_npw[c_r])
                                        c_npw.pop(c_r)
                                Lastap = np.array(c_npw)
                                if len(Lastap) == 1:
                                    MB = messagebox.askquestion(
                                        "確認",
                                        "自動仕訳抽出結果がありません。入出金条件不一致を表示しますか？",
                                        icon="warning",
                                    )
                                    if MB == "yes":  # If関数
                                        MB = messagebox.askquestion(
                                            "確認",
                                            "はい=入出金条件不一致表示\nいいえ=元帳全体表示",
                                            icon="warning",
                                        )
                                        if MB == "yes":  # If関数
                                            Lastap = np.array(NGList)
                                            return Lastap
                                        else:
                                            return MJS_data
                                    else:
                                        return Lastap
                                else:
                                    return Lastap
    except:
        Lastap = ["エラー:抽出失敗"]
        Lastap = np.array(Lastap)
        return Lastap


# ----------------------------------------------------------------------------
def RensouTextCheck(OCR_data, MJS_data, ChangeTxt_data, SetList, l_r):
    """
    テキストから曖昧一致抽出し元帳の摘要テキストに変換
    MJS_data:Numpy配列
    Txt:検索テキスト
    return bool,np.array(一致率表)
    """
    OCR_Column = OCR_data[0, :]
    ChangeTxt_Column = ChangeTxt_data[0, :]
    s_c = 0
    InTotalListFlag = False
    for SetListItem in SetList:
        if s_c != len(SetList) - 1:
            M_c = int(np.where(OCR_Column == SetListItem)[0])
            C_r = ChangeTxt_data.shape[0]  # 行数
            InTotalList = []  # 完成リスト
            OCR_Txt = (
                str(OCR_data[l_r][M_c]).replace("['", "").replace("']", "")
            )  # 検索対象(OCR列)の文字列
            if s_c == 0:
                F_txt = OCR_Txt
            for r in range(C_r):
                if r != 0:
                    Txt = (
                        str(ChangeTxt_data[r][s_c]).replace("['", "").replace("']", "")
                    )
                    if Txt != "" and OCR_Txt != "":
                        lTxt = len(Txt)  # 文字数
                        # NoList = []  # インデックス格納用リスト
                        InList = []  # 一致パラメータ格納リスト
                        # 検索文字列を一文字ずつ対象に含まれるかチェック--------------------
                        for T in range(lTxt):  # 現在のインデックスを格納
                            if Txt[T] in OCR_Txt:
                                InList.append(1)  # 含まれる場合
                            else:
                                InList.append(0)  # 含まれない場合
                        # ---------------------------------------------------------------
                        if sum(InList) != 0:  # 一致パラメータ合計値が0以外なら
                            InTotalListFlag = True
                            InList.append(
                                round((sum(InList) / len(InList)) * 100, 1)
                            )  # 一致率を計算し格納
                            # NoList.append(
                            #     [r, InList[len(InList) - 1]]
                            # )  # インデックス格納と一致パラメータ格納リストを結合
                            InTotalList.append([r, InList[len(InList) - 1]])  # 完成リストに格納
            if len(InTotalList) != 0:
                InTotalList = np.array(InTotalList)  # np配列に変換
                print(InTotalList.shape[1])
                rep = np.where(InTotalList[:, InTotalList.shape[1] - 1] > 80)
                InTotalList = InTotalList[rep]
                index = np.argsort(InTotalList[:, InTotalList.shape[1] - 1], axis=0)[
                    ::-1
                ]  # np配列を一致率降順ソート
                InTotalList = InTotalList[index]  # 変数格納
                InTotalList = InTotalList[:, 0]
                InTotalList = InTotalList.astype(int)
                InTotalList = ChangeTxt_data[InTotalList]
                print(InTotalList)
                ChangeTxt_data = np.vstack([ChangeTxt_Column, InTotalList])
                print(ChangeTxt_data)
            s_c += 1
    if ChangeTxt_data.shape[0] != 1 and InTotalListFlag is True:
        Txt = ChangeTxt_data[1][len(ChangeTxt_Column) - 1]
        return Txt
    else:
        return F_txt


# ----------------------------------------------------------------------------
def TxtDayChange(D_var):
    try:
        # 日付文字列データの変換------------------------------------------
        if (
            "." in D_var
            or "|" in D_var
            or "\\" in D_var
            or ":" in D_var
            or "^" in D_var
            or "~" in D_var
        ):
            D_var = (
                D_var.replace(".", "/")
                .replace("|", "")
                .replace("\\", "")
                .replace(":", "")
                .replace("^", "")
                .replace("~", "")
            )
            return D_var
        else:
            return D_var
    except:
        return D_var


# ----------------------------------------------------------------------------
def IOsplitFlow(IO, npw_Column, Kari, Kashi, npw, NGList, N_C, FinalList):
    try:
        if IO == "入金":
            colT = ColumCheckListUp(npw_Column, Kari)
            if colT[0] is True:
                c_npw = list(npw)

                for c_r in reversed(range((len(c_npw)))):
                    npwItem = c_npw[c_r][colT[1]]
                    npwItem = npwItem[0]
                    if c_r != 0 and "現金" not in npwItem and "預金" not in npwItem:
                        NGList.append(c_npw[c_r])
                        c_npw.pop(c_r)
                if len(c_npw) == 1:
                    if N_C == 1:
                        FinalList.append(list(c_npw[0]))
                    elif N_C < 2:
                        FinalList.append(list(NGList[len(NGList) - 1]))
                    else:
                        FinalList.append(list(NGList[1]))
                else:
                    FinalList.append(list(c_npw[1]))
        elif IO == "出金":
            colT = ColumCheckListUp(npw_Column, Kashi)
            if colT[0] is True:
                c_npw = list(npw)

                for c_r in reversed(range((len(c_npw)))):
                    npwItem = c_npw[c_r][colT[1]]
                    npwItem = npwItem[0]
                    if c_r != 0 and "現金" not in npwItem and "預金" not in npwItem:
                        NGList.append(c_npw[c_r])
                        c_npw.pop(c_r)
                if len(c_npw) == 1:
                    if N_C == 1:
                        FinalList.append(list(c_npw[0]))
                    elif N_C < 2:
                        FinalList.append(list(NGList[len(NGList) - 1]))
                    else:
                        FinalList.append(list(NGList[1]))
                else:
                    FinalList.append(list(c_npw[1]))
    except:
        return False


# ----------------------------------------------------------------------------
def AllChange(
    SetList,
    ColTxt,
    ColName,
    DayColName,
    D_coltxt,
    M_coltxt,
    Kari,
    Kashi,
    csvurl,
    FileNameenc,
    imgurl,
    JounalFileNameenc,
    Roolrul,
    Roolurlenc,
    Banktoml,
    tomltitle,
    ChangeTxtURL,
    ChangeTxtURLenc,
    I,
    O,
):
    try:
        HukugouKey = "複合"  # 複合仕訳の諸口勘定名
        FinalList = []
        OCR_data = np.genfromtxt(
            csvurl, dtype=None, delimiter=",", encoding=FileNameenc
        )  # OCRCSVをnp配列に変換
        MJS_data = np.genfromtxt(
            Roolrul, dtype=None, delimiter=",", encoding=Roolurlenc
        )  # 元帳CSVをnp配列に変換
        ChangeTxt_data = np.genfromtxt(
            ChangeTxtURL, dtype=None, delimiter=",", encoding=ChangeTxtURLenc
        )  # 元帳CSVをnp配列に変換
        l_OCR = OCR_data.shape[0]
        for l_r in range(l_OCR):
            NGList = []
            ColNames = MJS_data[0, :]
            OCRColNames = OCR_data[0, :]
            l_c = 0
            # ------------------------------------------------------------------
            for OCRColItem in OCRColNames:
                if I == OCRColItem.replace('"', "").replace('"', ""):
                    if OCR_data[l_r, l_c] != "":
                        M_var = OCR_data[l_r, l_c]
                        try:
                            M_var = int(M_var)
                            IO = "入金"
                        except:
                            IO = "出金"
                elif O == OCRColItem.replace('"', "").replace('"', ""):
                    if OCR_data[l_r, l_c] != "":
                        M_var = OCR_data[l_r, l_c]
                        try:
                            M_var = int(M_var)
                            IO = "出金"
                        except:
                            IO = "入金"
                elif DayColName == OCRColItem.replace('"', "").replace('"', ""):
                    if OCR_data[l_r, l_c] != "":
                        D_var = OCR_data[l_r, l_c]
                        IO = ""
                l_c += 1
            # ------------------------------------------------------------------
            if l_r != 0:
                if l_r == 9:
                    print("")
                l_c = 0
                for ColItem in OCRColNames:
                    if ColTxt == ColItem.replace('"', "").replace('"', ""):
                        SerchTxt = RensouTextCheck(
                            OCR_data,
                            MJS_data,
                            ChangeTxt_data,
                            SetList,
                            l_r,
                        )
                    l_c += 1
                NPC = npCreate(MJS_data, SerchTxt, ColName, "ALL")
                if NPC[0] is True:
                    # 一致率100%の仕訳が同日に複数あるか判定-----------------------------------
                    # ヘッダーとリストに仕訳番号列を挿入---------------------------------------
                    N_Arr = NPC[1]
                    # -----------------------------------------------------------------------
                    N_clen = len(N_Arr[0]) - 1
                    SortNp = N_Arr[1:, N_clen]
                    SortNp = SortNp.astype(int)
                    N_C = np.count_nonzero(SortNp >= 40, axis=0)
                    print(N_C)
                    # -----------------------------------------------------------------------
                    if N_C >= 2:
                        N_ArrHead = N_Arr[0, :]
                        N_ArrHead = np.insert(N_ArrHead, N_ArrHead.shape[0] - 2, "仕訳番号")
                        N_Arr = np.insert(N_Arr, N_ArrHead.shape[0] - 2, l_r, axis=1)
                        N_clen = len(N_Arr[0]) - 1
                        ind = np.where(N_Arr[:, N_clen] == "100")
                        print(N_Arr[ind])
                        Hukugou = np.where(N_Arr[ind] == HukugouKey)
                        if len(Hukugou) != 0:
                            Nind = N_Arr[ind]
                            # 日付文字列データの変換------------------------------------------
                            D_var = TxtDayChange(D_var)
                            # 末尾含め3列削除-------------------------------------
                            np_h = N_ArrHead
                            np_h_c = np_h.shape[0] - 1
                            for np_hItem in reversed(np_h):
                                if "一致率" == np_hItem:
                                    Nind = np.delete(Nind, np_h_c, 1)
                                    N_ArrHead = np.delete(N_ArrHead, np_h_c, 0)
                                elif "日付一致率" == np_hItem:
                                    Nind = np.delete(Nind, np_h_c, 1)
                                    N_ArrHead = np.delete(N_ArrHead, np_h_c, 0)
                                elif "仕訳金額差額" == np_hItem:
                                    Nind = np.delete(Nind, np_h_c, 1)
                                    N_ArrHead = np.delete(N_ArrHead, np_h_c, 0)
                                np_h_c -= 1
                            # ---------------------------------------------------
                            N_Arr = np.vstack([N_ArrHead, Nind])
                            if l_r == 1:
                                for l_s in range(len(Nind)):
                                    FinalList.append(list(Nind[l_s]))
                            else:
                                for l_s in range(len(Nind)):
                                    FinalList.append(list(Nind[l_s]))
                    else:
                        # -----------------------------------------------------------------------
                        print("not複合")
                        # 日付文字列データの変換------------------------------------------
                        D_var = TxtDayChange(D_var)
                        # 日付文字列データの変換------------------------------------------
                        DC = DayCheck(N_Arr, D_var, D_coltxt, "ALL")
                        if DC[0] is True:
                            MC = MoneyCheck(DC[1], M_var, M_coltxt, "ALL")
                            if MC[0] is True:
                                NNPC = npTidyUp(MC[1])
                                if NNPC[0] is True:
                                    # ヘッダーとリストに仕訳番号列を挿入---------------------------------------
                                    N_Arr = NNPC[1]
                                    N_ArrHead = N_Arr[0, :]
                                    Nind = N_Arr
                                    # 末尾含め3列削除-------------------------------------
                                    np_h = N_ArrHead
                                    np_h_c = np_h.shape[0] - 1
                                    for np_hItem in reversed(np_h):
                                        if "一致率" == np_hItem:
                                            Nind = np.delete(Nind, np_h_c, 1)
                                            N_ArrHead = np.delete(N_ArrHead, np_h_c, 0)
                                        elif "日付一致率" == np_hItem:
                                            Nind = np.delete(Nind, np_h_c, 1)
                                            N_ArrHead = np.delete(N_ArrHead, np_h_c, 0)
                                        elif "仕訳金額差額" == np_hItem:
                                            Nind = np.delete(Nind, np_h_c, 1)
                                            N_ArrHead = np.delete(N_ArrHead, np_h_c, 0)
                                        np_h_c -= 1
                                    # ---------------------------------------------------
                                    N_ArrHead = np.insert(
                                        N_ArrHead, N_ArrHead.shape[0] - 1, "仕訳番号"
                                    )
                                    Nind = np.insert(
                                        Nind[1:, :],
                                        N_ArrHead.shape[0] - 1,
                                        l_r,
                                        axis=1,
                                    )
                                    N_Arr = np.vstack([N_ArrHead, Nind])
                                    if l_r == 1:
                                        FinalList.append(list(np_h))
                                    NGList.append(list(np_h))
                                    # 入出金での処理分け#######################################
                                    IOsplitFlow(
                                        IO,
                                        np_h,
                                        Kari,
                                        Kashi,
                                        Nind,
                                        NGList,
                                        N_C,
                                        FinalList,
                                    )
                                    # ########################################################
                                else:
                                    print("NoNNPC")
                                    DammyList = []
                                    for ColNamesItem in ColNames:
                                        DammyList.append(ColNamesItem + "自動仕訳候補なし")
                                    DammyList.append(str(l_r))  # 仕訳番号代入
                                    FinalList.append(DammyList)
                            else:
                                print("NoMC")
                                DammyList = []
                                for ColNamesItem in ColNames:
                                    DammyList.append(ColNamesItem + "自動仕訳候補なし")
                                DammyList.append(str(l_r))  # 仕訳番号代入
                                FinalList.append(DammyList)
                        else:
                            print("NoDC")
                            DammyList = []
                            for ColNamesItem in ColNames:
                                DammyList.append(ColNamesItem + "自動仕訳候補なし")
                            DammyList.append(str(l_r))  # 仕訳番号代入
                            FinalList.append(DammyList)
                else:
                    print("NoNPC")
                    DC = DayCheck(NPC[1], D_var, D_coltxt, "ALL")
                    if DC[0] is True:
                        DammyList = []
                        for ColNamesItem in ColNames:
                            if ColNamesItem == D_coltxt:
                                DCRow = DC[1]
                                D_c = 0
                                for DCRowItem in DCRow[0]:
                                    if D_coltxt == DCRowItem:
                                        print(DCRow[1][D_c])
                                        DammyList.append(DCRow[1][D_c])
                                        break
                                    D_c += 1
                            else:
                                DammyList.append(ColNamesItem + "自動仕訳候補なし")
                        DammyList.append(str(l_r))  # 仕訳番号代入
                        FinalList.append(DammyList)
        Lis = np.array(FinalList)
        FL = np.vstack([N_ArrHead, Lis])
        FL = list(FL)
        FinalList = []
        for FL_r in range(len(FL)):
            FinalList.append(list(FL[FL_r]))
        return True, FinalList
    except:
        FinalList = ["エラー:抽出失敗"]
        return False, FinalList


# -----------------------------------------------------------------------------------------
if __name__ == "__main__":
    global imgurl, Roolrul, Banktoml, tomltitle
    imgurl = r"D:\OCRTESTPDF\PDFTEST\JA_1page.csv"
    Roolrul = r"D:\PythonScript\RPAScript\TKInterGUI\Mototyou\18_仕訳日記帳.csv"
    tomltitle = "JA"
    # toml読込------------------------------------------------------------------------------
    with open(os.getcwd() + r"/TKInterGUI/BankSetting.toml", encoding="utf-8") as f:
        Banktoml = toml.load(f)
        print(Banktoml)
    # -----------------------------------------------------------
    OCR_data = np.genfromtxt(imgurl, dtype=None, delimiter=",")  # OCRCSVをnp配列に変換

    ColTxt = "摘要"
    D_coltxt = "伝票日付"
    IO = "入金"
    Kari = "借方科目名"
    Kashi = "貸方科目名"
    AllChange(
        ColTxt,
        D_coltxt,
        IO,
        Kari,
        Kashi,
        imgurl,
        Roolrul,
        Banktoml,
        tomltitle,
    )
