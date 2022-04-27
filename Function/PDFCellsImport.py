﻿import os
import numpy as np
import pandas as pd


def ChangeBusyu(strs):
    try:
        MeUrl = os.getcwd().replace("\\", "/")  # 自分のパス
        df = pd.read_csv(MeUrl + "/Function/cmap置換.csv", encoding="utf8")
        npdf = np.array(df)
        lstr = len(strs)
        npdfRow = npdf.shape[0]
        Cst = ""
        for s in range(lstr):
            CF = False
            for d in range(npdfRow):
                Key = npdf[d, 3]
                Tar = npdf[d, 4]
                if strs[s] == Key:
                    strs.replace(strs[s], Tar)
                    CF = True
                    break
                else:
                    CF = False
            if CF is True:
                Cst += Tar
            else:
                Cst += strs[s]
        return Cst
    except:
        return ""


# --------------------------------------------------------------------------------------------------
def CellsAction(stt, cellsList, ColumList, TxtList):  # 主にeltax処理
    try:
        ColumFlag = False  # カラム対象フラグ
        TFlag = False  # テキスト取得対象フラグ
        txts = []
        for cellsListItem in cellsList:  # セルループ
            txt = repr(cellsListItem[1].text)  # 改行コードの数でセル分割の判定
            nc = txt.count(r"\n")  # テキスト内の改行コードの数
            if txt.endswith(r"\n") is True:  # テキスト内の最後の改行コードは省く
                nc -= 1
            if nc >= 2:  # テキスト内に改行コードが2つ以上ある場合
                txts = txt.split(r"\n")  # テキストを改行コードで分割する
                txtsc = len(txts)  # 改行コード分割後のリスト要素数
                for tx in range(txtsc):  # 改行コード分割後のリストを置換
                    txts[tx] = (
                        txts[tx]
                        .replace("'", "")
                        .replace('"', "")
                        .replace(r"\xa", "")
                        .replace(r"\n", "")
                        .replace(r"\u2003", " ")
                        .replace(r"\u3000", " ")
                    )
                    txts[tx] = ChangeBusyu(txts[tx])
                and_list = set(txts) & set(stt)  # テキストリストとカラムリストで一致する要素を抽出
                if len(and_list) > 0:  # テキストリストとカラムリストで一致する要素が一つ以上なら
                    TFlag = True  # テキスト取得対象フラグを立てる
                # テキスト取得対象の処理--------------------------------------------------------
                if TFlag is True:
                    for tc in range(txtsc):  # 分割後のリストループ
                        # ヘッダー判定後の処理--------------------------------------------------
                        if tc % 2 == 0:  # 2で割り切れたらヘッダー
                            # 処理中のテキストがカラムリストにあるか判定--------------------------
                            for sttItem in stt:
                                st = txts[tc]
                                if st == sttItem:
                                    ColumFlag = True  # カラム対象フラグを立てる
                                    break
                            # ----------------------------------------------------------------
                            # テキスト内の改行コード総数が3で割り切れる場合------------------------
                            if nc % 3 == 0 and tc == 0:  # テキスト内初回の処理
                                ColumList.append("項目")  # 項目リストに代入
                            if ColumFlag is True:  # テキスト内2回目以降でカラム対象フラグが立っている処理
                                ColumList.append(st)  # 項目リストに代入
                                ColumFlag = False  # カラム対象フラグ解除
                            else:
                                if TFlag is True:
                                    if not txts[tc] == "" and not txts[tc] == " ":
                                        TxtList.append(st)  # テキストリストに代入
                            # ----------------------------------------------------------------
                        else:
                            if not txts[tc] == "" and not txts[tc] == " ":
                                tsc = txts[tc]
                                if tsc.startswith(" ") is True:
                                    tsc = tsc.replace(" ", "")
                                TxtList.append(tsc)  # テキストリストに代入
                        # ---------------------------------------------------------------------
                    TFlag = False
                # -----------------------------------------------------------------------------
            else:
                txts = repr(cellsListItem[0].text.replace(r"\n", ""))  # 改行コード判定の為repr
                txts = (
                    txts.replace("'", "")
                    .replace('"', "")
                    .replace(r"\xa", "")
                    .replace(r"\n", "")
                    .replace(r"\u2003", " ")
                    .replace(r"\u3000", " ")
                )
                txts = ChangeBusyu(txts)
                if txts.startswith(" ") is True:
                    txts.replace(" ", "")
                ColumList.append(txts)  # 項目リストに代入
                txts = repr(cellsListItem[1].text.replace(r"\n", ""))  # 改行コード判定の為repr
                txts = (
                    txts.replace("'", "")
                    .replace('"', "")
                    .replace(r"\xa", "")
                    .replace(r"\n", "")
                    .replace(r"\u2003", " ")
                    .replace(r"\u3000", " ")
                )
                txts = ChangeBusyu(txts)
                if txts.startswith(" ") is True:
                    txts.replace(" ", "")
                TxtList.append(txts)  # テキストリストに代入
        return True, ColumList, TxtList
    except:
        return False, "", ""


