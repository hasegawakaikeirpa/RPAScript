#----------------------------------------------------------------------------------------------------------------------
from ast import For
from queue import Empty
from numpy import true_divide
from pyparsing import And
def DriverUIWaitXPATH(UIPATH,driver):#XPATH要素を取得するまで待機
    for x in range(10):
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
    for x in range(10):
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
    for x in range(10):
        try:
            driver.find_element_by_Name(UIPATH)
            Flag = 1
            return True
        except:
            Flag = 0
    if Flag == 0:
        return False
#------------------------------------------------------------r----------------------------------------------------------
def DriverUIWaitclassname(UIPATH,driver):#XPATH要素を取得するまで待機
    for x in range(10):
        try:
            driver.find_element_by_class_name(UIPATH)
            Flag = 1
            return True
        except:
            Flag = 0
    if Flag == 0:
        return False
#----------------------------------------------------------------------------------------------------------------------
def DriverFindClass(UIPATH,driver):#XPATH要素を取得するまで待機
    for x in range(10):
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
    for x in range(10):
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
def SortCSVItem(SortURL,SortName,Key):#CSVと列名を4つ与えて4つの複合と引数Keyが一致する行数を返す
    Sort_url = SortURL.replace("\\","/") + '/' + SortName + '.CSV'
    with codecs.open(Sort_url, "r", "utf-8", "ignore") as file:
        C_Child = pd.read_table(file,delimiter=",")
    C_CforCount = 0
    C_dfRow = np.array(C_Child).shape[0]#配列行数取得
    for x in range(C_dfRow):
        C_ChildDataRow = C_Child.iloc[x,:]
        C_Val = int(C_ChildDataRow['SyanaiCode'])
        if Key == C_Val:
            return True,C_ChildDataRow
        else:
            C_CforCount = C_CforCount + 1
    return False,""
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
def SortPreList(PreList,Key):#CSVと列名を4つ与えて4つの複合と引数Keyが一致する行数を返す
    try:
        PL_List = []
        for PreListItem in PreList:
            if Key == PreListItem[1]:
                PL_List.append([PreListItem[0],PreListItem[3],PreListItem[2]])
        return True,PreListItem[0],PreListItem[3],PreListItem[2]
    except:
        return False,"","",""
#----------------------------------------------------------------------------------------------------------------------
def MainStarter(FolURL2):
    #画像が出現するまで待機してクリック------------------------------------------------------------------------------------
    List = ["DensiSinkokuIcon.png","DensiSinkokuIcon2.png"]
    conf = 0.9#画像認識感度
    LoopVal = 10#検索回数
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
    while pg.locateOnScreen(FolURL2 + "/" + "SyomeiBtn.png", confidence=0.9) is None:
        time.sleep(1)
        if ImgCheck(FolURL2,"FMSG.png",0.9,1)[0] == True:
            pg.keyDown('alt')
            pg.press('c')
            pg.keyUp('alt')
    ImgClick(FolURL2,"SyomeiBtn.png",conf,LoopVal)#電子申告・申請タブを押す
    #----------------------------------------------------------------------------------------------------------------------
    while pg.locateOnScreen(FolURL2 + "/" + "TyouhyouList.png", confidence=0.9) is None:
        time.sleep(1)
