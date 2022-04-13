import os
import numpy as np
import Function.CSVOut as FCSV


def PDFSetting(
    dfIndexdata,
    SinkokuCSV,
    SinkokuCSV2,
    SinkokuCSV3,
    SinkokuCSV4,
    SyotokuCSV,
    SyotokuCSV2,
    SyotokuCSV3,
    SyotokuCSV4,
    SyouhiCSV,
    SyouhiCSV2,
    SyouhiCSV3,
    SyouhiCyukanCSV,
    YoteiCSV,
    HoujinCSV,
    HoujinSiminCSV,
    SyoukyakuCSV,
    SyoukyakuCSV2,
    ZouyoCSV,
    ZaisanCSV,
    SinkokuUkeCSV,
    ImageCSV,
):
    # 確定申告リストと突合------------------------------------------------------
    IndexFlags = SinkokuCSV == dfIndexdata
    FolseC = IndexFlags.sum(axis=1) - np.array(dfIndexdata).shape[0]
    if FolseC[0] >= -2:
        PDFFlag = "確定申告"
    # ------------------------------------------------------------------------
    # 確定申告リスト2と突合------------------------------------------------------
    IndexFlags = SinkokuCSV2 == dfIndexdata
    FolseC = IndexFlags.sum(axis=1) - np.array(dfIndexdata).shape[0]
    if FolseC[0] >= -2:
        PDFFlag = "確定申告2"
    # ------------------------------------------------------------------------
    # 確定申告リスト3と突合------------------------------------------------------
    IndexFlags = SinkokuCSV3 == dfIndexdata
    FolseC = IndexFlags.sum(axis=1) - np.array(dfIndexdata).shape[0]
    if FolseC[0] >= -2:
        PDFFlag = "確定申告3"
    # ------------------------------------------------------------------------
    # 確定申告リスト4と突合------------------------------------------------------
    IndexFlags = SinkokuCSV4 == dfIndexdata
    FolseC = IndexFlags.sum(axis=1) - np.array(dfIndexdata).shape[0]
    if FolseC[0] >= -2:
        PDFFlag = "確定申告4"
    # ------------------------------------------------------------------------
    # 所得税リストと突合--------------------------------------------------------
    IndexFlags = SyotokuCSV == dfIndexdata
    FolseC = IndexFlags.sum(axis=1) - np.array(dfIndexdata).shape[0]
    if FolseC[0] >= -2:
        PDFFlag = "所得税"
    # ------------------------------------------------------------------------
    # 所得税2リストと突合--------------------------------------------------------
    IndexFlags = SyotokuCSV2 == dfIndexdata
    FolseC = IndexFlags.sum(axis=1) - np.array(dfIndexdata).shape[0]
    if FolseC[0] >= -2:
        PDFFlag = "所得税2"
    # ------------------------------------------------------------------------
    # 所得税3リストと突合--------------------------------------------------------
    IndexFlags = SyotokuCSV3 == dfIndexdata
    FolseC = IndexFlags.sum(axis=1) - np.array(dfIndexdata).shape[0]
    if FolseC[0] >= -2:
        PDFFlag = "所得税3"
    # ------------------------------------------------------------------------
    # 所得税4リストと突合--------------------------------------------------------
    IndexFlags = SyotokuCSV4 == dfIndexdata
    FolseC = IndexFlags.sum(axis=1) - np.array(dfIndexdata).shape[0]
    if FolseC[0] >= -2:
        PDFFlag = "所得税4"
    # ------------------------------------------------------------------------
    # 消費税リストと突合--------------------------------------------------------
    IndexFlags = SyouhiCSV == dfIndexdata
    FolseC = IndexFlags.sum(axis=1) - np.array(dfIndexdata).shape[0]
    if FolseC[0] >= -2:
        PDFFlag = "消費税"
    # ------------------------------------------------------------------------
    # 消費税リストと突合--------------------------------------------------------
    IndexFlags = SyouhiCSV2 == dfIndexdata
    FolseC = IndexFlags.sum(axis=1) - np.array(dfIndexdata).shape[0]
    if FolseC[0] >= -2:
        PDFFlag = "消費税2"
    # ------------------------------------------------------------------------
    # 消費税リストと突合--------------------------------------------------------
    IndexFlags = SyouhiCSV3 == dfIndexdata
    FolseC = IndexFlags.sum(axis=1) - np.array(dfIndexdata).shape[0]
    if FolseC[0] >= -2:
        PDFFlag = "消費税3"
    # ------------------------------------------------------------------------
    # 消費税中間リストと突合--------------------------------------------------------
    IndexFlags = SyouhiCyukanCSV == dfIndexdata
    FolseC = IndexFlags.sum(axis=1) - np.array(dfIndexdata).shape[0]
    if FolseC[0] >= -2:
        PDFFlag = "消費税中間申告"
    # ------------------------------------------------------------------------
    # 予定申告リストと突合------------------------------------------------------
    IndexFlags = YoteiCSV == dfIndexdata
    FolseC = IndexFlags.sum(axis=1) - np.array(dfIndexdata).shape[0]
    if FolseC[0] >= -2:
        PDFFlag = "予定申告"
    # ------------------------------------------------------------------------
    # 法人税リストと突合--------------------------------------------------------
    IndexFlags = HoujinCSV == dfIndexdata
    FolseC = IndexFlags.sum(axis=1) - np.array(dfIndexdata).shape[0]
    if FolseC[0] >= -2:
        PDFFlag = "法人税"
    # ------------------------------------------------------------------------
    # 法人税市民税リストと突合--------------------------------------------------
    IndexFlags = HoujinSiminCSV == dfIndexdata
    FolseC = IndexFlags.sum(axis=1) - np.array(dfIndexdata).shape[0]
    if FolseC[0] >= -2:
        PDFFlag = "法人市民税"
    # ------------------------------------------------------------------------
    # 贈与税リストと突合--------------------------------------------------------
    IndexFlags = ZouyoCSV == dfIndexdata
    FolseC = IndexFlags.sum(axis=1) - np.array(dfIndexdata).shape[0]
    if FolseC[0] >= -2:
        PDFFlag = "贈与税"
    # ------------------------------------------------------------------------
    # 財産債務リストと突合--------------------------------------------------------
    IndexFlags = ZaisanCSV == dfIndexdata
    FolseC = IndexFlags.sum(axis=1) - np.array(dfIndexdata).shape[0]
    if FolseC[0] >= -2:
        PDFFlag = "財産債務"
    # ------------------------------------------------------------------------
    # 申告受付リストと突合--------------------------------------------------------
    IndexFlags = SinkokuUkeCSV == dfIndexdata
    FolseC = IndexFlags.sum(axis=1) - np.array(dfIndexdata).shape[0]
    if FolseC[0] >= -2:
        PDFFlag = "申告受付通知"
    # ------------------------------------------------------------------------
    # イメージ添付書類リストと突合--------------------------------------------------------
    IndexFlags = ImageCSV == dfIndexdata
    FolseC = IndexFlags.sum(axis=1) - np.array(dfIndexdata).shape[0]
    if FolseC[0] >= -2:
        PDFFlag = "イメージ添付書類"
    # ------------------------------------------------------------------------
    # 償却資産リストと突合------------------------------------------------------
    IndexFlags = SyoukyakuCSV == dfIndexdata
    FolseC = IndexFlags.sum(axis=1) - np.array(dfIndexdata).shape[0]
    if FolseC[0] >= -2:
        try:
            PDFFlag
            if PDFFlag == "法人税" or PDFFlag == "法人市民税":
                if "課税所在地" in dfIndexdata:
                    PDFFlag = "償却資産"
                else:
                    print("法人から償却への変更なし")
            else:
                PDFFlag = "償却資産"
        except:
            PDFFlag = "償却資産"
    # ------------------------------------------------------------------------
    # 償却資産2リストと突合------------------------------------------------------
    IndexFlags = SyoukyakuCSV2 == dfIndexdata
    FolseC = IndexFlags.sum(axis=1) - np.array(dfIndexdata).shape[0]
    if FolseC[0] >= -2:
        try:
            PDFFlag
            if PDFFlag == "法人税" or PDFFlag == "法人市民税":
                if "課税所在地" in dfIndexdata:
                    PDFFlag = "償却資産2"
                else:
                    print("法人から償却への変更なし")
            else:
                PDFFlag = "償却資産2"
        except:
            PDFFlag = "償却資産2"
    # ------------------------------------------------------------------------
    return PDFFlag


