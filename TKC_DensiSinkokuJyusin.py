#----------------------------------------------------------------------------------------------------------------------
def DriverUIWaitXPATH(UIPATH,driver):#XPATH要素を取得するまで待機
    for x in range(1000):
        try:
            driver.find_element_by_xpath(UIPATH)
            Flag = 1
            return True
        except:
            Flag = 0
    if Flag == 0:
        return False
#----------------------------------------------------------------------------------------------------------------------
def DriverUIWaitAutomationId(UIPATH,driver):#XPATH要素を取得するまで待機
    for x in range(1000):
        try:
            driver.find_element_by_accessibility_id(UIPATH)
            Flag = 1
            return True
        except:
            Flag = 0
    if Flag == 0:
        return False
#----------------------------------------------------------------------------------------------------------------------
def DriverUIWaitName(UIPATH,driver):#XPATH要素を取得するまで待機
    for x in range(1000):
        try:
            driver.find_element_by_Name(UIPATH)
            Flag = 1
            return True
        except:
            Flag = 0
    if Flag == 0:
        return False
#----------------------------------------------------------------------------------------------------------------------
def DriverUIWaitclassname(UIPATH,driver):#XPATH要素を取得するまで待機
    for x in range(10000):
        try:
            driver.find_element_by_class_name(UIPATH)
            Flag = 1
            return True
        except:
            Flag = 0
    if Flag == 0:
        return False
#----------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------
def DriverFindClass(UIPATH,driver):#XPATH要素を取得するまで待機
    for x in range(10000):
        try:
            elList = driver.find_elements_by_class_name(UIPATH)
            Flag = 1
            return True,elList
        except:
            Flag = 0
    if Flag == 0:
        return False
#----------------------------------------------------------------------------------------------------------------------
def DriverCheck(Hub,ObjName,driver):#XPATH要素を取得するまで待機
    for x in range(1000):
        if Hub == "AutomationID":
            if DriverUIWaitAutomationId(ObjName,driver) == True:#OMSメニューの年調起動ボタンを判定して初期処理分け
                #正常待機後処理
                OMSObj = driver.find_element_by_accessibility_id(ObjName)#一括電子申告送信ボタン
                return True
            else:
                #異常待機後処理
                print("要素取得に失敗しました。")
        elif Hub == "XPATH":
            if DriverUIWaitXPATH(ObjName,driver) == True:#OMSメニューの年調起動ボタンを判定して初期処理分け
                #正常待機後処理
                OMSObj = driver.find_element_by_xpath(ObjName)#一括電子申告送信ボタン
                return True
            else:
                #異常待機後処理
                print("要素取得に失敗しました。")
        elif Hub == "Name":
            if DriverUIWaitName(ObjName,driver) == True:#OMSメニューの年調起動ボタンを判定して初期処理分け
                #正常待機後処理
                OMSObj = driver.find_element_by_Name(ObjName)#一括電子申告送信ボタン
                return True
            else:
                #異常待機後処理
                print("要素取得に失敗しました。")
#----------------------------------------------------------------------------------------------------------------------
def DriverClick(Hub,ObjName,driver):
    if Hub == "AutomationID":
        if DriverUIWaitAutomationId(ObjName,driver) == True:#OMSメニューの年調起動ボタンを判定して初期処理分け
            #正常待機後処理
            OMSObj = driver.find_element_by_accessibility_id(ObjName)#一括電子申告送信ボタン
            OMSObj.click()
            return OMSObj
        else:
            #異常待機後処理
            print("要素取得に失敗しました。")
    elif Hub == "XPATH":
        if DriverUIWaitXPATH(ObjName,driver) == True:#OMSメニューの年調起動ボタンを判定して初期処理分け
            #正常待機後処理
            OMSObj = driver.find_element_by_xpath(ObjName)#一括電子申告送信ボタン
            OMSObj.click()
            return OMSObj
        else:
            #異常待機後処理
            print("要素取得に失敗しました。")
    elif Hub == "Name":
        if DriverUIWaitName(ObjName,driver) == True:#OMSメニューの年調起動ボタンを判定して初期処理分け
            #正常待機後処理
            OMSObj = driver.find_element_by_Name(ObjName)#一括電子申告送信ボタン
            OMSObj.click()
            return OMSObj
        else:
            #異常待機後処理
            print("要素取得に失敗しました。")
    elif Hub == "class_name":
        if DriverUIWaitclassname(ObjName,driver) == True:#OMSメニューの年調起動ボタンを判定して初期処理分け
            #正常待機後処理
            OMSObj = driver.find_element_by_class_name(ObjName)#一括電子申告送信ボタン
            OMSObj.click()
            return OMSObj
        else:
            #異常待機後処理
            print("要素取得に失敗しました。")
#----------------------------------------------------------------------------------------------------------------------
def ImgCheck(FolURL2,FileName,conf,LoopVal):#画像があればTrueを返す関数
    ImgURL = FolURL2 + "/" + FileName
    for x in range(LoopVal):
        try:
            p = pyautogui.locateOnScreen(ImgURL, confidence=conf)
            x, y = pyautogui.center(p)
            return True,x,y
        except:
            Flag = 0
    if Flag == 0:
        return False,"",""
#----------------------------------------------------------------------------------------------------------------------
def ImgNothingCheck(FolURL2,FileName,conf,LoopVal):#画像がなければTrueを返す
    ImgURL = FolURL2 + "/" + FileName
    for x in range(LoopVal):
        try:
            p = pyautogui.locateOnScreen(ImgURL, confidence=conf)
            x, y = pyautogui.center(p)
            return False
        except:
            Flag = 0
    if Flag == 0:
        return True
#----------------------------------------------------------------------------------------------------------------------
def ImgCheckForList(FolURL2,List,conf):#リスト内の画像があればTrueと画像名を返す
    for x in range(10):
        for ListItem in List:
            ImgURL = FolURL2 + "/" + ListItem
            try:
                p = pyautogui.locateOnScreen(ImgURL, confidence=conf)
                x, y = pyautogui.center(p)
                return True,ListItem
                break
            except:
                Flag = 0
    if Flag == 0:
        return False,""
