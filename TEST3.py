import numpy as np
import Function.CSVOut as CSVO
import TKInterGUI.AutoJournal as AJ


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


csvurl = r"D:\OCRTESTPDF\PDFTEST\Hirogin_1page.csv"
AJurl = r"D:\OCRTESTPDF\PDFTEST\Hirogin_1page_AutoJounal.csv"
AJSeturl = r"D:\OCRTESTPDF\PDFTEST\AJSet.csv"
Roolurl = r"D:\OCRTESTPDF\PDFTEST\1_仕訳日記帳.csv"
ChangeTxtURL = r"D:\OCRTESTPDF\PDFTEST\ChangeTxtList.csv"

FileNameenc = CSVO.getFileEncoding(csvurl)
JounalFileNameenc = CSVO.getFileEncoding(AJurl)
Roolurlenc = CSVO.getFileEncoding(Roolurl)
ChangeTxtURLenc = CSVO.getFileEncoding(ChangeTxtURL)

OCR_data = np.genfromtxt(
    csvurl, dtype=None, encoding=FileNameenc, delimiter=","
)  # 元帳CSVをnp配列に変換
MJS_data = np.genfromtxt(
    Roolurl, dtype=None, encoding=Roolurlenc, delimiter=","
)  # 元帳CSVをnp配列に変換
ChangeTxt_data = np.genfromtxt(
    ChangeTxtURL, dtype=None, encoding=ChangeTxtURLenc, delimiter=","
)  # 元帳CSVをnp配列に変換

SetList = ["摘要", "出金", "入金", "摘要"]
l_r = 3


SerchTxt = RensouTextCheck(
    OCR_data,
    MJS_data,
    ChangeTxt_data,
    SetList,
    l_r,
)

NPC = AJ.npCreate(MJS_data, SerchTxt, "摘要", "ALL")

if NPC[0] is True:
    N_Arr = NPC[1]
    N_clen = len(N_Arr[0]) - 1
    N_C = np.count_nonzero(N_Arr[:, N_clen] == "100", axis=0)
    print(N_C)
    if N_C >= 2:
        ind = np.where(N_Arr[:, N_clen] == "100")
        print(N_Arr[ind])
        Hukugou = np.where(N_Arr[ind] == "複合")
        if len(Hukugou) != 0:
            print("複合")
        else:
            print("not複合")
