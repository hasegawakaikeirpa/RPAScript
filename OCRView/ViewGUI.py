import sys
import ProgressBar as PB
import tkinter as tk
import os
from tkinter import filedialog, messagebox
import OpenWindow as OW
from ControlGUI import ControlGUI
from TKINTERCV2Setting import Main as CSVSetMain
import customtkinter as ck
import logging.config
from platform import machine, node, platform, processor, release, system, version
from socket import gethostbyname, gethostname
from uuid import getnode

# exe化コマンド↓
# pyinstaller ViewGUI.py --onefile --onedir --noconsole --clean --icon=hasegawa.ico
# 上記コマンドでできた[dist]→[ViewGUI]フォルダ内に
# [poppler-22.01.0フォルダ]・[Tesseract-OCRフォルダ]・[StraightListTate.csv]・[StraightListYoko.csv]・[key.json]
# をコピーして完了


class ViewGUI:
    """
    概要: TKinterメインWindowクラス
    """

    def __init__(self, window_root, title_n, default_path):
        global SideWidth, SideHeight, LabelWidth
        global LabelHeight, BtnWidth, BtnHeight, EntHeight, EntWidth
        global wid_Par, hei_Par
        print("#########################################################")
        print(os.getcwd())
        print("#########################################################")
        # logger設定-----------------------------------------------------------------------------------------------------
        logging.config.fileConfig(os.getcwd() + r"\LogConf\logging_debug.conf")
        self.logger = logging.getLogger(__name__)
        # ---------------------------------------------------------------------------------------------------------------
        # 初回Log
        self.logger.debug(f"Network: {node()}")  # ネットワーク名
        self.logger.debug(f"Machine: {machine()}")  # 機種
        self.logger.debug(f"Processor: {processor()}")  # プロセッサ名 (CPU)
        self.logger.debug(f"Platform: {platform() }")  # プラットフォーム (OS) 情報
        self.logger.debug(f"System: {system() }")  # OS名
        self.logger.debug(f"Release: {release()}")  # リリース情報
        self.logger.debug(f"Version: {version()}")  # バージョン情報
        self.logger.debug(f"MAC Address: {getnode():_X}")  # MACアドレス
        self.logger.debug(f"Host name: {gethostname()}")  # ホスト名
        self.logger.debug(f"IP Address: {gethostbyname(gethostname())}")  # IPアドレス
        self.logger.debug("ViewGUI起動")  # Log出力
        # ---------------------------------------------------------------------------------------------------------------
        # Controller Class生成
        self.control = ControlGUI(default_path)
        # 初期化
        self.dir_path = default_path
        self.file_list = ["..[select file]"]
        self.clip_enable = False
        self.File_url_List = []  # 書出しCSVURLリスト
        # customtkスタイル
        ck.set_appearance_mode("System")  # Modes: system (default), light, dark
        ck.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green
        # メインウィンドウ
        self.window_root = window_root
        width_of_window = int(int(self.window_root.winfo_screenwidth()) * 0.95)
        height_of_window = int(int(self.window_root.winfo_screenheight()) * 0.85)
        wid_Par = width_of_window / 1459
        hei_Par = height_of_window / 820
        x_coodinate = width_of_window * 0.01
        y_coodinate = height_of_window * 0.01
        # 　メインウィンドウサイズ指定
        self.window_root.geometry(
            "%dx%d+%d+%d"
            % (width_of_window, height_of_window, x_coodinate, y_coodinate)
        )
        self.window_root.minsize(width_of_window, height_of_window)
        # 　メインウィンドウタイトル
        self.window_root.title(title_n)
        self.window_root.protocol("WM_DELETE_WINDOW", self.click_close)  # 閉じる処理設定
        self.window_root.HeaderCol_c = 0  # ページ追加時の列数
        self.window_rootFrame = tk.Frame(
            self.window_root,
            width=width_of_window,
            height=height_of_window,
            bg="#60cad1",
        )
        self.window_rootFrame.pack(fill=tk.BOTH, expand=True)
        self.MenuCreate()  # メニューバー作成
        NWINSize = [str(width_of_window), str(height_of_window)]  # 横,縦
        self.FrameCreate(NWINSize)  # Frame作成
        self.CanvasCreate()  # Canvas作成
        self.str_dir = tk.StringVar()  # StringVar(ストリング)生成
        self.str_dir.set(self.dir_path)
        # ---------------------------------------------------------------
        self.ElementCreate()  # Element作成
        self.logger.debug("ViewGUI起動完了")  # Log出力
        # #############################################################################

    # Event Callback----------------------------------------------------------------------
    def ElementCreate(self):
        try:
            # SideWidth = int(100 * wid_Par)
            # SideHeight = int(50 * hei_Par)
            LabelWidth = int(50 * wid_Par)
            LabelHeight = int(20 * hei_Par)
            BtnWidth = int(140 * wid_Par)
            BtnHeight = int(20 * hei_Par)
            EntWidth = int(300 * hei_Par)
            EntHeight = int(20 * wid_Par)
            # t_font = (1, int(8 * wid_Par))

            # フォルダー・ファイル選択を配置
            self.window_sub_ctrl1.pack(side=tk.LEFT, padx=5, fill=tk.BOTH, expand=True)
            # 画像編集1を配置
            self.window_sub_ctrl2.pack(side=tk.LEFT, padx=5, fill=tk.BOTH, expand=True)
            # 画像編集2を配置
            self.window_sub_ctrl4.pack(side=tk.LEFT, padx=5, fill=tk.BOTH, expand=True)
            # window_sub_ctrl1#############################################################
            # フォルダ選択ボタン生成
            self.button_setdir = ck.CTkButton(
                master=self.window_sub_ctrl1,
                text="フォルダ選択",
                command=self.event_set_folder,
                width=BtnWidth,
                height=BtnHeight,
                border_width=2,
                corner_radius=8,
                text_color="snow",
                border_color="snow",
                fg_color="seagreen3",
            )
            # 前画像ボタン生成
            self.button_setdir.grid(row=1, column=1, padx=5, pady=5, sticky=tk.W)
            button_prev = ck.CTkButton(
                master=self.window_sub_ctrl1,
                text="前画像<<",
                command=self.event_prev,
                width=BtnWidth,
                height=BtnHeight,
                border_width=2,
                corner_radius=8,
                text_color="snow",
                border_color="snow",
            )
            button_prev.grid(row=1, column=2, padx=5, pady=5, sticky=tk.W)
            # 切替ボタン生成
            button_next = ck.CTkButton(
                master=self.window_sub_ctrl1,
                text=">>次画像",
                command=self.event_next,
                width=BtnWidth,
                height=BtnHeight,
                border_width=2,
                corner_radius=8,
                text_color="snow",
                border_color="snow",
            )
            button_next.grid(row=1, column=3, padx=5, pady=5, sticky=tk.W)
            # 　テキストエントリ生成
            self.entry_dir = ck.CTkEntry(
                master=self.window_sub_ctrl1,
                placeholder_text="entry_dir",
                textvariable=self.str_dir,
                width=EntWidth,
                height=EntHeight,
                border_width=2,
                corner_radius=8,
                text_color="black",
                border_color="snow",
            )
            self.entry_dir.grid(
                row=2, column=1, columnspan=4, padx=5, pady=5, sticky=tk.W
            )
            # ラベル
            label_target = ck.CTkLabel(
                master=self.window_sub_ctrl1,
                text="[ファイル]",
                width=LabelWidth,
                height=LabelHeight,
                corner_radius=8,
            )
            label_target.grid(
                row=3, column=0, columnspan=4, padx=5, pady=5, sticky=tk.W
            )
            # コンボBOX生成
            self.combo_file = ck.CTkComboBox(
                master=self.window_sub_ctrl1,
                # text="combo_file",
                # value=self.file_list,
                values=self.file_list,
                state="readonly",
                width=300,
                command=self.event_updatefile,
            )
            self.combo_file.set(self.file_list[0])
            self.combo_file.grid(
                row=4, column=1, columnspan=4, padx=5, pady=5, sticky=tk.W
            )
            # ファイル削除ボタン生成
            self.Delete_button = ck.CTkButton(
                master=self.window_sub_ctrl1,
                text="ファイル削除",
                command=self.FileDelete,
                width=BtnWidth,
                height=BtnHeight,
                border_width=2,
                corner_radius=8,
                text_color="snow",
                border_color="snow",
                fg_color="red",
            )
            self.Delete_button.grid(row=5, column=1, padx=5, pady=5, sticky=tk.W)
            # #############################################################################
            # window_sub_ctrl2#############################################################
            label_rotate = ck.CTkLabel(
                master=self.window_sub_ctrl2,
                text="[画像回転]",
                width=LabelWidth,
                height=LabelHeight,
                corner_radius=8,
            )
            label_rotate.grid(row=1, column=1, padx=5, pady=5, sticky=tk.W)
            # 回転角度ラジオボックス生成
            self.radio_intvar1 = tk.IntVar()
            self.radio_intvar2 = tk.IntVar()
            self.radio_intvar1.set(0)  # 0:No select
            self.radio_intvar2.set(0)  # 0:No select
            radio_rotate = []
            for val, text in enumerate(
                ["90°", "180°", "270°"]
            ):  # 1:rot90 2:rot180 3:rot270
                radio_rotate.append(
                    tk.Radiobutton(
                        self.window_sub_ctrl2,
                        text=text,
                        value=val + 1,
                        variable=self.radio_intvar1,
                        command=self.event_rotate,
                        bg="#60cad1",
                    )
                )
            radio_rotate[0].grid(row=2, column=1, padx=5, pady=5, sticky=tk.W)
            radio_rotate[1].grid(row=2, column=2, padx=5, pady=5, sticky=tk.W)
            radio_rotate[2].grid(row=2, column=3, padx=5, pady=5, sticky=tk.W)
            # 左回転ボタン生成
            button_LeftLotate = ck.CTkButton(
                master=self.window_sub_ctrl2,
                text="左回転",
                command=self.button_LeftLotate,
                width=BtnWidth,
                height=BtnHeight,
                border_width=2,
                corner_radius=8,
                text_color="snow",
                border_color="snow",
                fg_color="Orange",
            )
            button_LeftLotate.grid(row=4, column=1, padx=5, pady=5, sticky=tk.W)
            # 右回転ボタン生成
            button_RightLotate = ck.CTkButton(
                master=self.window_sub_ctrl2,
                text="右回転",
                command=self.button_RightLotate,
                width=BtnWidth,
                height=BtnHeight,
                border_width=2,
                corner_radius=8,
                text_color="snow",
                border_color="snow",
                fg_color="Orange",
            )
            button_RightLotate.grid(row=4, column=2, padx=5, pady=5, sticky=tk.W)
            label_flip = ck.CTkLabel(
                master=self.window_sub_ctrl2,
                text="[反転]",
                width=LabelWidth,
                height=LabelHeight,
                corner_radius=8,
            )
            label_flip.grid(row=5, column=1, padx=5, pady=5, sticky=tk.W)
            radio_flip = []
            for val, text in enumerate(["U/D", "L/R"]):  # 1:Flip U/L 2:Flip L/R
                radio_flip.append(
                    tk.Radiobutton(
                        self.window_sub_ctrl2,
                        text=text,
                        value=val + 1,
                        variable=self.radio_intvar2,
                        command=self.event_flip,
                        bg="#60cad1",
                    )
                )
            radio_flip[0].grid(row=6, column=1, padx=5, pady=5, sticky=tk.W)
            radio_flip[1].grid(row=6, column=2, padx=5, pady=5, sticky=tk.W)
            # #############################################################################
            # window_sub_ctrl4#############################################################
            label_clip = ck.CTkLabel(
                master=self.window_sub_ctrl4,
                text="[トリミング・削除]",
                width=LabelWidth,
                height=LabelHeight,
                corner_radius=8,
            )
            label_clip.grid(row=0, column=1, padx=5, pady=5, sticky=tk.W)
            # クリップボタン生成
            button_clip_start = ck.CTkButton(
                master=self.window_sub_ctrl4,
                text="選択開始",
                command=self.event_clip_try,
                width=BtnWidth,
                height=BtnHeight,
                border_width=2,
                corner_radius=8,
                text_color="snow",
                border_color="snow",
                fg_color="#7eb000",
            )
            button_clip_start.grid(row=1, column=1, padx=5, pady=5, sticky=tk.W)
            button_clip_done = ck.CTkButton(
                master=self.window_sub_ctrl4,
                text="範囲トリミング",
                command=self.event_clip_done,
                width=BtnWidth,
                height=BtnHeight,
                border_width=2,
                corner_radius=8,
                text_color="snow",
                border_color="snow",
                fg_color="#6100b0",
            )
            button_clip_done.grid(row=1, column=2, padx=5, pady=5, sticky=tk.W)
            button_clip_Erace = ck.CTkButton(
                master=self.window_sub_ctrl4,
                text="範囲削除",
                command=self.event_clip_Erace,
                width=BtnWidth,
                height=BtnHeight,
                border_width=2,
                corner_radius=8,
                text_color="snow",
                border_color="snow",
                fg_color="#c7048c",
            )
            button_clip_Erace.grid(row=1, column=3, padx=5, pady=5, sticky=tk.W)
            label_run = ck.CTkLabel(
                master=self.window_sub_ctrl4,
                text="[編集確定]",
                width=LabelWidth,
                height=LabelHeight,
                corner_radius=8,
            )
            label_run.grid(row=2, column=1, columnspan=2, padx=5, pady=5, sticky=tk.W)
            # Save/Undoボタン生成
            button_Oversave = ck.CTkButton(
                master=self.window_sub_ctrl4,
                text="上書保存",
                command=self.event_Oversave,
                width=BtnWidth,
                height=BtnHeight,
                border_width=2,
                corner_radius=8,
                text_color="snow",
                border_color="snow",
                fg_color="#cf94ff",
            )
            button_Oversave.grid(row=3, column=1, padx=5, pady=5, sticky=tk.W)
            button_undo = ck.CTkButton(
                master=self.window_sub_ctrl4,
                text="編集取消",
                command=self.event_undo,
                width=BtnWidth,
                height=BtnHeight,
                border_width=2,
                corner_radius=8,
                text_color="snow",
                border_color="snow",
                fg_color="gray",
            )
            button_undo.grid(row=3, column=2, padx=5, pady=5, sticky=tk.W)
            button_save = ck.CTkButton(
                master=self.window_sub_ctrl4,
                text="別名保存",
                command=self.event_save,
                width=BtnWidth,
                height=BtnHeight,
                border_width=2,
                corner_radius=8,
                text_color="snow",
                border_color="snow",
                fg_color="hotpink1",
            )
            button_save.grid(row=3, column=3, padx=5, pady=5, sticky=tk.W)
            # label_Line = ck.CTkLabel(
            #     master=self.window_sub_ctrl2,
            #     text="[サブメニュー]",
            #     width=LabelWidth,
            #     height=LabelHeight,
            #     corner_radius=8,
            # )
            # label_Line.grid(row=4, column=1, columnspan=2, padx=5, pady=5, sticky=tk.W)
            # LineOCR起動ボタン生成
            button_LinOCR = ck.CTkButton(
                master=self.window_sub_ctrl4,
                text="OCR起動",
                command=self.LinOCROpen,
                width=BtnWidth,
                height=BtnHeight,
                border_width=2,
                corner_radius=8,
                text_color="snow",
                border_color="snow",
                fg_color="tomato",
            )
            button_LinOCR.grid(row=5, column=1, padx=5, pady=5, sticky=tk.W)
            # SubMenu起動ボタン生成
            # button_SubMenu = ck.CTkButton(
            #     master=self.window_sub_ctrl4,
            #     text="サブメニュー",
            #     command=self.event_menu,
            #     width=BtnWidth,
            #     height=BtnHeight,
            #     border_width=2,
            #     corner_radius=8,
            #     text_color="snow",
            #     border_color="snow",
            # )
            # button_SubMenu.grid(row=5, column=2, padx=5, pady=5, sticky=tk.W)
            # -------------------------------------------------------------------
            # Exposeイベントbind
            for event_type in tk.EventType.__members__.keys():
                if event_type == "Expose":
                    event_seq = "<" + event_type + ">"
                    try:
                        self.window_rootFrame.bind_all(event_seq, self.event_handler)
                        # print(event_type)
                    except tk.TclError:
                        # print("bind error:", event_type)
                        pass
            # -------------------------------------------------------------------
            self.control.model.stock_url = ""  # 一時保存URLをリセット
        except:
            self.logger.debug("要素作成失敗")  # Log出力

    # ----------------------------------------------------------------------------------
    def ckBtnSetting(self, btn):
        btn.configure(
            width=120, height=32, border_width=0, corner_radius=8, text_color="snow"
        )
        btn.configure(height=32)
        btn.configure(border_width=0)
        btn.configure(corner_radius=8)
        btn.configure(text_color="snow")

    # ----------------------------------------------------------------------------------
    def CanvasCreate(self):
        """
        キャンバス作成
        """
        try:
            # キャンバス
            self.window_sub_canvas = tk.Canvas(
                self.window_rootFrame, height=self.FCH, width=self.FCW, bg="gray"
            )
            # キャンバス内クリック開始イベントに関数バインド
            self.window_sub_canvas.bind("<ButtonPress-1>", self.event_clip_start)
            # キャンバス内ドラッグイベントに関数バインド
            self.window_sub_canvas.bind("<Button1-Motion>", self.event_clip_keep)
            # キャンバス内クリック終了イベントに関数バインド
            self.window_sub_canvas.bind("<ButtonRelease-1>", self.event_clip_end)
            # キャンバスを配置
            self.window_sub_canvas.pack(side=tk.TOP, fill="both", expand=True)
            self.control.SetCanvas(self.window_sub_canvas)  # キャンバスをセット
        except:
            self.logger.debug("キャンバス作成失敗")  # Log出力

    # ----------------------------------------------------------------------------------
    def FrameCreate(self, NWINSize):
        """
        Frame作成
        """
        try:
            # フォルダ・ファイル選択
            self.window_sub_ctrl1 = tk.Frame(
                self.window_rootFrame,
                height=300,
                width=300,
                bg="#60cad1",
                relief=tk.GROOVE,
                bd=1,
            )
            # 画像加工
            self.window_sub_ctrl2 = tk.Frame(
                self.window_rootFrame,
                height=300,
                width=300,
                bg="#60cad1",
                relief=tk.GROOVE,
                bd=1,
            )
            # 画像加工2
            self.window_sub_ctrl4 = tk.Frame(
                self.window_rootFrame,
                height=50,
                width=400,
                bg="#60cad1",
                relief=tk.GROOVE,
                bd=1,
            )
            self.FCW = int(int(NWINSize[0]) * 0.4)
            self.FCH = int(int(NWINSize[1]) * 0.4)
            self.window_sub_FrameCanvas = tk.Frame(
                self.window_rootFrame, height=self.FCH, width=self.FCW
            )
        except:
            self.logger.debug("Frame作成失敗")  # Log出力

    # ----------------------------------------------------------------------------------
    def MenuCreate(self):
        """
        メニューバー作成
        """
        try:
            self.window_root.config(bg="#60cad1")
            # メニューバー作成
            self.men = tk.Menu(self.window_root, tearoff=0)
            # メニューバーを画面にセット
            self.window_root.config(menu=self.men)
            # ファイルメニューを作成する
            self.menu_file = tk.Menu(self.men)
            self.men.add_command(label="ファイル", command=self.event_set_file)
            # 保存メニューを作成する
            self.savemenu = tk.Menu(self.window_root, tearoff=False)
            self.men.add_cascade(label="保存", menu=self.savemenu)
            self.savemenu.add_command(label="上書保存", command=self.event_save)
            self.savemenu.add_separator()  # 仕切り線
            self.savemenu.add_command(label="別名保存", command=self.event_Searchsave)

            # OCRメニューを作成する
            self.OCR_men = tk.Menu(self.men)
            self.men.add_command(label="OCR起動", command=self.LinOCROpen)
        except:
            self.logger.debug("メニューバー作成失敗")  # Log出力

    # ----------------------------------------------------------------------------------
    def FileDelete(self):
        """
        ファイル削除ボタンクリックイベント
        """
        self.logger.debug("FileDelete関数起動")  # Log出力
        F_u = self.entry_dir.get() + r"\\" + self.combo_file.get()
        msg = messagebox.askokcancel("確認", F_u + "を削除しますか？")
        if msg is True:
            os.remove(F_u)
            self.file_list = self.control.SetDirlist(self.dir_path)  # ファイルリストリロード
            self.combo_file.set("")
            self.str_dir.set(self.dir_path)
            self.file_list = self.control.SetDirlist(self.dir_path)
            self.combo_file.configure(values=self.file_list)
            self.control.DrawImage("set", set_pos=0)
        else:
            messagebox.showinfo("確認", "処理を中断します。")

    # ----------------------------------------------------------------------------------
    # イベントハンドラ
    def event_handler(self, event):
        """
        Exposeイベントに関数設定
        """
        print(sys._getframe().f_code.co_name)  # ターミナルへ表示
        for r in range(len(self.combo_file.values)):
            if self.combo_file.get() == self.combo_file.values[r]:
                set_pos = r
                break
        self.control.DrawImage("Map", set_pos=set_pos)

    # ----------------------------------------------------------------------------------
    def event_menu(self):
        """
        SubMenu起動ボタン関数
        """
        # menu作成######################################################################
        self.logger.debug("SubMenuOpen関数起動")  # Log出力
        # サブフレーム起動確認
        try:
            if self.menuwin.widgetName == "toplevel":
                SMW = True
            else:
                SMW = False
        except:
            SMW = False
        # -------------------------------------------------------------------------------
        if SMW is False:
            self.menuwin = tk.Toplevel()  # サブWindow作成
            self.menuwin.wm_attributes("-topmost", True)  # 常に一番上のウィンドウに指定
            self.menuwin.geometry("360x180+0+0")  # トップWindow表示位置指定
            # フレーム作成
            self.menuwinFrame = tk.Frame(self.menuwin, height=360, width=180)
            self.menuwinFrame.pack(fill=tk.BOTH, expand=True)
            # 　ラベル生成--------------------------------------------------------------------
            label_tb1 = ck.CTkLabel(
                master=self.menuwinFrame,
                text="[ノイズ除去値]",
                width=LabelWidth,
                height=LabelHeight,
                corner_radius=8,
            )
            label_tb1.grid(row=1, column=1, padx=5, pady=5, sticky=tk.W)
            # ------------------------------------------------------------------------------
            # 　テキストボックス生成---------------------------------------------------------
            textbox1 = tk.Entry(self.menuwinFrame, text="ノイズ除去値(奇数)", width=15)
            textbox1.grid(row=1, column=2, padx=5, pady=5, sticky=tk.W)
            # ------------------------------------------------------------------------------
            # 　ボタン生成------------------------------------------------------------------
            menubutton2 = tk.Button(
                self.menuwinFrame,
                text="ノイズ除去",
                width=20,
                command=lambda: self.menubutton2_click(textbox1),
            )
            menubutton2.grid(row=1, column=3, padx=5, pady=5, sticky=tk.W)

        # ##############################################################################

    # ----------------------------------------------------------------------------------
    def Resize(self, Resizewidth, Resizeheight):
        """
        リサイズ処理(未使用2022/08/08時点)
        """
        for r in range(len(self.combo_file.values)):
            if self.combo_file.get() == self.combo_file.values[r]:
                set_pos = r
                break
        self.logger.debug("Resize関数起動")  # Log出力
        try:
            ReList = [int(Resizewidth.get()), int(Resizeheight.get())]
            msg = messagebox.askokcancel("確認", "リサイズを行いますか？")
            if msg is True:
                SCM = self.control.MenuFuncRun("Resize", ReList, set_pos=set_pos)
                if SCM == "画像無":
                    messagebox.showinfo("確認", "画像を指定して下さい。")
                elif SCM == "Err":
                    messagebox.showinfo("確認", "編集中にエラーが発生しました。")
        except:
            self.logger.debug("Resize関数Err")  # Log出力

    # ----------------------------------------------------------------------------------
    def menubutton2_click(self, textbox1):
        """
        サブメニュー内ノイズ除去ボタン処理
        """
        for r in range(len(self.combo_file.values)):
            if self.combo_file.get() == self.combo_file.values[r]:
                set_pos = r
                break
        self.logger.debug("ノイズ除去関数起動")  # Log出力
        try:
            noisepar = int(textbox1.get())
            if noisepar % 2 == 0:
                msg = messagebox.showinfo("確認", "ノイズ除去値は奇数で入力してください。")
            else:
                msg = messagebox.askokcancel(
                    "確認", "ノイズ除去を除去値" + str(textbox1.get()) + "で適用しますか？"
                )
                if msg is True:
                    SCM = self.control.MenuFuncRun(
                        "Noise",
                        noisepar,
                        set_pos=set_pos,
                    )
                    if SCM == "画像無":
                        messagebox.showinfo("確認", "画像を指定して下さい。")
                    elif SCM == "Err":
                        self.logger.debug("ノイズ除去関数control側Err")  # Log出力
                        messagebox.showinfo("確認", "編集中にエラーが発生しました。")
        except:
            msg = messagebox.showinfo("確認", "ノイズ除去値を入力してください。")

    # ----------------------------------------------------------------------------------
    def button_LeftLotate(self, event=None):
        """
        左回転ボタン処理
        """
        self.logger.debug("左回転関数起動")  # Log出力
        self.event_Searchsave()  # 編集履歴判定後上書き
        cmd = "rotateFree-" + str(1)
        self.control.EditImage(cmd)

    # ----------------------------------------------------------------------------------
    def button_RightLotate(self, event=None):
        """
        右回転ボタン処理
        """
        self.logger.debug("右回転関数起動")  # Log出力
        self.event_Searchsave()  # 編集履歴判定後上書き
        cmd = "rotateFree-" + str(-1)
        self.control.EditImage(cmd)

    # ----------------------------------------------------------------------------------
    def event_set_folder(self):
        """
        フォルダー選択ボタンクリックイベント
        """
        print(sys._getframe().f_code.co_name)  # ターミナルへ表示
        self.logger.debug("フォルダー選択起動")  # Log出力
        self.event_Searchsave()  # 編集履歴判定後上書き
        self.dir_path = filedialog.askdirectory(
            initialdir=self.dir_path, mustexist=True
        )
        self.str_dir.set(self.dir_path)
        self.file_list = self.control.SetDirlist(self.dir_path)
        # self.combo_file["value"] = self.file_list
        self.combo_file.configure(values=self.file_list)
        self.logger.debug(self.dir_path + "_フォルダー選択完了")  # Log出力

    # ----------------------------------------------------------------------------------
    def event_set_file(self):
        """
        ファイル選択ボタンクリックイベント
        """
        print(sys._getframe().f_code.co_name)  # ターミナルへ表示
        self.logger.debug("ファイル選択起動")  # Log出力
        self.event_Searchsave()  # 編集履歴判定後上書き
        self.Selectfile_url = filedialog.askopenfilename(
            title="画像ファイルを開く", filetypes=[("PNG", ".png")], initialdir="./"
        )
        self.dir_path = os.path.dirname(self.Selectfile_url)
        FN = os.path.basename(self.Selectfile_url)
        self.str_dir.set(self.dir_path)
        self.file_list = self.control.SetDirlist(self.dir_path)

        if ".PDF" in FN or ".pdf" in FN:
            msg = messagebox.askokcancel(
                "確認", "PDFが選択されています。PNGに変換しますか？\n10ページ以上の処理は処理時間が長時間になる可能性があります。"
            )
            if msg is True:
                self.logger.debug("PNG変換起動")  # Log出力
                # プログレスバーの起動
                PBAR = PB.Open(tk.Toplevel())  # サブWindow作成
                spd = self.control.pdf_image(FN, "png", 300, PBAR)
                if spd is True:
                    f_r = 0
                    for f_l in self.file_list:
                        if f_l == FN:
                            set_pos = f_r
                            break
                        f_r += 1
                    msg = messagebox.askokcancel("確認", "PNG変換完了しました。")
                    self.control.DrawImage("set", set_pos=set_pos)
                    self.combo_file.set(self.file_list[set_pos])
                    self.logger.debug(FN + "_PNG変換完了起動")  # Log出力
                else:
                    f_r = 0
                    for f_l in self.file_list:
                        if f_l == FN:
                            set_pos = f_r
                            break
                        f_r += 1
                    msg = messagebox.askokcancel(
                        "確認", "PNG変換に失敗しました。指定DPIが高すぎる可能性があります。"
                    )
                    self.control.DrawImage("set", set_pos=set_pos)
                    self.combo_file.set(self.file_list[set_pos])
                    self.logger.debug(FN + "_PNG変換失敗起動")  # Log出力
        else:
            f_r = 0
            for f_l in self.file_list:
                if f_l == FN:
                    set_pos = f_r
                    break
                f_r += 1
            self.control.DrawImage("set", set_pos=set_pos)
            self.combo_file.set(self.file_list[set_pos])
            self.logger.debug(self.dir_path + "_ファイル選択完了")  # Log出力

    # ----------------------------------------------------------------------------------
    def event_updatefile(self, event):
        """
        ファイル選択ウィンドウクリックイベント
        """
        print(sys._getframe().f_code.co_name)  # ターミナルへ表示
        self.logger.debug("ファイル選択起動")  # Log出力
        self.event_Searchsave()  # 編集履歴判定後上書き
        self.file_list = self.control.SetDirlist(self.dir_path)
        self.combo_file.configure(values=self.file_list)
        self.event_selectfile(self)

    # ----------------------------------------------------------------------------------
    def event_selectfile(self, event):
        """
        ファイル選択後イベント
        """

        print(sys._getframe().f_code.co_name)  # ターミナルへ表示
        for r in range(len(self.combo_file.values)):
            if self.combo_file.get() == self.combo_file.values[r]:
                set_pos = r
                break
        FN = self.control.get_file("set", set_pos=set_pos)
        self.Selectfile_url = FN
        if ".PDF" in FN or ".pdf" in FN:
            msg = messagebox.askokcancel(
                "確認", "PDFが選択されています。PNGに変換しますか？\n10ページ以上の処理は処理時間が長時間になる可能性があります。"
            )
            if msg is True:
                self.logger.debug("PNG変換起動")  # Log出力
                # プログレスバーの起動
                PBAR = PB.Open(tk.Toplevel())  # サブWindow作成
                spd = self.control.pdf_image(FN, "png", 300, PBAR)
                if spd is True:
                    msg = messagebox.askokcancel("確認", "PNG変換完了しました。")
                    self.logger.debug(FN + "_PNG変換完了起動")  # Log出力
                else:
                    msg = messagebox.askokcancel(
                        "確認", "PNG変換に失敗しました。指定DPIが高すぎる可能性があります。"
                    )
                    self.logger.debug(FN + "_PNG変換失敗起動")  # Log出力
        else:
            self.control.DrawImage("set", set_pos=set_pos)
            self.logger.debug(FN + "_ファイル選択後イベント完了")  # Log出力

    # ----------------------------------------------------------------------------------
    def event_prev(self):
        """
        prevボタンクリックイベント
        """
        self.event_Searchsave()  # 編集履歴判定後上書き
        self.logger.debug("prev起動")  # Log出力
        print(sys._getframe().f_code.co_name)  # ターミナルへ表示
        pos = self.control.DrawImage("prev")
        self.combo_file.set(self.file_list[pos])

    # ----------------------------------------------------------------------------------
    def event_next(self):
        """
        nextボタンクリックイベント
        """
        self.event_Searchsave()  # 編集履歴判定後上書き
        self.logger.debug("next起動")  # Log出力
        print(sys._getframe().f_code.co_name)  # ターミナルへ表示
        pos = self.control.DrawImage("next")
        self.combo_file.set(self.file_list[pos])

    # ----------------------------------------------------------------------------------
    def event_rotate(self):
        """
        画像回転変更イベント
        """
        self.event_Searchsave()  # 編集履歴判定後上書き
        self.logger.debug("画像回転変更起動")  # Log出力
        val = self.radio_intvar1.get()
        cmd = "rotate-" + str(val)
        self.control.EditImage(cmd)
        print("{} {} {}".format(sys._getframe().f_code.co_name, val, cmd))

    # ----------------------------------------------------------------------------------
    def event_flip(self):
        """
        画像反転イベント
        """
        self.event_Searchsave()  # 編集履歴判定後上書き
        self.logger.debug("画像反転変更起動")  # Log出力
        val = self.radio_intvar2.get()
        cmd = "flip-" + str(val)
        self.control.EditImage(cmd)
        print("{} {} {}".format(sys._getframe().f_code.co_name, val, cmd))

    # ----------------------------------------------------------------------------------
    def event_clip_try(self):
        """
        Tryボタンイベント
        """
        print(sys._getframe().f_code.co_name)  # ターミナルへ表示
        self.logger.debug("Tryボタン起動")  # Log出力
        if self.control.model.stock_url != "":
            if messagebox.askokcancel("確認", "編集履歴が残っています。上書きしますか？"):
                os.remove(self.control.model.stock_url)
                self.control.model.stock_url = ""
            self.control.OverSaveImage()
            # self.event_selectfile(self)
        self.clip_enable = True

    # ----------------------------------------------------------------------------------
    def event_clip_done(self):
        """
        Doneボタンイベント
        """
        print(sys._getframe().f_code.co_name)  # ターミナルへ表示
        self.logger.debug("Doneボタン起動")  # Log出力
        if self.clip_enable:
            self.control.EditImage("clip_done")
            self.clip_enable = False

    # ----------------------------------------------------------------------------------
    def event_clip_Erace(self):
        """
        Eraceボタンイベント
        """
        print(sys._getframe().f_code.co_name)  # ターミナルへ表示
        self.logger.debug("Eraceボタン起動")  # Log出力
        if self.clip_enable:
            self.control.EditImage("clip_Erace")
            self.clip_enable = False

    # ----------------------------------------------------------------------------------
    def event_clip_start(self, event):
        """
        画像処理Saveイベント
        """
        print(sys._getframe().f_code.co_name, event.x, event.y)
        self.logger.debug("画像処理Save起動")  # Log出力
        if self.clip_enable:
            self.control.DrawRectangle("clip_start", event.y, event.x)

    # ----------------------------------------------------------------------------------
    def event_clip_keep(self, event):
        """
        画像処理Undoイベント
        """
        print(sys._getframe().f_code.co_name)  # ターミナルへ表示
        self.logger.debug("画像処理Undo起動")  # Log出力
        if self.control.model.stock_url != "":
            os.remove(self.control.model.stock_url)
            self.control.model.stock_url = ""
        if self.clip_enable:
            self.control.DrawRectangle("clip_keep", event.y, event.x)

    # ----------------------------------------------------------------------------------
    def event_clip_end(self, event):
        """
        キャンバス画像左クリック範囲指定で終端まで確定後
        """
        print(sys._getframe().f_code.co_name, event.x, event.y)
        self.logger.debug("画像範囲選択イベント完了")  # Log出力
        self.event_Searchsave()  # 編集履歴判定後上書き
        if self.clip_enable:
            self.control.DrawRectangle("clip_end", event.y, event.x)

    # ----------------------------------------------------------------------------------
    def event_save(self):
        """
        Saveボタンクリックイベント
        """
        print(sys._getframe().f_code.co_name)  # ターミナルへ表示
        try:
            print(self.Selectfile_url)
            if self.Selectfile_url != "":
                self.logger.debug("Saveボタン起動")  # Log出力
                # 一時保存ファイルを確認
                if self.control.model.stock_url != "":
                    os.remove(self.control.model.stock_url)
                self.Newfilename = filedialog.asksaveasfilename(
                    filetypes=[("PNG", ".png"), ("JPEG", ".jpg")]
                )
                self.control.SaveImage(self.Newfilename)
                self.file_list = self.control.SetDirlist(self.dir_path)  # ファイルリストリロード
                for F_r in range(len(self.file_list)):
                    if self.file_list[F_r] in self.Newfilename:
                        self.control.model.stock_url = ""
                        self.combo_file.set(self.file_list[F_r])
            else:
                messagebox.showinfo("確認", "画像ファイルが選択されていません。")
        except:
            messagebox.showinfo("確認", "画像ファイルが選択されていません。")

    # ----------------------------------------------------------------------------------
    def event_Searchsave(self):
        """
        編集履歴確認イベント
        """
        print(sys._getframe().f_code.co_name)  # ターミナルへ表示
        try:
            self.logger.debug("OverSaveボタン起動")  # Log出力
            # 一時保存ファイルを確認
            if self.control.model.stock_url != "":
                if messagebox.askokcancel("確認", "編集履歴が残っています。上書きしますか？"):
                    os.remove(self.control.model.stock_url)
                    self.control.model.stock_url = ""
                    self.control.OverSaveImage()
        except:
            messagebox.showinfo("確認", "編集履歴確認でエラーが起きました。")

    # ----------------------------------------------------------------------------------
    def event_Oversave(self):
        """
        上書保存ボタンクリックイベント
        """
        print(sys._getframe().f_code.co_name)  # ターミナルへ表示
        try:
            print(self.Selectfile_url)
            if self.Selectfile_url != "":
                self.logger.debug("ファイル削除起動")  # Log出力
                # 一時保存ファイルを確認
                if self.control.model.stock_url != "":
                    os.remove(self.control.model.stock_url)
                    self.control.model.stock_url = ""
                self.control.OverSaveImage()
            else:
                messagebox.showinfo("確認", "画像ファイルが選択されていません。")
        except:
            messagebox.showinfo("確認", "画像ファイルが選択されていません。")

    # ----------------------------------------------------------------------------------
    def event_undo(self):
        """
        Undoボタンクリックイベント
        """
        print(sys._getframe().f_code.co_name)  # ターミナルへ表示
        self.logger.debug("Undoボタンクリック起動")  # Log出力
        # 一時保存ファイルを確認
        if self.control.model.stock_url != "":
            os.remove(self.control.model.stock_url)
            self.control.model.stock_url = ""
        self.control.UndoImage("None")
        self.radio_intvar1.set(0)
        self.radio_intvar2.set(0)

    # ----------------------------------------------------------------------------------
    def LinOCROpen(self):
        """
        OCROpenボタンクリックイベント
        """
        print(sys._getframe().f_code.co_name)  # ターミナルへ表示
        self.logger.debug("OCR処理起動")  # Log出力
        self.event_Searchsave()  # 編集履歴判定後上書き
        FDir = self.entry_dir.get()
        FN = self.combo_file.get()
        Imgurl = FDir + r"\\" + FN
        Imgurl = Imgurl.replace("/", r"\\")
        if "[select file]" in Imgurl:
            messagebox.showinfo("確認", "画像ファイルを選択してください。")
        else:
            try:
                print(self.tomlPath)
                CSVSetMain(
                    main_window,
                    Imgurl,
                    self.tomlPath,
                    self.logger,
                    self.File_url_List,
                )
            except:
                self.tomlPath = self.tomlread()
                try:
                    CSVSetMain(
                        main_window,
                        Imgurl,
                        self.tomlPath,
                        self.logger,
                        self.File_url_List,
                    )
                    self.logger.debug("OCR処理完了")  # Log出力
                except:
                    self.logger.debug("OCR処理tomlファイル選択時Err")  # Log出力

    # ----------------------------------------------------------------------------------
    def tomlread(self):
        """
        tomlリード
        """
        try:
            r_toml = os.getcwd() + r"\OCRView\Setting.toml"
            return r_toml
        except:
            r_toml = os.getcwd() + r"\Setting.toml"
            return r_toml

    # ----------------------------------------------------------------------------------
    def click_close(self):
        """
        ウィンドウ×ボタンクリック
        """
        if messagebox.askokcancel("確認", "終了しますか？"):
            self.logger.debug("OCRViewClose完了")  # Log出力
            self.window_root.destroy()


# ------------------------------------------------------------------------------------
def onResize(e):
    # ※ 但し、textウィジェットのwidth,height は文字数指定な点に注意
    # 設定しているフォントサイズにより大きさは異なります。

    if e.widget is main_window:
        e.widget.config(width=e.width // 20, height=e.height // 20)


if __name__ == "__main__":
    OW.Open("OCR読取 Ver:0.9")
    # 　Tk MainWindow 生成
    main_window = tk.Tk()
    # Viewクラス生成
    ViewGUI(main_window, "OCR読取 Ver:0.9", "./")

    # 　フレームループ処理
    main_window.mainloop()