#----------------------------------------------------------------------------------------------------------------------
def ImgClick(FolURL2,FileName,conf,LoopVal):#画像があればクリックしてx,y軸を返す
    ImgURL = FolURL2 + "/" + FileName
    for x in range(10):
        if ImgCheck(FolURL2,FileName,conf,LoopVal)[0] == True:#OMSメニューの年調起動ボタンを判定して初期処理分け
            #正常待機後処理
            for y in range(10):
                try:
                    p = pyautogui.locateOnScreen(ImgURL, confidence=conf)
                    x, y = pyautogui.center(p)
                    pyautogui.click(x, y)
                    time.sleep(1)
                    return x, y
                except:
                    print("失敗")
        else:
            #異常待機後処理
            print("要素取得に失敗しました。")
#----------------------------------------------------------------------------------------------------------------------
def getFileEncoding( file_path ) :#.format( getFileEncoding( "sjis.csv" ) )
    detector = UniversalDetector()
    with open(file_path, mode= "rb" ) as f:
        for binary in f:
            detector.feed( binary )
            if detector.done:
                break
    detector.close()
    return detector.result[ "encoding" ]
#---------------------------------------------------------------------------------------------------------------------- 
def main():
    ret = getFileEncoding( "sjis.csv" )
    print( "sjis.csv Encoding={0}".format( ret ) )
 
    ret = getFileEncoding( "utf8.csv" )
    print( "utf8.csv Encoding={0}".format( ret ) )
def EraceIMGWait(FolURL2,FileName):
    try:
        while all(pg.locateOnScreen(FolURL2 + "/" + FileName, confidence=0.9)) == True:
            time.sleep(1)
    except:
        print("待機終了")

def CSVOutPut(CSVURL,CSVName,driver,FolURL2):#TKCのCSVダイアログでの書出し操作
    while pg.locateOnScreen(FolURL2 + "/KiridasiWin.png" , confidence=0.99999) is None:
        time.sleep(1)
    #要素クリック----------------------------------------------------------------------------------------------------------
    Hub = "AutomationID" #取得要素のタイプ指定
    ObjName = "outputDirTextBox"
    DriverClick(Hub,ObjName,driver)
    pg.press(['right','right','right','right','right','right','right','right','right'\
        'right','right','right','right','right','right','right','right','right'\
        'right','right','right','right','right','right','right','right','right'\
        'right','right','right','right','right','right','right','right','right'\
        'right','right','right','right','right','right','right','right','right'\
        'right','right','right','right','right','right','right','right','right'\
        'right','right','right','right','right','right','right','right','right'\
        'right','right','right','right','right','right','right','right','right'\
        'right','right','right','right','right','right','right','right','right'])
    pg.press(['backspace','backspace','backspace','backspace','backspace','backspace','backspace','backspace','backspace'\
        'backspace','backspace','backspace','backspace','backspace','backspace','backspace','backspace','backspace'\
        'backspace','backspace','backspace','backspace','backspace','backspace','backspace','backspace','backspace'\
        'backspace','backspace','backspace','backspace','backspace','backspace','backspace','backspace','backspace'\
        'backspace','backspace','backspace','backspace','backspace','backspace','backspace','backspace','backspace'\
        'backspace','backspace','backspace','backspace','backspace','backspace','backspace','backspace','backspace'\
        'backspace','backspace','backspace','backspace','backspace','backspace','backspace','backspace','backspace'\
        'backspace','backspace','backspace','backspace','backspace','backspace','backspace','backspace','backspace'\
        'backspace','backspace','backspace','backspace','backspace','backspace','backspace','backspace','backspace'])
    pg.write(CSVURL, interval=0.01)#直接SENDできないのでpyautoguiで入力
    #----------------------------------------------------------------------------------------------------------------------
    #要素クリック----------------------------------------------------------------------------------------------------------
    Hub = "AutomationID" #取得要素のタイプ指定
    ObjName = "fileNameTextBox"
    DriverClick(Hub,ObjName,driver)
    pg.press(['right','right','right','right','right','right','right','right','right'\
        'right','right','right','right','right','right','right','right','right'\
        'right','right','right','right','right','right','right','right','right'\
        'right','right','right','right','right','right','right','right','right'\
        'right','right','right','right','right','right','right','right','right'\
        'right','right','right','right','right','right','right','right','right'\
        'right','right','right','right','right','right','right','right','right'\
        'right','right','right','right','right','right','right','right','right'\
        'right','right','right','right','right','right','right','right','right'])
    pg.press(['backspace','backspace','backspace','backspace','backspace','backspace','backspace','backspace','backspace'\
        'backspace','backspace','backspace','backspace','backspace','backspace','backspace','backspace','backspace'\
        'backspace','backspace','backspace','backspace','backspace','backspace','backspace','backspace','backspace'\
        'backspace','backspace','backspace','backspace','backspace','backspace','backspace','backspace','backspace'\
        'backspace','backspace','backspace','backspace','backspace','backspace','backspace','backspace','backspace'\
        'backspace','backspace','backspace','backspace','backspace','backspace','backspace','backspace','backspace'\
        'backspace','backspace','backspace','backspace','backspace','backspace','backspace','backspace','backspace'\
        'backspace','backspace','backspace','backspace','backspace','backspace','backspace','backspace','backspace'\
        'backspace','backspace','backspace','backspace','backspace','backspace','backspace','backspace','backspace'])
    pg.write(CSVName, interval=0.01)#直接SENDできないのでpyautoguiで入力
    #----------------------------------------------------------------------------------------------------------------------
    #要素クリック----------------------------------------------------------------------------------------------------------
    Hub = "AutomationID" #取得要素のタイプ指定
    ObjName = "fileTypeComboBox"
    DriverClick(Hub,ObjName,driver)
    pg.press('down')
    pg.press('down')
    pg.press('down')
    pg.press('return')
    #----------------------------------------------------------------------------------------------------------------------
    #要素クリック----------------------------------------------------------------------------------------------------------
    Hub = "AutomationID" #取得要素のタイプ指定
    ObjName = "saveButton"
    CsvPath = CSVURL + "/" + CSVName + ".CSV"
    if os.path.isfile(CsvPath) == True:
        DriverClick(Hub,ObjName,driver)
        time.sleep(1)
        FileNameList = ["FileOverQ.png","FileOverQ2.png"]
        conf = 0.9
        LoopVal = 10
        if ImgCheckForList(FolURL2,FileNameList,conf)[0] == True:
            pg.press('y')
    else:
        DriverClick(Hub,ObjName,driver)
        time.sleep(1)