#----------------------------------------------------------------------------------------------------------------------
def CharPar(MasterRow):
    try:
        MSyanaiCode = MasterRow["vc_KnrCd"]
    except:
        MSyanaiCode = ""
    try:
        MName = MasterRow["vc_Name"]
    except:
        try:
            MName = MasterRow["vc_NameW"]
        except:
            MName = ""
    try:
        Mkessan = MasterRow["in_KsnMon"]
    except:
        Mkessan = ""
    try:
        MAdd = MasterRow["vc_DaihyouMail"]
    except:
        MAdd = ""
    try:
        MAdd = MasterRow["vc_SeikyuMail"]
    except:
        MAdd = ""
    try:
        MSAdd = MasterRow["vc_SisanhyouMail"]
    except:
        MSAdd = ""
    try:
        MS2Add = MasterRow["vc_TantouMail"]
    except:
        MS2Add = ""
    return MSyanaiCode,MName,Mkessan,MAdd,MSAdd,MS2Add
    # [
    # "Title",
    # "MirokuCode",
    # "TKCJimusyoCode",
    # "TKCKanyoCode",
    # "TKCKojinCode",
    # "SyanaiCode",
    # "MirokuName",
    # "TKCName",
    # "MirokuKokuzeiUserCode",
    # "MirokuTihouzeiUserID",
    # "TKCKokuzeiUserCode",
    # "TKCTihouzeiUserID",
    # "etaxPass",
    # "eltaxPass",
    # "MailAddress",
    # "SubMailAddress",
    # "Sub2MailAddress",
    # "SeikyuuHantei",
    # "TKCKaijyo",
    # "SeiriBangou",
    # "HoujinBangou",
    # "Daihyousya",
    # "SharePointURL",
    # "SharePointListId",
    # "TeamsTouroku",
    # "KessanDuki",
    # "KanyoKeitai",
    # "GyousyuCode",
    # "Gyousyu",
    # "Gyousyu2",
    # "TantouhyouName",
    # "HoujinKojin",
    # "YuubinBangou",
    # "Jyuusyo",
    # "Houmonnsaki2",
    # "TelNo",
    # "AccountantSoft",
    # "TantouListTantoukacd",
    # "TantouListTantouka",
    # "TantouListTantousyaCD",
    # "TantouListKansaTantou",
    # "TantouListTantousyaCD2",
    # "TantouListKaikeiIkousaki",
    # "TantouListTantousyaCD3",
    # "TantouListKaikeiSub",
    # "TantouListTantousyaCD4",
    # "TantouListKaikeiSub2",
    # "TantouListTantousyaCD5",
    # "TantouListKaikeiSub3",
    # "TantouListSyahoTantoukaCD",
    # "TantouListSyahoTantouka",
    # "TantouListSyahoTantouCD",
    # "TantouListSyahoTantou",
    # "TantouListGetujihousyuu",
    # "TantouListKessanryou",
    # "TantouListKaikeisoftRental",
    # "TantouListPX",
    # "TantouListSX",
    # "TantouConsulhousyuu",
    # "TantouConsulnaiyou",
    # "TantouKyuuyokeisan",
    # "TantouKyuuyoSimebi",
    # "TantouKyuuyoSiharaibi",
    # "TantouKyuuyoNinzuu",
    # "TantouSyahohousyuu",
    # "TantouConsulCode",
    # "TantouConsulName",
    # "TantouConsulSubCode",
    # "TantouConsulSubName",
    # "TantouConsulSubCode2",
    # "TantouConsulSubName2",
    # "TantouKyuuyoCode",
    # "TantouKyuuyoName",
    # "TantouKyuuyoSubCode",
    # "TantouKyuuyoSubName",
    # "TantouKyuuyoSubCode2",
    # "TantouKyuuyoSubName2",
    # "TantouSyahoCode",
    # "TantouSyahoName",
    # "TantouSyahoSubCode",
    # "TantouSyahoSubName",
    # "TantouSyahoSubCode2",
    # "TantouSyahoSubName2",
    # "KanyosakiRank",
    # "tikuwari",
    # "TKChurigana",
    # "TantouListGyousyuBunrui",
    # "TantouListGyousyumoku",
    # "MSAccount",
    # "MSPass",
    # "MSTouroku"
    # ]
#------------------------------------------------------------------------------------------------------------------------------- 
def MainStarter(FolURL2):
    try:
        time.sleep(1)
        AppImg = ImgCheck(FolURL2,"AppIcon.png",0.9,1)
        if AppImg[0] == True:
           ImgClick(FolURL2,"AppIcon.png",0.9,1)
        ThreeImg = ImgCheck(FolURL2,"ThreeIcon.png",0.9,1)
        if ThreeImg[0] == False:
            ImgClick(FolURL2,"KaikeiIcon.png",0.9,1)
            while pg.locateOnScreen(FolURL2 + "/" + "ThreeIcon.png", confidence=0.9) is None:
                time.sleep(1)
            ImgClick(FolURL2,"TaisyouIcon.png",0.9,1)
            while pg.locateOnScreen(FolURL2 + "/" + "TaisyouSelect.png", confidence=0.9) is None:
                time.sleep(1)
            return True
        else:
            ImgClick(FolURL2,"TaisyouIcon.png",0.9,1)
            while pg.locateOnScreen(FolURL2 + "/" + "TaisyouSelect.png", confidence=0.9) is None:
                time.sleep(1)
            return True
    except:
        time.sleep(1)
        return False
