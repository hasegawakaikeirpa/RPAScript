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
def RensouTextCheck(ChangeTxt_data, OCR_Txt, OCR_c, U_c):
    """
    テキストから曖昧一致抽出し元帳の摘要テキストに変換
    MJS_data:Numpy配列
    Txt:検索テキスト
    return bool,np.array(一致率表)
    """
    ChangeTxt_Column = ChangeTxt_data[0, :]  # 文字列変換表の列名
    InTotalListFlag = False  # 抽出結果フラグ
    C_r = ChangeTxt_data.shape[0]
    InTotalList = []  # 格納リスト
    NoList = []  # 不一致パラメータ格納リスト
    for r in range(C_r):
        if r != 0:
            InList = []  # 一致パラメータ一時格納リスト
            Txt = (
                str(ChangeTxt_data[r][OCR_c]).replace("['", "").replace("']", "")
            )  # MJS側のの文字列
            if Txt != "" and OCR_Txt != "":
                lTxt = len(Txt)  # 文字数
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
                    InTotalList.append([r, InList[len(InList) - 1]])
                else:
                    NoList.append(
                        [r, InList[len(InList) - 1]]
                    )  # インデックス格納と一致パラメータ格納リストを結合

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

    if ChangeTxt_data.shape[0] != 1 and InTotalListFlag is True:
        Txt = ChangeTxt_data[ChangeTxt_data.shape[0] - 1][U_c]
        return True, Txt
    else:
        return False, OCR_Txt


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
def IOsplitFlow(
    OCR_data, OCR_data_Row, IO, npw_Column, Kari, Kashi, npw, NGList, N_C, M_coltxt
):
    """
    借貸方の科目名から現預金処理なのか判定
    """
    try:
        IOList = []
        OCR_h = OCR_data[0, :]

        if IO == "入金":
            OCR_h_c = np.where(OCR_h == IO)
            OCR_h_c = OCR_h_c[0]
            OCR_h_c = int(OCR_h_c[0])
            M = OCR_data_Row[OCR_h_c]
            # ミロクデータから入金列を抽出
            colT = ColumCheckListUp(npw_Column, Kari)
            if colT[0] is True:
                c_npw = list(npw)
                # ミロクデータの入金列に現預金処理なのか判定
                for c_r in reversed(range((len(c_npw)))):
                    npwItem = c_npw[c_r][colT[1]]
                    c_np_Row = c_npw[c_r]
                    npwItem = npwItem[0]
                    if c_r != 0 and "現金" not in npwItem and "預金" not in npwItem:
                        c_np_Bool = False
                        for c_np_RowItem in c_np_Row:
                            if "現金" in c_np_RowItem or "預金" in c_np_RowItem:
                                c_np_Bool = True
                                break
                        if c_np_Bool is False:
                            NGList.append(c_npw[c_r])
                            c_npw.pop(c_r)
                    elif c_r == 0:
                        c_npw.pop(c_r)
                if len(c_npw) == 1:
                    if N_C == 1:
                        IOList.append(list(c_npw[0]))
                        return True, IOList
                    elif N_C < 2:
                        IOList.append(list(NGList[len(NGList) - 1]))
                        return True, IOList
                    else:
                        IOList.append(list(NGList[1]))
                        return True, IOList
                elif len(c_npw) == 2:
                    GNV = getNearestValue(npw[1:, M_coltxt], M)
                    TS = npw[1:, :]
                    TS = TS[GNV]
                    return True, TS
                else:
                    if len(NGList) == 0:
                        TS = npw[1, :]
                        return True, TS
                    else:
                        return False, NGList
        elif IO == "出金":
            OCR_h_c = np.where(OCR_h == IO)
            OCR_h_c = OCR_h_c[0]
            OCR_h_c = int(OCR_h_c[0])
            M = OCR_data_Row[OCR_h_c]
            # ミロクデータから出金列を抽出
            colT = ColumCheckListUp(npw_Column, Kashi)
            if colT[0] is True:
                c_npw = list(npw)
                # ミロクデータの入金列に現預金処理なのか判定
                for c_r in reversed(range((len(c_npw)))):
                    npwItem = c_npw[c_r][colT[1]]
                    c_np_Row = c_npw[c_r]
                    npwItem = npwItem[0]
                    if c_r != 0 and "現金" not in npwItem and "預金" not in npwItem:
                        c_np_Bool = False
                        for c_np_RowItem in c_np_Row:
                            if "現金" in c_np_RowItem or "預金" in c_np_RowItem:
                                c_np_Bool = True
                                break
                        if c_np_Bool is False:
                            NGList.append(c_npw[c_r])
                            c_npw.pop(c_r)
                    elif c_r == 0:
                        c_npw.pop(c_r)
                if len(c_npw) == 1:
                    if N_C == 1:
                        IOList.append(list(c_npw[0]))
                        return True, IOList
                    elif N_C < 2:
                        IOList.append(list(NGList[len(NGList) - 1]))
                        return True, IOList
                    else:
                        IOList.append(list(NGList[1]))
                        return True, IOList
                elif len(c_npw) >= 2:
                    GNV = getNearestValue(npw[1:, M_coltxt], M)
                    TS = npw[1:, :]
                    TS = TS[GNV]
                    return True, TS
                else:
                    if len(NGList) == 0:
                        TS = npw[1, :]
                        return True, TS
                    else:
                        return False, NGList
    except:
        return False


