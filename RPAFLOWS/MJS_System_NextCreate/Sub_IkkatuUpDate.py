# ------------------------------------------------------------------------------------------------------------------
def IkkatuUpDate(FolURL, TFolURL, ExRow, driver):
    """
    会計大将:その他メニュー一括更新
    """
    try:
        RPA.ImgClick(TFolURL, r"\M_Sonota.png", 0.9, 10)  # その他メニュ-のアイコンをクリック
        # 一括更新のアイコンが表示されるまで待機----------------------------------
        while (
            pg.locateOnScreen(TFolURL + r"\IkkatsuKousin.png", confidence=0.9) is None
        ):
            time.sleep(1)
        # --------------------------------------------------------------------
        RPA.ImgClick(TFolURL, r"\IkkatsuKousin.png", 0.9, 10)  # その他メニュ-のアイコンをクリック
        # 一括更新メニューが表示されるまで待機------------------------------------
        while (
            pg.locateOnScreen(TFolURL + r"\IkkatuOpenFlag.png", confidence=0.9) is None
        ):
            time.sleep(1)
        # --------------------------------------------------------------------
        RPA.ImgClick(TFolURL, r"\IkkatuOpenFlag.png", 0.9, 10)  # 一括更新メニューのアイコンをクリック
        while (
            RPA.ImgCheckForList(
                TFolURL, [r"IkkatuFind.png", r"IkkatuFind2.png"], 0.9, 10
            )[0]
            is False
        ):
            time.sleep(1)

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

        # ThisYearKey.pngが表示されるまで繰り返し
        while RPA.ImgCheck(TFolURL, r"\ThisYearKey.png", 0.9, 10)[0] is False:
            pyperclip.copy(str(ExRow["関与先番号"]))
            pg.hotkey("ctrl", "v")
            # 検索ボタンまでエンター-------------------------------------
            while RPA.ImgCheck(TFolURL, r"FindFlag.png", 0.9, 10)[0] is False:
                time.sleep(1)
                pg.press("return")
            pg.press("return")
            time.sleep(1)
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
            RPA.ImgClick(TFolURL, r"\IkkatuStart.png", 0.9, 10)  # 一括更新開始のアイコンをクリック
            # 確認ウィンドウが表示されるまで待機-------------------------------------
            while pg.locateOnScreen(TFolURL + r"\SakuseiQ.png", confidence=0.9) is None:
                time.sleep(1)
            # --------------------------------------------------------------------
            pg.press("y")  # yで決定(nがキャンセル)
            # 確認ウィンドウが表示されるまで待機-------------------------------------
            while (
                pg.locateOnScreen(TFolURL + r"\SakuseiQ2.png", confidence=0.9) is None
            ):
                time.sleep(1)
            # --------------------------------------------------------------------
            pg.press("return")  # 決定
            # 処理終了ウィンドウが表示されるまで待機----------------------------------
            while (
                pg.locateOnScreen(TFolURL + r"\IkkatuEndFlag.png", confidence=0.9)
                is None
            ):
                time.sleep(1)
            # --------------------------------------------------------------------
            pg.press("return")  # 決定
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
            while (
                RPA.ImgCheck(TFolURL, r"\IkkatuUpDateStopFlag.png", 0.9, 10)[0] is False
            ):
                pg.press("tab")
            pg.press("tab")
        return True
    except:
        return False