#----------------------------------------------------------------------------------------------------------------------
def SortCSVItem(C_Child,Col1,Col2,Col3,Col4,Key):#CSVと列名を4つ与えて4つの複合と引数Keyが一致する行数を返す
        #切出CSVをループ処理-------------------------------------------------------------------------------------------------------
    C_CforCount = 0
    C_CdfRow = np.array(C_Child).shape[0]#配列行数取得
    C_CdfCol = np.array(C_Child).shape[1]#配列列数取得
    ItemList = []
    for y in range(C_CdfRow):
        #関与先DB配列をループして識別番号とPassを取得
        C_CdfDataRow = C_Child.loc[y]
        C_CSCode = C_CdfDataRow[Col1]
        C_CName = C_CdfDataRow[Col2]
        C_CZeimoku = C_CdfDataRow[Col3]
        C_CSousin = C_CdfDataRow[Col4]
        C_CAll = str(C_CSCode) + str(C_CName) 
        if Key == C_CAll and C_CSousin == "済":
            ItemList.append(C_CforCount)
            C_CforCount = C_CforCount + 1
        else:
            C_CforCount = C_CforCount + 1
    return ItemList
#----------------------------------------------------------------------------------------------------------------------
def SortPDF(PDFName):
    Fol = str(dt.today().year) + "-" + str(dt.today().month)
    pt = "\\\\Sv05121a\\e\\電子ファイル\\メッセージボックス\\" + Fol + "\\送信分受信通知"
    #path = path.replace('\\','/')#先
    PDFFileList = os.listdir(pt)
    Cou = 1
    for PDFItem in PDFFileList:
        PDFName = PDFName.replace("\u3000","").replace("PDF","") .replace("pdf","")  
        PDFItem = PDFItem.replace("\u3000","").replace("PDF","") .replace("pdf","")  
        if PDFName in PDFItem:
            Cou = Cou + 1
    return str(Cou),pt
#----------------------------------------------------------------------------------------------------------------------
def NitijiBunki(FolURL2,conf,LoopVal):
    List = ["SinkokuUketuke.png","SinkokuUketukeLire.png"]
    Tar = ImgCheckForList(FolURL2,List,conf)
    if Tar[0] == True:
        Cli = ImgClick(FolURL2,Tar[1],conf,LoopVal)
        FileName = "SinkokuUketukeTarget.png"
        while pg.locateOnScreen(FolURL2 + "/" + FileName, confidence=0.99999) is None:
            pyautogui.click(Cli[0], Cli[1])
#----------------------------------------------------------------------------------------------------------------------
def NitijiBunkiSinsei(FolURL2,conf,LoopVal):
    List = ["SinseiUketuke.png","SinseiUketukeLire.png"]
    Tar = ImgCheckForList(FolURL2,List,conf)
    if Tar[0] == True:
        Cli = ImgClick(FolURL2,Tar[1],conf,LoopVal)
        FileName = "SinseiUketukeTarget.png"
        while pg.locateOnScreen(FolURL2 + "/" + FileName, confidence=0.99999) is None:
            pyautogui.click(Cli[0], Cli[1])
#----------------------------------------------------------------------------------------------------------------------
def TaxHantei(List,FolURL2,FileName,conf,LoopVal,CSVName,driver):#選択済と未選択状態のタブアイコンをクリックし、各税申告処理を分ける
    if ImgCheck(FolURL2,FileName,conf,LoopVal)[0] == True:
        if ImgCheckForList(FolURL2,List,conf)[0] == True:
            FindURL = ImgCheckForList(FolURL2,List,conf)[1]
            ImgClick(FolURL2, FindURL, conf, LoopVal)
        time.sleep(1)
    #----------------------------------------------------------------------------------------------------------------------
    time.sleep(1)
    #読込画面が消える(ImgCheck==False)まで待機-----------------------------------------------------------------------------
    FileName = "SinkokuLoad.png"
    conf = 0.9#画像認識感度
    while ImgNothingCheck(FolURL2,FileName,conf,1) == False:
        time.sleep(1)
    if NitijiBunkiTrigger == "y":
        if CSVName == 'SinseiJyusinMaster' or CSVName == 'SinseiJyusinChild':#処理が申請の場合
            NitijiBunkiSinsei(FolURL2,conf,LoopVal)
        else:
            NitijiBunki(FolURL2,conf,LoopVal)
    #CSVOUT処理--------------------------------------------------------------------------------------------------------
    FileName = "NoCsvOutPut.png"
    conf = 0.9#画像認識感度
    time.sleep(1)
    if ImgNothingCheck(FolURL2,FileName,conf,10) == True:
        FileName = "CsvOutPut.png"
        conf = 0.9#画像認識感度
        if ImgCheck(FolURL2,FileName,conf,LoopVal)[0] == True:
            ImgClick(FolURL2,FileName,conf,LoopVal)
            time.sleep(1)
            CSVURL = FolURL2
            CSVOutPut(CSVURL,CSVName,driver,FolURL2)####################################################################################################################################################################################################################################
            C_url = CSVURL.replace("\\","/") + '/' + CSVName + '.CSV'
            SerchEnc = format(getFileEncoding(C_url))
            C_Array = pd.read_csv(C_url,encoding=SerchEnc)
            return C_Array,True
        else:
            print("ChildCSV無")
            return [],False
    else:
            print("ChildCSV無")
            return [],False
        #------------------------------------------------------------------------------------------------------------------