# ---------------------------------------------------------------------------------------
def getNearestValue(list, num):
    """
    概要: リストからある値に最も近い値を返却する関数
    @param list: データ配列
    @param num: 対象値
    @return 対象値に最も近い値
    """

    # リスト要素と対象値の差分を計算し最小値のインデックスを取得
    try:
        num = int(num)
        array = np.asarray(list)
        array = array.astype(int)
        idx = (np.abs(array - num)).argmin()
        return idx
    except:
        return ""


# -----------------------------------------------------------------------------------------
def main(
    ptpos,
    ColName,
    DayColName,
    D_coltxt,
    M_coltxt,
    Kari,
    Kashi,
    csvurl,
    FileNameenc,
    Roolrul,
    Roolurlenc,
    ChangeTxtURL,
    ChangeTxtURLenc,
    I,
    O,
    OCRList,
    MJSList,
    SortVar,
):

    try:
        """
        OCR表全体から摘要欄一致仕訳を抽出
        """
        ############################################################################
        # SortVar = 50  # 一致率
        ############################################################################
        HukugouKey = "複合"  # 複合仕訳の諸口勘定名

        TotalFinalList = []

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
        ColNames = MJS_data[0, :]  # MJSデータ列名
        OCRColNames = OCR_data[0, :]  # OCRデータ列名
        # OCRデータをループ処理---------------------------------------------------
        l_r = ptpos + 1
        NGList = []
        FinalList = []
        FinalListColumns = []
        if l_r != 0:
            OCR_data_Row = OCR_data[l_r, :]
            print("##########################################################")
            print("##########################################################")
            print(OCR_data_Row)
            print("##########################################################")
            print("##########################################################")
            # 自動仕訳判定列設定をループ----------------------------------------
            for OCR_r in range(len(OCRList)):
                ColNo = int(np.where(OCRColNames == OCRList[OCR_r])[0])
                txt = OCR_data_Row[ColNo]
                # 自動仕訳判定の処理番号から隣の列番号を計算-----------------
                if OCR_r == 0:
                    OCR_c = OCR_r
                    U_c = 1
                else:
                    OCR_c = OCR_c + 2
                    U_c = OCR_c + 1
                # ---------------------------------------------------------
                # 検索文字列を変換表と突合し変換
                SerchTxt = RensouTextCheck(ChangeTxt_data, txt, OCR_c, U_c)
                if SerchTxt[0] is True:
                    # 検索文字列が変換表から変換した場合
                    SerchTxt = SerchTxt[1]
                    # 元帳テキスト列名を取得
                    ColName = MJSList[OCR_r]
                    NPC = npCreate(MJS_data, SerchTxt, ColName, "ALL")
                    if NPC[0] is True:
                        # 一致率100%の仕訳が同日に複数あるか判定-----------------------------------

                        # ヘッダーとリストに仕訳番号列を挿入---------------------------------------
                        N_Arr = NPC[1]
                        # -----------------------------------------------------------------------
                        for N_r in range(len(N_Arr)):
                            if N_r != 0:
                                F_row = list(N_Arr[N_r])
                                F_row.append(True)
                                DS = DiplicateSearch(FinalList, F_row)  # 重複判定
                                if DS is False:
                                    FinalList.append(F_row)
                            else:
                                FinalListColumns.append(list(N_Arr[N_r]))
                else:
                    # 検索文字列が変換表から変換しない場合
                    SerchTxt = SerchTxt[1]
                    # 元帳テキスト列名を取得
                    ColName = MJSList[OCR_r]
                    NPC = npCreate(MJS_data, SerchTxt, ColName, "ALL")
                    if NPC[0] is True:
                        # 一致率100%の仕訳が同日に複数あるか判定-----------------------------------
                        # ヘッダーとリストに仕訳番号列を挿入---------------------------------------
                        N_Arr = NPC[1]
                        # -----------------------------------------------------------------------
                        for N_r in range(len(N_Arr)):
                            if N_r != 0:
                                F_row = list(N_Arr[N_r])
                                F_row.append(False)
                                DS = DiplicateSearch(FinalList, F_row)  # 重複判定
                                if DS is False:
                                    FinalList.append(F_row)
                            else:
                                FinalListColumns.append(list(N_Arr[N_r]))

            # 一致率100%の仕訳が同日に複数あるか判定-----------------------------------
            # ヘッダーとリストに仕訳番号列を挿入---------------------------------------
            FinalList = np.array(FinalList)
            BoolList = np.array(FinalList[:, FinalList.shape[1] - 1])
            Boolind = np.where(BoolList == "True")  # インデックス取得
            if Boolind[0].shape[0] != 0:
                FinalList = FinalList[Boolind]
            FinalList = FinalList[:, 0 : FinalList.shape[1] - 1]  # Bool列削除
            # -----------------------------------------------------------------------
            N_clen = len(FinalList[0]) - 1  # 集計リストの要素数
            SortNp = FinalList[:, N_clen]  # 集計リストの一致率列をスライス
            SortNp = SortNp.astype(int)  # 一致率列リストをint型変換
            # 抽出リスト内の指定一致率以上のデータ数を計算
            N_C = np.count_nonzero(SortNp >= SortVar, axis=0)
            if N_C == 1:  # 指定一致率以上が1件なら##########################################
                ind = np.where(SortNp >= SortVar)  # インデックス取得
                FinalList = FinalList[ind]
                SortNp = FinalList[:, N_clen]  # 集計リストの一致率列をスライス
                SortNp = SortNp.astype(int)  # 一致率列リストをint型変換
                ind = np.where(SortNp == max(SortNp))  # インデックス取得
                FinalListColumns = np.array(FinalListColumns[0])  # ヘッダースライス
                FinalList = np.vstack((FinalListColumns, FinalList[ind]))  # ヘッダーと結合
                Nind = NPFLOW(
                    HukugouKey,
                    TotalFinalList,
                    FinalList,
                    OCRColNames,
                    D_coltxt,
                    DayColName,
                    OCR_data_Row,
                    M_coltxt,
                    I,
                    O,
                )
                if Nind[0] is True:
                    # 複合仕訳の判定----------------------------
                    Hukugou = CheckHukugou(HukugouKey, Nind[1])
                    # -----------------------------------------
                    if Hukugou is True:
                        TFList = Nind[1][1 : Nind[1].shape[0], :]  # ヘッダーを取り除く
                        TotalFinalList.append(TFList)  # 入出金での処理分け後格納
                    else:
                        np_h = Nind[1][0, :]
                        # 入出金での処理分け
                        IOS = IOsplitFlow(
                            OCR_data,
                            OCR_data_Row,
                            Nind[2],
                            np_h,
                            Kari,
                            Kashi,
                            Nind[1],
                            NGList,
                            N_C,
                            M_coltxt,
                        )
                        if IOS[0] is True:
                            TotalFinalList.append(IOS[1])  # 入出金での処理分け後格納
                        else:
                            print("Err")
                            # DammyList = []
                            # for ColNamesItem in ColNames:
                            #     DammyList.append(ColNamesItem + "自動仕訳候補なし")
                            # TotalFinalList.append(DammyList)
                else:
                    print("Err")
                    DammyList = []
                    for ColNamesItem in ColNames:
                        DammyList.append(ColNamesItem + "自動仕訳候補なし")
                    TotalFinalList.append(DammyList)
            elif N_C > 1:  # 指定一致率以上が1件以上なら##########################################
                ind = np.where(SortNp >= SortVar)  # インデックス取得
                FinalList = FinalList[ind]
                SortNp = FinalList[:, N_clen]  # 集計リストの一致率列をスライス
                SortNp = SortNp.astype(int)  # 一致率列リストをint型変換
                ind = np.where(SortNp == max(SortNp))  # インデックス取得
                FinalListColumns = np.array(FinalListColumns[0])  # ヘッダースライス
                FinalList = np.vstack((FinalListColumns, FinalList[ind]))  # ヘッダーと結合
                Nind = NPFLOW(
                    HukugouKey,
                    TotalFinalList,
                    FinalList,
                    OCRColNames,
                    D_coltxt,
                    DayColName,
                    OCR_data_Row,
                    M_coltxt,
                    I,
                    O,
                )
                if Nind[0] is True:
                    # 複合仕訳の判定----------------------------
                    Hukugou = CheckHukugou(HukugouKey, Nind[1])
                    # -----------------------------------------
                    if Hukugou is True:
                        TFList = Nind[1][1 : Nind[1].shape[0], :]  # ヘッダーを取り除く
                        TotalFinalList.append(TFList)  # 入出金での処理分け後格納
                    else:
                        N_C = 1
                        np_h = Nind[1][0, :]
                        # 入出金での処理分け
                        IOS = IOsplitFlow(
                            OCR_data,
                            OCR_data_Row,
                            Nind[2],
                            np_h,
                            Kari,
                            Kashi,
                            Nind[1],
                            NGList,
                            N_C,
                            M_coltxt,
                        )
                        if IOS[0] is True:
                            TotalFinalList.append(IOS[1])  # 入出金での処理分け後格納
                        else:
                            print("Err")
                            # DammyList = []
                            # for ColNamesItem in ColNames:
                            #     DammyList.append(ColNamesItem + "自動仕訳候補なし")
                            # TotalFinalList.append(DammyList)
                else:
                    print("Err")
                    DammyList = []
                    for ColNamesItem in ColNames:
                        DammyList.append(ColNamesItem + "自動仕訳候補なし")
                    TotalFinalList.append(DammyList)
            else:
                print("Err")
                DammyList = []
                for ColNamesItem in ColNames:
                    DammyList.append(ColNamesItem + "自動仕訳候補なし")
                TotalFinalList.append(DammyList)
        return True, ColNames, TotalFinalList
    except:
        return False, "", ""


