# ------------------------------------------------------------------------------------------------------------------
def HouteiUpdate(FolURL, TFolURL, ExRow, driver):
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
    概要: 法定調書更新処理
    @param FolURL : ミロク起動関数のフォルダ(str)
    @param TFolURL : このpyファイルのフォルダ(str)
    @param ExRow : Excel抽出行(obj)
    @param driver : 画面操作ドライバー(obj)
    @return : bool,ミロク入力関与先コード, ミロク入力処理年, ミロク入力処理月
    """
    try:
        ErrStr = ""  # Rpaエラー判別変数
        # 法定調書のアイコンを探す-------------------------------------------------
        ImgList = [r"\Houtei.png", r"\Houtei2.png"]
        ICFL = RPA.ImgCheckForList(TFolURL, ImgList, 0.9, 10)
        # -----------------------------------------------------------------------
        if ICFL[0] is True:  # 法定調書のアイコンがあれば
            RPA.ImgClick(TFolURL, ICFL[1], 0.9, 10)  # 法定調書のアイコンをクリック
            # 法定調書フラグが表示されるまで待機------------------------------------
            while (
                pg.locateOnScreen(TFolURL + r"\HouteiFlag.png", confidence=0.9) is None
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
            # 入力した関与先コードを取得------------
            pg.keyDown("shift")
            pg.press(["tab", "tab"])
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
            pg.press("return")
            time.sleep(1)
            # 他システムとメニューが違う-------------------------------------------------------
            if str(ExRow["関与先番号"]) == ThisNo:
                print("関与先あり")
                pg.press(["return", "return", "return"])
                # 法定調書メニューが表示されるまで待機--------------------------------
                while (
                    pg.locateOnScreen(TFolURL + r"\HouteiMenu.png", confidence=0.9)
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
                # --------------------------------------------------------------------
                RPA.ImgClick(TFolURL, r"\Siharaisya.png", 0.9, 10)  # 支払者基本情報をクリック
                time.sleep(1)
                SAN = RPA.ImgCheck(TFolURL, r"\SansyouOK.png", 0.9, 50)  # 参照表示ダイアログを確認
                if SAN[0] is True:
                    time.sleep(1)
                    RPA.ImgClick(TFolURL, r"\DataInNo.png", 0.9, 50)
                    while (
                        pg.locateOnScreen(TFolURL + r"\DataInYes.png", confidence=0.9)
                        is not None
                    ):
                        RPA.ImgClick(TFolURL, r"\DataInYes.png", 0.9, 10)
                        time.sleep(1)
                # 顧問先情報取り込みアイコンが表示されるまで待機--------------------------------
                while (
                    pg.locateOnScreen(TFolURL + r"\DataInIcon.png", confidence=0.9)
                    is None
                ):
                    time.sleep(1)
                RPA.ImgClick(TFolURL, r"\DataInIcon.png", 0.9, 10)  # 顧問先情報取り込みアイコンをクリック
                # 取り込むボタンが表示されるまで待機--------------------------------
                while (
                    pg.locateOnScreen(TFolURL + r"\DataInIcon2.png", confidence=0.9)
                    is None
                ):
                    time.sleep(1)
                RPA.ImgClick(TFolURL, r"\DataInIcon2.png", 0.9, 10)  # 取り込むボタンをクリック
                time.sleep(3)
                pg.keyDown("alt")
                pg.press("x")
                pg.keyUp("alt")
                time.sleep(1)
                # 法定調書メニューが表示されるまで待機--------------------------------
                while (
                    pg.locateOnScreen(TFolURL + r"\HouteiMenu.png", confidence=0.9)
                    is None
                ):
                    time.sleep(1)
                    SKE = RPA.ImgCheck(
                        TFolURL, r"\SiharaiKihonEnd.png", 0.9, 10
                    )  # 終了ダイアログ確認
                    if SKE[0] is True:
                        pg.press("y")
                RPA.ImgClick(TFolURL, r"\HouteiKousin.png", 0.9, 10)  # 法定調書更新をクリック
                # 法定調書メニューが表示されるまで待機------------------------------------
                while (
                    pg.locateOnScreen(TFolURL + r"\HouteiAll.png", confidence=0.9)
                    is None
                ):
                    time.sleep(1)
                # --------------------------------------------------------------------
                time.sleep(1)
                # 更新区分フラグが表示されるまで待機------------------------------------
                while (
                    pg.locateOnScreen(TFolURL + r"\HouteiZenken.png", confidence=0.9)
                    is None
                ):
                    pg.press("tab")

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
                    RPA.ImgClick(TFolURL, FC[1], 0.9, 10)  # 一括検索メニューのアイコンをクリック
                    # 確認ウィンドウが表示されるまで待機-------------------------------------
                    while (
                        pg.locateOnScreen(TFolURL + r"\Rensou.png", confidence=0.9)
                        is None
                    ):
                        time.sleep(1)
                    p = pg.locateOnScreen(TFolURL + r"\Rensou.png", confidence=0.9)
                    x, y = pg.center(p)
                    pg.click(x + 100, y)
                    pyperclip.copy(str(ExRow["関与先番号"]))
                    pg.hotkey("ctrl", "v")
                    # 検索ボタンまでエンター-------------------------------------
                    while RPA.ImgCheck(TFolURL, r"ZFindFlag2.png", 0.9, 10)[0] is False:
                        time.sleep(1)
                        pg.press("return")
                pg.press("return")
                time.sleep(1)
                pg.press("space")

                # --------------------------------------------------------------------
                if ErrStr == "":
                    pg.press("return")
                    pg.press("space")
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
                    # --------------------------------------------------------------------
                    time.sleep(1)
                    RPA.ImgClick(
                        TFolURL, r"\HouteiStart.png", 0.9, 10
                    )  # 更新開始のアイコンをクリック
                    # 確認ウィンドウが表示されるまで待機-------------------------------------
                    while (
                        pg.locateOnScreen(TFolURL + r"\HouteiQ.png", confidence=0.9)
                        is None
                    ):
                        time.sleep(1)
                    # --------------------------------------------------------------------
                    pg.press("y")  # yで決定(nがキャンセル)
                    # 処理終了ウィンドウが表示されるまで待機----------------------------------
                    while (
                        pg.locateOnScreen(TFolURL + r"\HouteiEnd.png", confidence=0.9)
                        is None
                    ):
                        time.sleep(1)
                    # --------------------------------------------------------------------
                    pg.press("return")
                    # ロードを待機----------------------------------------------------------
                    while (
                        pg.locateOnScreen(
                            TFolURL + r"\HouteiNoCheck.png", confidence=0.9
                        )
                        is None
                    ):
                        time.sleep(1)
                    # --------------------------------------------------------------------
                    # 法定調書終了確認が表示されるまで待機--------------------------------------
                    while (
                        pg.locateOnScreen(
                            TFolURL + r"\HouteiEndMsg.png", confidence=0.9
                        )
                        is None
                    ):
                        time.sleep(1)
                        ME = RPA.ImgCheckForList(
                            TFolURL, [r"\MenuEnd.png", r"\MenuEnd2.png"], 0.9, 10
                        )
                        if ME[0] is True:
                            RPA.ImgClick(TFolURL, ME[1], 0.9, 10)  # 終了アイコンをクリック
                    # --------------------------------------------------------------------
                    pg.press("y")
                    # 法定調書開始フラグが表示されるまで待機--------------------------------------
                    while (
                        pg.locateOnScreen(TFolURL + r"\HouteiMenu.png", confidence=0.9)
                        is None
                    ):
                        time.sleep(1)
                    # --------------------------------------------------------------------
                    # 閉じる処理--------------------------
                    pg.keyDown("alt")
                    pg.press("f4")
                    pg.keyUp("alt")
                    # -----------------------------------
                    # 法定調書フラグが表示されるまで待機-------------------------------------
                    while (
                        pg.locateOnScreen(TFolURL + r"\HouteiFlag.png", confidence=0.9)
                        is None
                    ):
                        time.sleep(1)
                    # --------------------------------------------------------------------
                    print("更新完了")
                    if ErrStr == "":
                        return True, ThisNo, ThisYear, "ThisMonth"
            else:
                print("関与先なし")
                return False, "関与先なし", "", ""
        else:
            return False, "法定調書起動失敗", "", ""
    except:
        return False, "exceptエラー", "", ""
