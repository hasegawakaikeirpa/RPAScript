#----------------------------------------------------------------------------------------------------------------------
def DriverUIWaitXPATH(UIPATH,driver):#XPATH要素を取得するまで待機
    for x in range(10000):
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
    for x in range(10000):
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
    for x in range(10000):
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
    for x in range(10000):
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
def ImgCheckForList(FolURL2,List,conf,LoopVal):#リスト内の画像があればTrueと画像名を返す
    for x in range(LoopVal):
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
    for x in range(10000):
        if ImgCheck(FolURL2,FileName,conf,LoopVal)[0] == True:#OMSメニューの年調起動ボタンを判定して初期処理分け
            #正常待機後処理
            for y in range(10000):
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
def SortCSVItem(SortURL,SortName,Key):#CSVと列名を4つ与えて4つの複合と引数Keyが一致する行数を返す
    Sort_url = SortURL.replace("\\","/") + '/' + SortName + '.CSV'
    with codecs.open(Sort_url, "r", "utf-8", "ignore") as file:
        C_Child = pd.read_table(file,delimiter=",")
    C_CforCount = 0
    for C_ChildItem in C_Child:
        #C_ChildItemName = C_ChildItem['科目名']
        if Key == C_ChildItem:
            return C_CforCount
        else:
            C_CforCount = C_CforCount + 1
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

def MainStarter(FolURL2):
    #画像が出現するまで待機してクリック------------------------------------------------------------------------------------
    List = ["DensiSinkokuIcon.png","DensiSinkokuIcon2.png"]
    conf = 0.9#画像認識感度
    LoopVal = 10000#検索回数
    ListCheck = ImgCheckForList(FolURL2,List,conf,LoopVal)#画像検索関数
    if ListCheck[0] == True:
        ImgClick(FolURL2,ListCheck[1],conf,LoopVal)
        time.sleep(1)
        pg.keyDown('alt')
        pg.press('a')
        pg.keyUp('alt')
    time.sleep(1)
    #----------------------------------------------------------------------------------------------------------------------
    #画像が出現するまで待機してクリック------------------------------------------------------------------------------------
    List = ["DensiKaiteiClose.png","DensiKaiteiClose2.png"]
    conf = 0.9#画像認識感度
    LoopVal = 10#検索回数
    ListCheck = ImgCheckForList(FolURL2,List,conf,LoopVal)#画像検索関数
    if ListCheck[0] == True:
        ImgClick(FolURL2,ListCheck[1],conf,LoopVal)
        time.sleep(1)
    time.sleep(1)
    #----------------------------------------------------------------------------------------------------------------------
    #画像が出現するまで待機してクリック------------------------------------------------------------------------------------
    List = ["DensiKidouIcon.png","DensiKidouIcon2.png"]
    conf = 0.9#画像認識感度
    LoopVal = 10#検索回数
    ListCheck = ImgCheckForList(FolURL2,List,conf,LoopVal)#画像検索関数
    if ListCheck[0] == True:
        ImgClick(FolURL2,ListCheck[1],conf,LoopVal)
        time.sleep(1)
    time.sleep(1)
    #----------------------------------------------------------------------------------------------------------------------
    ImgClick(FolURL2,"DensiSyomei.png",conf,LoopVal)#電子申告・申請タブを押す
    #画像が出現するまで待機してクリック------------------------------------------------------------------------------------
    List = ["DensiSyomeiOpen.png","DensiSyomeiOpen2.png"]
    conf = 0.9#画像認識感度
    LoopVal = 10#検索回数
    ListCheck = ImgCheckForList(FolURL2,List,conf,LoopVal)#画像検索関数
    #if ListCheck[0] == True:
    #    ImgClick(FolURL2,ListCheck[1],conf,LoopVal)
    #    time.sleep(1)
    time.sleep(1)