# ----------------------------------------------------------------------------
def AllChange(
    ColName,
    DayColName,
    D_coltxt,
    M_coltxt,
    Kari,
    Kashi,
    csvurl,
    FileNameenc,
    Roolrul,
    Roolurlenc,
    ChangeTxtURL,
    ChangeTxtURLenc,
    I,
    O,
    OCRList,
    MJSList,
    SortVar,
):
    try:
        """
        OCR表全体から摘要欄一致仕訳を抽出
        """
        ############################################################################
        # SortVar = 50  # 一致率
        ############################################################################
        HukugouKey = "複合"  # 複合仕訳の諸口勘定名

        TotalFinalList = []

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
        ColNames = MJS_data[0, :]  # MJSデータ列名
        OCRColNames = OCR_data[0, :]  # OCRデータ列名
        # OCRデータをループ処理---------------------------------------------------
        for l_r in range(l_OCR):
            NGList = []
            FinalList = []
            FinalListColumns = []
            if l_r != 0:
                OCR_data_Row = OCR_data[l_r, :]
                print("##########################################################")
                print("##########################################################")
                print(OCR_data_Row)
                print("##########################################################")
                print("##########################################################")
                # 自動仕訳判定列設定をループ----------------------------------------
                for OCR_r in range(len(OCRList)):
                    ColNo = int(np.where(OCRColNames == OCRList[OCR_r])[0])
                    txt = OCR_data_Row[ColNo]
                    # 自動仕訳判定の処理番号から隣の列番号を計算-----------------
                    if OCR_r == 0:
                        OCR_c = OCR_r
                        U_c = 1
                    else:
                        OCR_c = OCR_c + 2
                        U_c = OCR_c + 1
                    # ---------------------------------------------------------
                    # 検索文字列を変換表と突合し変換
                    SerchTxt = RensouTextCheck(ChangeTxt_data, txt, OCR_c, U_c)
                    if SerchTxt[0] is True:
                        # 検索文字列が変換表から変換した場合
                        SerchTxt = SerchTxt[1]
                        # 元帳テキスト列名を取得
                        ColName = MJSList[OCR_r]
                        NPC = npCreate(MJS_data, SerchTxt, ColName, "ALL")
                        if NPC[0] is True:
                            # 一致率100%の仕訳が同日に複数あるか判定-----------------------------------

                            # ヘッダーとリストに仕訳番号列を挿入---------------------------------------
                            N_Arr = NPC[1]
                            # -----------------------------------------------------------------------
                            for N_r in range(len(N_Arr)):
                                if N_r != 0:
                                    F_row = list(N_Arr[N_r])
                                    F_row.append(True)
                                    DS = DiplicateSearch(FinalList, F_row)  # 重複判定
                                    if DS is False:
                                        FinalList.append(F_row)
                                else:
                                    FinalListColumns.append(list(N_Arr[N_r]))

                    else:
                        # 検索文字列が変換表から変換しない場合
                        SerchTxt = SerchTxt[1]
                        # 元帳テキスト列名を取得
                        ColName = MJSList[OCR_r]
                        NPC = npCreate(MJS_data, SerchTxt, ColName, "ALL")
                        if NPC[0] is True:
                            # 一致率100%の仕訳が同日に複数あるか判定-----------------------------------
                            # ヘッダーとリストに仕訳番号列を挿入---------------------------------------
                            N_Arr = NPC[1]
                            # -----------------------------------------------------------------------
                            for N_r in range(len(N_Arr)):
                                if N_r != 0:
                                    F_row = list(N_Arr[N_r])
                                    F_row.append(False)
                                    DS = DiplicateSearch(FinalList, F_row)  # 重複判定
                                    if DS is False:
                                        FinalList.append(F_row)
                                else:
                                    FinalListColumns.append(list(N_Arr[N_r]))

                # 一致率100%の仕訳が同日に複数あるか判定-----------------------------------
                # ヘッダーとリストに仕訳番号列を挿入---------------------------------------
                FinalList = np.array(FinalList)
                BoolList = np.array(FinalList[:, FinalList.shape[1] - 1])
                Boolind = np.where(BoolList == "True")  # インデックス取得
                if Boolind[0].shape[0] != 0:
                    FinalList = FinalList[Boolind]
                FinalList = FinalList[:, 0 : FinalList.shape[1] - 1]  # Bool列削除
                # -----------------------------------------------------------------------
                N_clen = len(FinalList[0]) - 1  # 集計リストの要素数
                SortNp = FinalList[:, N_clen]  # 集計リストの一致率列をスライス
                SortNp = SortNp.astype(int)  # 一致率列リストをint型変換
                # 抽出リスト内の指定一致率以上のデータ数を計算
                N_C = np.count_nonzero(SortNp >= SortVar, axis=0)
                if N_C == 1:  # 指定一致率以上が1件なら##########################################
                    ind = np.where(SortNp >= SortVar)  # インデックス取得
                    FinalList = FinalList[ind]
                    SortNp = FinalList[:, N_clen]  # 集計リストの一致率列をスライス
                    SortNp = SortNp.astype(int)  # 一致率列リストをint型変換
                    ind = np.where(SortNp == max(SortNp))  # インデックス取得
                    FinalListColumns = np.array(FinalListColumns[0])  # ヘッダースライス
                    FinalList = np.vstack((FinalListColumns, FinalList[ind]))  # ヘッダーと結合
                    Nind = NPFLOW(
                        HukugouKey,
                        TotalFinalList,
                        FinalList,
                        OCRColNames,
                        D_coltxt,
                        DayColName,
                        OCR_data_Row,
                        M_coltxt,
                        I,
                        O,
                    )
                    if Nind[0] is True:
                        # 複合仕訳の判定----------------------------
                        Hukugou = CheckHukugou(HukugouKey, Nind[1])
                        # -----------------------------------------
                        if Hukugou is True:
                            TFList = Nind[1][1 : Nind[1].shape[0], :]  # ヘッダーを取り除く
                            TotalFinalList.append(TFList)  # 入出金での処理分け後格納
                        else:
                            np_h = Nind[1][0, :]
                            # 入出金での処理分け
                            IOS = IOsplitFlow(
                                OCR_data,
                                OCR_data_Row,
                                Nind[2],
                                np_h,
                                Kari,
                                Kashi,
                                Nind[1],
                                NGList,
                                N_C,
                                M_coltxt,
                            )
                            if IOS[0] is True:
                                TotalFinalList.append(IOS[1])  # 入出金での処理分け後格納
                            else:
                                print("Err")
                                # DammyList = []
                                # for ColNamesItem in ColNames:
                                #     DammyList.append(ColNamesItem + "自動仕訳候補なし")
                                # TotalFinalList.append(DammyList)
                    else:
                        print("Err")
                        DammyList = []
                        for ColNamesItem in ColNames:
                            DammyList.append(ColNamesItem + "自動仕訳候補なし")
                        TotalFinalList.append(DammyList)
                elif (
                    N_C > 1
                ):  # 指定一致率以上が1件以上なら##########################################
                    ind = np.where(SortNp >= SortVar)  # インデックス取得
                    FinalList = FinalList[ind]
                    SortNp = FinalList[:, N_clen]  # 集計リストの一致率列をスライス
                    SortNp = SortNp.astype(int)  # 一致率列リストをint型変換
                    ind = np.where(SortNp == max(SortNp))  # インデックス取得
                    FinalListColumns = np.array(FinalListColumns[0])  # ヘッダースライス
                    FinalList = np.vstack((FinalListColumns, FinalList[ind]))  # ヘッダーと結合
                    Nind = NPFLOW(
                        HukugouKey,
                        TotalFinalList,
                        FinalList,
                        OCRColNames,
                        D_coltxt,
                        DayColName,
                        OCR_data_Row,
                        M_coltxt,
                        I,
                        O,
                    )
                    if Nind[0] is True:
                        # 複合仕訳の判定----------------------------
                        Hukugou = CheckHukugou(HukugouKey, Nind[1])
                        # -----------------------------------------
                        if Hukugou is True:
                            TFList = Nind[1][1 : Nind[1].shape[0], :]  # ヘッダーを取り除く
                            TotalFinalList.append(TFList)  # 入出金での処理分け後格納
                        else:
                            N_C = 1
                            np_h = Nind[1][0, :]
                            # 入出金での処理分け
                            IOS = IOsplitFlow(
                                OCR_data,
                                OCR_data_Row,
                                Nind[2],
                                np_h,
                                Kari,
                                Kashi,
                                Nind[1],
                                NGList,
                                N_C,
                                M_coltxt,
                            )
                            if IOS[0] is True:
                                TotalFinalList.append(IOS[1])  # 入出金での処理分け後格納
                            else:
                                print("Err")
                                # DammyList = []
                                # for ColNamesItem in ColNames:
                                #     DammyList.append(ColNamesItem + "自動仕訳候補なし")
                                # TotalFinalList.append(DammyList)
                    else:
                        print("Err")
                        DammyList = []
                        for ColNamesItem in ColNames:
                            DammyList.append(ColNamesItem + "自動仕訳候補なし")
                        TotalFinalList.append(DammyList)
                else:
                    print("Err")
                    DammyList = []
                    for ColNamesItem in ColNames:
                        DammyList.append(ColNamesItem + "自動仕訳候補なし")
                    TotalFinalList.append(DammyList)
        return True, ColNames, TotalFinalList
    except:
        return False, "", ""


