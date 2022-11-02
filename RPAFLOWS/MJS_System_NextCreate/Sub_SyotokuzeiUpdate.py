# ------------------------------------------------------------------------------------------------------------------
def SyotokuzeiUpdate(FolURL, TFolURL, ExRow, driver):
    """
    概要: 所得税更新処理
    @param FolURL : ミロク起動関数のフォルダ(str)
    @param TFolURL : このpyファイルのフォルダ(str)
    @param ExRow : Excel抽出行(obj)
    @param driver : 画面操作ドライバー(obj)
    @return : bool,ミロク入力関与先コード, ミロク入力処理年, ミロク入力処理月
    """
    try:
        ErrStr = ""  # Rpaエラー判別変数
        # 所得税のアイコンを探す-------------------------------------------------
        ImgList = [r"\Syotoku.png", r"\Syotoku2.png"]
        ICFL = RPA.ImgCheckForList(TFolURL, ImgList, 0.9, 10)
        # -----------------------------------------------------------------------
        if ICFL[0] is True:  # 所得税のアイコンがあれば
            RPA.ImgClick(TFolURL, ICFL[1], 0.9, 10)  # 所得税のアイコンをクリック
            # 所得税フラグが表示されるまで待機------------------------------------
            while (
                pg.locateOnScreen(TFolURL + r"\SyotokuFlag.png", confidence=0.9) is None
            ):
                time.sleep(1)
            # ------------------------------------------------------------------
            time.sleep(1)
            # 他システムとメニューが違う-------------------------------------------------------
            # 年度を最新に指定----------------------------------------------------
            IC = RPA.ImgCheck(TFolURL, r"\Nendo_Saisin.png", 0.9, 10)
            if IC[0] is False:
                IC2 = RPA.ImgCheck(TFolURL, r"\Nendo_All.png", 0.9, 10)
                if IC2[0] is False:
                    print("年度選択がない")
                else:
                    RPA.ImgClick(TFolURL, r"\Nendo_All.png", 0.9, 10)
                    pg.press("home")
                    time.sleep(1)
                    pg.press("down")
                    time.sleep(1)
                    pg.press("return")
                    time.sleep(1)
            # ------------------------------------------------------------------
            # 関与先コード入力ボックスをクリック------------------------------------
            while pg.locateOnScreen(TFolURL + r"\K_NoBox.png", confidence=0.9) is None:
                time.sleep(1)
            time.sleep(1)
            RPA.ImgClick(TFolURL, r"\K_NoBox.png", 0.9, 10)
            while (
                pg.locateOnScreen(TFolURL + r"\K_AfterNoBox.png", confidence=0.9)
                is None
            ):
                time.sleep(1)
            pg.write(str(ExRow["関与先番号"]))
            pg.press(["return", "return"])
            # -----------------------------------
            if RPA.ImgCheck(TFolURL, r"\NotData.png", 0.9, 10)[0] is True:
                # 入力した関与先コードを取得------------
                pg.press("return")
                pg.keyDown("shift")
                pg.press(["tab", "tab", "tab"])
                pg.keyUp("shift")
                if windll.user32.OpenClipboard(None):
                    windll.user32.EmptyClipboard()
                    windll.user32.CloseClipboard()
                pg.hotkey("ctrl", "c")
                ThisNo = pyperclip.paste()
                pg.press("return")
                # クリップボードをクリア----------------
                if windll.user32.OpenClipboard(None):
                    windll.user32.EmptyClipboard()
                    windll.user32.CloseClipboard()
                # ------------------------------------
                # 表示された年度を取得-----------------
                if windll.user32.OpenClipboard(None):
                    windll.user32.EmptyClipboard()
                    windll.user32.CloseClipboard()
                pg.hotkey("ctrl", "c")
                ThisYear = pyperclip.paste()
                # -----------------------------------
                pg.press("return")
                # 表示された申告種類を取得---------------
                if windll.user32.OpenClipboard(None):
                    windll.user32.EmptyClipboard()
                    windll.user32.CloseClipboard()
                pg.hotkey("ctrl", "c")
                ThisMonth = pyperclip.paste()
                pg.press("return")
                # -----------------------------------
            else:
                # 入力した関与先コードを取得------------
                pg.press("return")
                pg.keyDown("shift")
                pg.press(["tab", "tab", "tab"])
                pg.keyUp("shift")
                if windll.user32.OpenClipboard(None):
                    windll.user32.EmptyClipboard()
                    windll.user32.CloseClipboard()
                pg.hotkey("ctrl", "c")
                ThisNo = pyperclip.paste()
                pg.press("return")
                # 表示された年度を取得-----------------
                if windll.user32.OpenClipboard(None):
                    windll.user32.EmptyClipboard()
                    windll.user32.CloseClipboard()
                pg.hotkey("ctrl", "c")
                ThisYear = pyperclip.paste()
                # -----------------------------------
                pg.press("return")
                # 表示された申告種類を取得---------------
                if windll.user32.OpenClipboard(None):
                    windll.user32.EmptyClipboard()
                    windll.user32.CloseClipboard()
                pg.hotkey("ctrl", "c")
                ThisMonth = pyperclip.paste()
                pg.press("return")
                # -----------------------------------
            # 他システムとメニューが違う-------------------------------------------------------
            if str(ExRow["関与先番号"]) == ThisNo:
                print("関与先あり")
                if (
                    Start_Year < int(ThisYear) or Start_Year - int(ThisYear) == 1
                ):  # 次年度更新か判定
                    pg.press(["return", "return", "return"])
                    # 所得税メニューが表示されるまで待機------------------------------------
                    while (
                        pg.locateOnScreen(TFolURL + r"\SyotokuMenu.png", confidence=0.9)
                        is None
                    ):
                        time.sleep(1)
                        # 顧問先情報変更ダイアログが表示されたら
                        CDQ = RPA.ImgCheck(
                            TFolURL,
                            r"ChangeDataQ.png",
                            0.9,
                            10,
                        )
                        if CDQ[0] is True:
                            pg.press("y")  # yで決定
                            # 顧問先情報取込メニューが表示されるまで待機--------------------------
                            while (
                                RPA.ImgCheckForList(
                                    TFolURL,
                                    [r"ChangeDataBtn.png", r"ChangeDataBtn2.png"],
                                    0.9,
                                    10,
                                )[0]
                                is False
                            ):
                                time.sleep(1)
                            CDB = RPA.ImgCheckForList(
                                TFolURL,
                                [r"ChangeDataBtn.png", r"ChangeDataBtn2.png"],
                                0.9,
                                10,
                            )
                            RPA.ImgClick(TFolURL, CDB[1], 0.9, 10)  # 顧問先情報取込ボタンをクリック
                        # 自治体情報変更ダイアログが表示されたら
                        THI = RPA.ImgCheck(
                            TFolURL,
                            r"THI.png",
                            0.9,
                            10,
                        )
                        if THI[0] is True:
                            pg.press("return")
                    # --------------------------------------------------------------------
                    RPA.ImgClick(
                        TFolURL, r"\KojinKihon.png", 0.9, 10
                    )  # 個人基本情報のアイコンをクリック
                    SQ = RPA.ImgCheck(TFolURL, r"SansyouQ.png", 0.9, 10)
                    if SQ[0] is True:
                        pg.press("n")
                        time.sleep(1)
                        pg.press("y")
                        time.sleep(1)
                    # 顧問先情報取り込みアイコンが表示されるまで待機--------------------------------
                    while (
                        pg.locateOnScreen(TFolURL + r"\DataInIcon.png", confidence=0.9)
                        is None
                    ):
                        time.sleep(1)
                    RPA.ImgClick(
                        TFolURL, r"\DataInIcon.png", 0.9, 10
                    )  # 顧問先情報取り込みアイコンをクリック
                    while (
                        pg.locateOnScreen(TFolURL + r"\DataInOK.png", confidence=0.9)
                        is None
                    ):
                        time.sleep(1)
                    RPA.ImgClick(TFolURL, r"\DataInOK.png", 0.9, 10)  # 取り込むボタンをクリック
                    # 自治体情報変更ダイアログが表示されたら
                    THI = RPA.ImgCheck(
                        TFolURL,
                        r"THI.png",
                        0.9,
                        10,
                    )
                    if THI[0] is True:
                        pg.press("return")
                        time.sleep(1)
                        pg.press("return")
                        time.sleep(1)
                    SCH = RPA.ImgCheck(
                        TFolURL,
                        r"SyotokuCheck.png",
                        0.9,
                        10,
                    )
                    if SCH[0] is True:
                        pg.press("return")
                        time.sleep(1)
                        pg.press("return")
                        time.sleep(1)
                    time.sleep(3)
                    pg.keyDown("alt")
                    pg.press("x")
                    pg.keyUp("alt")
                    time.sleep(1)
                    pg.press("y")
                    # 一括更新のアイコンが表示されるまで待機------------------------------------
                    while (
                        pg.locateOnScreen(
                            TFolURL + r"\SyotokuKousin.png", confidence=0.9
                        )
                        is None
                    ):
                        time.sleep(1)
                    RPA.ImgClick(
                        TFolURL, r"\SyotokuKousin.png", 0.9, 10
                    )  # 一括更新のアイコンをクリック
                    # 所得税メニューが表示されるまで待機------------------------------------
                    while (
                        pg.locateOnScreen(
                            TFolURL + r"\SyotokuKMenu.png", confidence=0.9
                        )
                        is None
                    ):
                        time.sleep(1)
                    # --------------------------------------------------------------------
                    while (
                        RPA.ImgCheckForList(
                            TFolURL, [r"IkkatuFind.png", r"IkkatuFind2.png"], 0.9, 10
                        )[0]
                        is False
                    ):
                        time.sleep(1)
                    # 検索メニューが表示されるまでループ------------------------------------
                    while (
                        pg.locateOnScreen(TFolURL + r"\Find.png", confidence=0.9)
                        is None
                    ):
                        time.sleep(1)
                        pg.press("return")
                        time.sleep(1)
                        pg.keyDown("alt")
                        pg.press("s")
                        pg.keyUp("alt")
                    time.sleep(3)
                    pyperclip.copy(str(ExRow["関与先番号"]))
                    pg.hotkey("ctrl", "v")
                    pg.press(["return", "return"])
                    time.sleep(1)
                    pg.press("space")
                    time.sleep(1)
                    # --------------------------------------------------------------------
                    SNC = RPA.ImgCheck(TFolURL, r"SyotokuNoCalc.png", 0.9, 10)
                    if SNC[0] is True:
                        ErrStr = "Nocalc"
                        pg.press("y")  # yで決定(nがキャンセル)
                    time.sleep(2)
                    RPA.ImgClick(
                        TFolURL, r"\SyotokuStart.png", 0.9, 10
                    )  # 更新開始のアイコンをクリック
                    # 確認ウィンドウが表示されるまで待機-------------------------------------
                    while (
                        pg.locateOnScreen(TFolURL + r"\SyotokuQ.png", confidence=0.9)
                        is None
                    ):
                        time.sleep(1)
                    # --------------------------------------------------------------------
                    pg.press("y")  # yで決定(nがキャンセル)
                    # 処理終了ウィンドウが表示されるまで待機----------------------------------
                    while (
                        pg.locateOnScreen(TFolURL + r"\SyotokuEnd.png", confidence=0.9)
                        is None
                    ):
                        time.sleep(1)
                    # --------------------------------------------------------------------
                    pg.press("return")  # 決定
                    # 一括更新のアイコンが表示されるまで待機----------------------------------
                    while (
                        pg.locateOnScreen(TFolURL + r"\SyotokuMenu.png", confidence=0.9)
                        is None
                    ):
                        time.sleep(1)
                        ME = RPA.ImgCheckForList(
                            TFolURL, [r"\MenuEnd.png", r"\MenuEnd2.png"], 0.9, 10
                        )
                        if ME[0] is True:
                            RPA.ImgClick(TFolURL, ME[1], 0.9, 10)  # 終了アイコンをクリック
                    # --------------------------------------------------------------------
                    # 閉じる処理--------------------------
                    pg.keyDown("alt")
                    pg.press("f4")
                    pg.keyUp("alt")
                    # -----------------------------------
                    # 所得税フラグが表示されるまで待機-------------------------------------
                    while (
                        pg.locateOnScreen(TFolURL + r"\SyotokuFlag.png", confidence=0.9)
                        is None
                    ):
                        time.sleep(1)
                    # --------------------------------------------------------------------
                    # 初期画面で開封された所得税項目を閉じる----------------------------------
                    HoujinList = [
                        r"\Syotoku.png",
                        r"\Syotoku2.png",
                    ]
                    HLI = RPA.ImgCheckForList(TFolURL, HoujinList, 0.9, 10)
                    if HLI[0] is True:
                        RPA.ImgClick(TFolURL, HLI[1], 0.9, 10)
                    # --------------------------------------------------------------------
                    print("更新完了")
                    if ErrStr == "":
                        return True, ThisNo, ThisYear, ThisMonth
                    elif ErrStr == "Nocalc":
                        return True, "Nocalc", ThisYear, ThisMonth
                elif Start_Year == int(ThisYear):  # 次年度更新か判定
                    return False, "当年データ重複エラー", "", ""
            else:
                print("関与先なし")
                # 初期画面で開封された所得税項目を閉じる----------------------------------
                HoujinList = [
                    r"\Syotoku.png",
                    r"\Syotoku2.png",
                ]
                HLI = RPA.ImgCheckForList(TFolURL, HoujinList, 0.9, 10)
                if HLI[0] is True:
                    RPA.ImgClick(TFolURL, HLI[1], 0.9, 10)
                # --------------------------------------------------------------------
                return False, "関与先なし", "", ""
        else:
            return False, "所得税起動失敗", "", ""
    except:
        return False, "exceptエラー", "", ""