# --------------------------------------------------------------------------------------------------
def CellsActionJigyounendo(stt, cellsList, ColumList, TxtList):  # 主にeltax処理
    try:
        ColumFlag = False  # カラム対象フラグ
        TFlag = False  # テキスト取得対象フラグ
        txts = []
        cicount = 0
        for cellsListItem in cellsList:  # セルループ
            Skiprows = False
            for cLIItem in cellsListItem:  # セルループ
                if "月数換算" in cLIItem.text:
                    Skiprows = True
            if Skiprows is False:
                for cLIItem in cellsListItem:  # セルループ
                    if len(ColumList) == 4:
                        ColumList.append("前事業年度等")
                    txt = repr(cLIItem.text)  # 改行コードの数でセル分割の判定
                    # テキスト検出ミスの修正-------------------------------------------
                    if (
                        "日 修正・更正・決定の年月日\\n" in txt
                        or "円 前課税" in txt
                        or "円 同上" in txt
                        or "円 差引" in txt
                        or "円 納付" in txt
                    ):
                        txtsp = txt.split(" ")
                        for txtspItem in txtsp:
                            txtspItem = (
                                txtspItem.replace("'", "")
                                .replace('"', "")
                                .replace(r"\xa", "")
                                .replace(r"\n", "")
                                .replace(r"\u2003", " ")
                                .replace(r"\u3000", " ")
                            )
                            txtspItem = ChangeBusyu(txtspItem)
                            # 処理中のテキストがカラムリストにあるか判定--------------------------
                            for sttItem in stt:
                                st = txtspItem
                                if st == sttItem:
                                    ColumFlag = True  # カラム対象フラグを立てる
                                    break
                            # ----------------------------------------------------------------
                            if not st == "" and not st == " ":
                                if st.startswith(" ") is True:
                                    st = st.replace(" ", "")
                                if ColumFlag is True:
                                    ColumList.append(st)
                                    ColumFlag = False
                                else:
                                    TxtList.append(st)  # テキストリストに代入
                    else:
                        # ----------------------------------------------------------------
                        nc = txt.count(r"\n")  # テキスト内の改行コードの数
                        if txt.endswith(r"\n") is True:  # テキスト内の最後の改行コードは省く
                            nc -= 1
                        if nc >= 2:  # テキスト内に改行コードが2つ以上ある場合
                            txts = txt.split(r"\n")  # テキストを改行コードで分割する
                            txtsc = len(txts)  # 改行コード分割後のリスト要素数
                            for tx in range(txtsc):  # 改行コード分割後のリストを置換
                                txts[tx] = (
                                    txts[tx]
                                    .replace("'", "")
                                    .replace('"', "")
                                    .replace(r"\xa", "")
                                    .replace(r"\n", "")
                                    .replace(r"\u2003", " ")
                                    .replace(r"\u3000", " ")
                                )
                                txts[tx] = ChangeBusyu(txts[tx])
                            and_list = set(txts) & set(stt)  # テキストリストとカラムリストで一致する要素を抽出
                            if len(and_list) > 0:  # テキストリストとカラムリストで一致する要素が一つ以上なら
                                TFlag = True  # テキスト取得対象フラグを立てる
                            # テキスト取得対象の処理--------------------------------------------------------
                            if TFlag is True:
                                al = str(and_list).replace("{'", "").replace("'}", "")
                                if al == "同上のうち土地譲渡税額等及":
                                    # 処理中のテキストがカラムリストにあるか判定--------------------------
                                    for sttItem in stt:
                                        st = txts[0]
                                        if st == sttItem:
                                            ColumFlag = True  # カラム対象フラグを立てる
                                            break
                                    # ----------------------------------------------------------------
                                    if ColumFlag is True:  # テキスト内2回目以降でカラム対象フラグが立っている処理
                                        ColumList.append(st)  # 項目リストに代入
                                        ColumFlag = False  # カラム対象フラグ解除
                                    else:
                                        if TFlag is True:
                                            if not txts[0] == "" and not txts[0] == " ":
                                                TxtList.append(st)  # テキストリストに代入
                                    # ----------------------------------------------------------------
                                else:
                                    for tc in range(txtsc):  # 分割後のリストループ
                                        # ヘッダー判定後の処理--------------------------------------------------
                                        if tc % 2 == 0:  # 2で割り切れたらヘッダー
                                            # 処理中のテキストがカラムリストにあるか判定--------------------------
                                            for sttItem in stt:
                                                st = txts[tc]
                                                if st == sttItem:
                                                    ColumFlag = True  # カラム対象フラグを立てる
                                                    break
                                            # ----------------------------------------------------------------
                                            if (
                                                ColumFlag is True
                                            ):  # テキスト内2回目以降でカラム対象フラグが立っている処理
                                                ColumList.append(st)  # 項目リストに代入
                                                ColumFlag = False  # カラム対象フラグ解除
                                            else:
                                                if TFlag is True:
                                                    if (
                                                        not txts[tc] == ""
                                                        and not txts[tc] == " "
                                                    ):
                                                        TxtList.append(st)  # テキストリストに代入
                                            # ----------------------------------------------------------------
                                        else:
                                            if (
                                                not txts[tc] == ""
                                                and not txts[tc] == " "
                                            ):
                                                tsc = txts[tc]
                                                if tsc.startswith(" ") is True:
                                                    tsc = tsc.replace(" ", "")
                                                TxtList.append(tsc)  # テキストリストに代入
                                        # ---------------------------------------------------------------------
                                    TFlag = False
                                # -----------------------------------------------------------------------------
                        else:
                            txts = txt.split(r"\n")  # テキストを改行コードで分割する
                            txtsc = len(txts)  # 改行コード分割後のリスト要素数
                            for tx in range(txtsc):  # 改行コード分割後のリストを置換
                                txts[tx] = (
                                    txts[tx]
                                    .replace("'", "")
                                    .replace('"', "")
                                    .replace(r"\xa", "")
                                    .replace(r"\n", "")
                                    .replace(r"\u2003", " ")
                                    .replace(r"\u3000", " ")
                                )
                                txts[tx] = ChangeBusyu(txts[tx])
                            and_list = set(txts) & set(stt)  # テキストリストとカラムリストで一致する要素を抽出
                            if len(and_list) > 0:  # テキストリストとカラムリストで一致する要素が一つ以上なら
                                TFlag = True  # テキスト取得対象フラグを立てる
                            # テキスト取得対象の処理--------------------------------------------------------
                            if TFlag is True:
                                al = str(and_list).replace("{'", "").replace("'}", "")
                                if al == "同上のうち土地譲渡税額等及":
                                    # 処理中のテキストがカラムリストにあるか判定--------------------------
                                    for sttItem in stt:
                                        st = txts[0]
                                        if st == sttItem:
                                            ColumFlag = True  # カラム対象フラグを立てる
                                            break
                                    # ----------------------------------------------------------------
                                    if ColumFlag is True:  # テキスト内2回目以降でカラム対象フラグが立っている処理
                                        ColumList.append(st)  # 項目リストに代入
                                        ColumFlag = False  # カラム対象フラグ解除
                                    else:
                                        if TFlag is True:
                                            if not txts[0] == "" and not txts[0] == " ":
                                                TxtList.append(st)  # テキストリストに代入
                                    # ----------------------------------------------------------------
                                else:
                                    for tc in range(txtsc):  # 分割後のリストループ
                                        # ヘッダー判定後の処理--------------------------------------------------
                                        if tc % 2 == 0:  # 2で割り切れたらヘッダー
                                            # 処理中のテキストがカラムリストにあるか判定--------------------------
                                            for sttItem in stt:
                                                st = txts[tc]
                                                if st == sttItem:
                                                    ColumFlag = True  # カラム対象フラグを立てる
                                                    break
                                            # ----------------------------------------------------------------
                                            if (
                                                ColumFlag is True
                                            ):  # テキスト内2回目以降でカラム対象フラグが立っている処理
                                                st = (
                                                    st.replace("'", "")
                                                    .replace('"', "")
                                                    .replace(r"\xa", "")
                                                    .replace(r"\n", "")
                                                    .replace(r"\u2003", " ")
                                                    .replace(r"\u3000", " ")
                                                )
                                                if (
                                                    not st == ""
                                                    and not st == " "
                                                    and not st == "殿"
                                                    and not st == "法人税額の計算"
                                                    and not st == "地方法人税額の計算"
                                                ):
                                                    ColumList.append(st)  # 項目リストに代入
                                                    ColumFlag = False  # カラム対象フラグ解除
                                            else:
                                                if TFlag is True:
                                                    if (
                                                        not txts[tc] == ""
                                                        and not txts[tc] == " "
                                                    ):
                                                        TxtList.append(st)  # テキストリストに代入
                                            # ----------------------------------------------------------------
                                        else:
                                            if (
                                                not txts[tc] == ""
                                                and not txts[tc] == " "
                                                and ColumFlag is not False
                                            ):
                                                tsc = txts[tc]
                                                if tsc.startswith(" ") is True:
                                                    tsc = tsc.replace(" ", "")
                                                TxtList.append(tsc)  # テキストリストに代入
                                        # ---------------------------------------------------------------------
                    cicount += 1
        return True, ColumList, TxtList
    except:
        return False, "", ""