# ----------------------------------------------------------------------------
def MoneyCalc(L_r, AJ_List, AJtxt, R_CName, L_CName, L_CName_c, Var):
    """
    複合仕訳の金額割合摘要関数
    """

    if "金" in R_CName:
        MoneyList = CompositeCalc(AJtxt, L_CName_c)
        AJtxt_r = AJtxt.shape[0]
        for A_r in range(AJtxt_r):
            AJtxt_Row = AJtxt[A_r]
            A_t = AJtxt_Row[L_CName_c]
            C_Txt = TxtEdit(
                L_CName,
                A_t,
                Var,
            )
            X_Var = C_Txt[1] * MoneyList[1][A_r]
            X_Var = round(X_Var)
            AJ_List[L_r][A_r][L_CName_c] = int(X_Var)
    else:
        AJtxt_r = AJtxt.shape[0]
        for A_r in range(AJtxt_r):
            AJtxt_Row = AJtxt[A_r]
            A_t = AJtxt_Row[L_CName_c]
            C_Txt = TxtEdit(
                L_CName,
                A_t,
                Var,
            )
            AJ_List[L_r][A_r][L_CName_c] = C_Txt[1]


# ----------------------------------------------------------------------------
def CompositeCalc(FinalList, c):
    """
    1列データの割合計算(int)
    """
    try:
        FL = FinalList[:, c]
        FL = FL.astype(int)
        ret = FL / FL.max()  # 割合計算
        return True, ret
    except:
        return False, ""