def Jyusin(driver,FolURL2,C_SCode,C_Name,C_Zeimoku,C_Teisyutu,CSVName):
    Fol = str(dt.today().year) + "-" + str(dt.today().month)
    pt = "\\\\Sv05121a\\e\\電子ファイル\\メッセージボックス\\" + Fol + "\\送信分受信通知"
    if CSVName == "SinseiJyusinMaster" or CSVName == "SinseiJyusinChild":
        time.sleep(1)
        # while pg.locateOnScreen(FolURL2 + "/TaikiBar.png" ,confidence = 0.9) is not None:
        #     Cyou = 0
        while pg.locateOnScreen(FolURL2 + "/DensiSinseiUnderArrow.png" ,confidence = 0.9) is None:
            time.sleep(1)
        MPC = ImgCheck(FolURL2,"MPSET.png",0.9,3)
        if MPC[0] == True:
            time.sleep(1)
            IList = ["MPOut.png","MPOutOn.png"]
            IListC = ImgCheckForList(FolURL2,IList,0.9)
            Cyou = 0
            if IListC[0] == True:
                ImgClick(FolURL2,IListC[1],0.9,1)
                while pg.locateOnScreen(FolURL2 + "/CsvOutPut.png" ,confidence = 0.99999) is None:
                    time.sleep(1)
                    ICP = ImgCheck(FolURL2,"PrintKekka.png",0.9,3)
                    if ICP[0] == True:                        
                        if Cyou == 0:
                            FileURL = pt + "\\" + str(C_SCode) + "_" + C_Name + "_" + C_Zeimoku + "_" + C_Teisyutu +  ".pdf"
                        else:
                            FileURL = pt + "\\" + str(C_SCode) + "_" + C_Name + "_" + C_Zeimoku + "_" + C_Teisyutu + str(Cyou) + ".pdf"
                        pyperclip.copy(FileURL)
                        pg.hotkey('ctrl', 'v')#pg日本語不可なのでコピペ
                        pg.press(['return'])                        
                        time.sleep(1)
                        pg.keyDown('alt')
                        pg.press(['s'])
                        pg.keyUp('alt')
                        time.sleep(1)
                        FSI = ImgCheck(FolURL2,"FOQSinsei.png",0.9,3)
                        if FSI[0] == True:
                            pg.press("y")
                        Cyou = Cyou + 1
                time.sleep(1)
        else:
            ImgClick(FolURL2,"DensiSinseiUnderArrow.png",0.9,3)
            time.sleep(1)
            ImgClick(FolURL2,"MPPDF.png",0.9,3)
            time.sleep(1)
            IList = ["MPOut.png","MPOutOn.png"]
            IListC = ImgCheckForList(FolURL2,IList,0.9)
            Cyou = 0
            if IListC[0] == True:
                ImgClick(FolURL2,IListC[1],0.9,1)                   
                while pg.locateOnScreen(FolURL2 + "/CsvOutPut.png" ,confidence = 0.99999) is None:
                    time.sleep(1)
                    ICP = ImgCheck(FolURL2,"PrintKekka.png",0.9,3)
                    if ICP[0] == True:
                        if Cyou == 0:
                            FileURL = pt + "\\" + str(C_SCode) + "_" + C_Name + "_" + C_Zeimoku + "_" + C_Teisyutu +  ".pdf"
                        else:
                            FileURL = pt + "\\" + str(C_SCode) + "_" + C_Name + "_" + C_Zeimoku + "_" + C_Teisyutu + str(Cyou) + ".pdf"
                        pyperclip.copy(FileURL)
                        pg.hotkey('ctrl', 'v')#pg日本語不可なのでコピペ
                        pg.press(['return'])
                        time.sleep(1)
                        pg.keyDown('alt')
                        pg.press(['s'])
                        pg.keyUp('alt')
                        time.sleep(1)
                        FSI = ImgCheck(FolURL2,"FOQSinsei.png",0.9,3)
                        if FSI[0] == True:
                            pg.press("y")
                        Cyou = Cyou + 1
                time.sleep(1)
    else:
        #要素クリック----------------------------------------------------------------------------------------------------------
        Hub = "AutomationID" #取得要素のタイプ指定
        ObjName = "printerComboBox"
        DriverClick(Hub,ObjName,driver)#一括電子申告起動ボタン2を押す
        conf = 0.9
        LoopVal = 10
        List = ["MSPdfIcon.png","MSPdfIcon2.png"]
        MSPdfIcon = ImgCheckForList(FolURL2,List,conf)
        if MSPdfIcon[0] == True:
            ImgClick(FolURL2,MSPdfIcon[1],conf,LoopVal)
        #----------------------------------------------------------------------------------------------------------------------
        #要素クリック----------------------------------------------------------------------------------------------------------
        Hub = "AutomationID" #取得要素のタイプ指定
        ObjName = "printButton"
        DriverClick(Hub,ObjName,driver)#一括電子申告起動ボタン2を押す
        #----------------------------------------------------------------------------------------------------------------------           
        time.sleep(1)
        conf = 0.9
        LoopVal = 500
        FileName = "PrintKekka.png"
        if ImgCheck(FolURL2,FileName,conf,LoopVal)[0] == True:
            #----------------------------------------------------------------------------------------------------------------------
            Tyouhuku = SortPDF(str(C_SCode) + "_" + C_Name + ".pdf")
            if Tyouhuku[0] == str(1):
                FileURL = Tyouhuku[1] + "\\" + str(C_SCode) + "_" + C_Name + "_" + C_Zeimoku + "_" + C_Teisyutu +  ".pdf"
            else:
                FileURL = Tyouhuku[1] + "\\" +  str(C_SCode) + "_" + C_Name + Tyouhuku[0] + "_" + C_Zeimoku + "_" + C_Teisyutu + ".pdf"

            pyperclip.copy(FileURL)
            pg.hotkey('ctrl', 'v')#pg日本語不可なのでコピペ
            pg.press(['return'])
            time.sleep(1)
            pg.keyDown('alt')
            pg.press(['s'])
            pg.keyUp('alt')
            time.sleep(1)
            FileName = "DensiSousintyu.png"
            EraceIMGWait(FolURL2,FileName)
            #要素クリック----------------------------------------------------------------------------------------------------------
            Hub = "AutomationID" #取得要素のタイプ指定
            ObjName = "cancelButton"
            DriverClick(Hub,ObjName,driver)#一括電子申告起動ボタン2を押す
            time.sleep(1)
            FileName = "IkkatuEndMsg.png"
            EraceIMGWait(FolURL2,FileName)
            Syoridumi = 1
            #----------------------------------------------------------------------------------------------------------------------
        else:
            Syoridumi = 0 