def MasterCSVGet(FolURL2): 
    #----------------------------------------------------------------------------------------------------------------------
    pg.keyDown('alt')
    pg.press('p')
    pg.keyUp('alt')
    time.sleep(1)
    #画像が出現するまで待機してクリック------------------------------------------------------------------------------------
    List = ["FileOut.png","FileOut2.png"]
    conf = 0.9#画像認識感度
    LoopVal = 10000#検索回数
    ListCheck = ImgCheckForList(FolURL2,List,conf,LoopVal)#画像検索関数
    if ListCheck[0] == True:
       ImgClick(FolURL2,ListCheck[1],conf,LoopVal)
       time.sleep(1)
    time.sleep(1)
    #----------------------------------------------------------------------------------------------------------------------
    #画像が出現するまで待機してクリック------------------------------------------------------------------------------------
    List = ["PDFIcon.png","CSVIcon.png"]
    conf = 0.9#画像認識感度
    LoopVal = 10#検索回数
    ListCheck = ImgCheckForList(FolURL2,List,conf,LoopVal)#画像検索関数
    if ListCheck[0] == True:
       ImgClick(FolURL2,ListCheck[1],conf,LoopVal)
       time.sleep(1)
    time.sleep(1)
    pg.press(['up','up','up','up','up'])
    pg.press(['return'])
    #----------------------------------------------------------------------------------------------------------------------
    FileURL = os.getcwd().replace('\\','/') + "\RPAPhoto\MJS_DensiSinkoku\SyomeiMaster.CSV"
    FileURL = FileURL.replace('*',':')
    pg.write(FileURL, interval=0.01)#直接SENDできないのでpyautoguiで入力
    pg.press(['return'])
    # ---------------------------------------------------------------------------------------------------------------------- 
    ImgClick(FolURL2,"FileOutPutBtn.png",conf,LoopVal)
    FileName = "FileOverCheck.png"
    conf = 0.9#画像認識感度
    LoopVal = 10#検索回数
    if ImgNothingCheck(FolURL2,FileName,conf,LoopVal) == True:#画像がなければTrueを返す
       pg.keyDown('alt')
       pg.press('j')
       pg.keyUp('alt')
       time.sleep(1)
       pg.keyDown('alt')
       pg.press('g')
       pg.keyUp('alt')
       time.sleep(1)
    else:
       pg.press('y')
       time.sleep(1)
       pg.keyDown('alt')
       pg.press('j')
       pg.keyUp('alt')
       time.sleep(1)

    #出力したCSVを読込み----------------------------------------------------------------------------------------------------------
    CSVURL = FolURL2
    CSVName = '/SyomeiMaster'
    #C_url = CSVURL.replace("\\","/") + '/' + CSVName + '.CSV'
    C_url = CSVURL + '/' + CSVName + '.CSV'
    with codecs.open(C_url, "r", "Shift-JIS", "ignore") as file:
        C_df = pd.read_table(file, delimiter=",")
        ColLister = ['顧問先コード','年度', '税目','申告種類']
        C_df = C_df.drop_duplicates(subset=ColLister)
    print(C_df)
    return(C_df)
