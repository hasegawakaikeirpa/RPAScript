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
import ContextTimeOut as CTO
import Function.CSVOut as FCSV
import Function.FolderCreate as FC
#logger設定------------------------------------------------------------------------------
import logging.config
logging.config.fileConfig("LogConf\logging_debug.conf")
logger = logging.getLogger(__name__)
#----------------------------------------------------------------------------------------
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
def CSVIndexSort(SCode,path_pdf,SinkokuCSVList,SinkokuCSV2List,SyotokuCSVList,SyouhiCSVList,HoujinCSVList,YoteiCSVList,SyoukyakuCSVList,CSVBadList,SinkokuCSV,SinkokuCSV2,SyotokuCSV,SyouhiCSV,HoujinCSV,YoteiCSV,SyoukyakuCSV):
    #PDFから抽出したリストと形式があわないので、税目リストを行列入替---------------------------
    SinkokuCSV = SinkokuCSV.transpose()#行列入替
    SinkokuCSV2 = SinkokuCSV2.transpose()#行列入替
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
    #------------------------------------------------------------------------------------
    try:
        for y in range(num_pages): 
            # TX = extract_text(path_pdf,page_numbers=y,codec='utf-8') テキストのみ取得できる
            # print(TX)
            PageVol = str(y + 1)
            CTO.PDFReadTimeOut(1,0,0,1,path_pdf,PageVol,'stream')#タイムアウト時間,実行,ポストプロセス,ループ回数,ファイルパス,ページ番号,エンジン
            tables = camelot.read_pdf(path_pdf, pages=PageVol)# PDFのテーブルを取得
            t_count = len(tables)# PDFのテーブル数を格納
            for x in range(t_count):# PDFテーブル数分ループ
                PDFdf = tables[x].df# PDFテーブルをdf化
                print(PDFdf)
                dfIndexdata = PDFdf.iloc[:,0]#PDFのインデックス
                #print(dfIndexdata)
                PDFFlag = ''
                #確定申告リストと突合------------------------------------------------------
                IndexFlags = SinkokuCSV == dfIndexdata
                FolseC = IndexFlags.sum(axis=1)-np.array(dfIndexdata).shape[0]
                if FolseC[0] >= -2:
                    PDFFlag = '確定申告'
                #------------------------------------------------------------------------
                #確定申告リスト2と突合------------------------------------------------------
                IndexFlags = SinkokuCSV2 == dfIndexdata
                FolseC = IndexFlags.sum(axis=1)-np.array(dfIndexdata).shape[0]
                if FolseC[0] >= -2:
                    PDFFlag = '確定申告2'
                #------------------------------------------------------------------------
                #所得税リストと突合--------------------------------------------------------
                IndexFlags = SyotokuCSV == dfIndexdata
                FolseC = IndexFlags.sum(axis=1)-np.array(dfIndexdata).shape[0]
                if FolseC[0] >= -2:
                    PDFFlag = '所得税'
                #------------------------------------------------------------------------
                #消費税リストと突合--------------------------------------------------------
                IndexFlags = SyouhiCSV == dfIndexdata
                FolseC = IndexFlags.sum(axis=1)-np.array(dfIndexdata).shape[0]
                if FolseC[0] >= -2:
                    PDFFlag = '消費税'
                #------------------------------------------------------------------------
                #予定申告リストと突合------------------------------------------------------
                IndexFlags = YoteiCSV == dfIndexdata
                FolseC = IndexFlags.sum(axis=1)-np.array(dfIndexdata).shape[0]
                if FolseC[0] >= -2:
                    PDFFlag = '予定申告'
                #------------------------------------------------------------------------
                #法人税リストと突合--------------------------------------------------------
                IndexFlags = HoujinCSV == dfIndexdata
                FolseC = IndexFlags.sum(axis=1)-np.array(dfIndexdata).shape[0]
                if FolseC[0] >= -2:
                    PDFFlag = '法人税'
                #------------------------------------------------------------------------
                #償却資産リストと突合------------------------------------------------------
                IndexFlags = SyoukyakuCSV == dfIndexdata
                FolseC = IndexFlags.sum(axis=1)-np.array(dfIndexdata).shape[0]
                if FolseC[0] >= -2:
                    if PDFFlag == '法人税':
                        if '課税所在地' in dfIndexdata:
                            PDFFlag = '償却資産'
                        else:
                            PDFFlag = '法人税'
                    else:
                        PDFFlag = '償却資産'
                #------------------------------------------------------------------------
                PDFdfRow = np.array(PDFdf).shape[0]#配列行数取得
                OutputList = []
                if PDFFlag == '確定申告':
                    for z in range(PDFdfRow):#PDFのテーブル行数分ループ
                        dfdatarow = PDFdf.iloc[z]#PDFのテーブル行データ1
                        if dfdatarow[0] == '手続名':
                            PDFTitle = str(dfdatarow[1])                        
                        elif dfdatarow[0] == '氏名又は名称':
                            PDFName = str(dfdatarow[1])                        
                        elif dfdatarow[0] == '受付日時':
                            PDFDate = str(dfdatarow[1])
                        elif dfdatarow[0] == '種目':
                            PDFSyumoku = str(dfdatarow[1]) 
                        elif dfdatarow[0] == '事業年度　自':
                            PDFJigyouNendo = str(dfdatarow[1]) 
                        elif dfdatarow[0] == '事業年度　至':
                            PDFJigyouNendo = PDFJigyouNendo + "-" + str(dfdatarow[1])                         
                        elif dfdatarow[0] == '税目':
                            if z == 10:
                                PDFZeimoku = str(dfdatarow[1])
                            elif z == 16:
                                PDFZeimoku2 = str(dfdatarow[1])
                        elif dfdatarow[0] == '申告の種類':
                            if z == 11:
                                PDFSinkokuSyu = str(dfdatarow[1])
                            elif z == 17:
                                PDFSinkokuSyu2 = str(dfdatarow[1])              
                        elif dfdatarow[0] == '所得金額又は欠損金額':
                            PDFSyotokuAndKesson = str(dfdatarow[1])                        
                        elif dfdatarow[0] == '差引確定法人税額':
                            PDFKakuteiHoujingaku = str(dfdatarow[1])
                        elif '欠損金又は災害損失金等の当期' in dfdatarow[0]:
                            PDFKessonAndSaigai = str(dfdatarow[1]) 
                        elif '翌期へ繰り越す欠損金又は災害' in dfdatarow[0]:
                            PDFKuriketusai = str(dfdatarow[1])
                        elif dfdatarow[0] == '課税標準法人税額':
                            PDFKazeiHyoujyun = str(dfdatarow[1])
                        elif dfdatarow[0] == '差引確定地方法人税額':
                            PDFSasihiki = str(dfdatarow[1])  
                    OutputList = [SCode,path_pdf.replace('/','\\'),str(y+1) + 'ページ目',PDFTitle,PDFName,PDFDate,PDFSyumoku,PDFJigyouNendo,PDFZeimoku,PDFSinkokuSyu,PDFSyotokuAndKesson,PDFKakuteiHoujingaku,PDFKessonAndSaigai,PDFKuriketusai,PDFZeimoku2,PDFSinkokuSyu2,PDFKazeiHyoujyun,PDFSasihiki]
                    SinkokuCSVList.append(OutputList)
                #------------------------------------------------------------------------ 
                elif PDFFlag == '確定申告2':
                    for z in range(PDFdfRow):#PDFのテーブル行数分ループ
                        dfdatarow = PDFdf.iloc[z]#PDFのテーブル行データ1
                        if dfdatarow[0] == '手続名':
                            PDFTitle = str(dfdatarow[1])                        
                        elif dfdatarow[0] == '氏名又は名称':
                            PDFName = str(dfdatarow[1])                        
                        elif dfdatarow[0] == '受付日時':
                            PDFDate = str(dfdatarow[1])
                        elif dfdatarow[0] == '種目':
                            PDFSyumoku = str(dfdatarow[1]) 
                        elif dfdatarow[0] == '事業年度　自':
                            PDFJigyouNendo = str(dfdatarow[1]) 
                        elif dfdatarow[0] == '事業年度　至':
                            PDFJigyouNendo = PDFJigyouNendo + "-" + str(dfdatarow[1])                         
                        elif dfdatarow[0] == '税目':
                            if z == 10:
                                PDFZeimoku = str(dfdatarow[1])
                            elif z == 16:
                                PDFZeimoku2 = str(dfdatarow[1])
                        elif dfdatarow[0] == '申告の種類':
                            if z == 11:
                                PDFSinkokuSyu = str(dfdatarow[1])
                            elif z == 17:
                                PDFSinkokuSyu2 = str(dfdatarow[1])              
                        elif dfdatarow[0] == '所得金額又は欠損金額':
                            PDFSyotokuAndKesson = str(dfdatarow[1])                        
                        elif dfdatarow[0] == 'この申告による還付金額':
                            if z == 13:
                                PDFSinkokuKanpu = str(dfdatarow[1])
                            elif z == 19:
                                PDFSinkokuKanpu2 = str(dfdatarow[1])  
                        elif '欠損金又は災害損失金等の当期' in dfdatarow[0]:
                            PDFKessonAndSaigai = str(dfdatarow[1]) 
                        elif '翌期へ繰り越す欠損金又は災害' in dfdatarow[0]:
                            PDFKuriketusai = str(dfdatarow[1])
                        elif dfdatarow[0] == '課税標準法人税額':
                            PDFKazeiHyoujyun = str(dfdatarow[1])
                    OutputList = [SCode,path_pdf.replace('/','\\'),str(y+1) + 'ページ目',PDFTitle,PDFName,PDFDate,PDFSyumoku,PDFJigyouNendo,PDFZeimoku,PDFSinkokuSyu,PDFSyotokuAndKesson,PDFSinkokuKanpu,PDFKessonAndSaigai,PDFKuriketusai,PDFZeimoku2,PDFSinkokuSyu2,PDFKazeiHyoujyun,PDFSinkokuKanpu2]
                    SinkokuCSV2List.append(OutputList)
                #------------------------------------------------------------------------ 
                elif PDFFlag == '所得税':
                    for z in range(PDFdfRow):#PDFのテーブル行数分ループ
                        dfdatarow = PDFdf.iloc[z]#PDFのテーブル行データ1
                        if dfdatarow[0] == '手続名':
                            PDFTitle = str(dfdatarow[1])                        
                        elif dfdatarow[0] == '氏名又は名称':
                            PDFName = str(dfdatarow[1])                        
                        elif dfdatarow[0] == '受付日時':
                            PDFDate = str(dfdatarow[1])                        
                        elif dfdatarow[0] == '年分':
                            PDFNendo = str(dfdatarow[1])                        
                        elif dfdatarow[0] == '種目':
                            PDFSyumoku = str(dfdatarow[1])                        
                        elif dfdatarow[0] == '所得金額':
                            PDFSyotoku = str(dfdatarow[1])                        
                        elif '納める税金' in dfdatarow[0]:
                            PDFNouzeigaku = str(dfdatarow[1])                        
                        elif '還付される税金' in dfdatarow[0]:
                            PDFKanpugaku = str(dfdatarow[1])
                    OutputList = [SCode,path_pdf.replace('/','\\'),str(y+1) + 'ページ目',PDFTitle,PDFName,PDFDate,PDFNendo,PDFSyumoku,PDFSyotoku,PDFNouzeigaku,PDFKanpugaku]
                    SyotokuCSVList.append(OutputList)
                #------------------------------------------------------------------------
                elif PDFFlag == '消費税':
                    for z in range(PDFdfRow):#PDFのテーブル行数分ループ
                        dfdatarow = PDFdf.iloc[z]#PDFのテーブル行データ1
                        if dfdatarow[0] == '手続名':
                            PDFTitle = str(dfdatarow[1])                        
                        elif dfdatarow[0] == '氏名又は名称':
                            PDFName = str(dfdatarow[1])                        
                        elif dfdatarow[0] == '受付日時':
                            PDFDate = str(dfdatarow[1])
                        elif dfdatarow[0] == '種目':
                            PDFSyumoku = str(dfdatarow[1])                       
                        elif dfdatarow[0] == '申告の種類':
                            PDFSyurui = str(dfdatarow[1])                                              
                        elif dfdatarow[0] == '課税標準額':
                            PDFKazeigaku = str(dfdatarow[1])                        
                        elif '消費税及び地方消費税の合計' in dfdatarow[0]:
                            PDFGoukeigaku = str(dfdatarow[1])                        
                        elif dfdatarow[0] == '課税期間　自':
                            PDFKazeikikan = str(dfdatarow[1]) 
                        elif dfdatarow[0] == '課税期間　至':
                            PDFKazeikikan = PDFKazeikikan + "-" + str(dfdatarow[1])
                    OutputList = [SCode,path_pdf.replace('/','\\'),str(y+1) + 'ページ目',PDFTitle,PDFName,PDFDate,PDFSyumoku,PDFSyurui,PDFKazeigaku,PDFGoukeigaku,PDFKazeikikan]
                    SyouhiCSVList.append(OutputList)
                #------------------------------------------------------------------------
                elif PDFFlag == '予定申告':
                    for z in range(PDFdfRow):#PDFのテーブル行数分ループ
                        dfdatarow = PDFdf.iloc[z]#PDFのテーブル行データ1
                        if dfdatarow[0] == '手続名':
                            PDFTitle = str(dfdatarow[1])                        
                        elif dfdatarow[0] == '氏名又は名称':
                            PDFName = str(dfdatarow[1])                        
                        elif dfdatarow[0] == '受付日時':
                            PDFDate = str(dfdatarow[1])
                        elif dfdatarow[0] == '種目':
                            PDFSyumoku = str(dfdatarow[1]) 
                        elif dfdatarow[0] == '事業年度　自':
                            PDFJigyouNendo = str(dfdatarow[1]) 
                        elif dfdatarow[0] == '事業年度　至':
                            PDFJigyouNendo = PDFJigyouNendo + "-" + str(dfdatarow[1])                         
                        elif dfdatarow[0] == '税目':
                            if z == 10:
                                PDFZeimoku = str(dfdatarow[1])
                            elif z == 12:
                                PDFZeimoku2 = str(dfdatarow[1])                                            
                        elif dfdatarow[0] == '納付すべき法人税額':
                            PDFNouhuHoujin = str(dfdatarow[1])                        
                        elif dfdatarow[0] == '納付すべき地方法人税額':
                            PDFNouhuTihou = str(dfdatarow[1])
                    OutputList = [SCode,path_pdf.replace('/','\\'),str(y+1) + 'ページ目',PDFTitle,PDFName,PDFDate,PDFSyumoku,PDFJigyouNendo,PDFZeimoku,PDFNouhuHoujin,PDFZeimoku2,PDFNouhuTihou]
                    YoteiCSVList.append(OutputList)
                #------------------------------------------------------------------------                                          
                elif PDFFlag == '償却資産':
                    for z in range(PDFdfRow):#PDFのテーブル行数分ループ
                        dfdatarow = PDFdf.iloc[z]#PDFのテーブル行データ1
                        if dfdatarow[0] == '手続名':
                            PDFTitle = str(dfdatarow[1])                        
                        elif dfdatarow[0] == '氏名又は名称':
                            PDFName = str(dfdatarow[1])                        
                        elif dfdatarow[0] == '発行元名':
                            PDFHakkou = str(dfdatarow[1])                        
                        elif dfdatarow[0] == '発行元所属名':
                            PDFHakkouSyozoku = str(dfdatarow[1])                        
                        elif dfdatarow[0] == '受付日時':
                            PDFDate = str(dfdatarow[1])                        
                        elif dfdatarow[0] == '提出先':
                            PDFTeisyutu = str(dfdatarow[1])                        
                        elif dfdatarow[0] == '年度・期別':
                            PDFNendo = str(dfdatarow[1])                        
                        elif dfdatarow[0] == '課税所在地':
                            PDFSyozaiti = str(dfdatarow[1])
                    OutputList = [SCode,path_pdf.replace('/','\\'),str(y+1) + 'ページ目',PDFTitle,PDFName,PDFHakkou,PDFHakkouSyozoku,PDFDate,PDFTeisyutu,PDFNendo,PDFSyozaiti]
                    SyoukyakuCSVList.append(OutputList)
                #------------------------------------------------------------------------ 
                elif PDFFlag == '法人税':
                    for z in range(PDFdfRow):#PDFのテーブル行数分ループ
                        dfdatarow = PDFdf.iloc[z]#PDFのテーブル行データ1
                        if dfdatarow[0] == '手続名':
                            PDFTitle = str(dfdatarow[1])                        
                        elif dfdatarow[0] == '氏名又は名称':
                            PDFName = str(dfdatarow[1])                        
                        elif dfdatarow[0] == '発行元名':
                            PDFHakkou = str(dfdatarow[1])                        
                        elif dfdatarow[0] == '発行元所属名':
                            PDFHakkouSyozoku = str(dfdatarow[1])                        
                        elif dfdatarow[0] == '受付日時':
                            PDFDate = str(dfdatarow[1])                        
                        elif dfdatarow[0] == '提出先':
                            PDFTeisyutu = str(dfdatarow[1])                        
                        elif dfdatarow[0] == '年度・期別':
                            PDFNendo = str(dfdatarow[1])                        
                        elif dfdatarow[0] == '納税者氏名':
                            PDFNouzeiName = str(dfdatarow[1])
                    OutputList = [SCode,path_pdf.replace('/','\\'),str(y+1) + 'ページ目',PDFTitle,PDFName,PDFHakkou,PDFHakkouSyozoku,PDFDate,PDFTeisyutu,PDFNendo,PDFNouzeiName]
                    HoujinCSVList.append(OutputList)
                #------------------------------------------------------------------------
                else:
                    logger.debug(path_pdf + '_' + str(y+1) + 'ページ目取得失敗書式登録なし')
                    OutputList = [SCode,path_pdf.replace('/','\\'),str(y+1) + 'ページ目取得失敗書式登録なし','','','','','','','','']
                    CSVBadList.append(OutputList)
                    print('書式登録されていません。')
        return True                     
    except Exception as e:
        logger.debug(path_pdf + '_' + str(y+1) + 'ページ目取得失敗')
        OutputList = [SCode,path_pdf.replace('/','\\'),str(y+1) + 'ページ目取得失敗','','','','','','','','']
        CSVBadList.append(OutputList)
        return False
