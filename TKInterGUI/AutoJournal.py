import numpy as np

# from tkinter import messagebox

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
            lis = list(nar[:, 1])
            idx = np.argmin(np.abs(np.array(lis) - value))
            print(data[idx])
            indicesArr.append(data[idx][0])
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
def TextCheck(MJS_data, Txt):
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
                InList.append(round((sum(InList) / len(InList)) * 100, 1))  # 一致率を計算し格納
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
        return False, ""


# ----------------------------------------------------------------------------
def IntCheck(MJS_data, Int):
    """
    テキストから曖昧一致抽出
    MJS_data:Numpy配列
    Txt:検索テキスト
    return bool,np.array(一致率表)
    """
    try:
        M_r = MJS_data.shape[0]  # 行数
        InTotalList = []  # 完成リスト
        NoList = []  # インデックス格納用リスト

        for r in range(M_r):
            if r != 0:
                M_s = MJS_data[r].shape[0] - 1
                M_Txt = MJS_data[r][M_s]  # 検索対象の文字列
                try:
                    NoList.append([r, Int - int(M_Txt)])  # 含まれる場合
                except:
                    NoList.append([r, ""])  # 含まれる場合
            # ---------------------------------------------------------------
        InTotalList.append(NoList)  # 完成リストに格納
        nl = nearestList(NoList, 0)
        if nl[0] is True:
            return True, nl[1]
    except:
        return False, ""


# ----------------------------------------------------------------------------
def npCreate(MJS_data, Txt, ColTxt):
    try:
        MJS_Column = MJS_data[0, :]
        CC = ColumCheck(MJS_data, ColTxt)  # 元帳CSVから列名番号を検出
        if CC[0] is True:
            TC = TextCheck(MJS_data[:, CC[1][1]], Txt)  # 検索文字列から一致率リストを作成
            if TC[0] is True:
                TCL = np.floor(TC[1][:, 0]).astype(int)  # インデックスを丸めて整数に
                Pac = TC[1][:, 1]  # 一致率列のみ取り出す
                Pac = Pac.reshape(Pac.shape[0], -1)  # 一致率リストを多次元に変換
                MJS_Column = MJS_Column.reshape(-1, MJS_Column.shape[0])  # 列名リストを多次元に変換
                MJS_Column = np.insert(MJS_Column, MJS_Column.shape[1], "", axis=1)
                index = list(TCL)  # 丸めたインデックスnparrayをリストに
                MJS_data = MJS_data[index, :]  # インデックス一致のリスト作成
                MJS_data = np.hstack((MJS_data, Pac))  # 一致率リストを横連結
                MJS_Column[0][MJS_Column.shape[1] - 1] = "一致率"
                MJS_data = np.vstack((MJS_Column, MJS_data))  # 列名リストを縦連結
                print(MJS_data)
                return True, MJS_data
    except:
        return False, MJS_data


# ----------------------------------------------------------------------------
def DayCheck(MJS_data, Txt, ColTxt):
    try:
        MJS_Column = MJS_data[0, :]
        CC = ColumCheck(MJS_data, ColTxt)  # 元帳CSVから列名番号を検出
        if CC[0] is True:
            TC = TextCheck(MJS_data[:, CC[1][1]], Txt)  # 検索文字列から一致率リストを作成
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
    except:
        return False, MJS_data


# ----------------------------------------------------------------------------
def MoneyCheck(MJS_data, Int, ColTxt):
    try:
        CC = ColumCheck(MJS_data, ColTxt)  # 元帳CSVから列名番号を検出
        if CC[0] is True:
            TC = IntCheck(MJS_data[:, CC[1][1]], Int)  # 検索文字列から一致率リストを作成
            if TC[0] is True:
                index = TC[1]
                MJS_data = MJS_data[index, :]  # インデックス一致のリスト作成
                print(MJS_data)
                return True, MJS_data
    except:
        return False, MJS_data


# ----------------------------------------------------------------------------
def mainListUp(ColTxt, SerchTxt, imgurl, Roolrul, Banktoml, tomltitle):
    MJS_data = np.genfromtxt(Roolrul, dtype=None, delimiter=",")  # 元帳CSVをnp配列に変換
    NPC = npCreate(MJS_data, SerchTxt, ColTxt)
    if NPC[0] is True:
        return NPC[1]


# ----------------------------------------------------------------------------
def main(ColTxt, SerchTxt, imgurl, Roolrul, Banktoml, tomltitle):
    MJS_data = np.genfromtxt(Roolrul, dtype=None, delimiter=",")  # 元帳CSVをnp配列に変換
    # CC = ColumCheck(MJS_data, ColTxt)  # 元帳CSVから列名番号を検出
    # if CC[0] is True:
    #     TC = TextCheck(MJS_data[:, CC[1][1]], SerchTxt)  # 検索文字列から一致率リストを作成
    #     if TC[0] is True:
    #         TCL = np.floor(TC[1][:, 0]).astype(int)  # インデックスを丸めて整数に

    #         index = list(TCL)
    #         print(MJS_data[index, :])
    NPC = npCreate(MJS_data, SerchTxt, ColTxt)
    if NPC[0] is True:
        DC = DayCheck(NPC[1], "01/08/26", "伝票日付")
        if DC[0] is True:
            MC = MoneyCheck(DC[1], 5000, "金額")
            if MC[0] is True:
                print("############################################################")
                print(MC[1])


# -----------------------------------------------------------------------------------------
if __name__ == "__main__":
    global imgurl, Roolrul, Banktoml, tomltitle
    imgurl = r"D:\OCRTESTPDF\PDFTEST\tuka_1page.csv"
    Roolrul = r"D:\PythonScript\RPAScript\TKInterGUI\Mototyou\18_仕訳日記帳.csv"
    tomltitle = "Tuka"
    # toml読込------------------------------------------------------------------------------
    with open(os.getcwd() + r"/TKInterGUI/BankSetting.toml", encoding="utf-8") as f:
        Banktoml = toml.load(f)
        print(Banktoml)
    # -----------------------------------------------------------
    MJS_data = np.genfromtxt(Roolrul, dtype=None, delimiter=",")  # 元帳CSVをnp配列に変換
    NPC = npCreate(MJS_data, "しんきんカード", "摘要")
    if NPC[0] is True:
        DC = DayCheck(NPC[1], "2022/3/31", "伝票日付")
        if DC[0] is True:
            MC = MoneyCheck(DC[1], 14414, "金額")
            if MC[0] is True:
                print("############################################################")
                print(MC[1])
