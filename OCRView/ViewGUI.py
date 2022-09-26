import sys
import ProgressBar as PB
import tkinter as tk
import os
from tkinter import ttk, filedialog, messagebox

# from tkinter import ttk, filedialog
from ControlGUI import ControlGUI

# import TKINTERCV2Setting as TKCV2
from TKINTERCV2Setting import Main

# from tkinter import messagebox

# プログレスバーの起動
# PBAR = PB.ProgressBar(tk.Tk())

import logging.config
from platform import machine, node, platform, processor, release, system, version
from socket import gethostbyname, gethostname
from uuid import getnode

# exe化コマンド↓
# pyinstaller ViewGUI.py --onefile --onedir --noconsole --clean --icon=hasegawa.ico
# 上記コマンドでできた[dist]→[ViewGUI]フォルダ内に
# [poppler-22.01.0フォルダ]・[StraightListTate.csv]・[StraightListYoko.csv]・[key.json]
# をコピーして完了


class ViewGUI:
    """
    概要: TKinterメインWindowクラス
    """

    def __init__(self, window_root, default_path):
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
        global Sval  # スライダー初期値
        Sval = 0  # スライダー初期値
        # Controller Class生成
        self.control = ControlGUI(default_path)

        # 初期化
        self.dir_path = default_path
        self.file_list = ["..[select file]"]
        self.clip_enable = False

        # メインウィンドウ
        self.window_root = window_root
        # 　メインウィンドウサイズ指定
        self.window_root.geometry("1480x750")  # 横,縦
        NWINSize = ["1480", "750"]  # 横,縦
        # 　メインウィンドウタイトル
        self.window_root.title("OCR読取 Ver:0.9")
        self.window_root.protocol("WM_DELETE_WINDOW", self.click_close)  # 閉じる処理設定
        # self.window_root.bind("<Button-1>", self.ChangeWSize)
        # サブウィンドウ
        # フォルダ・ファイル選択
        self.window_sub_ctrl1 = tk.Frame(self.window_root, height=300, width=300)
        # 画像加工
        self.window_sub_ctrl2 = tk.Frame(self.window_root, height=300, width=300)
        # 画像加工2
        self.window_sub_ctrl4 = tk.Frame(self.window_root, height=50, width=400)
        # キャンバス
        FCW = int(int(NWINSize[0]) * 0.4)
        FCH = int(int(NWINSize[1]) * 0.4)
        self.window_sub_FrameCanvas = tk.Frame(self.window_root, height=FCH, width=FCW)
        self.window_sub_canvas = tk.Canvas(
            self.window_root, height=FCH, width=FCW, bg="gray"
        )

        # オブジェクト
        # StringVar(ストリング)生成
        self.str_dir = tk.StringVar()
        # IntVar生成
        self.radio_intvar1 = tk.IntVar()
        self.radio_intvar2 = tk.IntVar()

        # GUIウィジェット・イベント登録
        # ラベル
        label_target = tk.Label(self.window_sub_ctrl1, text="[ファイル]")
        label_rotate = tk.Label(self.window_sub_ctrl2, text="[画像回転]")
        label_flip = tk.Label(self.window_sub_ctrl2, text="[反転]")
        label_clip = tk.Label(self.window_sub_ctrl2, text="[トリミング・削除]")
        label_run = tk.Label(self.window_sub_ctrl4, text="[編集確定]")
        label_Line = tk.Label(self.window_sub_ctrl4, text="[サブメニュー]")

        # フォルダ選択ボタン生成
        self.button_setdir = tk.Button(
            self.window_sub_ctrl1,
            text="フォルダ選択",
            width=10,
            command=self.event_set_folder,
        )
        # 　テキストエントリ生成
        self.entry_dir = tk.Entry(
            self.window_sub_ctrl1, text="entry_dir", textvariable=self.str_dir, width=40
        )
        self.str_dir.set(self.dir_path)
        # コンボBOX生成
        self.combo_file = ttk.Combobox(
            self.window_sub_ctrl1,
            text="combo_file",
            value=self.file_list,
            state="readonly",
            width=30,
            postcommand=self.event_updatefile,
        )
        self.combo_file.set(self.file_list[0])
        self.combo_file.bind("<<ComboboxSelected>>", self.event_selectfile)
        # ファイル削除ボタン生成
        self.Delete_button = tk.Button(
            self.window_sub_ctrl1,
            text="ファイル削除",
            width=10,
            command=self.FileDelete,
        )
        # 　切替ボタン生成
        button_next = tk.Button(
            self.window_sub_ctrl1, text=">>次画像", width=10, command=self.event_next
        )
        button_prev = tk.Button(
            self.window_sub_ctrl1, text="前画像<<", width=10, command=self.event_prev
        )

        # クリップボタン生成
        button_clip_start = tk.Button(
            self.window_sub_ctrl2, text="選択開始", width=10, command=self.event_clip_try
        )
        button_clip_done = tk.Button(
            self.window_sub_ctrl2,
            text="範囲トリミング",
            width=10,
            command=self.event_clip_done,
        )
        button_clip_Erace = tk.Button(
            self.window_sub_ctrl2,
            text="範囲削除",
            width=10,
            command=self.event_clip_Erace,
        )

        # Save/Undoボタン生成
        button_Oversave = tk.Button(
            self.window_sub_ctrl4,
            text="上書保存",
            width=10,
            command=self.event_Oversave,
        )
        button_save = tk.Button(
            self.window_sub_ctrl4, text="別名保存", width=10, command=self.event_save
        )
        button_undo = tk.Button(
            self.window_sub_ctrl4, text="編集取消", width=10, command=self.event_undo
        )

        # LineOCR起動ボタン生成
        button_LinOCR = tk.Button(
            self.window_sub_ctrl4, text="OCR起動", width=10, command=self.LinOCROpen
        )

        # SubMenu起動ボタン生成
        button_SubMenu = tk.Button(
            self.window_sub_ctrl4, text="サブメニュー", width=10, command=self.event_menu
        )

        # ラジオボタン生成
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
                )
            )
        self.radio_intvar1.set(0)  # 0:No select

        radio_flip = []
        for val, text in enumerate(["U/D", "L/R"]):  # 1:Flip U/L 2:Flip L/R
            radio_flip.append(
                tk.Radiobutton(
                    self.window_sub_ctrl2,
                    text=text,
                    value=val + 1,
                    variable=self.radio_intvar2,
                    command=self.event_flip,
                )
            )
        self.radio_intvar2.set(0)  # 0:No select

        # 右回転ボタン生成
        button_RightLotate = tk.Button(
            self.window_sub_ctrl2,
            text="右回転",
            width=10,
            command=self.button_RightLotate,
        )
        # 左回転ボタン生成
        button_LeftLotate = tk.Button(
            self.window_sub_ctrl2,
            text="左回転",
            width=10,
            command=self.button_LeftLotate,
        )
        # ---------------------------------------------------------------

        # キャンバス内クリック開始イベントに関数バインド
        self.window_sub_canvas.bind("<ButtonPress-1>", self.event_clip_start)
        # キャンバス内ドラッグイベントに関数バインド
        self.window_sub_canvas.bind("<Button1-Motion>", self.event_clip_keep)
        # キャンバス内クリック終了イベントに関数バインド
        self.window_sub_canvas.bind("<ButtonRelease-1>", self.event_clip_end)

        # ウィジェット配置
        # キャンバスを配置
        self.window_sub_canvas.pack(side=tk.TOP, fill="both", expand=True)
        # フォルダー・ファイル選択を配置
        self.window_sub_ctrl1.pack(side=tk.LEFT, padx=100, fill="both", expand=True)
        # 画像編集1を配置
        self.window_sub_ctrl2.pack(side=tk.LEFT, padx=5, fill="both", expand=True)
        # 画像編集2を配置
        self.window_sub_ctrl4.pack(side=tk.LEFT, padx=5, fill="both", expand=True)
        # window_sub_ctrl1---------------------------------------------------
        self.button_setdir.grid(row=1, column=1, padx=5, pady=5, sticky=tk.W)
        button_prev.grid(row=1, column=2, padx=5, pady=5, sticky=tk.W)
        button_next.grid(row=1, column=3, padx=5, pady=5, sticky=tk.W)
        self.entry_dir.grid(row=2, column=1, columnspan=4, padx=5, pady=5, sticky=tk.W)
        label_target.grid(row=3, column=1, columnspan=4, padx=5, pady=5, sticky=tk.W)
        self.combo_file.grid(row=4, column=1, columnspan=4, padx=5, pady=5, sticky=tk.W)
        self.Delete_button.grid(row=5, column=1, padx=5, pady=5, sticky=tk.W)
        # -------------------------------------------------------------------
        # window_sub_ctrl2---------------------------------------------------
        label_rotate.grid(row=1, column=1, padx=5, pady=5, sticky=tk.W)
        radio_rotate[0].grid(row=2, column=1, padx=5, pady=5, sticky=tk.W)
        radio_rotate[1].grid(row=2, column=2, padx=5, pady=5, sticky=tk.W)
        radio_rotate[2].grid(row=2, column=3, padx=5, pady=5, sticky=tk.W)
        button_LeftLotate.grid(row=4, column=1, padx=5, pady=5, sticky=tk.W)
        button_RightLotate.grid(row=4, column=2, padx=5, pady=5, sticky=tk.W)
        label_flip.grid(row=5, column=1, padx=5, pady=5, sticky=tk.W)
        radio_flip[0].grid(row=6, column=1, padx=5, pady=5, sticky=tk.W)
        radio_flip[1].grid(row=6, column=2, padx=5, pady=5, sticky=tk.W)

        label_clip.grid(row=7, column=1, padx=5, pady=5, sticky=tk.W)
        button_clip_start.grid(row=8, column=1, padx=5, pady=5, sticky=tk.W)
        button_clip_done.grid(row=8, column=2, padx=5, pady=5, sticky=tk.W)
        button_clip_Erace.grid(row=8, column=3, padx=5, pady=5, sticky=tk.W)
        # -------------------------------------------------------------------
        # window_sub_ctrl4---------------------------------------------------
        label_run.grid(row=1, column=1, columnspan=2, padx=5, pady=5, sticky=tk.W)
        button_Oversave.grid(row=2, column=1, padx=5, pady=5, sticky=tk.W)
        button_undo.grid(row=2, column=2, padx=5, pady=5, sticky=tk.W)
        button_save.grid(row=2, column=3, padx=5, pady=5, sticky=tk.W)
        label_Line.grid(row=3, column=1, columnspan=2, padx=5, pady=5, sticky=tk.W)
        button_LinOCR.grid(row=4, column=1, padx=5, pady=5, sticky=tk.W)
        button_SubMenu.grid(row=4, column=2, padx=5, pady=5, sticky=tk.W)
        # -------------------------------------------------------------------
        # Exposeイベントbind
        for event_type in tk.EventType.__members__.keys():
            if event_type == "Expose":
                event_seq = "<" + event_type + ">"
                try:
                    self.window_root.bind_all(event_seq, self.event_handler)
                    # print(event_type)
                except tk.TclError:
                    # print("bind error:", event_type)
                    pass
        # -------------------------------------------------------------------
        self.control.SetCanvas(self.window_sub_canvas)  # キャンバスをセット
        self.control.model.stock_url = ""  # 一時保存URLをリセット
        self.logger.debug("ViewGUI起動完了")  # Log出力

    # Event Callback----------------------------------------------------------------------
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
            self.event_selectfile
        else:
            messagebox.showinfo("確認", "処理を中断します。")

    # イベントハンドラ
    def event_handler(self, event):
        """
        Exposeイベントに関数設定
        """
        # print(sys._getframe().f_code.co_name)  # ターミナルへ表示
        set_pos = self.combo_file.current()
        self.control.DrawImage("Map", set_pos=set_pos)

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
            # self.top.overrideredirect(True)  # ウィンドウのタイトル部分を消去
            self.menuwin.geometry("360x180+0+0")  # トップWindow表示位置指定
            # フレーム作成
            self.menuwinFrame = tk.Frame(self.menuwin, height=360, width=180)
            self.menuwinFrame.pack(fill=tk.BOTH, expand=True)
            # 　ラベル生成--------------------------------------------------------------------
            label_tb1 = tk.Label(self.menuwinFrame, text="[ノイズ除去値]")
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

    def Resize(self, Resizewidth, Resizeheight):
        """
        リサイズ処理(未使用2022/08/08時点)
        """
        set_pos = self.combo_file.current()
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

    def menubutton2_click(self, textbox1):
        """
        サブメニュー内ノイズ除去ボタン処理
        """
        set_pos = self.combo_file.current()
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

    def button_LeftLotate(self, event=None):
        """
        左回転ボタン処理
        """
        self.logger.debug("左回転関数起動")  # Log出力
        self.event_Searchsave()  # 編集履歴判定後上書き
        cmd = "rotateFree-" + str(1)
        self.control.EditImage(cmd)

    def button_RightLotate(self, event=None):
        """
        右回転ボタン処理
        """
        self.logger.debug("右回転関数起動")  # Log出力
        self.event_Searchsave()  # 編集履歴判定後上書き
        cmd = "rotateFree-" + str(-1)
        self.control.EditImage(cmd)

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
        self.combo_file["value"] = self.file_list
        self.logger.debug("フォルダー選択完了")  # Log出力

    def event_updatefile(self):
        """
        ファイル選択ウィンドウクリックイベント
        """
        print(sys._getframe().f_code.co_name)  # ターミナルへ表示
        self.logger.debug("ファイル選択起動")  # Log出力
        self.event_Searchsave()  # 編集履歴判定後上書き
        self.file_list = self.control.SetDirlist(self.dir_path)
        self.combo_file["value"] = self.file_list
        self.logger.debug("ファイル選択完了")  # Log出力

    def event_selectfile(self, event):
        """
        ファイル選択後イベント
        """

        print(sys._getframe().f_code.co_name)  # ターミナルへ表示
        set_pos = self.combo_file.current()
        FN = self.control.get_file("set", set_pos=set_pos)
        if ".PDF" in FN or ".pdf" in FN:
            msg = messagebox.askokcancel(
                "確認", "PDFが選択されています。PNGに変換しますか？\n10ページ以上の処理は処理時間が長時間になる可能性があります。"
            )
            if msg is True:
                self.logger.debug("PNG変換起動")  # Log出力
                # プログレスバーの起動
                PBAR = PB.Open(tk.Toplevel())  # サブWindow作成
                spd = self.control.pdf_image(FN, "png", 600, PBAR)
                if spd is True:
                    msg = messagebox.askokcancel("確認", "PNG変換完了しました。")
                    self.logger.debug("PNG変換完了起動")  # Log出力
                else:
                    msg = messagebox.askokcancel("確認", "PNG変換に失敗しました。")
                    self.logger.debug("PNG変換失敗起動")  # Log出力
        else:
            self.control.DrawImage("set", set_pos=set_pos)
            self.logger.debug("PNG変換起動")  # Log出力

    def event_prev(self):
        """
        prevボタンクリックイベント
        """
        self.event_Searchsave()  # 編集履歴判定後上書き
        self.logger.debug("prev起動")  # Log出力
        print(sys._getframe().f_code.co_name)  # ターミナルへ表示
        pos = self.control.DrawImage("prev")
        self.combo_file.set(self.file_list[pos])

    def event_next(self):
        """
        nextボタンクリックイベント
        """
        self.event_Searchsave()  # 編集履歴判定後上書き
        self.logger.debug("next起動")  # Log出力
        print(sys._getframe().f_code.co_name)  # ターミナルへ表示
        pos = self.control.DrawImage("next")
        self.combo_file.set(self.file_list[pos])

    def event_rotate(self):
        """
        画像回転変更イベント
        """
        self.event_Searchsave()  # 編集履歴判定後上書き
        val = self.radio_intvar1.get()
        cmd = "rotate-" + str(val)
        self.control.EditImage(cmd)
        print("{} {} {}".format(sys._getframe().f_code.co_name, val, cmd))

    def event_flip(self):
        """
        画像反転イベント
        """
        self.event_Searchsave()  # 編集履歴判定後上書き
        val = self.radio_intvar2.get()
        cmd = "flip-" + str(val)
        self.control.EditImage(cmd)
        print("{} {} {}".format(sys._getframe().f_code.co_name, val, cmd))

    def event_clip_try(self):
        """
        Tryボタンイベント
        """
        print(sys._getframe().f_code.co_name)  # ターミナルへ表示
        if self.control.model.stock_url != "":
            if messagebox.askokcancel("確認", "編集履歴が残っています。上書きしますか？"):
                os.remove(self.control.model.stock_url)
                self.control.model.stock_url = ""
            self.control.OverSaveImage()
        self.clip_enable = True

    def event_clip_done(self):
        """
        Doneボタンイベント
        """
        print(sys._getframe().f_code.co_name)  # ターミナルへ表示
        if self.clip_enable:
            self.control.EditImage("clip_done")
            self.clip_enable = False

    def event_clip_Erace(self):
        """
        Eraceボタンイベント
        """
        print(sys._getframe().f_code.co_name)  # ターミナルへ表示
        if self.clip_enable:
            self.control.EditImage("clip_Erace")
            self.clip_enable = False

    def event_clip_start(self, event):
        """
        画像処理Saveイベント
        """
        print(sys._getframe().f_code.co_name, event.x, event.y)
        if self.clip_enable:
            self.control.DrawRectangle("clip_start", event.y, event.x)

    def event_clip_keep(self, event):
        """
        画像処理Undoイベント
        """
        print(sys._getframe().f_code.co_name)  # ターミナルへ表示
        if self.control.model.stock_url != "":
            os.remove(self.control.model.stock_url)
            self.control.model.stock_url = ""
        if self.clip_enable:
            self.control.DrawRectangle("clip_keep", event.y, event.x)

    def event_clip_end(self, event):
        """
        キャンバス画像左クリック範囲指定で終端まで確定後
        """
        print(sys._getframe().f_code.co_name, event.x, event.y)
        self.event_Searchsave()  # 編集履歴判定後上書き
        if self.clip_enable:
            self.control.DrawRectangle("clip_end", event.y, event.x)

    def event_save(self):
        """
        Saveボタンクリックイベント
        """
        print(sys._getframe().f_code.co_name)  # ターミナルへ表示
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

    def event_Searchsave(self):
        """
        OverSaveボタンクリックイベント
        """
        print(sys._getframe().f_code.co_name)  # ターミナルへ表示
        # 一時保存ファイルを確認
        if self.control.model.stock_url != "":
            if messagebox.askokcancel("確認", "編集履歴が残っています。上書きしますか？"):
                os.remove(self.control.model.stock_url)
                self.control.model.stock_url = ""
                self.control.OverSaveImage()

    def event_Oversave(self):
        """
        OverSaveボタンクリックイベント
        """
        print(sys._getframe().f_code.co_name)  # ターミナルへ表示
        # 一時保存ファイルを確認
        if self.control.model.stock_url != "":
            os.remove(self.control.model.stock_url)
            self.control.model.stock_url = ""
        self.control.OverSaveImage()

    def event_undo(self):
        """
        Undoボタンクリックイベント
        """
        print(sys._getframe().f_code.co_name)  # ターミナルへ表示
        # 一時保存ファイルを確認
        if self.control.model.stock_url != "":
            os.remove(self.control.model.stock_url)
            self.control.model.stock_url = ""
        self.control.UndoImage("None")
        self.radio_intvar1.set(0)
        self.radio_intvar2.set(0)

    def LinOCROpen(self):
        """
        OCROpenボタンクリックイベント
        """
        print(sys._getframe().f_code.co_name)  # ターミナルへ表示
        self.event_Searchsave()  # 編集履歴判定後上書き
        FDir = self.entry_dir.get()
        FN = self.combo_file.get()
        Imgurl = FDir + r"\\" + FN
        Imgurl = Imgurl.replace("/", r"\\")
        if "[select file]" in Imgurl:
            messagebox.showinfo("確認", "画像ファイルを選択してください。")
        else:
            typ = [("tomlファイル", "*.toml")]
            messagebox.showinfo("確認", "次にOCR読取設定が格納されているtomlファイルを指定して下さい。")
            self.tomlPath = filedialog.askopenfilename(
                filetypes=typ, initialdir=self.dir_path
            )
            Main(main_window, Imgurl, self.tomlPath)

    def click_close(self):
        """
        ウィンドウ×ボタンクリック
        """
        if messagebox.askokcancel("確認", "終了しますか？"):
            self.window_root.destroy()

    # ------------------------------------------------------------------------------------


if __name__ == "__main__":

    # 　Tk MainWindow 生成
    main_window = tk.Tk()

    # Viewクラス生成
    ViewGUI(main_window, "./")

    # 　フレームループ処理
    main_window.mainloop()
