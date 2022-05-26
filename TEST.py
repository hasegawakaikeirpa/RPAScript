import Function.GCloudVision as GCV
import re
import os
from dateutil.parser import parse
import toml
import pandas as pd


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
        # if "eLTAX受信通知" in PDFDir:
        #     Flag = "eltax"
        # else:
        Flag = ""
        GF = GCV.Bankrentxtver(
            FileURL, 5000, 50, 2500, 5000, 10, 500, "::", 50, Flag, Banktoml["Hirogin"]
        )  # 画像URL,横軸閾値,縦軸閾値,ラベル配置間隔,etax横軸閾値,etax縦軸閾値,etaxラベル配置間隔,ラベル(str),同行として扱う縦間隔
        if GF[0] is True:
            GFTable = GF[1]
            GFRow = len(GFTable)
            # OCR結果を整形----------------------------------------------------------------
            for g in range(GFRow):
                for c in Banktoml["Hirogin"]["MoneyCol"]:
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
                        .replace('"', "")
                    )
                    if len(strs) == 0:
                        GFTable[g][c - 1] = ints
                    elif len(ints) == 0:
                        GFTable[g][c - 1] = strs
                    else:
                        GFTable[g][c - 1] = strs + "::" + ints
            # ----------------------------------------------------------------------------
            # DataFrame作成
            df = pd.DataFrame(GFTable)
            with open(
                r"\\Sv05121a\e\電子ファイル\メッセージボックス\TEST\XYList.csv",
                mode="w",
                encoding="shiftjis",
                errors="ignore",
                newline="",
            ) as f:
                # pandasでファイルオブジェクトに書き込む
                df.to_csv(f, index=False)

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