# 以下変数設定-------------------------------------------------------------------------
MeUrl = os.getcwd().replace("\\", "/")  # 自分のパス
# 各税目のインデックスリストを加工して格納------------------------------------------------
SinkokuCSV = FCSV.CsvReadHeaderless(
    MeUrl + "/RPAPhoto/PDFReadForList/確定申告.CSV"
)  # 内国法人確定申告のインデックスリスト
SinkokuCSV2 = FCSV.CsvReadHeaderless(
    MeUrl + "/RPAPhoto/PDFReadForList/確定申告2.CSV"
)  # 内国法人確定申告のインデックスリスト
SinkokuCSV3 = FCSV.CsvReadHeaderless(
    MeUrl + "/RPAPhoto/PDFReadForList/確定申告3.CSV"
)  # 内国法人確定申告のインデックスリスト
SinkokuCSV4 = FCSV.CsvReadHeaderless(
    MeUrl + "/RPAPhoto/PDFReadForList/確定申告4.CSV"
)  # 内国法人確定申告のインデックスリスト
SyotokuCSV = FCSV.CsvReadHeaderless(
    MeUrl + "/RPAPhoto/PDFReadForList/所得税.CSV"
)  # 所得税のインデックスリスト
SyotokuCSV2 = FCSV.CsvReadHeaderless(
    MeUrl + "/RPAPhoto/PDFReadForList/所得税2.CSV"
)  # 所得税のインデックスリスト
SyotokuCSV3 = FCSV.CsvReadHeaderless(
    MeUrl + "/RPAPhoto/PDFReadForList/所得税3.CSV"
)  # 所得税のインデックスリスト
SyotokuCSV4 = FCSV.CsvReadHeaderless(
    MeUrl + "/RPAPhoto/PDFReadForList/所得税4.CSV"
)  # 所得税のインデックスリスト
SyouhiCSV = FCSV.CsvReadHeaderless(
    MeUrl + "/RPAPhoto/PDFReadForList/消費税.CSV"
)  # 消費税のインデックスリスト
SyouhiCSV2 = FCSV.CsvReadHeaderless(
    MeUrl + "/RPAPhoto/PDFReadForList/消費税2.CSV"
)  # 消費税のインデックスリスト
SyouhiCSV3 = FCSV.CsvReadHeaderless(
    MeUrl + "/RPAPhoto/PDFReadForList/消費税3.CSV"
)  # 消費税のインデックスリスト
SyouhiCyukanCSV = FCSV.CsvReadHeaderless(
    MeUrl + "/RPAPhoto/PDFReadForList/消費税中間申告.CSV"
)  # 消費税のインデックスリスト
HoujinCSV = FCSV.CsvReadHeaderless(
    MeUrl + "/RPAPhoto/PDFReadForList/法人税.CSV"
)  # 法人税のインデックスリスト
HoujinSiminCSV = FCSV.CsvReadHeaderless(
    MeUrl + "/RPAPhoto/PDFReadForList/法人市民税.CSV"
)  # 法人市民税のインデックスリスト
YoteiCSV = FCSV.CsvReadHeaderless(
    MeUrl + "/RPAPhoto/PDFReadForList/予定申告.CSV"
)  # 予定申告のインデックスリスト
SyoukyakuCSV = FCSV.CsvReadHeaderless(
    MeUrl + "/RPAPhoto/PDFReadForList/償却資産.CSV"
)  # 償却資産のインデックスリスト
SyoukyakuCSV2 = FCSV.CsvReadHeaderless(
    MeUrl + "/RPAPhoto/PDFReadForList/償却資産2.CSV"
)  # 償却資産のインデックスリスト
ZouyoCSV = FCSV.CsvReadHeaderless(
    MeUrl + "/RPAPhoto/PDFReadForList/贈与税.CSV"
)  # 償却資産のインデックスリスト
ZaisanCSV = FCSV.CsvReadHeaderless(
    MeUrl + "/RPAPhoto/PDFReadForList/財産債務調書.CSV"
)  # 償却資産のインデックスリスト
SinkokuUkeCSV = FCSV.CsvReadHeaderless(
    MeUrl + "/RPAPhoto/PDFReadForList/申告受付通知.CSV"
)  # 償却資産のインデックスリスト
ImageCSV = FCSV.CsvReadHeaderless(
    MeUrl + "/RPAPhoto/PDFReadForList/イメージ添付書類.CSV"
)  # 償却資産のインデックスリスト
# PDFから抽出したリストと形式があわないので、税目リストを行列入替---------------------------
SinkokuCSV = SinkokuCSV[1].transpose()  # 行列入替
SinkokuCSV2 = SinkokuCSV2[1].transpose()  # 行列入替
SinkokuCSV3 = SinkokuCSV3[1].transpose()  # 行列入替
SinkokuCSV4 = SinkokuCSV4[1].transpose()  # 行列入替
SyotokuCSV = SyotokuCSV[1].transpose()  # 行列入替
SyotokuCSV2 = SyotokuCSV2[1].transpose()  # 行列入替
SyotokuCSV3 = SyotokuCSV3[1].transpose()
SyotokuCSV4 = SyotokuCSV4[1].transpose()  # 行列入替
SyouhiCSV = SyouhiCSV[1].transpose()  # 行列入替
SyouhiCSV2 = SyouhiCSV2[1].transpose()  # 行列入替
SyouhiCSV3 = SyouhiCSV3[1].transpose()  # 行列入替
SyouhiCyukanCSV = SyouhiCyukanCSV[1].transpose()  # 行列入替
HoujinCSV = HoujinCSV[1].transpose()  # 行列入替
HoujinSiminCSV = HoujinSiminCSV[1].transpose()  # 行列入替
YoteiCSV = YoteiCSV[1].transpose()  # 行列入替
SyoukyakuCSV = SyoukyakuCSV[1].transpose()  # 行列入替
SyoukyakuCSV2 = SyoukyakuCSV2[1].transpose()  # 行列入替
ZouyoCSV = ZouyoCSV[1].transpose()  # 行列入替
ZaisanCSV = ZaisanCSV[1].transpose()  # 行列入替
SinkokuUkeCSV = SinkokuUkeCSV[1].transpose()  # 行列入替
ImageCSV = ImageCSV[1].transpose()  # 行列入替
# ------------------------------------------------------------------------------------
SinkokuCSVList = []  # 成功リスト初期化
SinkokuCSV2List = []  # 成功リスト初期化
SinkokuCSV3List = []  # 成功リスト初期化
SinkokuCSV4List = []  # 成功リスト初期化
SyotokuCSVList = []  # 成功リスト初期化
SyotokuCSV2List = []  # 成功リスト初期化
SyotokuCSV3List = []  # 成功リスト初期化
SyotokuCSV4List = []  # 成功リスト初期化
SyouhiCSVList = []  # 成功リスト初期化
SyouhiCSV2List = []  # 成功リスト初期化
SyouhiCSV3List = []  # 成功リスト初期化
SyouhiCyukanCSVList = []
HoujinCSVList = []  # 成功リスト初期化
HoujinSiminCSVList = []
YoteiCSVList = []  # 成功リスト初期化
SyoukyakuCSVList = []  # 成功リスト初期化
SyoukyakuCSV2List = []  # 成功リスト初期化
ZouyoCSVList = []  # 成功リスト初期化
ZaisanCSVList = []  # 成功リスト初期化
SinkokuUkeCSVList = []
TKCListSinsei = []  # 成功リスト初期化
TKCListHTS = []
TKCListHTPDF = []
TKCListSyouhi = []
TKCListSyouhiPDF = []
TKCListTodouhu = []
TKCListSityou = []
ImageCSVList = []
CSVBadList = []  # 失敗リスト初期化
# 関数の引数様にDict格納-------------------------------------------------------------------------
CSVIndexSortFuncArray = {
    "SinkokuCSVList": SinkokuCSVList,
    "SinkokuCSV2List": SinkokuCSV2List,
    "SinkokuCSV3List": SinkokuCSV3List,
    "SinkokuCSV4List": SinkokuCSV4List,
    "SyotokuCSVList": SyotokuCSVList,
    "SyotokuCSV2List": SyotokuCSV2List,
    "SyotokuCSV3List": SyotokuCSV3List,
    "SyotokuCSV4List": SyotokuCSV4List,
    "SyouhiCSVList": SyouhiCSVList,
    "SyouhiCSV2List": SyouhiCSV2List,
    "SyouhiCSV3List": SyouhiCSV3List,
    "SyouhiCyukanCSVList": SyouhiCyukanCSVList,
    "HoujinCSVList": HoujinCSVList,
    "HoujinSiminCSVList": HoujinSiminCSVList,
    "YoteiCSVList": YoteiCSVList,
    "SyoukyakuCSVList": SyoukyakuCSVList,
    "SyoukyakuCSV2List": SyoukyakuCSV2List,
    "ZouyoCSVList": ZouyoCSVList,
    "ZaisanCSVList": ZaisanCSVList,
    "SinkokuUkeCSVList": SinkokuUkeCSVList,
    "TKCListSinsei": TKCListSinsei,
    "TKCListHTS": TKCListHTS,
    "TKCListHTPDF": TKCListHTPDF,
    "TKCListSyouhi": TKCListSyouhi,
    "TKCListSyouhiPDF": TKCListSyouhiPDF,
    "TKCListTodouhu": TKCListTodouhu,
    "TKCListSityou": TKCListSityou,
    "ImageCSVList": ImageCSVList,
    "CSVBadList": CSVBadList,
    "SinkokuCSV": SinkokuCSV,
    "SinkokuCSV2": SinkokuCSV2,
    "SinkokuCSV3": SinkokuCSV3,
    "SinkokuCSV4": SinkokuCSV4,
    "SyotokuCSV": SyotokuCSV,
    "SyotokuCSV2": SyotokuCSV2,
    "SyotokuCSV3": SyotokuCSV3,
    "SyotokuCSV4": SyotokuCSV4,
    "SyouhiCSV": SyouhiCSV,
    "SyouhiCSV2": SyouhiCSV2,
    "SyouhiCSV3": SyouhiCSV3,
    "SyouhiCyukanCSV": SyouhiCyukanCSV,
    "HoujinCSV": HoujinCSV,
    "HoujinSiminCSV": HoujinSiminCSV,
    "YoteiCSV": YoteiCSV,
    "SyoukyakuCSV": SyoukyakuCSV,
    "SyoukyakuCSV2": SyoukyakuCSV2,
    "ZouyoCSV": ZouyoCSV,
    "ZaisanCSV": ZaisanCSV,
    "SinkokuUkeCSV": SinkokuUkeCSV,
    "ImageCSV": ImageCSV,
}
# ------------------------------------------------------------------------------------
ReadActionTKC_TKCFlagisTrue = {
    "TKCListSinsei": TKCListSinsei,
    "TKCListHTS": TKCListHTS,
    "TKCListHTPDF": TKCListHTPDF,
    "TKCListSyouhi": TKCListSyouhi,
    "TKCListSyouhiPDF": TKCListSyouhiPDF,
    "TKCListTodouhu": TKCListTodouhu,
    "TKCListSityou": TKCListSityou,
}
# ------------------------------------------------------------------------------------
ReadActionTKC_TKCFlagisTrue_PDFSetting = {
    "SinkokuCSV": SinkokuCSV,
    "SinkokuCSV2": SinkokuCSV2,
    "SinkokuCSV3": SinkokuCSV3,
    "SinkokuCSV4": SinkokuCSV4,
    "SyotokuCSV": SyotokuCSV,
    "SyotokuCSV2": SyotokuCSV2,
    "SyotokuCSV3": SyotokuCSV3,
    "SyotokuCSV4": SyotokuCSV4,
    "SyouhiCSV": SyouhiCSV,
    "SyouhiCSV2": SyouhiCSV2,
    "SyouhiCSV3": SyouhiCSV3,
    "SyouhiCyukanCSV": SyouhiCyukanCSV,
    "YoteiCSV": YoteiCSV,
    "HoujinCSV": HoujinCSV,
    "HoujinSiminCSV": HoujinSiminCSV,
    "SyoukyakuCSV": SyoukyakuCSV,
    "SyoukyakuCSV2": SyoukyakuCSV2,
    "ZouyoCSV": ZouyoCSV,
    "ZaisanCSV": ZaisanCSV,
    "SinkokuUkeCSV": SinkokuUkeCSV,
    "ImageCSV": ImageCSV,
}