#各税目チャイルドCSVに対する処理----------------------------------------------------------------------------------------------------------------------
def MLChild(List,FileName,CSVName,CSVChildName,C_Master,C_dfRow,C_dfCol,C_Sousin,driver,FolURL2,DayCount,C_All,C_Child,C_SCode,C_Name,C_Zeimoku,C_Teisyutu):
    if C_Sousin == "済" and DayCount.days <= DayC and DayCount.days >= -DayC: #送信パラメータが済かつターミナル指定の日数内のデータか判定
        if CSVName == "SinseiJyusinMaster" or CSVName == "SinseiJyusinChild": #対象税目が申請か判定
            ItemRowArray = SortCSVItem(C_Child,"関与先コード","納税者(関与先)","申請・届出書類名","送信",C_All) #CSVと列名を4つ与えて4つの複合と引数Keyが一致する行数を返す
        else:
            ItemRowArray = SortCSVItem(C_Child,"関与先コード","納税者(関与先)","税目","送信",C_All) #CSVと列名を4つ与えて4つの複合と引数Keyが一致する行数を返す
        Pc = ItemRowArray[0] #取得した行数を格納
        #Target選択の為にページダウンが必要か行数から割り出す-------------------------------------------------------------------------------------------
        if ItemRowArray[0] >= 14: #取得した行数が14以上なら
            Pc = ItemRowArray[0]/14 #取得した行数を14で除する
            for p in range(int(Pc)):#14で除した整数分処理
                FileName = "densiIcon.png"#画面テキスト「電子申告完了報告書の一括印刷」の画像データ
                conf = 0.9#画像認識感度
                LoopVal = 10
                ImgClick(FolURL2,FileName,conf,LoopVal)#フォーカス移動の為に画像選択
                pg.press('pagedown') 
                ItemRowArray[0] = (ItemRowArray[0] - (14*int(Pc)))#ページダウン後のTargetの行数を計算
        FileName = "AnotherTrigger.png"#データ指定画面のヘッダー「送信」の画像データ
        conf = 0.9#画像認識感度
        LoopVal = 10
        xpos = ImgCheck(FolURL2,FileName,conf,LoopVal)[1]       #データ指定画面のヘッダー「送信」の画像データ横軸
        ypos = ImgCheck(FolURL2,FileName,conf,LoopVal)[2] + 70  #データ指定画面のヘッダー「送信」の画像データ縦軸に値をプラスして1行目の縦軸に
        ypos = ypos + (ItemRowArray[0]*30)                      #ページダウンがあればその分縦軸に追加
        pg.click(xpos, ypos,1, 0,'left') #送信「可」を選択
        time.sleep(3) #指定時間待機
        #要素クリック------------------------------------------------------------------------------------------------
        Hub = "AutomationID" #取得要素のタイプ指定
        ObjName = "printButton" #取得要素のName指定
        DriverClick(Hub,ObjName,driver)#電子申告送信ボタンを押す
        #------------------------------------------------------------------------------------------------------------
        #送信エラー画像判定------------------------------------------------------------------------------------------
        List = ["JyusinKanryouIcon.png"]#送信エラーウィンドウを指定
        ErrMsg = ""
        if ImgCheckForList(FolURL2,List,conf)[0] == True:#リスト内の画像があればTrueと画像名を返す
            pg.press('return') 
            ErrMsg = "送信エラー"
            time.sleep(1)
        #------------------------------------------------------------------------------------------------------------
        if ErrMsg == "送信エラー":#前工程で送信エラーなら
            FileName = "jimusyoCD.png"#画面左上の事務所コード画像を元に読込判定
            conf = 0.9#画像認識感度
            LoopVal = 10#検索回数
            if ImgCheck(FolURL2,FileName,conf,LoopVal)[0] == True:
                print("送信エラーをスキップしました。")
            LoopVal = 10#検索回数
        else:
            print("送信エラー無")
            Jyusin(driver,FolURL2,C_SCode,C_Name,C_Zeimoku,C_Teisyutu,CSVName)
            for x in range(int(Pc)):
                NitijiBunki(FolURL2,conf,LoopVal)
                pg.press('pageup')
    else:
        NoAction = True
        print("送信不可") 