# --------------------------------------------------------------------------------------------------
def CellsActionOsirase(stt, cellsList, ColumList, TxtList):  # 申告のお知らせ処理
    try:
        ColumFlag = False  # カラム対象フラグ
        TFlag = False  # テキスト取得対象フラグ
        txts = []
        cicount = 0
        for cellsListItem in cellsList:  # セルループ
            if cicount >= 2:
                for cLIItem in cellsListItem:  # セルループ
                    if len(ColumList) == 4:
                        ColumList.append("項目")
                    elif len(ColumList) == 7:
                        ColumList.append("社名")
                    elif len(ColumList) == 8:
                        ColumList.append("氏名")
                    elif len(ColumList) == 9:
                        ColumList.append("相手氏名")
                    elif len(ColumList) == 10:
                        ColumList.append("件名")
                    elif len(TxtList) == 10:
                        TxtList.append("申告のお知らせ")
                    txt = repr(cLIItem.text)  # 改行コードの数でセル分割の判定
                    nc = txt.count(r"\n")  # テキスト内の改行コードの数
                    if txt.endswith(r"\n") is True:  # テキスト内の最後の改行コードは省く
                        nc -= 1
                    if nc >= 2:  # テキスト内に改行コードが2つ以上ある場合
                        txts = txt.split(r"\n")  # テキストを改行コードで分割する
                        txtsc = len(txts)  # 改行コード分割後のリスト要素数
                        for tx in range(txtsc):  # 改行コード分割後のリストを置換
                            txts[tx] = (
                                txts[tx]
                                .replace("'", "")
                                .replace('"', "")
                                .replace(r"\xa", "")
                                .replace(r"\n", "")
                                .replace(r"\u2003", " ")
                                .replace(r"\u3000", " ")
                            )
                            txts[tx] = ChangeBusyu(txts[tx])
                        and_list = set(txts) & set(stt)  # テキストリストとカラムリストで一致する要素を抽出
                        if len(and_list) > 0:  # テキストリストとカラムリストで一致する要素が一つ以上なら
                            TFlag = True  # テキスト取得対象フラグを立てる
                        # テキスト取得対象の処理--------------------------------------------------------
                        if TFlag is True:
                            for tc in range(txtsc):  # 分割後のリストループ
                                # ヘッダー判定後の処理--------------------------------------------------
                                if tc % 2 == 0:  # 2で割り切れたらヘッダー
                                    # 処理中のテキストがカラムリストにあるか判定--------------------------
                                    for sttItem in stt:
                                        st = txts[tc]
                                        if st == sttItem:
                                            ColumFlag = True  # カラム対象フラグを立てる
                                            break
                                    # ----------------------------------------------------------------
                                    # テキスト内の改行コード総数が3で割り切れる場合------------------------
                                    if nc % 3 == 0 and tc == 0:  # テキスト内初回の処理
                                        ColumList.append("項目")  # 項目リストに代入
                                    if ColumFlag is True:  # テキスト内2回目以降でカラム対象フラグが立っている処理
                                        ColumList.append(st)  # 項目リストに代入
                                        ColumFlag = False  # カラム対象フラグ解除
                                    else:
                                        if TFlag is True:
                                            if (
                                                not txts[tc] == ""
                                                and not txts[tc] == " "
                                            ):
                                                TxtList.append(st)  # テキストリストに代入
                                    # ----------------------------------------------------------------
                                else:
                                    if not txts[tc] == "" and not txts[tc] == " ":
                                        tsc = txts[tc]
                                        if tsc.startswith(" ") is True:
                                            tsc = tsc.replace(" ", "")
                                        TxtList.append(tsc)  # テキストリストに代入
                                # ---------------------------------------------------------------------
                            TFlag = False
                        # -----------------------------------------------------------------------------
                    else:
                        if not len(TxtList) >= 10:
                            txts = repr(
                                cLIItem.text.replace(r"\n", "")
                            )  # 改行コード判定の為repr
                            txts = (
                                txts.replace("'", "")
                                .replace('"', "")
                                .replace(r"\xa", "")
                                .replace(r"\n", "")
                                .replace(r"\u2003", " ")
                                .replace(r"\u3000", " ")
                            )
                            txts = ChangeBusyu(txts)
                            if txts.startswith(" ") is True:
                                txts.replace(" ", "")
                            if not txts == "" and not txts == " " and not txts == "殿":
                                TxtList.append(txts)  # テキストリストに代入
                cicount += 1
            else:
                cicount += 1
        return True, ColumList, TxtList
    except:
        return False, "", ""


