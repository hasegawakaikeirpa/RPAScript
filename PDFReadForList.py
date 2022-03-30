import os
import PyPDF2
import time
from time import time
import pandas as pd
import numpy as np
import camelot.io as camelot
from pdfminer.high_level import extract_text
from pdfminer.pdfparser import PDFParser 
from pdfminer.pdfdocument import PDFDocument 
from pdfminer.pdfpage import PDFPage
from io import StringIO
import os
from PIL import Image
import pyocr
import PyPDF2
import CSVOut
#logger設定------------------------------------------------------------------------------------------------------------
import logging.config
logging.config.fileConfig("logging_debug.conf")
logger = logging.getLogger(__name__)
#----------------------------------------------------------------------------------------------------------------------
def SerchdirFolders(URL):#指定URL配下のサブフォルダを取得
    List = []
    for fd_path, sb_folder, sb_file in os.walk(URL):
        for fol in sb_folder:
            # print(fd_path + '\\' + fol)
            List.append([fd_path,fol])
    return List
#----------------------------------------------------------------------------------------
def SerchdirFiles(URL):#指定URL配下のファイルを取得
    List = []
    for fd_path, sb_folder, sb_file in os.walk(URL):
        for fil in sb_file:
            # print(fd_path + '\\' + fil)
            List.append([fd_path,fil])
    return List
#----------------------------------------------------------------------------------------
def PDFOCRRead():       
    #インストールしたTesseract-OCRのパスを環境変数「PATH」へ追記する。
    #OS自体に設定してあれば以下の2行は不要
    path='C:\\Program Files\\Tesseract-OCR'
    os.environ['PATH'] = os.environ['PATH'] + path    
    #pyocrへ利用するOCRエンジンをTesseractに指定する。
    tools = pyocr.get_available_tools()
    print(tools[0].get_name())
    tool = tools[0]
    #OCR対象の画像ファイルを読み込む
    img = Image.open("test2.jpg")
    #画像を読みやすいように加工。
    img=img.convert('RGB')
    size=img.size
    img2=Image.new('RGB',size)
    border=110
    for x in range(size[0]):
        for y in range(size[1]):
            r,g,b=img.getpixel((x,y))
            if r > border or g > border or b > border:
                r = 255
                g = 255
                b = 255
            img2.putpixel((x,y),(r,g,b))
    #画像から文字を読み込む
    builder = pyocr.builders.TextBuilder(tesseract_layout=3)
    text = tool.image_to_string(img2, lang="jpn", builder=builder)
    return text
#----------------------------------------------------------------------------------------
def CSVIndexSort(path_pdf,CSVList,CSVBatList,SyotokuCSV,SyouhiCSV,HoujinCSV,YoteiCSV,SyoukyakuCSV):
    #PDFから抽出したリストと形式があわないので、税目リストを行列入替---------------------------
    SyotokuCSV = SyotokuCSV.transpose()#行列入替
    SyouhiCSV = SyouhiCSV.transpose()#行列入替
    HoujinCSV = HoujinCSV.transpose()#行列入替
    YoteiCSV = YoteiCSV.transpose()#行列入替
    SyoukyakuCSV = SyoukyakuCSV.transpose()#行列入替
    #------------------------------------------------------------------------------------
    fp = open(path_pdf, 'rb') # PDFファイルを読み込み
    parser = PDFParser(fp)#PDFperserを作成。
    document = PDFDocument(parser) #PDFperserを格納。
    num_pages = 0 #ページ数格納変数を初期化
    for page in PDFPage.create_pages(document): #ページオブジェ分ループ
        num_pages += 1 #ページ数カウント
    print(num_pages) #ページ数確認
    for y in range(num_pages): 
        # TX = extract_text(path_pdf,page_numbers=y,codec='utf-8') テキストのみ取得できる
        # print(TX)
        tables = camelot.read_pdf(path_pdf)# PDFのテーブルを取得
        t_count = len(tables)# PDFのテーブル数を格納
        for x in range(t_count):# PDFテーブル数分ループ
            PDFdf = tables[x].df# PDFテーブルをdf化
            print(PDFdf)
            dfIndexdata = PDFdf.iloc[:,0]#PDFのインデックス
            print(dfIndexdata)
            PDFFlag = ''
            #所得税リストと突合--------------------------------------------------------
            IndexFlags = SyotokuCSV == dfIndexdata
            FolseC = IndexFlags.sum(axis=1)-np.array(dfIndexdata).shape[0]
            if FolseC[0] == 0:
                PDFFlag = '所得税'
            #------------------------------------------------------------------------
            #消費税リストと突合--------------------------------------------------------
            IndexFlags = SyouhiCSV == dfIndexdata
            FolseC = IndexFlags.sum(axis=1)-np.array(dfIndexdata).shape[0]
            if FolseC[0] == 0:
                PDFFlag = '消費税'
            #------------------------------------------------------------------------
            #予定申告リストと突合------------------------------------------------------
            IndexFlags = YoteiCSV == dfIndexdata
            FolseC = IndexFlags.sum(axis=1)-np.array(dfIndexdata).shape[0]
            if FolseC[0] == 0:
                PDFFlag = '予定申告'
            #------------------------------------------------------------------------
            #法人税リストと突合--------------------------------------------------------
            IndexFlags = HoujinCSV == dfIndexdata
            FolseC = IndexFlags.sum(axis=1)-np.array(dfIndexdata).shape[0]
            if FolseC[0] == 0:
                PDFFlag = '法人税'
            #------------------------------------------------------------------------
            #償却資産リストと突合------------------------------------------------------
            IndexFlags = SyoukyakuCSV == dfIndexdata
            FolseC = IndexFlags.sum(axis=1)-np.array(dfIndexdata).shape[0]
            if FolseC[0] == 0:
                PDFFlag = '償却資産'
            #------------------------------------------------------------------------
            PDFdfRow = np.array(PDFdf).shape[0]#配列行数取得
            if PDFFlag == '所得税':
                for z in range(PDFdfRow):#PDFのテーブル行数分ループ
                    dfdatarow = PDFdf.iloc[z]#PDFのテーブル行データ1
            







            #         CSVList.append([path_pdf,str(y+1) + 'ページ目',dfdatarow[1]])
            #     elif '納付すべき地方法人税額' == dfdatarow[0]:
            #         CSVList.append([path_pdf,str(y+1) + 'ページ目',dfdatarow[1]])
            # # if Flag == True:
            # #     CSVList.append([path_pdf,str(y+1) + 'ページ目',dfdatarow[1]])
            # # else:
            # #     CSVBatList.append([path_pdf,str(y+1) + 'ページ目取得失敗',dfdatarow[1]])
            # #     logger.debug(path_pdf + '_' + str(y+1) + 'ページ目取得失敗')    
