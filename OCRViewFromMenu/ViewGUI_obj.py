from tkinter import LEFT, BOTH, Radiobutton, IntVar, EventType, W, E, TclError
from customtkinter import CTkButton, CTkEntry, CTkLabel, CTkComboBox

# Event Callback----------------------------------------------------------------------
def ElementCreate(self):
    try:
        # ウィジェットサイズ設定##########################################################
        self.wid_Par = self.width_of_window / 1459
        self.hei_Par = self.height_of_window / 820
        self.SideWidth = int(100 * self.wid_Par)
        self.SideHeight = int(50 * self.hei_Par)
        self.LabelWidth = int(50 * self.wid_Par)
        self.LabelHeight = int(20 * self.hei_Par)
        self.BtnWidth = int(170 * self.wid_Par)
        self.BtnHeight = int(20 * self.hei_Par)
        self.EntWidth = int(300 * self.hei_Par)
        self.EntHeight = int(20 * self.wid_Par)
        self.t_font = (1, int(8 * self.wid_Par))
        ###############################################################################
        # フォルダー・ファイル選択を配置
        self.window_sub_ctrl1.pack(side=LEFT, padx=5, fill=BOTH, expand=True)
        # 画像編集1を配置
        self.window_sub_ctrl2.pack(side=LEFT, padx=5, fill=BOTH, expand=True)
        # 画像編集2を配置
        self.window_sub_ctrl4.pack(side=LEFT, padx=5, fill=BOTH, expand=True)
        # window_sub_ctrl1#############################################################
        # フォルダ選択ボタン生成
        self.button_setdir = CTkButton(
            master=self.window_sub_ctrl1,
            text="フォルダ選択",
            command=self.event_set_folder,
            width=self.BtnWidth,
            height=self.BtnHeight,
            border_width=2,
            corner_radius=8,
            text_color="snow",
            border_color="snow",
            fg_color="seagreen3",
        )
        # 前画像ボタン生成
        self.button_setdir.grid(row=0, column=0, padx=5, pady=5, sticky=W + E)
        self.button_prev = CTkButton(
            master=self.window_sub_ctrl1,
            text="前画像<<",
            command=self.event_prev,
            width=self.BtnWidth,
            height=self.BtnHeight,
            border_width=2,
            corner_radius=8,
            text_color="snow",
            border_color="snow",
        )
        self.button_prev.grid(row=0, column=1, padx=5, pady=5, sticky=W + E)
        # 切替ボタン生成
        self.button_next = CTkButton(
            master=self.window_sub_ctrl1,
            text=">>次画像",
            command=self.event_next,
            width=self.BtnWidth,
            height=self.BtnHeight,
            border_width=2,
            corner_radius=8,
            text_color="snow",
            border_color="snow",
        )
        self.button_next.grid(row=0, column=2, padx=5, pady=5, sticky=W + E)
        # 　テキストエントリ生成
        self.entry_dir = CTkEntry(
            master=self.window_sub_ctrl1,
            placeholder_text="entry_dir",
            textvariable=self.str_dir,
            width=self.EntWidth,
            height=self.EntHeight,
            border_width=2,
            corner_radius=8,
            text_color="black",
            border_color="snow",
        )
        self.entry_dir.grid(row=1, column=0, columnspan=3, padx=5, pady=5, sticky=W + E)
        # ラベル
        self.label_target = CTkLabel(
            master=self.window_sub_ctrl1,
            text="[ファイル]",
            width=self.LabelWidth,
            height=self.LabelHeight,
            corner_radius=8,
        )
        self.label_target.grid(row=2, column=0, columnspan=3, padx=5, pady=5, sticky=W)
        # コンボBOX生成
        self.combo_file = CTkComboBox(
            master=self.window_sub_ctrl1,
            # text="combo_file",
            # value=self.file_list,
            values=self.file_list,
            state="readonly",
            width=self.EntWidth,
            command=self.event_updatefile,
        )
        self.combo_file.set(self.file_list[0])
        self.combo_file.grid(
            row=3, column=0, columnspan=3, padx=5, pady=5, sticky=W + E
        )
        # ファイル削除ボタン生成
        self.Delete_button = CTkButton(
            master=self.window_sub_ctrl1,
            text="ファイル削除",
            command=self.FileDelete,
            width=self.BtnWidth,
            height=self.BtnHeight,
            border_width=2,
            corner_radius=8,
            text_color="snow",
            border_color="snow",
            fg_color="red",
        )
        self.Delete_button.grid(row=4, column=0, padx=5, pady=5, sticky=W + E)
        # #############################################################################
        # window_sub_ctrl2#############################################################
        self.label_rotate = CTkLabel(
            master=self.window_sub_ctrl2,
            text="[画像回転]",
            width=self.LabelWidth,
            height=self.LabelHeight,
            corner_radius=8,
        )
        self.label_rotate.grid(row=0, column=0, padx=5, pady=5, sticky=W)
        # 回転角度ラジオボックス生成
        self.radio_intvar1 = IntVar()
        self.radio_intvar2 = IntVar()
        self.radio_intvar1.set(0)  # 0:No select
        self.radio_intvar2.set(0)  # 0:No select
        self.radio_rotate = []
        for val, text in enumerate(
            ["90°", "180°", "270°"]
        ):  # 1:rot90 2:rot180 3:rot270
            self.radio_rotate.append(
                Radiobutton(
                    self.window_sub_ctrl2,
                    text=text,
                    value=val + 1,
                    variable=self.radio_intvar1,
                    command=self.event_rotate,
                    bg="#60cad1",
                )
            )
        self.radio_rotate[0].grid(row=1, column=0, padx=5, pady=5, sticky=W + E)
        self.radio_rotate[1].grid(row=1, column=1, padx=5, pady=5, sticky=W + E)
        self.radio_rotate[2].grid(row=1, column=2, padx=5, pady=5, sticky=W + E)
        # 左回転ボタン生成
        self.button_LeftLotate = CTkButton(
            master=self.window_sub_ctrl2,
            text="左回転",
            command=self.button_LeftLotate_func,
            width=self.BtnWidth,
            height=self.BtnHeight,
            border_width=2,
            corner_radius=8,
            text_color="snow",
            border_color="snow",
            fg_color="Orange",
        )
        self.button_LeftLotate.grid(row=2, column=0, padx=5, pady=5, sticky=W + E)
        # 右回転ボタン生成
        self.button_RightLotate = CTkButton(
            master=self.window_sub_ctrl2,
            text="右回転",
            command=self.button_RightLotate_func,
            width=self.BtnWidth,
            height=self.BtnHeight,
            border_width=2,
            corner_radius=8,
            text_color="snow",
            border_color="snow",
            fg_color="Orange",
        )
        self.button_RightLotate.grid(
            row=2, column=1, columnspan=2, padx=5, pady=5, sticky=W + E
        )
        self.label_flip = CTkLabel(
            master=self.window_sub_ctrl2,
            text="[反転]",
            width=self.LabelWidth,
            height=self.LabelHeight,
            corner_radius=8,
        )
        self.label_flip.grid(row=3, column=0, padx=5, pady=5, sticky=W)
        self.radio_flip = []
        for val, text in enumerate(["U/D", "L/R"]):  # 1:Flip U/L 2:Flip L/R
            self.radio_flip.append(
                Radiobutton(
                    self.window_sub_ctrl2,
                    text=text,
                    value=val + 1,
                    variable=self.radio_intvar2,
                    command=self.event_flip,
                    bg="#60cad1",
                )
            )
        self.radio_flip[0].grid(row=4, column=0, padx=5, pady=5, sticky=W + E)
        self.radio_flip[1].grid(row=4, column=1, padx=5, pady=5, sticky=W + E)
        # #############################################################################
        # window_sub_ctrl4#############################################################
        self.label_clip = CTkLabel(
            master=self.window_sub_ctrl4,
            text="[トリミング・削除]",
            width=self.LabelWidth,
            height=self.LabelHeight,
            corner_radius=8,
        )
        self.label_clip.grid(row=0, column=0, padx=5, pady=5, sticky=W)
        # クリップボタン生成
        self.button_clip_start = CTkButton(
            master=self.window_sub_ctrl4,
            text="選択開始",
            command=self.event_clip_try,
            width=self.BtnWidth,
            height=self.BtnHeight,
            border_width=2,
            corner_radius=8,
            text_color="snow",
            border_color="snow",
            fg_color="#7eb000",
        )
        self.button_clip_start.grid(row=1, column=0, padx=5, pady=5, sticky=W + E)
        self.button_clip_done = CTkButton(
            master=self.window_sub_ctrl4,
            text="範囲トリミング",
            command=self.event_clip_done,
            width=self.BtnWidth,
            height=self.BtnHeight,
            border_width=2,
            corner_radius=8,
            text_color="snow",
            border_color="snow",
            fg_color="#6100b0",
        )
        self.button_clip_done.grid(row=1, column=1, padx=5, pady=5, sticky=W + E)
        self.button_clip_Erace = CTkButton(
            master=self.window_sub_ctrl4,
            text="範囲削除",
            command=self.event_clip_Erace,
            width=self.BtnWidth,
            height=self.BtnHeight,
            border_width=2,
            corner_radius=8,
            text_color="snow",
            border_color="snow",
            fg_color="#c7048c",
        )
        self.button_clip_Erace.grid(row=1, column=2, padx=5, pady=5, sticky=W + E)
        self.label_run = CTkLabel(
            master=self.window_sub_ctrl4,
            text="[編集確定]",
            width=self.LabelWidth,
            height=self.LabelHeight,
            corner_radius=8,
        )
        self.label_run.grid(row=2, column=0, columnspan=2, padx=5, pady=5, sticky=W)
        # Save/Undoボタン生成
        self.button_Oversave = CTkButton(
            master=self.window_sub_ctrl4,
            text="上書保存",
            command=self.event_Oversave,
            width=self.BtnWidth,
            height=self.BtnHeight,
            border_width=2,
            corner_radius=8,
            text_color="snow",
            border_color="snow",
            fg_color="#cf94ff",
        )
        self.button_Oversave.grid(row=3, column=0, padx=5, pady=5, sticky=W + E)
        self.button_undo = CTkButton(
            master=self.window_sub_ctrl4,
            text="編集取消",
            command=self.event_undo,
            width=self.BtnWidth,
            height=self.BtnHeight,
            border_width=2,
            corner_radius=8,
            text_color="snow",
            border_color="snow",
            fg_color="gray",
        )
        self.button_undo.grid(row=3, column=1, padx=5, pady=5, sticky=W + E)
        self.button_save = CTkButton(
            master=self.window_sub_ctrl4,
            text="別名保存",
            command=self.event_save,
            width=self.BtnWidth,
            height=self.BtnHeight,
            border_width=2,
            corner_radius=8,
            text_color="snow",
            border_color="snow",
            fg_color="hotpink1",
        )
        self.button_save.grid(row=3, column=2, padx=5, pady=5, sticky=W + E)
        # label_Line = CTkLabel(
        #     master=self.window_sub_ctrl2,
        #     text="[サブメニュー]",
        #     width=self.LabelWidth,
        #     height=self.LabelHeight,
        #     corner_radius=8,
        # )
        # label_Line.grid(row=4, column=1, columnspan=2, padx=5, pady=5, sticky=W)
        # LineOCR起動ボタン生成
        self.button_LinOCR = CTkButton(
            master=self.window_sub_ctrl4,
            text="OCR起動",
            command=self.LinOCROpen,
            width=self.BtnWidth,
            height=self.BtnHeight,
            border_width=2,
            corner_radius=8,
            text_color="snow",
            border_color="snow",
            fg_color="tomato",
        )
        self.button_LinOCR.grid(row=4, column=0, padx=5, pady=5, sticky=W + E)
        # self.button_PTable = CTkButton(
        #     master=self.window_sub_ctrl4,
        #     text="比較ウィンドウ起動",
        #     command=self.Open_pt,
        #     width=self.BtnWidth,
        #     height=self.BtnHeight,
        #     border_width=2,
        #     corner_radius=8,
        #     text_color="snow",
        #     border_color="snow",
        #     fg_color="lightpink",
        # )
        # self.button_PTable.grid(row=5, column=2, padx=5, pady=5, sticky=W + E)
        # SubMenu起動ボタン生成
        # button_SubMenu = CTkButton(
        #     master=self.window_sub_ctrl4,
        #     text="サブメニュー",
        #     command=self.event_menu,
        #     width=self.BtnWidth,
        #     height=self.BtnHeight,
        #     border_width=2,
        #     corner_radius=8,
        #     text_color="snow",
        #     border_color="snow",
        # )
        # button_SubMenu.grid(row=5, column=2, padx=5, pady=5, sticky=W + E)
        # -------------------------------------------------------------------
        # Exposeイベントbind
        for event_type in EventType.__members__.keys():
            if event_type == "Expose":
                event_seq = "<" + event_type + ">"
                try:
                    self.window_rootFrame.bind_all(event_seq, self.event_handler)
                    # print(event_type)
                except TclError:
                    # print("bind error:", event_type)
                    pass
        # -------------------------------------------------------------------
        self.control.model.stock_url = ""  # 一時保存URLをリセット
        return
    except:
        self.logger.debug("要素作成失敗")  # Log出力
        return