# ----------------------------------------------------------------------------
def TxtEdit(Txt, L_txt, R_txt):
    """
    R_txtの書式をL_txtの書式と揃える
    """
    try:
        if "日" in Txt:
            L_txt = (
                L_txt.replace("-", "/")
                .replace("_", "/")
                .replace("\\", "/")
                .replace(".", "/")
                .replace("|", "")
                .replace("\\", "")
                .replace(":", "")
                .replace("^", "")
                .replace("~", "")
            )

            R_txt = (
                R_txt.replace("-", "/")
                .replace("_", "/")
                .replace("\\", "/")
                .replace(".", "/")
                .replace("|", "")
                .replace("\\", "")
                .replace(":", "")
                .replace("^", "")
                .replace("~", "")
            )
            L_txtSp = L_txt.split("/")
            R_txtSp = R_txt.split("/")
            if len(L_txtSp[0]) < 4:
                L_y = wh.R(int(L_txtSp[0])).to_ad()
                L_txtSp[0] = str(L_y)
                L_txt = "/".join(L_txtSp)
            if len(R_txtSp[0]) < 4:
                R_y = wh.R(int(R_txtSp[0])).to_ad()
                R_txtSp[0] = str(R_y)
                R_txt = "/".join(R_txtSp)
            L_d = dt.strptime(L_txt, "%Y/%m/%d")
            R_d = dt.strptime(R_txt, "%Y/%m/%d")
            L_txt = (
                str(L_d.year)
                + "/"
                + "{0:02}".format(str(L_d.month))
                + "/"
                + "{0:02}".format(str(L_d.day))
            )
            R_txt = (
                str(R_d.year)
                + "/"
                + "{0:02}".format(str(R_d.month))
                + "/"
                + "{0:02}".format(str(R_d.day))
            )
            return L_txt, R_txt
        else:
            return L_txt, R_txt
    except:
        return L_txt, R_txt