# --------------------------------------------------------------------------------------------------
def CellsImport(Settingtoml, SCode, path_pdf, tables, page, TaxType):
    try:
        # MeUrl = os.getcwd().replace("\\", "/")  # 自分のパス
        # # toml読込------------------------------------------------------------------------------
        # with open(
        #     MeUrl + r"/RPAPhoto/PDFReadForList/Setting.toml", encoding="utf-8"
        # ) as f:
        #     Settingtoml = toml.load(f)
        #     print(Settingtoml)
        # # ----------------------------------------------------------------------------------------
        ColumList = []  # 項目リスト
        TxtList = []  # テキストリスト
        cellsList = list(tables._tables[page].cells)  # セル情報のリスト

        # 固定パラメーターを挿入------------------------------------------------
        ColumList.append("URL")
        ColumList.append("ページ")
        ColumList.append("コード")
        TxtList.append(path_pdf.replace("/", "\\"))
        TxtList.append(str(page + 1) + "ページ")
        TxtList.append(str(SCode))
        # --------------------------------------------------------------------
        if "etaxosirase" == TaxType:
            stt = Settingtoml["CsvSaveEnc"][TaxType]
            CA = CellsActionOsirase(stt, cellsList, ColumList, TxtList)
        elif "eltaxList" == TaxType:
            stt = Settingtoml["CsvSaveEnc"][TaxType]
            CA = CellsAction(stt, cellsList, ColumList, TxtList)
        elif "etaxjigyounendo" == TaxType:
            stt = Settingtoml["CsvSaveEnc"][TaxType]
            CA = CellsActionJigyounendo(stt, cellsList, ColumList, TxtList)
        else:
            stt = Settingtoml["CsvSaveEnc"][TaxType]
            CA = CellsAction(stt, cellsList, ColumList, TxtList)
        if CA[0] is True:
            return CA
        else:
            return CA
    except:
        print("CellsImport中のエラー")
        return False, "CellsImport中のエラー", ""


# ----------------------------------------------------------------------------------------------