#----------------------------------------------------------------------------------------------------------------------
#各税目毎の処理-------------------------------------------------------------------------------------------------------------
def MasterLoop(List,FileName,CSVName,CSVChildName,C_Master,C_dfRow,C_dfCol,driver,FolURL2):
    C_forCount = 0
    NoAction = False #各税目初回起動時はFalse
    Todays = dt.today() #今日の日付
    #----------------------------------------------------------------------------------------------------------------------
    #切出MasterCSVをループ処理---------------------------------------------------------------------------------------------
    for x in range(C_dfRow):
        #関与先DB配列をループして識別番号とPassを取得
        if CSVName == 'SinseiJyusinMaster':#処理が申請の場合
            C_dfDataRow = C_Master.iloc[x,:]#行データ取得
            C_SCode = C_dfDataRow["関与先コード"]
            C_Name = C_dfDataRow["納税者(関与先)"]
            C_All =  str(C_SCode) + str(C_Name) 
            C_Name = C_Name.replace("\u3000"," ")
            C_Zeimoku = C_dfDataRow["申請・届出書類名"]
            C_Sousin = C_dfDataRow["送信"]
            C_UketukeDay = C_dfDataRow["申請受付日時"]
            C_Houkoku = C_dfDataRow["報告書"]
            C_Teisyutu = C_dfDataRow["提出先"]
        else:#処理が申請以外の場合
            C_dfDataRow = C_Master.iloc[x,:]#行データ取得
            C_SCode = C_dfDataRow["関与先コード"]
            C_Name = C_dfDataRow["納税者(関与先)"]
            C_All =  str(C_SCode) + str(C_Name) 
            C_Name = C_Name.replace("\u3000"," ")
            C_Zeimoku = C_dfDataRow["税目"]
            C_Sousin = C_dfDataRow["送信"]
            C_UketukeDay = C_dfDataRow["申告受付日時"]
            C_Houkoku = C_dfDataRow["報告書"]
            C_Teisyutu = C_dfDataRow["事業年度／課税期間"]
        #申請処理----------------------------------------------------------------------------------------------------------
        conf = 0.9#画像認識感度
        LoopVal = 10
        if Syoridumi == 0:#処理済フラグが立っているか判定
            C_CM = TaxHantei(List,FolURL2,FileName,conf,LoopVal,CSVChildName,driver)#チャイルドCSVを取得
            C_Child = C_CM[0]#チャイルドCSVを格納
            C_CdfRow = np.array(C_Child).shape[0]#配列行数取得
            C_CdfCol = np.array(C_Child).shape[1]#配列列数取得
        C_CforCount = 0
        #ターミナルで指定した日数の対象になるか計算----------------------------------------------------------------------------------
        C_UketukeDay = C_UketukeDay.replace("(",".").replace("（",".").replace(")","").replace("）","")
        C_UkeSplit = C_UketukeDay.split(".")
        WarekiSpl = WarekiHenkan.SeirekiDate("R",int(C_UkeSplit[0]),int(C_UkeSplit[1]),int(C_UkeSplit[2]))
        WarekiSpl = WarekiSpl + " 00:00:00"
        C_UketukeDay = dt.strptime(WarekiSpl, '%Y/%m/%d %H:%M:%S')
        DayCount = Todays - C_UketukeDay
        DayCount.days
        #----------------------------------------------------------------------------------------------------------------------
        #引数を渡してチャイルドCSVに対しループ処理----------------------------------------------------------------------------------
        if CSVName == 'SinseiJyusinMaster':
            MLChild(List,FileName,CSVName,CSVChildName,C_Master,C_dfRow,C_dfCol,C_Sousin,driver,FolURL2,DayCount,C_All,C_Child,C_SCode,C_Name,C_Zeimoku,C_Teisyutu)
            time.sleep(1)
        else:
            MLChild(List,FileName,CSVName,CSVChildName,C_Master,C_dfRow,C_dfCol,C_Sousin,driver,FolURL2,DayCount,C_All,C_Child,C_SCode,C_Name,C_Zeimoku,C_Teisyutu)
            time.sleep(1)
        #----------------------------------------------------------------------------------------------------------------------
