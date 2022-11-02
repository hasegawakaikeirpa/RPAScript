# ------------------------------------------------------------------------------------------------------------------
def ZaisanUpdate(FolURL, TFolURL, ExRow, driver):
    """
    00:"関与先番号"
    01:"関与先名"
    02:"担当者_ｺｰﾄﾞ"
    03:"担当者_担当者名"
    04:"会計大将_繰越対象"
    07:"会計大将_繰越処理日"
    08:"決算内訳書_繰越対象"
    11:"決算内訳書_繰越処理日"
    12:"減価償却_繰越対象"
    15:"減価償却_繰越処理日"
    16:"法人税申告書_繰越対象"
    19:"法人税申告書_繰越処理日"
    20:"財産評価明細書_繰越対象"
    23:"財産評価明細書_繰越処理日"
    24:"財産評価明細書"
    25:"年末調整"
    26:"法定調書"
    27:"所得税確定申告"
    """
    """
    概要: 財産評価更新処理
    @param FolURL : ミロク起動関数のフォルダ(str)
    @param TFolURL : このpyファイルのフォルダ(str)
    @param ExRow : Excel抽出行(obj)
    @param driver : 画面操作ドライバー(obj)
    @return : bool,ミロク入力関与先コード, ミロク入力処理年, ミロク入力処理月
    """
    try:
        ErrStr = ""  # Rpaエラー判別変数
        # 財産評価のアイコンを探す-------------------------------------------------
        ImgList = [r"\Zaisanhyouka.png", r"\Zaisanhyouka2.png"]
        ICFL = RPA.ImgCheckForList(TFolURL, ImgList, 0.9, 10)
        # -----------------------------------------------------------------------
        if ICFL[0] is True:  # 財産評価のアイコンがあれば
            RPA.ImgClick(TFolURL, ICFL[1], 0.9, 10)  # 財産評価のアイコンをクリック
            # 財産評価フラグが表示されるまで待機------------------------------------
            while (
                pg.locateOnScreen(TFolURL + r"\ZaisanhyoukaFlag.png", confidence=0.9)
                is None
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
                pg.press(["return", "return"])
                pg.keyDown("shift")
                pg.press(["tab", "tab", "tab", "tab"])
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
                pg.press(["return", "return"])
                pg.keyDown("shift")
                pg.press(["tab", "tab", "tab", "tab"])
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
                pg.press(["return", "return", "return"])
                # 財産評価更新アイコンが表示されるまで待機--------------------------------
                while (
                    pg.locateOnScreen(TFolURL + r"\ZaisanKousin.png", confidence=0.9)
                    is None
                ):
                    time.sleep(1)
                    HQ = RPA.ImgCheck(TFolURL, r"\ZaisanOpenQ.png", 0.9, 10)
                    if HQ[0] is True:
                        RPA.ImgClick(TFolURL, r"\ZaisanOpenQCansel.png", 0.9, 10)
                    # 顧問先情報変更ダイアログが表示されたら
                    CDQ = RPA.ImgCheck(
                        TFolURL,
                        r"ZChangeDataQ.png",
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
                # データ基本情報を更新---------------------------------------------------
                RPA.ImgClick(TFolURL, r"\DataIcon.png", 0.9, 10)
                while (
                    pg.locateOnScreen(TFolURL + r"\DataInIcon.png", confidence=0.9)
                    is None
                ):
                    time.sleep(1)
                RPA.ImgClick(TFolURL, r"\DataInIcon.png", 0.9, 10)
                while (
                    pg.locateOnScreen(TFolURL + r"\DataInOK.png", confidence=0.9)
                    is None
                ):
                    time.sleep(1)
                RPA.ImgClick(TFolURL, r"\DataInOK.png", 0.9, 10)
                while (
                    pg.locateOnScreen(TFolURL + r"\DataInIcon.png", confidence=0.9)
                    is None
                ):
                    time.sleep(1)
                ME = RPA.ImgCheckForList(
                    TFolURL, [r"\MenuEnd.png", r"\MenuEnd2.png"], 0.9, 10
                )
                if ME[0] is True:
                    RPA.ImgClick(TFolURL, ME[1], 0.9, 10)  # 終了アイコンをクリック
                while (
                    pg.locateOnScreen(TFolURL + r"\DataEndQ.png", confidence=0.9)
                    is None
                ):
                    time.sleep(1)
                pg.press("y")
                while (
                    pg.locateOnScreen(TFolURL + r"\ZaisanKousin.png", confidence=0.9)
                    is None
                ):
                    time.sleep(1)
                # --------------------------------------------------------------------
                # --------------------------------------------------------------------
                RPA.ImgClick(TFolURL, r"\ZaisanKousin.png", 0.9, 10)  # 一括更新のアイコンをクリック
                # 財産評価メニューが表示されるまで待機------------------------------------
                while (
                    pg.locateOnScreen(TFolURL + r"\ZaisanOpenFlag.png", confidence=0.9)
                    is None
                ):
                    time.sleep(1)
                # --------------------------------------------------------------------
                time.sleep(3)
                # 更新区分を次年繰越に変更---------------------------------------------
                RPA.ImgClick(TFolURL, r"\Kousinkubun.png", 0.9, 10)
                pg.press("home")
                pg.press("return")
                # 更新区分フラグが表示されるまで待機------------------------------------
                while (
                    pg.locateOnScreen(TFolURL + r"\KousinkubunFlag.png", confidence=0.9)
                    is None
                ):
                    time.sleep(1)
                # --------------------------------------------------------------------
                FC = RPA.ImgCheckForList(
                    TFolURL,
                    [
                        r"IkkatuFind.png",
                        r"IkkatuFind2.png",
                    ],
                    0.9,
                    10,
                )
                if FC[0] is True:
                    RPA.ImgClick(TFolURL, FC[1], 0.9, 10)  # 一括更新メニューのアイコンをクリック
                    pyperclip.copy(str(ExRow["関与先番号"]))
                    pg.hotkey("ctrl", "v")
                    # 検索ボタンまでエンター-------------------------------------
                    while RPA.ImgCheck(TFolURL, r"ZFindFlag.png", 0.9, 10)[0] is False:
                        time.sleep(1)
                        pg.press("return")
                pg.press("return")
                time.sleep(1)
                pg.press("space")

                if ErrStr == "":
                    # チェックマークが表示されるまで待機-------------------------------------
                    while (
                        RPA.ImgCheckForList(
                            TFolURL,
                            [
                                r"IkkatuCheck.png",
                                r"ZaisanCheck.png",
                                r"NendCheck.png",
                                r"HouteiCheck.png",
                            ],
                            0.9,
                            10,
                        )[0]
                        is False
                    ):
                        time.sleep(1)
                        ZND = RPA.ImgCheck(TFolURL, r"ZaisanNoData.png", 0.9, 10)
                        if ZND[0] is True:
                            ErrStr = "NoData"
                            break
                    # --------------------------------------------------------------------
                    time.sleep(1)
                    if not ErrStr == "NoData":
                        RPA.ImgClick(
                            TFolURL, r"\ZaisanStart.png", 0.9, 10
                        )  # 更新開始のアイコンをクリック
                        # 確認ウィンドウが表示されるまで待機-------------------------------------
                        while (
                            pg.locateOnScreen(
                                TFolURL + r"\ZaisanStartQ.png", confidence=0.9
                            )
                            is None
                        ):
                            time.sleep(1)
                        # --------------------------------------------------------------------
                        pg.press("y")  # yで決定(nがキャンセル)
                        # 処理終了ウィンドウが表示されるまで待機----------------------------------
                        while (
                            pg.locateOnScreen(
                                TFolURL + r"\ZaisanEnd.png", confidence=0.9
                            )
                            is None
                        ):
                            time.sleep(1)
                        # --------------------------------------------------------------------
                        pg.press("return")
                        # チェックマークが表示されなくなるまで待機-------------------------------
                        while (
                            RPA.ImgCheckForList(
                                TFolURL,
                                [
                                    r"IkkatuCheck.png",
                                    r"ZaisanCheck.png",
                                    r"NendCheck.png",
                                    r"HouteiCheck.png",
                                ],
                                0.9,
                                10,
                            )[0]
                            is True
                        ):
                            time.sleep(1)
                        # --------------------------------------------------------------------
                        ME = RPA.ImgCheckForList(
                            TFolURL, [r"\MenuEnd.png", r"\MenuEnd2.png"], 0.9, 10
                        )
                        if ME[0] is True:
                            RPA.ImgClick(TFolURL, ME[1], 0.9, 10)  # 終了アイコンをクリック
                        # 一括更新のアイコンが表示されるまで待機----------------------------------
                        while (
                            pg.locateOnScreen(
                                TFolURL + r"\ZaisanOpenFlag.png", confidence=0.9
                            )
                            is None
                        ):
                            time.sleep(1)
                        # --------------------------------------------------------------------
                        # 閉じる処理--------------------------
                        pg.keyDown("alt")
                        pg.press("f4")
                        pg.keyUp("alt")
                        # -----------------------------------
                        # 財産評価フラグが表示されるまで待機-------------------------------------
                        while (
                            pg.locateOnScreen(
                                TFolURL + r"\ZaisanhyoukaFlag.png", confidence=0.9
                            )
                            is None
                        ):
                            time.sleep(1)
                        # --------------------------------------------------------------------
                        # 初期画面で開封された財産評価項目を閉じる----------------------------------
                        HoujinList = [r"\Zaisanhyouka.png", r"\Zaisanhyouka2.png"]
                        HLI = RPA.ImgCheckForList(TFolURL, HoujinList, 0.9, 10)
                        if HLI[0] is True:
                            RPA.ImgClick(TFolURL, HLI[1], 0.9, 10)
                        # --------------------------------------------------------------------
                        print("更新完了")
                    if ErrStr == "":
                        return True, ThisNo, ThisYear, ThisMonth
                    else:
                        # --------------------------------------------------------------------
                        DD = RPA.ImgCheck(TFolURL, r"\DoubleDataQ.png", 0.9, 10)
                        if DD[0] is True:
                            pg.press("return")
                            time.sleep(1)
                        # --------------------------------------------------------------------
                        ME = RPA.ImgCheckForList(
                            TFolURL, [r"\MenuEnd.png", r"\MenuEnd2.png"], 0.9, 10
                        )
                        if ME[0] is True:
                            RPA.ImgClick(TFolURL, ME[1], 0.9, 10)  # 終了アイコンをクリック
                        # 一括更新のアイコンが表示されるまで待機----------------------------------
                        while (
                            pg.locateOnScreen(
                                TFolURL + r"\ZaisanOpenFlag.png", confidence=0.9
                            )
                            is None
                        ):
                            time.sleep(1)
                        # --------------------------------------------------------------------
                        # 閉じる処理--------------------------
                        pg.keyDown("alt")
                        pg.press("f4")
                        pg.keyUp("alt")
                        # -----------------------------------
                        # 財産評価フラグが表示されるまで待機-------------------------------------
                        while (
                            pg.locateOnScreen(
                                TFolURL + r"\ZaisanhyoukaFlag.png", confidence=0.9
                            )
                            is None
                        ):
                            time.sleep(1)
                        # --------------------------------------------------------------------
                        # 初期画面で開封された財産評価項目を閉じる----------------------------------
                        HoujinList = [r"\Zaisanhyouka.png", r"\Zaisanhyouka2.png"]
                        HLI = RPA.ImgCheckForList(TFolURL, HoujinList, 0.9, 10)
                        if HLI[0] is True:
                            RPA.ImgClick(TFolURL, HLI[1], 0.9, 10)
                        # --------------------------------------------------------------------
                        print("更新完了_更新対象年度無し")
                        return False, "更新対象年度無し", "", ""
            else:
                print("関与先なし")
                return False, "関与先なし", "", ""
        else:
            return False, "財産評価起動失敗", "", ""
    except:
        return False, "exceptエラー", "", ""