#------------------------------------------------------------------------------------------------------------------------------- 
def MJSFlow(FolURL2,driver):
    try:
        MJSF = driver.find_element_by_class_name("Edit")
        MJSF.click()
        time.sleep(1)
        pyperclip.copy("一括印刷")
        pg.hotkey('ctrl', 'v')#pg日本語不可なのでコピペ
        pg.press("return")               
        time.sleep(1)
        pg.press("return")               
        time.sleep(1)
        while pg.locateOnScreen(FolURL2 + "/AllPrintFlag.png",confidence=0.9) is None:
            time.sleep(1)                
        return True
    except:
        MJSF = driver.find_element_by_class_name("Edit")
        MJSF.click()
        time.sleep(1)
        pyperclip.copy("一括印刷")
        pg.hotkey('ctrl', 'v')#pg日本語不可なのでコピペ
        pg.press("return")
        time.sleep(1)
        KBB = ImgCheck(FolURL2,"KeieiBunsekiBar2.png",0.9,1)
        if KBB[0] == False:
            ImgClick(FolURL2,"KeieiBunsekiBar.png",0.9,1)
        time.sleep(1)
        ImgClick(FolURL2,"SyoriKidou.png",0.9,1)
        while pg.locateOnScreen(FolURL2 + "/AllPrintFlag.png",confidence=0.9) is None:
            time.sleep(1)
        return False