# ------------------------------------------------------------------------------------
ReadActionTKC_TKCFlagiselse_PDFSetting = {
    "SinkokuCSVList": SinkokuCSVList,
    "SinkokuCSV2List": SinkokuCSV2List,
    "SinkokuCSV3List": SinkokuCSV3List,
    "SinkokuCSV4List": SinkokuCSV4List,
    "SyouhiCSVList": SyouhiCSVList,
    "SyouhiCSV2List": SyouhiCSV2List,
    "SyouhiCSV3List": SyouhiCSV3List,
    "SyouhiCyukanCSVList": SyouhiCSV3List,
    "SyotokuCSVList": SyotokuCSVList,
    "SyotokuCSV2List": SyotokuCSV2List,
    "SyotokuCSV3List": SyotokuCSV3List,
    "SyotokuCSV4List": SyotokuCSV4List,
    "YoteiCSVList": YoteiCSVList,
    "SyoukyakuCSVList": SyoukyakuCSVList,
    "SyoukyakuCSV2List": SyoukyakuCSV2List,
    "ZouyoCSVList": ZouyoCSVList,
    "ZaisanCSVList": ZaisanCSVList,
    "SinkokuUkeCSVList": SinkokuUkeCSVList,
    "HoujinCSVList": HoujinCSVList,
    "HoujinSiminCSVList": HoujinSiminCSVList,
    "ImageCSVList": ImageCSVList,
    "CSVBadList": CSVBadList,
}
# ------------------------------------------------------------------------------------
TKC_PDFSetting = {
    "TKCListSinsei": TKCListSinsei,
    "TKCListHTS": TKCListHTS,
    "TKCListHTPDF": TKCListHTPDF,
    "TKCListSyouhi": TKCListSyouhi,
    "TKCListSyouhiPDF": TKCListSyouhiPDF,
    "TKCListTodouhu": TKCListTodouhu,
    "TKCListSityou": TKCListSityou,
}

TestArray = {"SinkokuCSV": SinkokuCSV, "ZouyoCSV": ZouyoCSV}