# ----------------------------------------------------------------------------
def DiplicateSearch(FinalList, N_Arr):
    """
    行データ比較で重複判定
    """
    try:
        for i in range(len(FinalList)):
            F_List = np.array(FinalList[i])
            N_List = np.array(N_Arr)
            # ------------------------------------------
            try:
                F_c = F_List.shape[1] - 2
                F_List_S = F_List
                # F_List_S = F_List[:, 0:F_c]
            except:
                F_c = F_List.shape[0] - 2
                F_List_S = F_List
                # F_List_S = F_List[0:F_c]
            # ------------------------------------------
            try:
                N_c = N_List.shape[1] - 2
                N_List_S = N_List
                # N_List_S = N_List[:, 0:N_c]
            except:
                N_c = N_List.shape[0] - 2
                N_List_S = N_List
                # N_List_S = N_List[0:N_c]
            # ------------------------------------------
            FE = np.array_equal(F_List_S, N_List_S)
            if FE is True:
                return True
        return False
    except:
        return False


# ----------------------------------------------------------------------------
def NPFLOW(
    HukugouKey,
    TotalFinalList,
    FinalList,
    OCRColNames,
    D_coltxt,
    DayColName,
    OCR_data_Row,
    M_coltxt,
    I,
    O,
):
    """
    摘要欄一致仕訳リストへの処理
    """
    try:
        ColNo = int(np.where(OCRColNames == DayColName)[0])
        D_var = OCR_data_Row[ColNo]
        D_var = TxtDayChange(D_var)
        # OCRデータの日付情報を元に近い日付データの仕訳を検索------------------
        DC = DayCheck(FinalList, D_var, D_coltxt, "ALL")
        if DC[0] is True:
            # ------------------------------------------------------------------
            # 入出金列の判定(値が数値のみの場合入出金列として判定)
            l_c = 0
            for OCRColItem in OCRColNames:
                if I == OCRColItem.replace('"', "").replace('"', ""):
                    if OCR_data_Row[l_c] != "":
                        M_var = OCR_data_Row[l_c]
                        try:
                            M_var = int(M_var)
                            IO = "入金"
                        except:
                            IO = "出金"
                elif O == OCRColItem.replace('"', "").replace('"', ""):
                    if OCR_data_Row[l_c] != "":
                        M_var = OCR_data_Row[l_c]
                        try:
                            M_var = int(M_var)
                            IO = "出金"
                        except:
                            IO = "入金"
                l_c += 1
            # ------------------------------------------------------------------
            MC = MoneyCheck(DC[1], M_var, M_coltxt, "ALL")
            print(MC[0])
            Nind = NPS_FLOW(
                HukugouKey,
                TotalFinalList,
                MC[1],
            )
            return Nind[0], Nind[1], IO
    except:
        return False, "", ""