#------------------------------------------------------------------------------------------------------------------------------- 
def AllPrint(FolURL2,driver,MaChar,Tuki):
    try:
        time.sleep(1)
        Zen = ImgCheck(FolURL2,"ZengetuIcon.png",0.9,1)
        if Zen[0] == True:
            while pg.locateOnScreen(FolURL2 + "/CheckingBox.png",confidence=0.9) is not None:
                time.sleep(1)
                ImgClick(FolURL2,"ZengetuIcon.png",0.9,1)
            time.sleep(1)
            if Tuki == "1":
                ImgClick(FolURL2,"1mon.png",0.99999,1)
                time.sleep(1)
                ImgClick(FolURL2,"1n.png",0.85,1)
                conf=0.85
                while pg.locateOnScreen(FolURL2 + "/PrintStart.png",confidence=0.99999) is None:
                    time.sleep(1)
                    ImgClick(FolURL2,"1n.png",conf,1)
                    conf = conf - 0.1
                time.sleep(1)
                ImgClick(FolURL2,"PrintStart.png",0.9,1)
                time.sleep(1)
                while pg.locateOnScreen(FolURL2 + "/FileOut.png",confidence=0.85) is None:
                    time.sleep(1)
                return True
            elif Tuki == "2":
                ImgClick(FolURL2,"2mon.png",0.99999,1)
                time.sleep(1)
                ImgClick(FolURL2,"2n.png",0.85,1)
                conf=0.85
                while pg.locateOnScreen(FolURL2 + "/PrintStart.png",confidence=0.99999) is None:
                    time.sleep(1)
                    ImgClick(FolURL2,"2n.png",conf,1)
                    conf = conf - 0.1
                time.sleep(1)
                ImgClick(FolURL2,"PrintStart.png",0.9,1)
                time.sleep(1)
                while pg.locateOnScreen(FolURL2 + "/FileOut.png",confidence=0.85) is None:
                    time.sleep(1)
                return True
            elif Tuki == "3":
                ImgClick(FolURL2,"3mon.png",0.99999,1)
                time.sleep(1)
                ImgClick(FolURL2,"3n.png",0.85,1)
                conf=0.85
                while pg.locateOnScreen(FolURL2 + "/PrintStart.png",confidence=0.99999) is None:
                    time.sleep(1)
                    ImgClick(FolURL2,"3n.png",conf,1)
                    conf = conf - 0.1
                time.sleep(1)
                ImgClick(FolURL2,"PrintStart.png",0.9,1)
                time.sleep(1)
                while pg.locateOnScreen(FolURL2 + "/FileOut.png",confidence=0.85) is None:
                    time.sleep(1)
                return True
            elif Tuki == "4":
                ImgClick(FolURL2,"4mon.png",0.99999,1)
                time.sleep(1)
                ImgClick(FolURL2,"4n.png",0.85,1)
                conf=0.85
                while pg.locateOnScreen(FolURL2 + "/PrintStart.png",confidence=0.99999) is None:
                    time.sleep(1)
                    ImgClick(FolURL2,"4n.png",conf,1)
                    conf = conf - 0.1
                time.sleep(1)
                ImgClick(FolURL2,"PrintStart.png",0.9,1)
                time.sleep(1)
                while pg.locateOnScreen(FolURL2 + "/FileOut.png",confidence=0.85) is None:
                    time.sleep(1)
                return True
            elif Tuki == "5":
                ImgClick(FolURL2,"5mon.png",0.99999,1)
                time.sleep(1)
                ImgClick(FolURL2,"5n.png",0.85,1)
                conf=0.85
                while pg.locateOnScreen(FolURL2 + "/PrintStart.png",confidence=0.99999) is None:
                    time.sleep(1)
                    ImgClick(FolURL2,"5n.png",conf,1)
                    conf = conf - 0.1
                time.sleep(1)
                ImgClick(FolURL2,"PrintStart.png",0.9,1)
                time.sleep(1)
                while pg.locateOnScreen(FolURL2 + "/FileOut.png",confidence=0.85) is None:
                    time.sleep(1)
                return True
            elif Tuki == "6":
                ImgClick(FolURL2,"6mon.png",0.99999,1)
                time.sleep(1)
                ImgClick(FolURL2,"6n.png",0.85,1)
                conf=0.85
                while pg.locateOnScreen(FolURL2 + "/PrintStart.png",confidence=0.99999) is None:
                    time.sleep(1)
                    ImgClick(FolURL2,"6n.png",conf,1)
                    conf = conf - 0.1
                time.sleep(1)
                ImgClick(FolURL2,"PrintStart.png",0.9,1)
                time.sleep(1)
                while pg.locateOnScreen(FolURL2 + "/FileOut.png",confidence=0.85) is None:
                    time.sleep(1)
                return True
            elif Tuki == "7":
                ImgClick(FolURL2,"7mon.png",0.99999,1)
                time.sleep(1)
                ImgClick(FolURL2,"7n.png",0.85,1)
                conf=0.85
                while pg.locateOnScreen(FolURL2 + "/PrintStart.png",confidence=0.99999) is None:
                    time.sleep(1)
                    ImgClick(FolURL2,"7n.png",conf,1)
                    conf = conf - 0.1
                time.sleep(1)
                ImgClick(FolURL2,"PrintStart.png",0.9,1)
                time.sleep(1)
                while pg.locateOnScreen(FolURL2 + "/FileOut.png",confidence=0.85) is None:
                    time.sleep(1)
                return True
            elif Tuki == "8":
                ImgClick(FolURL2,"8mon.png",0.99999,1)
                time.sleep(1)
                ImgClick(FolURL2,"8n.png",0.85,1)
                conf=0.85
                while pg.locateOnScreen(FolURL2 + "/PrintStart.png",confidence=0.99999) is None:
                    time.sleep(1)
                    ImgClick(FolURL2,"8n.png",conf,1)
                    conf = conf - 0.1
                time.sleep(1)
                ImgClick(FolURL2,"PrintStart.png",0.9,1)
                time.sleep(1)
                while pg.locateOnScreen(FolURL2 + "/FileOut.png",confidence=0.85) is None:
                    time.sleep(1)
                return True
            elif Tuki == "9":
                ImgClick(FolURL2,"9mon.png",0.99999,1)
                time.sleep(1)
                ImgClick(FolURL2,"9n.png",0.85,1)
                conf=0.85
                while pg.locateOnScreen(FolURL2 + "/PrintStart.png",confidence=0.99999) is None:
                    time.sleep(1)
                    ImgClick(FolURL2,"9n.png",conf,1)
                    conf = conf - 0.1
                time.sleep(1)
                ImgClick(FolURL2,"PrintStart.png",0.9,1)
                time.sleep(1)
                while pg.locateOnScreen(FolURL2 + "/FileOut.png",confidence=0.85) is None:
                    time.sleep(1)
                return True
            elif Tuki == "10":
                ImgClick(FolURL2,"10mon.png",0.99999,1)
                time.sleep(1)
                ImgClick(FolURL2,"10n.png",0.85,1)
                conf=0.85
                while pg.locateOnScreen(FolURL2 + "/PrintStart.png",confidence=0.99999) is None:
                    time.sleep(1)
                    ImgClick(FolURL2,"10n.png",conf,1)
                    conf = conf - 0.1
                time.sleep(1)
                ImgClick(FolURL2,"PrintStart.png",0.9,1)
                time.sleep(1)
                while pg.locateOnScreen(FolURL2 + "/FileOut.png",confidence=0.85) is None:
                    time.sleep(1)
                    Berr = ImgCheck(FolURL2,"BalanceErr.png",0.9,3)
                    if Berr[0] == True:
                        pg.press('n')
                        time.sleep(1)
                        return False
                return True
            elif Tuki == "11":
                ImgClick(FolURL2,"11mon.png",0.99999,1)
                time.sleep(1)
                ImgClick(FolURL2,"11n.png",0.85,1)
                conf=0.85
                while pg.locateOnScreen(FolURL2 + "/PrintStart.png",confidence=0.99999) is None:
                    time.sleep(1)
                    ImgClick(FolURL2,"11n.png",conf,1)
                    conf = conf - 0.1
                time.sleep(1)
                ImgClick(FolURL2,"PrintStart.png",0.9,1)
                time.sleep(1)
                while pg.locateOnScreen(FolURL2 + "/FileOut.png",confidence=0.85) is None:
                    time.sleep(1)
                return True
            elif Tuki == "12":
                ImgClick(FolURL2,"12mon.png",0.99999,1)
                time.sleep(1)
                ImgClick(FolURL2,"12n.png",0.85,1)
                conf=0.85
                while pg.locateOnScreen(FolURL2 + "/PrintStart.png",confidence=0.99999) is None:
                    time.sleep(1)
                    ImgClick(FolURL2,"12n.png",conf,1)
                    conf = conf - 0.1
                time.sleep(1)
                ImgClick(FolURL2,"PrintStart.png",0.9,1)
                time.sleep(1)
                while pg.locateOnScreen(FolURL2 + "/FileOut.png",confidence=0.85) is None:
                    time.sleep(1)
                return True
    except:
        time.sleep(1)
        return False
