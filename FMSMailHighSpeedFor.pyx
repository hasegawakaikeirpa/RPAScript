#モジュールインポート
import pyautogui as pg
import time
#pandasインポート
import pandas as pd
#配列計算関数numpyインポート
import numpy as np
from chardet.universaldetector import UniversalDetector
#----------------------------------------------------------------------------------------------------------------------
def PageDownLoop(TRow):
        if TRow[0] == True:
            TRowPer = TRow[1]
            if TRowPer >= 19:
                PDV = int(TRowPer/19)
                for y in range(PDV):
                    pg.press('pagedown')
                time.sleep(1)
                PDA = int(TRowPer - (PDV*19))
                for y in range(PDA):
                    pg.press('down')
                time.sleep(1)
                return True,PDV
                # FMSAction(FolURL2,wsRow,PDV)                
            else:
                for y in range(TRowPer):
                    pg.press('down')
                time.sleep(1)
                return False,0
                # FMSAction(FolURL2,wsRow,0)
#---------------------------------------------------------------------------------------------------------------------- 
def CsvSortRowDouble(URL,KeyCol1,KeyCol2,Key1,Key2):#dtype={"TKCKokuzeiUserCode": str,"TKCKokuzeiUserCode": str}.........　#引数指定の条件一致行を対象から抽出
    try:
        Sort_url = URL
        SerchEnc = format(getFileEncoding(Sort_url))
        C_Child = pd.read_csv(Sort_url,encoding = SerchEnc)
        C_CforCount = 0
        C_dfRow = np.array(C_Child).shape[0]#配列行数取得
        for x in range(C_dfRow):
            C_ChildDataRow = C_Child.iloc[x,:]
            if C_ChildDataRow[KeyCol2] == '  ':#TKCFMSで枝番なしは半角空白2つなので
                C_Val = str(C_ChildDataRow[KeyCol1])
            else:
                C_Val = str(C_ChildDataRow[KeyCol1]) + str(C_ChildDataRow[KeyCol2])
            if not Key2:
                Key = str(Key1)
            else:
                Key = str(Key1) + str(Key2)

            if Key == C_Val:
                return True,C_CforCount
            else:
                C_CforCount = C_CforCount + 1
        return False,""
    except:
        return False,""
#------------------------------------------------------------------------------------------------------------------------------- 
def getFileEncoding( file_path ) :#.format( getFileEncoding( "sjis.csv" ) )
    detector = UniversalDetector()
    with open(file_path, mode= "rb" ) as f:
        for binary in f:
            detector.feed( binary )
            if detector.done:
                break
    detector.close()
    return detector.result[ "encoding" ]
#------------------------------------------------------------------------------------------------------------------------------