def MainFirstAction(FolURL2,C_SCode,C_Name ):
    conf = 0.9#画像認識感度
    LoopVal = 10000#検索回数
    if ImgCheck(FolURL2,"SousinKekka.png",conf,LoopVal)[0] == True:
        conf = 0.9#画像認識感度
        LoopVal = 10#検索回数
        if ImgCheck(FolURL2,"SousinAfterErr.png",conf,LoopVal)[0] == True:
            pg.press('x')
            conf = 0.9#画像認識感度
            LoopVal = 20#検索回数
            FileName = "MSGNokori.png"
            if ImgCheck(FolURL2, FileName, conf, LoopVal)[0] == True:
                pg.press('n')
                time.sleep(1)
                ImgClick(FolURL2,"UnderArrow.png",conf,LoopVal) 
                time.sleep(1)
                pg.press('q')
                #----------------------------------------------------------------------------------------------------------------------
                conf = 0.9#画像認識感度
                LoopVal = 20#検索回数
                FileName = "EturanCheck.png"
                if ImgCheck(FolURL2, FileName, conf, LoopVal)[0] == True:
                    pg.press('return')            
                FileName = "MSGSyousaiErr.png"
                if ImgCheck(FolURL2, FileName, conf, LoopVal)[0] == True:
                    pg.press('return')
                #画像が出現するまで待機してクリック------------------------------------------------------------------------------------
                List = ["FileOut.png","FileOut2.png"]
                conf = 0.9#画像認識感度
                LoopVal = 10000#検索回数
                ListCheck = ImgCheckForList(FolURL2,List,conf,LoopVal)#画像検索関数
                if ListCheck[0] == True:
                    ImgClick(FolURL2,ListCheck[1],conf,LoopVal)
                    time.sleep(1)
                #----------------------------------------------------------------------------------------------------------------------
                #画像が出現するまで待機してクリック------------------------------------------------------------------------------------
                List = ["PDFIcon.png","CSVIcon.png"]
                conf = 0.9#画像認識感度
                LoopVal = 10#検索回数
                ListCheck = ImgCheckForList(FolURL2,List,conf,LoopVal)#画像検索関数
                if ListCheck[0] == True:
                    ImgClick(FolURL2,ListCheck[1],conf,LoopVal)
                    time.sleep(1)
                    pg.press(['down','down','down','down','down'])
                    pg.press(['return'])
                #----------------------------------------------------------------------------------------------------------------------
                Tyouhuku = SortPDF(C_SCode + "_" + C_Name + ".pdf")
                if Tyouhuku[0] == str(1):
                    FileURL = Tyouhuku[1] + "\\" + C_SCode + "_" + C_Name + ".pdf"
                else:
                    FileURL = Tyouhuku[1] + "\\" +  C_SCode + "_" + C_Name + Tyouhuku[0] + ".pdf"
                pyperclip.copy(FileURL)
                pg.hotkey('ctrl', 'v')#pg日本語不可なのでコピペ
                pg.press(['return'])
                # ---------------------------------------------------------------------------------------------------------------------- 
                # ---------------------------------------------------------------------------------------------------------------------- 
                ImgClick(FolURL2,"FileOutPutBtn.png",conf,LoopVal) 
                time.sleep(5)
                pg.press(['x'])
                conf = 0.9#画像認識感度
                LoopVal = 20#検索回数
                FileName = "Kanryou.png"
                if ImgCheck(FolURL2, FileName, conf, LoopVal)[0] == True:
                    ImgClick(FolURL2,"DensiSyomei.png",conf,LoopVal)#電子申告・申請タブを押す
                    #画像が出現するまで待機してクリック------------------------------------------------------------------------------------
                    List = ["DensiSyomeiOpen.png","DensiSyomeiOpen2.png"]
                    conf = 0.9#画像認識感度
                    LoopVal = 10#検索回数
                    while ImgCheckForList(FolURL2,List,conf,LoopVal) == True:
                        time.sleep(1) 
                    pg.keyDown('alt')
                    pg.press('j')
                    pg.keyUp('alt') 
                    time.sleep(1) 
                    pg.press('r') 
            else:
                print("送信エラー")
                time.sleep(1)
                ImgClick(FolURL2,"DensiSyomeiXXX.png",conf,LoopVal)#電子申告・申請タブを押す
                #画像が出現するまで待機してクリック------------------------------------------------------------------------------------
                List = ["DensiSyomeiOpenXXX.png","DensiSyomeiOpenXXX2.png"]
                conf = 0.9#画像認識感度
                LoopVal = 10#検索回数
                ListCheck = ImgCheckForList(FolURL2,List,conf,LoopVal)#画像検索関数
                time.sleep(1) 
                ImgClick(FolURL2,"DensiSyomei.png",conf,LoopVal)#電子申告・申請タブを押す
                #画像が出現するまで待機してクリック------------------------------------------------------------------------------------
                List = ["DensiSyomeiOpen.png","DensiSyomeiOpen2.png"]
                conf = 0.9#画像認識感度
                LoopVal = 10#検索回数
                while ImgCheckForList(FolURL2,List,conf,LoopVal) == True:
                    time.sleep(1) 
                pg.keyDown('alt')
                pg.press('j')
                pg.keyUp('alt')
                time.sleep(1) 
                pg.press('r')
        else:
            ImgClick(FolURL2,"UnderArrow.png",conf,LoopVal) 
            time.sleep(1)
            pg.press('q')
            #----------------------------------------------------------------------------------------------------------------------
            conf = 0.9#画像認識感度
            LoopVal = 20#検索回数
            FileName = "EturanCheck.png"
            if ImgCheck(FolURL2, FileName, conf, LoopVal)[0] == True:
                pg.press('return')            
            FileName = "MSGSyousaiErr.png"
            if ImgCheck(FolURL2, FileName, conf, LoopVal)[0] == True:
                pg.press('return')
            #画像が出現するまで待機してクリック------------------------------------------------------------------------------------
            List = ["FileOut.png","FileOut2.png"]
            conf = 0.9#画像認識感度
            LoopVal = 10000#検索回数
            ListCheck = ImgCheckForList(FolURL2,List,conf,LoopVal)#画像検索関数
            if ListCheck[0] == True:
                ImgClick(FolURL2,ListCheck[1],conf,LoopVal)
                time.sleep(1)
            #----------------------------------------------------------------------------------------------------------------------
            #画像が出現するまで待機してクリック------------------------------------------------------------------------------------
            List = ["PDFIcon.png","CSVIcon.png"]
            conf = 0.9#画像認識感度
            LoopVal = 10#検索回数
            ListCheck = ImgCheckForList(FolURL2,List,conf,LoopVal)#画像検索関数
            if ListCheck[0] == True:
                ImgClick(FolURL2,ListCheck[1],conf,LoopVal)
                time.sleep(1)
                pg.press(['down','down','down','down','down'])
                pg.press(['return'])
            #----------------------------------------------------------------------------------------------------------------------
            Tyouhuku = SortPDF(C_SCode + "_" + C_Name + ".pdf")
            if Tyouhuku[0] == str(1):
                FileURL = Tyouhuku[1] + "\\" + C_SCode + "_" + C_Name + ".pdf"
            else:
                FileURL = Tyouhuku[1] + "\\" +  C_SCode + "_" + C_Name + Tyouhuku[0] + ".pdf"
            pyperclip.copy(FileURL)
            pg.hotkey('ctrl', 'v')#pg日本語不可なのでコピペ
            pg.press(['return'])
            # ---------------------------------------------------------------------------------------------------------------------- 
            # ---------------------------------------------------------------------------------------------------------------------- 
            ImgClick(FolURL2,"FileOutPutBtn.png",conf,LoopVal) 
            time.sleep(5)
            pg.press(['x'])
            conf = 0.9#画像認識感度
            LoopVal = 20#検索回数
            FileName = "Kanryou.png"
            if ImgCheck(FolURL2, FileName, conf, LoopVal)[0] == True:
                ImgClick(FolURL2,"DensiSyomei.png",conf,LoopVal)#電子申告・申請タブを押す
                #画像が出現するまで待機してクリック------------------------------------------------------------------------------------
                List = ["DensiSyomeiOpen.png","DensiSyomeiOpen2.png"]
                conf = 0.9#画像認識感度
                LoopVal = 10#検索回数
                while ImgCheckForList(FolURL2,List,conf,LoopVal) == True:
                    time.sleep(1) 
                pg.keyDown('alt')
                pg.press('j')
                pg.keyUp('alt') 
                time.sleep(1) 
                pg.press('r') 