#--------------------------------------------------------------------------------------------------------------------------
def FolCre(FolURL2,MaChar,Nen,Tuki):
    Out_Dir = "//Sv05121a/e/C 作業台/RPA/試算表/承認待ち"
    try:
        SyanaiCode = MaChar#'{0:04}'.format(MaChar)#MaChar[0])
        sqlstr = 'SELECT * FROM m_kkanyo WHERE vc_KnrCd=' + SyanaiCode
        SqlData = sq.MySQLHeaderTo_df('ws77','SYSTEM','SYSTEM',3306,'test_db','utf8',sqlstr)
        if SqlData[0] == True:
            SqlRow = SqlData[1]
            if len(SqlRow['vc_KansaTantouNo'][0]) == 0\
            or len(SqlRow['vc_KansaTantou'][0]) == 0\
            or len(SqlRow['vc_Name'][0]) == 0:
                return False,"担当情報もしくは関与先名不足"
            else:
                TanNo = str(int(SqlRow['vc_KansaTantouNo'][0]))
                TanName = SqlRow['vc_KansaTantou'][0].replace('\u3000',' ')
                MNo = str(int(SqlRow['vc_KnrCd'][0]))
                MName = SqlRow['vc_Name'][0].replace('\u3000',' ')
                if len(TanName) == 0:
                    Dir_Name = Out_Dir + "/" + '担当未登録' #MaChar[0])
                else:
                    Dir_Name = Out_Dir + "/" + TanNo + "_" + TanName #MaChar[0])
                if os.path.isdir(str(Dir_Name)) == False:
                    os.mkdir(str(Dir_Name))
                    Dir_Name = Dir_Name + "/" + MNo + "-" + MName
                    os.mkdir(str(Dir_Name))
                    return True,Dir_Name
                else:
                    Dir_Name = Dir_Name + "/" + MNo + "-" + MName
                    if os.path.isdir(str(Dir_Name)) == False:
                        os.mkdir(str(Dir_Name))
                    return True,Dir_Name
        else:
            return False,"FolCreでSql失敗"
    except:
        return False,"FolCreでTryエラー"
