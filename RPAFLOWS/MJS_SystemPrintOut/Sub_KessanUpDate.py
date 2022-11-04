from ctypes import windll
import pyautogui as pg
import time
import RPA_Function as RPA
import pyperclip  # クリップボードへのコピーで使用

# ------------------------------------------------------------------------------------------------------------------
def KessanUpDate(Job, Exc):
    """
    概要: 決算内訳書更新処理
    @param FolURL : ミロク起動関数のフォルダ(str)
    @param Job.PrintOut_url : このpyファイルのフォルダ(str)
    @param Exc.row_data : Excel抽出行(obj)
    @param driver : 画面操作ドライバー(obj)
    @return : bool,ミロク入力関与先コード, ミロク入力処理年, ミロク入力処理月
    """
    try:
        # 決算内訳書のアイコンを探す-------------------------------------------------
        ImgList = [r"\K_Uchiwake.png", r"\K_Uchiwake2.png"]
        ICFL = RPA.ImgCheckForList(Job.PrintOut_url, ImgList, 0.9, 10)
        # -----------------------------------------------------------------------
        if ICFL[0] is True:  # 決算内訳書のアイコンがあれば
            RPA.ImgClick(Job.PrintOut_url, ICFL[1], 0.9, 10)  # 決算内訳書のアイコンをクリック
            # 決算内訳書フラグが表示されるまで待機------------------------------------
            while (
                pg.locateOnScreen(
                    Job.PrintOut_url + r"\Kessan_CFlag.png", confidence=0.9
                )
                is None
            ):
                time.sleep(1)
            # ------------------------------------------------------------------
            time.sleep(1)
            # 年度を最新に指定----------------------------------------------------
            IC = RPA.ImgCheck(Job.PrintOut_url, r"\Nendo_Saisin.png", 0.9, 10)
            if IC[0] is False:
                IC2 = RPA.ImgCheck(Job.PrintOut_url, r"\Nendo_All.png", 0.9, 10)
                if IC2[0] is False:
                    print("年度選択がない")
                else:
                    RPA.ImgClick(Job.PrintOut_url, r"\Nendo_All.png", 0.9, 10)
                    pg.press("home")
                    time.sleep(1)
                    pg.press("down")
                    time.sleep(1)
                    pg.press("return")
                    time.sleep(1)
            # ------------------------------------------------------------------
            # 関与先コード入力ボックスをクリック------------------------------------
            RPA.ImgClick(Job.PrintOut_url, r"\K_NoBox.png", 0.9, 10)
            while (
                pg.locateOnScreen(
                    Job.PrintOut_url + r"\K_AfterNoBox.png", confidence=0.9
                )
                is None
            ):
                time.sleep(1)
            pg.write(str(Exc.row_kanyo_no))
            pg.press(["return", "return", "return"])
            # 入力した関与先コードを取得------------
            pg.keyDown("shift")
            pg.press(["tab", "tab", "tab"])
            pg.keyUp("shift")
            if windll.user32.OpenClipboard(None):
                windll.user32.EmptyClipboard()
                windll.user32.CloseClipboard()
            pg.hotkey("ctrl", "c")
            ThisNo = pyperclip.paste()
            # -----------------------------------
            pg.press("return")
            # 表示された年度を取得-----------------
            if windll.user32.OpenClipboard(None):
                windll.user32.EmptyClipboard()
                windll.user32.CloseClipboard()
            pg.hotkey("ctrl", "c")
            ThisYear = pyperclip.paste()
            # -----------------------------------
            pg.press("return")
            # 表示された月を取得-------------------
            if windll.user32.OpenClipboard(None):
                windll.user32.EmptyClipboard()
                windll.user32.CloseClipboard()
            pg.hotkey("ctrl", "c")
            ThisMonth = pyperclip.paste()
            # -----------------------------------
            time.sleep(1)
            if str(Exc.row_kanyo_no) == ThisNo:
                print("関与先あり")
                pg.press(["return", "return", "return"])
                # 決算内訳書メニューが表示されるまで待機------------------------------------
                while (
                    pg.locateOnScreen(
                        Job.PrintOut_url + r"\KessanMenu.png", confidence=0.9
                    )
                    is None
                ):
                    time.sleep(1)
                    # 顧問先情報更新ダイアログ確認------------------------------------------
                    KK = RPA.ImgCheck(Job.PrintOut_url, r"\KomonKoushin.png", 0.9, 10)
                    if KK[0] is True:
                        pg.press("y")
                        while (
                            pg.locateOnScreen(
                                Job.PrintOut_url + r"\KomonKoushinBar.png",
                                confidence=0.9,
                            )
                            is None
                        ):
                            time.sleep(1)
                        RPA.ImgClick(
                            Job.PrintOut_url, r"\KomonKoushinInput.png", 0.9, 10
                        )
                    DL = RPA.ImgCheck(Job.PrintOut_url, r"\DLCheck.png", 0.9, 10)
                    if DL[0] is True:
                        pg.press("return")
                        while (
                            pg.locateOnScreen(
                                Job.PrintOut_url + r"\K_TaisyouMenu.png", confidence=0.9
                            )
                            is None
                        ):
                            time.sleep(1)
                # --------------------------------------------------------------------
                # 内訳書印刷メニューが表示されるまで待機----------------------------------
                while (
                    pg.locateOnScreen(URL + r"\Uchiwake\11U_Flag.png", confidence=0.9)
                    is None
                ):
                    time.sleep(1)
                # --------------------------------------------------------------------
                # 内訳書印刷のアイコンを探す-------------------------------------------------
                ImgList = [
                    r"\Uchiwake\11U_Uchiwake.png",
                    r"\Uchiwake\11U_Uchiwake2.png",
                ]
                ICFL = RPA.ImgCheckForList(URL, ImgList, 0.9, 10)
                # -----------------------------------------------------------------------
                if ICFL[0] is True:
                    RPA.ImgClick(URL, ICFL[1], 0.9, 10)  # 内訳書印刷アイコンをクリック
                # 印刷ボタンが表示されるまで待機---------------------------------
                while (
                    pg.locateOnScreen(
                        URL + r"\Uchiwake\11U_PrintBtn.png", confidence=0.9
                    )
                    is None
                ):
                    time.sleep(1)
                # --------------------------------------------------------------------
                RPA.ImgClick(URL, r"\Uchiwake\11U_PrintBtn.png", 0.9, 10)  # 印刷ボタンをクリック
                PSQ = False, ""
                # 印刷設定が表示されるまで待機---------------------------------
                while (
                    pg.locateOnScreen(URL + r"\Houjinzei\PrintBar.png", confidence=0.9)
                    is None
                ):
                    time.sleep(1)
                    PSQ = RPA.ImgCheck(URL, r"\Houjinzei\PrintStyleQ.png", 0.9, 10)
                    if PSQ[0] is True:
                        pg.press("return")
                        break
                # --------------------------------------------------------------------
                if PSQ[0] is False:
                    # 申告税一覧表印刷処理----------------------------------------------------
                    FO = RPA.ImgCheckForList(
                        URL,
                        [
                            r"\Houjinzei\FileOut.png",
                            r"\Houjinzei\FileOut2.png",
                        ],
                        0.9,
                        10,
                    )
                    if FO[0] is True:
                        RPA.ImgClick(URL, FO[1], 0.9, 10)
                    RPA.ImgClick(URL, r"\Houjinzei\PDFBar.png", 0.9, 10)
                    pg.press("return")
                    pg.press("delete")
                    pg.press("backspace")
                    time.sleep(1)
                    pyperclip.copy(Exc.Fname.replace("\\\\", "\\").replace("/", "\\"))
                    time.sleep(1)
                    pg.hotkey("ctrl", "v")
                    pg.press("return")
                    time.sleep(1)
                    RPA.ImgClick(URL, r"\Houjinzei\PrintOut.png", 0.9, 10)
                    time.sleep(2)
                    #  印刷設定が表示されなくなるまで待機---------------------------------
                    while (
                        pg.locateOnScreen(
                            URL + r"\Houjinzei\PrintBar.png", confidence=0.9
                        )
                        is not None
                    ):
                        time.sleep(1)
                        FO = RPA.ImgCheck(URL, r"\Houjinzei\FileOver.png", 0.9, 10)
                        if FO[0] is True:
                            pg.press("y")
                    # --------------------------------------------------------------------
                    #  印刷中が表示されるまで待機-------------------------------------------
                    IC = 0
                    while (
                        pg.locateOnScreen(
                            URL + r"\Houjinzei\NowPrint.png", confidence=0.9
                        )
                        is None
                    ):
                        time.sleep(1)
                        IC += 1
                        if IC == 5:
                            pg.press("tab")
                            break
                    #  印刷中が表示されなくなるまで待機-------------------------------------
                    while (
                        pg.locateOnScreen(
                            URL + r"\Houjinzei\NowPrint.png", confidence=0.9
                        )
                        is not None
                    ):
                        time.sleep(1)
                    #  確実に閉じる--------------------------------------------------------
                    UED = RPA.ImgCheck(URL, r"\Uchiwake\11U_End.png", 0.9, 10)
                    if UED[0] is True:
                        RPA.ImgClick(URL, r"\Uchiwake\11U_End.png", 0.9, 10)
                    else:
                        pg.keyDown("alt")
                        pg.press("x")
                        pg.keyUp("alt")
                    # --------------------------------------------------------------------
                    time.sleep(1)
                    while (
                        RPA.ImgCheckForList(
                            URL,
                            [
                                r"\Uchiwake\11U_Uchiwake.png",
                                r"\Uchiwake\11U_Uchiwake2.png",
                            ],
                            0.9,
                            10,
                        )[0]
                        is False
                    ):
                        time.sleep(1)
                    # 閉じる処理--------------------------
                    pg.keyDown("alt")
                    pg.press("f4")
                    pg.keyUp("alt")
                    # -----------------------------------
                    f = 0
                    # 決算内訳書フラグが表示されるまで待機------------------------------------
                    while (
                        pg.locateOnScreen(
                            Job.PrintOut_url + r"\Kessan_CFlag.png", confidence=0.9
                        )
                        is None
                    ):
                        time.sleep(1)
                        f += 1
                        if f == 5:
                            pg.keyDown("alt")
                            pg.press("f4")
                            pg.keyUp("alt")
                            f = 0
                    # ------------------------------------------------------------------
                    return True, ThisNo, ThisYear, ThisMonth
                else:
                    #  確実に閉じる--------------------------------------------------------
                    UED = RPA.ImgCheck(URL, r"\Uchiwake\11U_End.png", 0.9, 10)
                    if UED[0] is True:
                        RPA.ImgClick(URL, r"\Uchiwake\11U_End.png", 0.9, 10)
                    else:
                        pg.keyDown("alt")
                        pg.press("x")
                        pg.keyUp("alt")
                    # --------------------------------------------------------------------
                    time.sleep(1)
                    while (
                        RPA.ImgCheckForList(
                            URL,
                            [
                                r"\Uchiwake\11U_Uchiwake.png",
                                r"\Uchiwake\11U_Uchiwake2.png",
                            ],
                            0.9,
                            10,
                        )[0]
                        is False
                    ):
                        time.sleep(1)
                    # 閉じる処理--------------------------
                    pg.keyDown("alt")
                    pg.press("f4")
                    pg.keyUp("alt")
                    # -----------------------------------
                    f = 0
                    # 決算内訳書フラグが表示されるまで待機------------------------------------
                    while (
                        pg.locateOnScreen(
                            Job.PrintOut_url + r"\Kessan_CFlag.png", confidence=0.9
                        )
                        is None
                    ):
                        time.sleep(1)
                        f += 1
                        if f == 5:
                            pg.keyDown("alt")
                            pg.press("f4")
                            pg.keyUp("alt")
                            f = 0
                    # ------------------------------------------------------------------
                    return False, "印刷様式未設定", "", ""
            else:
                print("関与先なし")
                return False, "関与先なし", "", ""
        else:
            return False, "決算内訳書起動失敗", "", ""
    except:
        return False, "exceptエラー", "", ""