#----------------------------------------------------------------------------------------
def PDFRead(URL):
    MeUrl = os.getcwd().replace('\\','/')#自分のパス
    #各税目のインデックスリストを加工して格納------------------------------------------------
    SyotokuCSV = CSVOut.CsvReadHeaderless(MeUrl + "/RPAPhoto/PDFReadForList/所得税.CSV")#所得税のインデックスリスト
    SyouhiCSV = CSVOut.CsvReadHeaderless(MeUrl + "/RPAPhoto/PDFReadForList/消費税.CSV")#消費税のインデックスリスト
    HoujinCSV = CSVOut.CsvReadHeaderless(MeUrl + "/RPAPhoto/PDFReadForList/法人税.CSV")#法人税のインデックスリスト
    YoteiCSV = CSVOut.CsvReadHeaderless(MeUrl + "/RPAPhoto/PDFReadForList/予定申告.CSV")#予定申告のインデックスリスト
    SyoukyakuCSV = CSVOut.CsvReadHeaderless(MeUrl + "/RPAPhoto/PDFReadForList/償却資産.CSV")#償却資産のインデックスリスト
    #------------------------------------------------------------------------------------
    CSVList = []#成功リスト初期化
    CSVBatList = []#失敗リスト初期化
    dir_List = SerchdirFolders(URL)#指定URL配下のサブフォルダを取得
    for dir_ListItem  in dir_List:
        Serchd = dir_ListItem[0] + '\\' + dir_ListItem[1]#サブフォルダ名
        dir_Files = SerchdirFiles(Serchd)#サブフォルダ配下のサブフォルダを取得
        for dir_FilesItem  in dir_Files:
            dif = dir_FilesItem[0] + '\\' +  dir_FilesItem[1]#ファイル名
            try:
                if not ".xdw" in dif:#Docuファイルじゃなければ
                    path_pdf = dif.replace('\\','/')#PDFパスを代入
                    CSVIndexSort(path_pdf,CSVList,CSVBatList,SyotokuCSV[1],SyouhiCSV[1],HoujinCSV[1],YoteiCSV[1],SyoukyakuCSV[1])
                else:
                    print('xdw')
            except Exception as e:
                #CSVBatList.append([path_pdf,str(y+1) + 'ページ目取得失敗',dfdatarow[1]])
                logger.debug(path_pdf + '_' + str(y+1) + 'ページ目取得失敗')
                print(e)
    CSVOut.CsvSave(URL.replace("\\","/") + "/PDFDataSuccess.csv",CSVList)
    CSVOut.CsvSave(URL.replace("\\","/") + "/PDFFailData.csv",CSVBatList)
URL = "\\\\Sv05121a\\e\\電子ファイル\\メッセージボックス\\2022-2\\送信分受信通知"
# URL = "//Sv05121a/e/電子ファイル/メッセージボックス/2022-2/eLTAX"
# URL = "\\\\\\Sv05121a\\e\\電子ファイル\\メッセージボックス\\2022-2\\eLTAX"
try:
    logger.debug(URL + "内のPDF結合開始")
    PDFRead(URL)
    logger.debug(URL + "内のPDF結合完了")
except Exception as e:
    logger.debug("エラー終了" + e)