#--------------------------------------------------------------------------------------------------------------------------
def S_Printout(FolURL2,driver,MaChar,Nen,Tuki,Out_Dir):#MaChar = CharPar(MasterRow)
    try:
        #MSyanaiCode,MName,Mkessan,MAdd,MSAdd,MS2Add
        FileName = Out_Dir + "\\" + str(int(MaChar[0])) + "-R" + Nen + "." + Tuki + " " + MaChar[1] + "様試算表.pdf"
        ImgClick(FolURL2,"FileOut.png",0.9,3)
        time.sleep(1)
        ImgClick(FolURL2,"PDFBar.png",0.9,3)
        time.sleep(1)
        pg.press('return')
        time.sleep(1)
        pyperclip.copy(FileName)
        pg.hotkey('ctrl', 'v')#pg日本語不可なのでコピペ
        pg.press("return")
        ImgClick(FolURL2,"LastFileOut.png",0.9,3)
        time.sleep(2)
        if ImgCheck(FolURL2,"/FileOver.png" ,0.9,3)[0] == True:
            pg.press('y')
            time.sleep(2)
        while pg.locateOnScreen(FolURL2 + "/Insatutyu.png" , confidence=0.9) is not None:
            time.sleep(1)
        time.sleep(1)
        while pg.locateOnScreen(FolURL2 + "/EndIcon.png" , confidence=0.99999) is None:
            time.sleep(1)
        while pg.locateOnScreen(FolURL2 + "/Insatutyu.png" , confidence=0.9) is not None:
            time.sleep(1)
        ImgClick(FolURL2,"EndIcon.png",0.99999,3)
        time.sleep(1)
        while pg.locateOnScreen(FolURL2 + "/SyoriKidou.png" , confidence=0.9) is None:
            time.sleep(5)
            ImgClick(FolURL2,"EndIcon.png",0.99999,3)            
        time.sleep(3)
        ImgClick(FolURL2,"EndTaisyou.png",0.9,3)
        time.sleep(1)
        while pg.locateOnScreen(FolURL2 + "/FrontKaikeiIcon.png" , confidence=0.9) is None:
            time.sleep(1)
        time.sleep(1)
        return True,FileName
    except:
        return False,""
#--------------------------------------------------------------------------------------------------------------------------    
def LogWrite(FolURL2,Ends):
    LogList = CSVOut.CsvRead(FolURL2 + "/Log/Log.csv")[1]
    CSVOut.CsvPlus(FolURL2 + "/Log/Log.csv",LogList,Ends)
    time.sleep(1)