# ----------------------------------------------------------------------------
def NPS_Sort(
    FL,
    TotalFinalList,
    FinalList,
):
    try:
        np_h = FinalList[0, :]
        # 末尾含め3列削除-------------------------------------
        np_h_c = np_h.shape[0] - 1
        for np_hItem in reversed(np_h):
            if "一致率" == np_hItem and FL == np_hItem:
                F_List = FinalList[1:, np_h_c]
                F_List = np.where(F_List == max(F_List))
                FinalList = FinalList[1:, :]
                FinalList = FinalList[F_List]
                FinalList = np.vstack((np_h, FinalList))
                break
            elif "日付一致率" == np_hItem and FL == np_hItem:
                F_List = FinalList[1:, np_h_c]
                FinalList = FinalList[1:, :]
                FinalList = np.vstack((np_h, FinalList))
                break
            elif "仕訳金額差額" == np_hItem and FL == np_hItem:
                F_List = FinalList[1:, np_h_c]
                FinalList = FinalList[1:, :]
                FinalList = np.vstack((np_h, FinalList))
                break
            np_h_c -= 1
        # ---------------------------------------------------
        TotalFinalList = FinalList
        return True, TotalFinalList
    except:
        return False, ""


# ----------------------------------------------------------------------------
def NPS_FLOW(
    HukugouKey,
    TotalFinalList,
    FinalList,
):
    try:
        np_h = FinalList[0, :]
        # 末尾含め3列削除-------------------------------------
        np_h_c = np_h.shape[0] - 1
        for np_hItem in reversed(np_h):
            if "一致率" == np_hItem:
                FinalList = NPS_Sort("一致率", TotalFinalList, FinalList)
                if FinalList[0] is True:
                    FinalList = FinalList[1]
                    FinalList = np.delete(FinalList, np_h_c, 1)
                    np_h = np.delete(np_h, np_h_c, 0)
                else:
                    print("一致率ソートで失敗")
            elif "日付一致率" == np_hItem:
                FinalList = NPS_Sort("日付一致率", TotalFinalList, FinalList)
                if FinalList[0] is True:
                    FinalList = FinalList[1]
                    FinalList = np.delete(FinalList, np_h_c, 1)
                    np_h = np.delete(np_h, np_h_c, 0)
                else:
                    print("日付一致率ソートで失敗")
            elif "仕訳金額差額" == np_hItem:
                FinalList = NPS_Sort("仕訳金額差額", TotalFinalList, FinalList)
                if FinalList[0] is True:
                    FinalList = FinalList[1]
                    FinalList = np.delete(FinalList, np_h_c, 1)
                    np_h = np.delete(np_h, np_h_c, 0)
                else:
                    print("仕訳金額差額ソートで失敗")
            np_h_c -= 1
        # ---------------------------------------------------
        TotalFinalList = FinalList
        TR = TotalFinalList.shape[0]
        if TR > 2:
            for TR_r in reversed(range(TR)):
                if TR_r != 0:
                    TFL = TotalFinalList[TR_r]
                    TestList = np.delete(TotalFinalList, TR_r, 0)
                    DP = DiplicateSearch(TestList, TFL)
                    if DP is True:
                        TotalFinalList = np.delete(TotalFinalList, TR_r, 0)
        return True, TotalFinalList
    except:
        return False, ""


# ----------------------------------------------------------------------------
def CheckHukugou(HukugouKey, FinalList):
    """
    抽出仕訳科目の中に複合仕訳科目があるか判定
    """
    # 諸口勘定の名称を変数から抽出
    Hukugou = np.where(FinalList == HukugouKey)
    try:
        if len(Hukugou[0]) != 0:  # 複合キーがリストにふくまれていたら
            # 複合仕訳
            return True
        else:
            return False
    except:
        if len(Hukugou) != 0:  # 複合キーがリストにふくまれていたら
            # 複合仕訳
            return True
        else:
            return False


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