#メインの処理----------------------------------------------------------------------------------------------------------------
def MainFlow(FolURL2):#メインの処理
    BatUrl = FolURL2 + "/bat/AWADriverOpen.bat"#4724ポート指定でappiumサーバー起動バッチを開く
    driver = OMSOpen.MainFlow(BatUrl,FolURL2,"RPAPhoto")#OMSを起動しログイン後インスタンス化
    FolURL2 = FolURL2 + "/RPAPhoto/TKC_DensiSinkoku"#このフローで必要な画像保存先
    #----------------------------------------------------------------------------------------------------------------------
    #要素クリック----------------------------------------------------------------------------------------------------------
    Hub = "AutomationID" #取得要素のタイプ指定
    ObjName = "um12PictureButton" #取得要素のName指定
    DriverClick(Hub,ObjName,driver)#一括電子申告ボタンを押す
    #----------------------------------------------------------------------------------------------------------------------
    #要素クリック----------------------------------------------------------------------------------------------------------
    FileName = "DensiSinkokuHub.png" #取得画像のName指定
    conf = 0.9 #画像認識感度
    LoopVal = 10 #検索回数
    ImgClick(FolURL2,FileName,conf,LoopVal)#電子申告・申請タブを押す
    #----------------------------------------------------------------------------------------------------------------------
    #要素クリック----------------------------------------------------------------------------------------------------------
    Hub = "AutomationID" #取得要素のタイプ指定
    ObjName = "ao215Button" #取得要素のName指定
    DriverClick(Hub,ObjName,driver)#一括電子申告起動ボタン2を押す
    #----------------------------------------------------------------------------------------------------------------------
    time.sleep(5) #指定時間待機
    for x in range(10):#MSGが出てくるので、消えるまでエンターを押す
        if not DriverCheck(Hub,ObjName,driver) == True:
            pg.press('return')
        else:
            pg.press('return')
            break
    #要素クリック----------------------------------------------------------------------------------------------------------
    Hub = "AutomationID" #取得要素のタイプ指定  
    ObjName = "taxAccountantComboBox"#税理士選択コンボボックスをクリック
    DriverClick(Hub,ObjName,driver)
    time.sleep(1)
    pg.press('down')
    pg.press('return')#小林常務を選択
    #FileName = "KanyoHasegawa.png"#担当税理士所長判定
    #法人税消費税処理------------------------------------------------------------------------------------------------------
    # FileName = "KanyoZeirisi.png"#担当税理士小林常務判定
    # conf = 0.9#画像認識感度
    # LoopVal = 500
    # CSVName = 'HoujinSyouhizeiJyusinMaster'
    # CSVChildName = 'HoujinSyouhizeiJyusinChild'#チャイルドのCSVファイル名を指定
    # List = ["HoujinSyouhizei.png","HoujinSyouhizei2.png"]
    # TaxAns = TaxHantei(List,FolURL2,FileName,conf,LoopVal,CSVName,driver)#pandasにマスターCSVぶっこみ(戻り値：配列,Boolean)
    # C_Master = TaxAns[0]
    # C_Master = C_Master[C_Master.duplicated(subset='関与先コード')]
    # C_MasterFlag = TaxAns[1]
    # C_dfRow = np.array(C_Master).shape[0]#配列行数取得
    # C_dfCol = np.array(C_Master).shape[1]#配列列数取得
    # if C_MasterFlag == False:
    #     print("C_Masterは空です")
    # else:
    #     C_LoopRow = np.array(C_Master).shape[0]#配列行数取得
    #     for x in range(C_LoopRow):
    #         MasterLoop(List,FileName,CSVName,CSVChildName,C_Master,C_dfRow,C_dfCol,driver,FolURL2) 
    #-----------------------------------------------------------------------------------------------------------------------
    ##所得税消費税処理------------------------------------------------------------------------------------------------------
    #FileName = "KanyoZeirisi.png"#担当税理士小林常務判定
    #conf = 0.9#画像認識感度
    #LoopVal = 500
    #CSVName = 'SyotokuSyouhizeiJyusinMaster'
    #CSVChildName = 'SyotokuSyouhizeiJyusinChild'#チャイルドのCSVファイル名を指定
    #List = ["SyotokuSyouhizei.png","SyotokuSyouhizei2.png"]
    #TaxAns = TaxHantei(List,FolURL2,FileName,conf,LoopVal,CSVName,driver)#pandasにマスターCSVぶっこみ(戻り値：配列,Boolean)
    #C_Master = TaxAns[0]
    #C_MasterFlag = TaxAns[1]
    #if C_MasterFlag == False:
    #    print("C_Masterは空です")
    #else:
    #    C_Master = C_Master[C_Master['送信']=='可']#送信列「可」のみ抽出
    #    C_Master = C_Master.drop_duplicates(subset='関与先コード')#関与先コードをキーに重複削除
    #    C_dfRow = np.array(C_Master).shape[0]#配列行数取得
    #    C_dfCol = np.array(C_Master).shape[1]#配列列数取得
    #    MasterLoop(List,FileName,CSVName,CSVChildName,C_Master,C_dfRow,C_dfCol,driver,FolURL2) 
    ##-----------------------------------------------------------------------------------------------------------------------
    # #法定調書給報処理------------------------------------------------------------------------------------------------------
    # FileName = "KanyoZeirisi.png"#担当税理士小林常務判定
    # conf = 0.9#画像認識感度
    # LoopVal = 500
    # CSVName = 'HouteiKyuuhouJyusinMaster'
    # CSVChildName = 'HouteiKyuuhouJyusinChild'#チャイルドのCSVファイル名を指定
    # List = ["HouteiKyuuhou.png","HouteiKyuuhou2.png"] #タブアイコン2色のNameをリスト化
    # TaxAns = TaxHantei(List,FolURL2,FileName,conf,LoopVal,CSVName,driver)#pandasにマスターCSVぶっこみ(戻り値：配列,Boolean)
    # C_Master = TaxAns[0]
    # C_Master = C_Master[C_Master.duplicated(subset='関与先コード')]
    # C_MasterFlag = TaxAns[1]
    # C_dfRow = np.array(C_Master).shape[0]#配列行数取得
    # C_dfCol = np.array(C_Master).shape[1]#配列列数取得
    # if C_MasterFlag == False:
    #     print("C_Masterは空です")
    # else:
    #     C_LoopRow = np.array(C_Master).shape[0]#配列行数取得
    #     for x in range(C_LoopRow):
    #         MasterLoop(List,FileName,CSVName,CSVChildName,C_Master,C_dfRow,C_dfCol,driver,FolURL2)   
    # #-----------------------------------------------------------------------------------------------------------------------
    #申請処理---------------------------------------------------------------------------------------------------------------
    FileName = "KanyoZeirisi.png"#担当税理士小林常務判定
    conf = 0.9#画像認識感度
    LoopVal = 500
    CSVName = 'SinseiJyusinMaster' #保存するCSVの名称を指定
    CSVChildName = 'SinseiJyusinChild'#チャイルドのCSVファイル名を指定
    List = ["Sinsei.png","Sinsei2.png"] #タブアイコン2色のNameをリスト化
    TaxAns = TaxHantei(List,FolURL2,FileName,conf,LoopVal,CSVName,driver)#pandasにマスターCSVぶっこみ(戻り値：配列,Boolean)
    C_Master = TaxAns[0]#マスターCSVを格納
    #C_Master = C_Master[C_Master.duplicated(subset='関与先コード')]#マスターCSVから関与先コードの重複削除##############################################################
    C_MasterFlag = TaxAns[1]#マスターCSV読込結果を格納
    C_dfRow = np.array(C_Master).shape[0]#配列行数取得
    C_dfCol = np.array(C_Master).shape[1]#配列列数取得
    if C_MasterFlag == False:#マスターCSVが空だったら～
        print("C_Masterは空です")
    else:
        C_LoopRow = np.array(C_Master).shape[0]#マスターCSV行数取得
        for x in range(C_LoopRow):#マスターCSV行数分取得ループ実行
            MasterLoop(List,FileName,CSVName,CSVChildName,C_Master,C_dfRow,C_dfCol,driver,FolURL2)  
    #-----------------------------------------------------------------------------------------------------------------------
    #償却資産処理------------------------------------------------------------------------------------------------------
    FileName = "KanyoZeirisi.png"#担当税理士小林常務判定
    conf = 0.9#画像認識感度
    LoopVal = 500
    CSVName = 'SyoukyakuJyusinMaster'
    CSVChildName = 'SyoukyakuJyusinChild'#チャイルドのCSVファイル名を指定
    List = ["Syoukyaku.png","Syoukyaku2.png"] #タブアイコン2色のNameをリスト化
    TaxAns = TaxHantei(List,FolURL2,FileName,conf,LoopVal,CSVName,driver)#pandasにマスターCSVぶっこみ(戻り値：配列,Boolean)
    C_Master = TaxAns[0]#マスターCSVを格納
    C_MasterFlag = TaxAns[1]#マスターCSV読込結果を格納
    if C_MasterFlag == False:#マスターCSVが空だったら～
        print("C_Masterは空です")
    else:
        C_Master = C_Master[C_Master['送信']=='可']#送信列「可」のみ抽出
        C_Master = C_Master.drop_duplicates(subset='関与先コード')#関与先コードをキーに重複削除
        C_dfRow = np.array(C_Master).shape[0]#配列行数取得
        C_dfCol = np.array(C_Master).shape[1]#配列列数取得
        MasterLoop(List,FileName,CSVName,CSVChildName,C_Master,C_dfRow,C_dfCol,driver,FolURL2)     
    #-----------------------------------------------------------------------------------------------------------------------
    #贈与税処理------------------------------------------------------------------------------------------------------
    FileName = "KanyoZeirisi.png"#担当税理士小林常務判定
    conf = 0.9#画像認識感度
    LoopVal = 500
    CSVName = 'ZouyoJyusinMaster'
    CSVChildName = 'ZouyoJyusinChild'#チャイルドのCSVファイル名を指定
    List = ["Zouyo.png","Zouyo2.png"] #タブアイコン2色のNameをリスト化
    TaxAns = TaxHantei(List,FolURL2,FileName,conf,LoopVal,CSVName,driver)#pandasにマスターCSVぶっこみ(戻り値：配列,Boolean)
    C_Master = TaxAns[0]
    C_MasterFlag = TaxAns[1]
    if C_MasterFlag == False:
        print("C_Masterは空です")
    else:
        C_Master = C_Master[C_Master['送信']=='可']#送信列「可」のみ抽出
        C_Master = C_Master.drop_duplicates(subset='関与先コード')#関与先コードをキーに重複削除
        C_dfRow = np.array(C_Master).shape[0]#配列行数取得
        C_dfCol = np.array(C_Master).shape[1]#配列列数取得
        MasterLoop(List,FileName,CSVName,CSVChildName,C_Master,C_dfRow,C_dfCol,driver,FolURL2)        
    #-----------------------------------------------------------------------------------------------------------------------
    #相続税処理------------------------------------------------------------------------------------------------------
    FileName = "KanyoZeirisi.png"#担当税理士小林常務判定
    conf = 0.9#画像認識感度
    LoopVal = 500
    CSVName = 'SouzokuJyusinMaster'
    CSVChildName = 'SouzokuJyusinChild'#チャイルドのCSVファイル名を指定
    List = ["Souzoku.png","Souzoku2.png"] #タブアイコン2色のNameをリスト化
    TaxAns = TaxHantei(List,FolURL2,FileName,conf,LoopVal,CSVName,driver)#pandasにマスターCSVぶっこみ(戻り値：配列,Boolean)
    C_Master = TaxAns[0]
    C_MasterFlag = TaxAns[1]
    if C_MasterFlag == False:
        print("C_Masterは空です")
    else:
        C_Master = C_Master[C_Master['送信']=='可']#送信列「可」のみ抽出
        C_Master = C_Master.drop_duplicates(subset='関与先コード')#関与先コードをキーに重複削除
        C_dfRow = np.array(C_Master).shape[0]#配列行数取得
        C_dfCol = np.array(C_Master).shape[1]#配列列数取得
        MasterLoop(List,FileName,CSVName,CSVChildName,C_Master,C_dfRow,C_dfCol,driver,FolURL2)
    #-----------------------------------------------------------------------------------------------------------------------
    #配当調書処理------------------------------------------------------------------------------------------------------
    FileName = "KanyoZeirisi.png"#担当税理士小林常務判定
    conf = 0.9#画像認識感度
    LoopVal = 500
    CSVName = 'HaitouJyusinMaster'
    CSVChildName = 'HaitouJyusinChild'#チャイルドのCSVファイル名を指定
    List = ["Haitou.png","Haitou2.png"] #タブアイコン2色のNameをリスト化
    TaxAns = TaxHantei(List,FolURL2,FileName,conf,LoopVal,CSVName,driver)#pandasにマスターCSVぶっこみ(戻り値：配列,Boolean)
    C_Master = TaxAns[0]
    C_MasterFlag = TaxAns[1]
    if C_MasterFlag == False:
        print("C_Masterは空です")
    else:
        C_Master = C_Master[C_Master['送信']=='可']#送信列「可」のみ抽出
        C_Master = C_Master.drop_duplicates(subset='関与先コード')#関与先コードをキーに重複削除
        C_dfRow = np.array(C_Master).shape[0]#配列行数取得
        C_dfCol = np.array(C_Master).shape[1]#配列列数取得
        MasterLoop(List,FileName,CSVName,CSVChildName,C_Master,C_dfRow,C_dfCol,driver,FolURL2)        
    #-----------------------------------------------------------------------------------------------------------------------