#--------------------------------------------------------------------------------------------------------------------------
def MainFlow(FolURL2,MasterCSV):
    BatUrl = FolURL2 + "/bat/AWADriverOpen.bat"#4724ポート指定でappiumサーバー起動バッチを開く
    driver = MJSOpen.MainFlow(BatUrl,FolURL2,"RPAPhoto/MJS_DensiSinkoku")#OMSを起動しログイン後インスタンス化
    FolURL2 = FolURL2 + "/RPAPhoto/MJS_Sisanhyou"
    MainStarter(FolURL2)
    #--------------------------------------------------------------------------------------------------------------------------
    MasRow = np.array(MasterCSV[1]).shape[0]#配列行数取得
    time.sleep(1)
    #クラス要素クリック----------------------------------------------------------------------------------------------------------
    for x in range(MasRow):
        if x >= 62:
        #マスターから値を取得--------------------------------------------------------------------------------------------------------
            MasterRow = MasterCSV[1].iloc[x,:]
            MaChar = CharPar(MasterRow)#MSyanaiCode,MName,Mkessan,MAdd,MSAdd,MS2Add
            Nen = 3#和暦年---------------------------------------------------------------------------------------------------------
            Tuki = 10#和暦月--------------------------------------------------------------------------------------------------------
        #関与先コード指定でデータを開く-----------------------------------------------------------------------------------------------
            DC = driver.find_elements_by_class_name("TMNumEdit")
            DC[1].click()
            time.sleep(1)
            pg.press(["delete","delete","delete","delete","delete","delete","delete","delete","delete"])
            time.sleep(1)
            pg.write(str(int(MaChar[0])))#CSVデータIndex0
            time.sleep(1)
            pg.press("return")
            time.sleep(1)
         #指定画像標示まで待機-----------------------------------------------------------------------------------------------
            while pg.locateOnScreen(FolURL2 + "/" + "OpenFlag.png", confidence=0.99999) is not None:
                time.sleep(3)
                OF = ImgCheck(FolURL2,"OpenFlag.png",0.9,5)
                if OF[0] == True:
                    print("データオープン失敗")
                    break
            OF = ImgCheck(FolURL2,"OpenFlag.png",0.9,5)
            if OF[0] == False:
                time.sleep(1)
                pg.write(str(Nen))
                pg.press("return")
                pg.write(str(Tuki))
                pg.press("return")
                time.sleep(1)
                AnsDC = DC[1].text
                AnsNen = DC[0].text
                AnsTuki = DC[2].text
                if AnsDC == str(int(MaChar[0])) and AnsNen == str(Nen):# and AnsTuki == str(Tuki):
                    pg.keyDown('alt')
                    pg.press('o')
                    pg.keyUp('alt')
                    time.sleep(3)
                    Dq = ImgCheck(FolURL2,"DataUpQ.png",0.9,2)
                    if Dq[0] == True:
                        pg.press('n')
                        time.sleep(1)
                    #指定画像標示まで待機-----------------------------------------------------------------------------------------------
                    while pg.locateOnScreen(FolURL2 + "/" + "FamilyOpenFlag.png", confidence=0.9) is None:
                        Dq = ImgCheck(FolURL2,"DataUpQ.png",0.9,10)
                        if Dq[0] == True:
                            pg.press('n')
                            time.sleep(1)
                        MJF = MJSFlow(FolURL2,driver)
                        time.sleep(1)
                        if MJF == True:
                            break
                    if MJF == True:
                        AllPrint(FolURL2,driver,MaChar,str(Tuki))
                        FLC = FolCre(FolURL2, MaChar[0],Nen,Tuki)
                        if FLC[0] == True: #格納先が作成されていれば 
                            SP = S_Printout(FolURL2,driver,MaChar,str(Nen),str(Tuki),FLC[1])
                            if SP[0] == True:
                                Ends = ["成功",SP[1],str(dt.today()),"",""]
                                LogWrite(FolURL2,Ends)
                        else:
                            time.sleep(1)
                            ImgClick(FolURL2,"POCancel.png",0.9,3)
                            time.sleep(1)
                            ImgClick(FolURL2,"EndTaisyou.png",0.9,3)
                            time.sleep(1)
                            while pg.locateOnScreen(FolURL2 + "/FrontKaikeiIcon.png" , confidence=0.9) is None:
                                time.sleep(1)
                                TE = ImgCheck(FolURL2,"TaisyouEnd.png",0.9,3)
                                if TE[0] == True:
                                    pg.press('y')
                                    time.sleep(1)
                            time.sleep(1)
                            Ends = ["失敗",x,str(dt.today()),"DB項目不足",""]
                            LogWrite(FolURL2,Ends)                          
                    else:
                        print("一括印刷起動失敗")
                        Ends = ["一括印刷起動失敗",MaChar[0],str(dt.today()),"",""]
                        LogWrite(FolURL2,Ends)
            else:
                    print("入力社内コ19")
                    Ends = ["入力社内コードと一致しません",MaChar[0],str(dt.today()),"",""]
                    LogWrite(FolURL2,Ends)                    
#------------------------------------------------------------------------------------------------------------------------------- 
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
#例外処理判定の為のtracebackインポート
import traceback
#pandas(pd)で関与先データCSVを取得
import pyautogui
import time
import shutil
import codecs
import pyperclip #クリップボードへのコピーで使用
from collections import OrderedDict
import jaconv
import WarekiHenkan
from chardet.universaldetector import UniversalDetector
import calendar
import CSVOut
import SQLConnect as sq
#RPA用画像フォルダの作成---------------------------------------------------------
FolURL = "//Sv05121a/e/C 作業台/RPA/ALLDataBase/RPAPhoto/MJS_DensiSinkoku"#元
FolURL2 = os.getcwd().replace('\\','/')#先
#--------------------------------------------------------------------------------
#マスター読込----------------------------------------------------------------------------------
sqlstr = 'SELECT * FROM m_kkanyo'
MasSql = sq.MySQLHeaderTo_df('ws77','SYSTEM','SYSTEM',3306,'test_db','utf8',sqlstr)
MasterCSV = MasSql
#---------------------------------------------------------------------------------------------
try:
    MainFlow(FolURL2,MasterCSV)
except:
    traceback.print_exc()