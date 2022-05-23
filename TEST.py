import Function.GCloudVision as GCV
import re
import os
from dateutil.parser import parse
import toml


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
            GFTColList = []
            GFTParList = []
            # OCR結果を整形----------------------------------------------------------------
            for g in reversed(range(GFRow)):
                if "::" not in GFTable[g]:  # OCR結果行に区切り文字がない場合
                    if GFTable[g].endswith("円") is True:  # OCR結果行が円で終わる場合
                        if Flag == "eltax":  # eltax処理の場合
                            Koumoku = GFTable[g]  # 項目を代入
                            Money = int(re.sub(r"\D", "", GFTable[g]))  # 数値のみ取得
                            Money = "{:,}".format(Money)  # 取り出した数値をカンマ区切りにする
                            Money = Money + "円"  # 末尾に円をつける
                            Koumoku = Koumoku.replace(Money, "")  # 金額と項目名を置換で切り分け
                            if Koumoku.endswith("-") is True:
                                GFTable[g] = (
                                    Koumoku.replace("-", "") + "::-" + Money
                                )  # 区切り文字を挿入
                            else:
                                GFTable[g] = Koumoku + "::" + Money  # 区切り文字を挿入
                            Money = ""
                            Koumoku = ""
                        else:
                            GFTable.pop(g)
                    else:
                        GFTable.pop(g)
            # ----------------------------------------------------------------------------
            GFTCount = 0
            BeLastList = []
            LastList = []
            for GFTableItem in GFTable:
                strCount = str(GFTableItem).count("::")
                if strCount < 4:
                    SGF = str(GFTableItem).split("::")
                    SC = len(SGF)
                    for SI in range(SC):
                        SGFItem = SGF[SI]
                        strCount = str(GFTableItem).count(".")
                        if strCount < 2:
                            if bool(re.search(r"\d", SGFItem)) is True:
                                try:
                                    parse(SGFItem)
                                except:
                                    strc = len(SGFItem)
                                    for s in range(strc):
                                        if not s == strc and not s == 0:
                                            btx = SGFItem[s - 1].isdecimal()
                                            tx = SGFItem[s].isdecimal()
                                            ntx = SGFItem[s + 1].isdecimal()
                        else:
                            strc = len(SGFItem)
                            for s in range(strc):
                                if not s >= (strc - 1) and not s == 0:
                                    btx = SGFItem[s - 1].isdecimal()
                                    tx = SGFItem[s].isdecimal()
                                    ntx = SGFItem[s + 1].isdecimal()
                                    if (
                                        btx is True
                                        and tx is False
                                        and ntx is True
                                        and not SGFItem[s] == ","
                                        and not SGFItem[s] == "."
                                    ):
                                        SGFItem = SGFItem.replace(SGFItem[s], "::")
                                        SGF[SI] = SGFItem
                                        GFTableItem = "::".join(SGF)
                            if "::" not in SGFItem:
                                DTT = re.sub(r"[^0-9]", "", SGFItem)
                                DTTL = []
                                if len(DTT) == 6:
                                    for c in range(len(DTT)):
                                        if c % 2 == 0 and not c == 0:
                                            DTTL.append(".")
                                            DTTL.append(DTT[c])
                                            SGFItem = SGFItem.replace(DTT[c], "")
                                        else:
                                            DTTL.append(DTT[c])
                                            SGFItem = SGFItem.replace(DTT[c], "")
                                    CDA = "".join(DTTL)
                                    SGF[SI] = CDA + "::" + SGFItem
                                    GFTableItem = "::".join(SGF)

                SGF = str(GFTableItem).split("::")
                SC = len(SGF)
                for SI in range(SC):
                    SGFItem = SGF[SI]
                    try:
                        if len(SGFItem) >= 8:
                            parse(SGFItem)
                            LastList.append(SGFItem)
                        elif bool(re.search(r"\d", SGFItem)) is True:
                            SGFItem = re.sub(r"[^0-9]", "", SGFItem)
                            LastList.append(SGFItem)
                        else:
                            LastList.append(SGFItem)
                    except:
                        if bool(re.search(r"\d", SGFItem)) is True:
                            SGFItem = re.sub(r"[^0-9]", "", SGFItem)
                            LastList.append(SGFItem)
                        else:
                            LastList.append(SGFItem)
                BeLastList.append(LastList)
                LastList = []
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
