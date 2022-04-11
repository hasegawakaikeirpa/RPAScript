import RPAPhoto.PDFReadForList.CSVSetting as CSVSet  # CSVの設定ファイルの読込


def ReadAction(
    SCode,
    path_pdf,
    PDFFlag,
    y,
    PDFdfRow,
    PDFdf,
    SubPDFdf,
    SinkokuCSVList,
    SinkokuCSV2List,
    SinkokuCSV3List,
    SinkokuCSV4List,
    SyouhiCSVList,
    SyouhiCSV2List,
    SyouhiCSV3List,
    SyouhiCyukanCSVList,
    SyotokuCSVList,
    SyotokuCSV2List,
    SyotokuCSV3List,
    SyotokuCSV4List,
    YoteiCSVList,
    SyoukyakuCSVList,
    SyoukyakuCSV2List,
    ZouyoCSVList,
    ZaisanCSVList,
    SinkokuUkeCSVList,
    HoujinCSVList,
    HoujinSiminCSVList,
    ImageCSVList,
    CSVBadList,
):
    print("起動")


SCode = 0
path_pdf = 0
PDFFlag = ""
y = 0
PDFdfRow = 20
PDFdf = []
SubPDFdf = []
ReadAction(
    SCode,
    path_pdf,
    PDFFlag,
    y,
    PDFdfRow,
    PDFdf,
    SubPDFdf,
    **CSVSet.ReadActionTKC_TKCFlagiselse_PDFSetting,
)