def MainFlow(FolURL2):
    BatUrl = FolURL2 + "/bat/AWADriverOpen.bat"#4724ポート指定でappiumサーバー起動バッチを開く
    driver = MJSOpen.MainFlow(BatUrl,FolURL2,"RPAPhoto/MJS_DensiSinkoku")#OMSを起動しログイン後インスタンス化
    FolURL2 = FolURL2 + "/RPAPhoto/MJS_DensiSinkoku"
    #----------------------------------------------------------------------------------------------------------------------
    MainStarter(FolURL2)#データ送信画面までの関数
    C_df = MasterCSVGet(FolURL2)
    pg.keyDown('alt')
    pg.press('j')
    pg.keyUp('alt')
    CSVURL = FolURL2
    CSVName = '/SyomeiMaster'
    C_url = CSVURL + '/' + CSVName + '.CSV'
    with codecs.open(C_url, "r", "Shift-JIS", "ignore") as file:
        C_df = pd.read_table(file, delimiter=",")
    C_dfRow = np.array(C_df).shape[0]#配列行数取得
    C_dfCol = np.array(C_df).shape[1]#配列列数取得
    ItemList = []
    time.sleep(1)
    #クラス要素クリック----------------------------------------------------------------------------------------------------------
    for y in range(C_dfRow):


        # pg.keyDown('alt')
        # pg.press('j')
        # pg.keyUp('alt')
        # time.sleep(1)


        #CSV要素取得-------------------------------------------------------------------------------------------------------------
        C_dfDataRow = C_df.iloc[y,:]
        C_SCode = str(C_dfDataRow["顧問先コード"])
        C_Name = str(C_dfDataRow["顧問先名称"])
        C_Nendo = str(C_dfDataRow["年度"])
        C_Zeimoku = str(C_dfDataRow["税目"])
        C_Syurui = str(C_dfDataRow["申告種類"])
        #------------------------------------------------------------------------------------------------------------------------
        conf = 0.9#画像認識感度
        LoopVal = 10#検索回数
        FileName = "Tantousya.png"
        if ImgCheck(FolURL2, FileName, conf, LoopVal)[0] == True:
            ImgClick(FolURL2,FileName,conf,LoopVal)
            pg.press('Home')
            pg.press('return')
        time.sleep(1)
        #----------------------------------------------------------------------------------------------------------------------        
        Hub = "class_name"
        ObjName = "TMNumEdit"#関与先コードボックス
        DriverClick(Hub,ObjName,driver)
        pg.write(C_SCode, interval=0.01)#直接SENDできないのでpyautoguiで入力
        pg.press(['return'])
        #クラス要素クリック----------------------------------------------------------------------------------------------------------
        #---------------------------------------------------------------------------------------------------------------------- 
        #---------------------------------------------------------------------------------------------------------------------- 
        #---------------------------------------------------------------------------------------------------------------------- 
        #---------------------------------------------------------------------------------------------------------------------- 
        #---------------------------------------------------------------------------------------------------------------------- 
        #---------------------------------------------------------------------------------------------------------------------- 
        time.sleep(1)
        ImgClick(FolURL2,"NendoBox.png",conf,LoopVal)#電子申告・申請タブを押す
        # Hub = "class_name"
        # ObjName = "TMDateEdit"
        # ClassList = DriverFindClass(ObjName,driver)
        # ClassObjList = ClassList[1]
        # ClassObjList[3].click()
        #---------------------------------------------------------------------------------------------------------------------- 
        #---------------------------------------------------------------------------------------------------------------------- 
        #---------------------------------------------------------------------------------------------------------------------- 
        #---------------------------------------------------------------------------------------------------------------------- 
        #---------------------------------------------------------------------------------------------------------------------- 
        #---------------------------------------------------------------------------------------------------------------------- 

        pg.write(C_Nendo, interval=0.01)#直接SENDできないのでpyautoguiで入力
        pg.press(['return'])
        pg.write(C_Nendo, interval=0.01)#直接SENDできないのでpyautoguiで入力
        pg.press(['return'])
        #----------------------------------------------------------------------------------------------------------------------
        conf = 0.9#画像認識感度
        LoopVal = 10#検索回数
        FileName = "ZeimokuRadio.png"
        if ImgCheck(FolURL2, FileName, conf, LoopVal)[0] == True:
            pg.press(['tab'])
        else:
            pg.press(['right'])
            pg.press(['right'])
            pg.press(['tab'])
        time.sleep(1)
        #----------------------------------------------------------------------------------------------------------------------
        SortURL = FolURL2 + '/ミロク税目分岐'
        ZeimokuRow = SortCSVItem(SortURL,"Master",C_Zeimoku)
        for x in range(ZeimokuRow):
            pg.press(['down'])
        pg.press(['space'])
        pg.press(['down'])
        time.sleep(1)
        SortURL = FolURL2 + '/ミロク税目分岐'
        ZeimokuRow = SortCSVItem(SortURL,C_Zeimoku,C_Syurui)
        for x in range(ZeimokuRow):
            pg.press(['down'])
        pg.press(['space'])
        time.sleep(1)
        #クラス要素クリック----------------------------------------------------------------------------------------------------------
        Hub = "class_name"
        ObjName = "TMBitBtn"#関与先コードボックス
        ClassList = DriverFindClass(ObjName,driver)
        ClassObjList = ClassList[1]
        ClassObjList[1].click()
        #----------------------------------------------------------------------------------------------------------------------
        time.sleep(3)
        #画像が出現するまで待機してクリック------------------------------------------------------------------------------------
        List = ["FindCheckBox.png","FindCheckBox2.png","FindCheckBox3.png","FindCheckBox4.png"]
        conf = 0.9#画像認識感度
        LoopVal = 10#検索回数
        ListCheck = ImgCheckForList(FolURL2,List,conf,LoopVal)#画像検索関数
        conf = 0.9#画像認識感度
        LoopVal = 10000#検索回数
        if ListCheck[0] == True:
            for x in range(100):
                ListCheck = ImgCheckForList(FolURL2,List,conf,LoopVal)#画像検索関数
                if ListCheck[0] == True:
                    LoopVal = 10#検索回数
                    ImgClick(FolURL2,ListCheck[1],conf,LoopVal)
                    time.sleep(1)
                else:
                    time.sleep(1)
                if ImgCheck(FolURL2,"FindCheckBoxNext.png",conf,LoopVal)[0] == False:
                    break
            time.sleep(1)
            pg.press('left')
            time.sleep(1)
            pg.keyDown('alt')
            pg.press('s')
            pg.keyUp('alt')
            time.sleep(1)
            if ImgCheck(FolURL2,"Tetuduki.png",conf,LoopVal)[0] == False:
                time.sleep(1)
                if ImgCheck(FolURL2,"TihouTourokuKakunin.png",conf,LoopVal)[0] == False:
                    #クラス要素クリック----------------------------------------------------------------------------------------------------------
                    Hub = "AutomationID"
                    ObjName = "DropDown"
                    DriverClick(Hub,ObjName,driver)
                    pg.press(['up','up','up'])
                    pg.press('return')
                    #クラス要素クリック----------------------------------------------------------------------------------------------------------
                    Hub = "class_name"
                    ObjName = "TMBitBtn"#関与先コードボックス
                    ClassList = DriverFindClass(ObjName,driver)
                    ClassObjList = ClassList[1]
                    ClassObjList[1].click()
                    #----------------------------------------------------------------------------------------------------------------------
                    MainFirstAction(FolURL2,C_SCode,C_Name )
                    time.sleep(1)
                else:
                    time.sleep(1)
                    conf = 0.9#画像認識感度
                    LoopVal = 10#検索回数
                    if ImgCheck(FolURL2,"Tetuduki.png",conf,LoopVal)[0] == True:
                        pg.press('return')
                        time.sleep(1)
                        pg.press('o')
                        print("手続き未登録")
                        time.sleep(1)
                    else:
                        pg.press('o')
                        print("手続き未登録")
                        time.sleep(1)
                    #クラス要素クリック----------------------------------------------------------------------------------------------------------
                    time.sleep(1)
                    Hub = "AutomationID"
                    ObjName = "DropDown"
                    DriverClick(Hub,ObjName,driver)
                    pg.press(['up','up','up'])
                    pg.press('return')
                    #クラス要素クリック----------------------------------------------------------------------------------------------------------
                    Hub = "class_name"
                    ObjName = "TMBitBtn"#関与先コードボックス
                    ClassList = DriverFindClass(ObjName,driver)
                    ClassObjList = ClassList[1]
                    ClassObjList[1].click()
                    #----------------------------------------------------------------------------------------------------------------------
                    MainFirstAction(FolURL2,C_SCode,C_Name )
            else:
                time.sleep(1)
                conf = 0.9#画像認識感度
                LoopVal = 10#検索回数
                if ImgCheck(FolURL2,"Tetuduki.png",conf,LoopVal)[0] == True:
                    pg.press('return')
                    time.sleep(1)
                    pg.press('o')
                    print("手続き未登録")
                    time.sleep(1)
                else:
                    pg.press('o')
                    print("手続き未登録")
                    time.sleep(1)
                #クラス要素クリック----------------------------------------------------------------------------------------------------------
                time.sleep(1)
                Hub = "AutomationID"
                ObjName = "DropDown"
                DriverClick(Hub,ObjName,driver)
                pg.press(['up','up','up'])
                pg.press('return')
                #クラス要素クリック----------------------------------------------------------------------------------------------------------
                Hub = "class_name"
                ObjName = "TMBitBtn"#関与先コードボックス
                ClassList = DriverFindClass(ObjName,driver)
                ClassObjList = ClassList[1]
                ClassObjList[1].click()
                #----------------------------------------------------------------------------------------------------------------------
                MainFirstAction(FolURL2,C_SCode,C_Name )               
        else:
                print("検索結果なし")
                time.sleep(1)
                ImgClick(FolURL2,"DensiSyomeiXXX.png",conf,LoopVal)#電子申告・申請タブを押す
                #画像が出現するまで待機してクリック------------------------------------------------------------------------------------
                List = ["DensiSyomeiOpenXXX.png","DensiSyomeiOpenXXX2.png"]
                conf = 0.9#画像認識感度
                LoopVal = 10#検索回数
                ListCheck = ImgCheckForList(FolURL2,List,conf,LoopVal)#画像検索関数
                time.sleep(1) 
                ImgClick(FolURL2,"DensiSyomei.png",conf,LoopVal)#電子申告・申請タブを押す
                #画像が出現するまで待機してクリック------------------------------------------------------------------------------------
                List = ["DensiSyomeiOpen.png","DensiSyomeiOpen2.png"]
                conf = 0.9#画像認識感度
                LoopVal = 10#検索回数
                while ImgCheckForList(FolURL2,List,conf,LoopVal) == True:
                    time.sleep(1)                  
                pg.keyDown('alt')
                pg.press('j')
                pg.keyUp('alt')
                time.sleep(1)
                pg.press('r') 

#モジュールインポート
from appium import webdriver
import subprocess
from subprocess import run
from subprocess import PIPE
import pyautogui as pg
import time
import MJSOpen
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
import codecs
import pyperclip #クリップボードへのコピーで使用

#RPA用画像フォルダの作成---------------------------------------------------------
FolURL = "//Sv05121a/e/C 作業台/RPA/ALLDataBase/RPAPhoto/MJS_DensiSinkoku"#元
#FolURL2 = os.getcwd().replace('\\','/') + "/TKC_DensiSinkoku"#先
FolURL2 = os.getcwd().replace('\\','/')#先
#try:
#    shutil.copytree(FolURL,FolURL2)
#except:
#    print(FolURL2 + "あります。")
#--------------------------------------------------------------------------------
try:
    MainFlow(FolURL2)
except:
    traceback.print_exc()