#----------------------------------------------------------------------------------------
def PDFRead(URL):
    MeUrl = os.getcwd().replace('\\','/')#自分のパス
    #各税目のインデックスリストを加工して格納------------------------------------------------
    SinkokuCSV = FCSV.CsvReadHeaderless(MeUrl + "/RPAPhoto/PDFReadForList/確定申告.CSV")#内国法人確定申告のインデックスリスト
    SinkokuCSV2 = FCSV.CsvReadHeaderless(MeUrl + "/RPAPhoto/PDFReadForList/確定申告2.CSV")#内国法人確定申告のインデックスリスト
    SyotokuCSV = FCSV.CsvReadHeaderless(MeUrl + "/RPAPhoto/PDFReadForList/所得税.CSV")#所得税のインデックスリスト
    SyouhiCSV = FCSV.CsvReadHeaderless(MeUrl + "/RPAPhoto/PDFReadForList/消費税.CSV")#消費税のインデックスリスト
    HoujinCSV = FCSV.CsvReadHeaderless(MeUrl + "/RPAPhoto/PDFReadForList/法人税.CSV")#法人税のインデックスリスト
    YoteiCSV = FCSV.CsvReadHeaderless(MeUrl + "/RPAPhoto/PDFReadForList/予定申告.CSV")#予定申告のインデックスリスト
    SyoukyakuCSV = FCSV.CsvReadHeaderless(MeUrl + "/RPAPhoto/PDFReadForList/償却資産.CSV")#償却資産のインデックスリスト
    #------------------------------------------------------------------------------------
    SinkokuCSVList = []#成功リスト初期化
    SinkokuCSV2List = []#成功リスト初期化
    SyotokuCSVList = []#成功リスト初期化
    SyouhiCSVList = []#成功リスト初期化
    HoujinCSVList = []#成功リスト初期化
    YoteiCSVList = []#成功リスト初期化
    SyoukyakuCSVList = []#成功リスト初期化
    CSVBadList = []#失敗リスト初期化
    #------------------------------------------------------------------------------------
    # FCSV.CsvSaveEnc(URL.replace("\\","/") + "/PDFDataSuccess.csv",CSVList,"shiftjis")
    dir_List = SerchdirFolders(URL)#指定URL配下のサブフォルダを取得
    print(dir_List)
    for dir_ListItem  in dir_List:
        Serchd = dir_ListItem[0] + '\\' + dir_ListItem[1]#サブフォルダ名
        dir_Files = SerchdirFiles(Serchd)#サブフォルダ配下のサブフォルダを取得
        print(dir_Files)
        for dir_FilesItem  in dir_Files:
            if Serchd == dir_FilesItem[0]:
                dif = dir_FilesItem[0] + '\\' +  dir_FilesItem[1]#ファイル名
                dirsplit = dir_FilesItem[1].split("_")
                dirsplit = dirsplit[0].split(".")
                SCode = dirsplit[0]
                try:
                    if not ".xdw" in dif:#Docuファイルじゃなければ
                        path_pdf = dif.replace('\\','/')#PDFパスを代入
                        CSVIndexSort(SCode,path_pdf,SinkokuCSVList,SinkokuCSV2List,SyotokuCSVList,SyouhiCSVList,HoujinCSVList,YoteiCSVList,SyoukyakuCSVList,CSVBadList,SinkokuCSV[1],SinkokuCSV2[1],SyotokuCSV[1],SyouhiCSV[1],HoujinCSV[1],YoteiCSV[1],SyoukyakuCSV[1])
                    else:
                        print('xdw')
                except Exception as e:
                    print(e)
    #------------------------------------------------------------------------------------
    ListURL = FC.CreFol("//Sv05121a/e/電子ファイル/メッセージボックス/TEST","受信通知CSV")
    if not np.array(SinkokuCSVList).shape[0] == 0:
        FCSV.CsvSaveEnc(ListURL + "/内国法人確定申告受信通知リスト.csv",SinkokuCSVList,"cp932",['コード','URL','ページ','手続名','氏名又は名称','受付日時','種目','事業年度','税目','申告の種類','所得金額又は欠損金額','差引確定法人税額','欠損金又は災害損失金等の当期控除額','翌期へ繰り越す欠損金又は災害損失金','税目2','申告の種類2','課税標準法人税額','差引確定地方法人税額'])
    if not np.array(SinkokuCSV2List).shape[0] == 0:
        FCSV.CsvSaveEnc(ListURL + "/内国法人確定申告受信通知リスト2.csv",SinkokuCSV2List,"cp932",['コード','URL','ページ','手続名','氏名又は名称','受付日時','種目','事業年度','税目','申告の種類','所得金額又は欠損金額','この申告による還付金額','欠損金又は災害損失金等の当期控除額','翌期へ繰り越す欠損金又は災害損失金','税目2','申告の種類2','課税標準法人税額','この申告による還付金額2'])
    if not np.array(SyotokuCSVList).shape[0] == 0:
        FCSV.CsvSaveEnc(ListURL + "/所得税受信通知リスト.csv",SyotokuCSVList,"cp932",['コード','URL','ページ','手続名','氏名又は名称','受付日時','年分','種目','所得金額','納める税金','還付される税金'])
    if not np.array(SyouhiCSVList).shape[0] == 0:
        FCSV.CsvSaveEnc(ListURL + "/消費税受信通知リスト.csv",SyouhiCSVList,"cp932",['コード','URL','ページ','手続名','氏名又は名称','受付日時','種目','申告の種類','課税標準額','消費税及び地方消費税の合計','課税期間'])
    if not np.array(HoujinCSVList).shape[0] == 0:
        FCSV.CsvSaveEnc(ListURL + "/法人税受信通知リスト.csv",HoujinCSVList,"cp932",['コード','URL','ページ','手続名','氏名又は名称','発行元名','発行元所属名','受付日時','提出先','年度・期別','納税者氏名'])
    if not np.array(YoteiCSVList).shape[0] == 0:
        FCSV.CsvSaveEnc(ListURL + "/予定納税受信通知リスト.csv",YoteiCSVList,"cp932",['コード','URL','ページ','手続名','氏名又は名称','受付日時','種目','事業年度','税目','納付すべき法人税額','税目2','納付すべき地方法人税額'])
    if not np.array(SyoukyakuCSVList).shape[0] == 0:
        FCSV.CsvSaveEnc(ListURL + "/償却資産受信通知リスト.csv",SyoukyakuCSVList,"cp932",['コード','URL','ページ','手続名','氏名又は名称','発行元名','発行元所属名','受付日時','提出先','年度・期別','課税所在地'])
    if not np.array(CSVBadList).shape[0] == 0:
        FCSV.CsvSaveEnc(ListURL + "/受信通知取得失敗リスト.csv",CSVBadList,"cp932",['コード','URL','ページ','手続名','氏名又は名称','発行元名','発行元所属名','受付日時','提出先','年度・期別','納税者氏名'])
    #------------------------------------------------------------------------------------
#URL = "\\\\Sv05121a\\e\\電子ファイル\\メッセージボックス\\2022-2\\送信分受信通知"
URL = "\\\\Sv05121a\\e\\電子ファイル\\メッセージボックス\\TEST"
try:
    logger.debug(URL + "内のPDF結合開始")
    PDFRead(URL)
    logger.debug(URL + "内のPDF結合完了")
except Exception as e:
    logger.debug("エラー終了" + e)