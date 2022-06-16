import os
import pandas as pd
import numpy as np
from collections import OrderedDict
import csv
import toml


def DfTuuchou(Banktoml):
    try:
        strList = []
        strs = ""  # テキスト代入変数
        FstrList = []
        with open(
            r"D:\PythonScript\RPAScript\RPAPhoto\PDFeTaxReadForList\XYList3.csv",
            mode="r",
            encoding="shiftjis",
            errors="ignore",
            newline="",
        ) as f:
            # pandasでファイルオブジェクトに書き込む
            dfnp = list(csv.reader(f))
        # ---------------------------------------------------------------------------
        dfRow = len(dfnp)
        InputCount = 0  # テキスト代入変数に代入した回数
        InputSlide = 1  # 現在の編集列番号
        YeqXlistTrrigeer = False
        FontSize = Banktoml["FontSize"]
        # 並び替えたListにループ処理---------------------------------------------------
        for lb in range(1, dfRow):
            btxt = dfnp[lb][1]  # 現在の文字
            bjsonX = dfnp[lb][3]  # 現在の文字の縦軸
            bjsonY = dfnp[lb][2]  # 現在の文字の横軸
            NeDiff = FontSize * Banktoml[str(InputSlide) + "Col"]
            FS = int(dfnp[lb][2])
            LS = int(dfnp[lb - 1][2])
            NextYDiff = FS - LS  # 前の文字との横軸差
            # テキスト代入変数に代入した回数がtomlの値以外なら---------------------------
            if not InputCount == Banktoml[str(InputSlide) + "Col"]:
                if YeqXlistTrrigeer is False:
                    # 横軸値のリスト作成-------------------------------------------------
                    YeqXlist = []  # 行範囲リスト
                    bjsonYMinXRange = []  # 行範囲代入リスト
                    Gyou = bjsonX  # 現在の行の縦軸
                    Yav = []
                    for Yeq in range(len(dfnp)):  # 同行の横軸リスト作成
                        if dfnp[Yeq][3] == bjsonX:
                            YeqXlist.append(int(dfnp[Yeq][2]))
                            if not Yeq == len(dfnp) - 1:
                                # ----------------------------
                                thisT = dfnp[Yeq][1]
                                NextT = dfnp[Yeq + 1][1]
                                if (
                                    thisT.isdecimal() is True
                                    and NextT.isdecimal() is True
                                ):
                                    this = int(dfnp[Yeq][2])
                                    Next = int(dfnp[Yeq + 1][2])
                                    sa = Next - this
                                    if len(Yav) == 0:
                                        if not sa <= 0:
                                            Yav.append(sa)
                                    else:
                                        hei = sum(Yav) / len(Yav)
                                        if not sa <= 0:
                                            if not hei - sa >= (hei / 2):
                                                Yav.append(sa)
                                # ----------------------------
                    for bj in range(Banktoml["ColCount"]):

                        if bj == 0:
                            if (bj + 1) in Banktoml["SmallTXTCol"]:
                                PlusStr = (
                                    FontSize * Banktoml["SmallTXTMag"]
                                ) * Banktoml[str(bj + 1) + "Col"]
                            else:
                                PlusStr = FontSize * Banktoml[str(bj + 1) + "Col"]
                            Fval = min(YeqXlist)  # 行範囲始点
                            # Fval = Banktoml["StartPos"]  # 行範囲始点
                            Lval = PlusStr + Fval  # 行範囲終点
                            bjsonYMinXRange.append([round(Fval), round(Lval)])
                        else:
                            try:
                                KVal = bjsonYMinXRange[bj - 1][1]
                                KValList = []
                                for YeqXlistItem in YeqXlist:
                                    if KVal < YeqXlistItem:
                                        KValList.append(YeqXlistItem)
                                Fval = min(KValList)  # 行範囲始点
                                if (Fval - KVal) > (FontSize * 4):
                                    Fval = FontSize + bjsonYMinXRange[bj - 1][1]
                                if (bj + 1) in Banktoml["SmallTXTCol"]:
                                    PlusStr = (
                                        FontSize * Banktoml["SmallTXTMag"]
                                    ) * Banktoml[str(bj + 1) + "Col"]
                                else:
                                    PlusStr = FontSize * Banktoml[str(bj + 1) + "Col"]
                                # Fval = FontSize + bjsonYMinXRange[bj - 1][1]  # 行範囲始点
                                Lval = PlusStr + Fval  # 行範囲終点
                                bjsonYMinXRange.append([round(Fval), round(Lval)])
                            except:
                                print("文章分けテーブル作成失敗")
                    YeqXlistTrrigeer = True
                    # -----------------------------------------------------------------
                if len(YeqXlist) >= 8:
                    # リスト先頭軸とリスト最終軸の計算
                    try:
                        bjDiff = (
                            bjsonYMinXRange[InputSlide - 1][1]
                            - bjsonYMinXRange[InputSlide - 1][0]
                        )
                    except:
                        bjDiff = 0
                    if bjDiff > 0:
                        # 現在の文字位置が行範囲内ならテキスト代入変数に代入
                        if (
                            bjsonY >= bjsonYMinXRange[InputSlide - 1][0]
                            and bjsonY <= bjsonYMinXRange[InputSlide - 1][1]
                        ):
                            if Gyou == bjsonX:  # 現在の文字縦軸が現在の行の縦軸と一致する場合
                                strs = strs + btxt
                                InputCount += 1
                        else:
                            if NextYDiff > NeDiff:
                                strList.append(strs)
                                strs = ""
                                InputSlide += 1
                                NeDiff = FontSize * Banktoml[str(InputSlide) + "Col"]
                                if NextYDiff > NeDiff:
                                    strList.append("")
                                    InputSlide += 1
                                    InputCount = 0
                                    strs = strs + btxt
                                    InputCount += 1
                                else:
                                    strs = strs + btxt
                                    InputCount += 1
                            else:
                                strList.append(strs)
                                strs = ""
                                InputSlide += 1
                                if not dfnp[lb][3] == dfnp[lb - 1][3]:
                                    InputSlide += 1
                                InputCount = 0
                                strs = strs + btxt
                                InputCount += 1
                            # 現在のスライドが最大行設定と一致する場合
                            if InputSlide - 1 == Banktoml["ColCount"]:
                                strList.append("")
                                InputSlide += 1
                                InputCount = 0
                                strs = strs + btxt
                                InputCount += 1
                                FstrList.append(strList)
                                YeqXlistTrrigeer = False
                                InputSlide = 1
                                strList = []
                            elif InputSlide - 2 == Banktoml["ColCount"]:
                                FstrList.append(strList)
                                YeqXlistTrrigeer = False
                                InputSlide = 1
                                strList = []
                else:
                    # 横軸リストのデータ数が不足していれば読まずにリセット
                    YeqXlistTrrigeer = False
        return True, FstrList
    except:
        return False, ""


# toml読込------------------------------------------------------------------------------
with open(
    os.getcwd() + r"/RPAPhoto/PDFeTaxReadForList/BankSetting.toml", encoding="utf-8"
) as f:
    Banktoml = toml.load(f)
    print(Banktoml)
# -----------------------------------------------------------

DfTuuchou(Banktoml["Momiji"])