# # ------------------------------------------------------------------------------------------------------------------
# def KessanUpDate(Job, Exc):
#     """
#     概要: 決算内訳書更新処理
#     @param FolURL : ミロク起動関数のフォルダ(str)
#     @param URL : このpyファイルのフォルダ(str)
#     @param Exc.row_data : Excel抽出行(obj)
#     @param driver : 画面操作ドライバー(obj)
#     @return : bool,ミロク入力関与先コード, ミロク入力処理年, ミロク入力処理月
#     """
#     try:
#         ErrStr = ""  # Rpaエラー判別変数
#         URL = Job.imgdir_url + r"\\KessanUpDate"

#         # 決算内訳書フラグが表示されるまで待機------------------------------------
#         while pg.locateOnScreen(URL + r"\Kessan_CFlag.png", confidence=0.9) is None:
#             time.sleep(1)
#         # ------------------------------------------------------------------
#         time.sleep(1)
#         # 年度を最新に指定----------------------------------------------------
#         IC = RPA.RPA.ImgCheck(URL, r"\Nendo_Saisin.png", 0.9, 10)
#         if IC[0] is False:
#             IC2 = RPA.RPA.ImgCheck(URL, r"\Nendo_All.png", 0.9, 10)
#             if IC2[0] is False:
#                 print("年度選択がない")
#             else:
#                 RPA.RPA.ImgClick(URL, r"\Nendo_All.png", 0.9, 10)
#                 pg.press("home")
#                 time.sleep(1)
#                 pg.press("down")
#                 time.sleep(1)
#                 pg.press("return")
#                 time.sleep(1)
#         # ------------------------------------------------------------------
#         # 関与先コード入力ボックスをクリック------------------------------------
#         while pg.locateOnScreen(URL + r"\K_NoBox.png", confidence=0.9) is None:
#             time.sleep(1)
#         time.sleep(1)
#         RPA.RPA.ImgClick(URL, r"\K_NoBox.png", 0.9, 10)
#         while pg.locateOnScreen(URL + r"\K_AfterNoBox.png", confidence=0.9) is None:
#             time.sleep(1)
#         time.sleep(1)
#         pg.write(str(Exc.row_data["関与先番号"]))
#         pg.press(["return", "return", "return"])
#         # 入力した関与先コードを取得------------
#         pg.keyDown("shift")
#         pg.press(["tab", "tab", "tab"])
#         pg.keyUp("shift")
#         if windll.user32.OpenClipboard(None):
#             windll.user32.EmptyClipboard()
#             windll.user32.CloseClipboard()
#         pg.hotkey("ctrl", "c")
#         ThisNo = pyperclip.paste()
#         # -----------------------------------
#         pg.press("return")
#         # 表示された年度を取得-----------------
#         if windll.user32.OpenClipboard(None):
#             windll.user32.EmptyClipboard()
#             windll.user32.CloseClipboard()
#         pg.hotkey("ctrl", "c")
#         ThisYear = pyperclip.paste()
#         # -----------------------------------
#         pg.press("return")
#         # 表示された月を取得-------------------
#         if windll.user32.OpenClipboard(None):
#             windll.user32.EmptyClipboard()
#             windll.user32.CloseClipboard()
#         pg.hotkey("ctrl", "c")
#         ThisMonth = pyperclip.paste()
#         # -----------------------------------
#         time.sleep(1)
#         if str(Exc.row_data["関与先番号"]) == ThisNo:
#             print("関与先あり")
#             pg.press(["return", "return", "return"])
#             # 決算内訳書メニューが表示されるまで待機------------------------------------
#             while pg.locateOnScreen(URL + r"\KessanMenu.png", confidence=0.9) is None:
#                 time.sleep(1)
#                 # 顧問先情報変更ダイアログが表示されたら
#                 CDQ = RPA.RPA.ImgCheck(
#                     URL,
#                     r"ChangeDataQ.png",
#                     0.9,
#                     10,
#                 )
#                 if CDQ[0] is True:
#                     pg.press("y")  # yで決定
#                     # 顧問先情報取込メニューが表示されるまで待機--------------------------
#                     while (
#                         RPA.RPA.ImgCheckForList(
#                             URL,
#                             [r"ChangeDataBtn.png", r"ChangeDataBtn2.png"],
#                             0.9,
#                             10,
#                         )[0]
#                         is False
#                     ):
#                         time.sleep(1)
#                     CDB = RPA.RPA.ImgCheckForList(
#                         URL,
#                         [r"ChangeDataBtn.png", r"ChangeDataBtn2.png"],
#                         0.9,
#                         10,
#                     )
#                     RPA.RPA.ImgClick(URL, CDB[1], 0.9, 10)  # 顧問先情報取込ボタンをクリック
#             # --------------------------------------------------------------------
#             # 一括更新のアイコンが表示されるまで待機----------------------------------
#             while (
#                 pg.locateOnScreen(URL + r"\IkkatsuKessanKousin.png", confidence=0.9)
#                 is None
#             ):
#                 time.sleep(1)
#             # --------------------------------------------------------------------
#             RPA.RPA.ImgClick(URL, r"\IkkatsuKessanKousin.png", 0.9, 10)  # 一括更新のアイコンをクリック
#             # 一括更新メニューが表示されるまで待機------------------------------------
#             while (
#                 pg.locateOnScreen(URL + r"\IkkatuKessanOpenFlag.png", confidence=0.9)
#                 is None
#             ):
#                 time.sleep(1)
#             # --------------------------------------------------------------------
#             RPA.RPA.ImgClick(
#                 URL, r"\IkkatuKessanOpenFlag.png", 0.9, 10
#             )  # 一括更新メニューのアイコンをクリック
#             time.sleep(1)
#             RPA.RPA.ImgClick(URL, r"\IkkatuKessanStart.png", 0.9, 10)  # 一括更新開始のアイコンをクリック
#             # 確認ウィンドウが表示されるまで待機-------------------------------------
#             while (
#                 pg.locateOnScreen(URL + r"\SakuseiKessanQ.png", confidence=0.9) is None
#             ):
#                 time.sleep(1)
#             # --------------------------------------------------------------------
#             pg.press("y")  # yで決定(nがキャンセル)
#             # 処理終了ウィンドウが表示されるまで待機----------------------------------
#             while (
#                 pg.locateOnScreen(URL + r"\IkkatuKessanEndFlag.png", confidence=0.9)
#                 is None
#             ):
#                 time.sleep(1)
#                 Noren = RPA.RPA.ImgCheckForList(
#                     URL, [r"No_Rendou.png", r"No_Rendou2.png"], 0.9, 10
#                 )
#                 if Noren[0] is True:
#                     # ErrStr = "Noren"
#                     break
#                     # RPA.RPA.ImgClick(URL, r"\No_Rendou_Cansel.png", 0.9, 10)
#             # --------------------------------------------------------------------
#             pg.press("return")  # 決定
#             # 一括更新のアイコンが表示されるまで待機----------------------------------
#             while (
#                 pg.locateOnScreen(URL + r"\IkkatsuKessanKousin.png", confidence=0.9)
#                 is None
#             ):
#                 time.sleep(1)
#                 ME = RPA.RPA.ImgCheckForList(
#                     URL, [r"\MenuEnd.png", r"\MenuEnd2.png", r"\MenuEnd3.png", r"\MenuEnd4.png"], 0.9, 10
#                 )
#                 if ME[0] is True:
#                     pg.press("return")  # 決定
#                     # RPA.RPA.ImgClick(URL, ME[1], 0.9, 10)  # 終了アイコンをクリック
#             # --------------------------------------------------------------------
#             # 閉じる処理--------------------------
#             pg.keyDown("alt")
#             pg.press("f4")
#             pg.keyUp("alt")
#             # -----------------------------------
#             # 決算内訳書フラグが表示されるまで待機-------------------------------------
#             while pg.locateOnScreen(URL + r"\Kessan_CFlag.png", confidence=0.9) is None:
#                 time.sleep(1)
#                 al4c = RPA.RPA.ImgCheck(URL, r"\altf4Q.png", 0.9, 10)  # 終了確認が表示されたら
#                 if al4c[0] is True:
#                     pg.press("y")  # yで決定(nがキャンセル)
#             # --------------------------------------------------------------------
#             print("更新完了")
#             if ErrStr == "":
#                 return True, ThisNo, ThisYear, ThisMonth
#             elif ErrStr == "Noren":
#                 return False, ErrStr, "", ""
#         else:
#             print("関与先なし")
#             return False, "関与先なし", "", ""
#     except:
#         return False, "exceptエラー", "", ""


# # ------------------------------------------------------------------------------------------------------------------