#モジュールインポート
from appium import webdriver
import subprocess
from subprocess import run
from subprocess import PIPE
import pyautogui as pg
import time
import OMSOpen
from selenium.webdriver.common.keys import Keys
#lxmlインポート
import lxml.html
#pandasインポート
import pandas as pd
#配列計算関数numpyインポート
import numpy as np
#小数点切り捨ての為にmathをインポート
import math
#timeインポート
import time
#reインポート
import re
#jsonインポート
import json
#osインポート
import os
#datetimeインポート
from datetime import datetime as dt
#日付加減算インポート
from dateutil.relativedelta import relativedelta
#glob(フォルダファイルチェックコマンド)インポート
import glob
#shutil(フォルダファイル編集コマンド)インポート
import shutil
#例外処理判定の為のtracebackインポート
import traceback
#pandas(pd)で関与先データCSVを取得
import pyautogui
import time
import shutil
from datetime import datetime, timedelta
import pyperclip #クリップボードへのコピーで使用
import WarekiHenkan #WarekiHenkan.SeirekiDate("R",4,1,19) = 返り値2022/1/19(str)
import sys
from tkinter import messagebox
import chardet
from chardet.universaldetector import UniversalDetector

#RPA用画像フォルダの作成---------------------------------------------------------
FolURL = "//Sv05121a/e/C 作業台/RPA/ALLDataBase/RPAPhoto/TKC_DensiSinkoku"#元
FolURL2 = os.getcwd().replace('\\','/')#先
#印刷対象をターミナルで設定------------------------------------------------------------
NitijiBunkiTrigger = input("最新日時順にダウンロードしますか？y/n\n")
if NitijiBunkiTrigger == "y":
    DayC = int(input("申告受付日時が本日から何日以内の範囲でダウンロードしますか？数値のみ記載してください。\n"))
else:
    DayC = 15
try:
    Syoridumi = 0#初回起動フラグ
    MainFlow(FolURL2)
except:
    traceback.print_exc()