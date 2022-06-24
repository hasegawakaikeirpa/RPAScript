import sys
import tkinter as tk
from tkinter import ttk, filedialog
from ControlGUI import ControlGUI
import TKINTERCV2Setting as TKCV2
from tkinter import messagebox


class ViewGUI:
    def __init__(self, window_root, default_path):
        # Controller Class生成
        self.control = ControlGUI(default_path)

        # 初期化
        self.dir_path = default_path
        self.file_list = ["..[select file]"]
        self.clip_enable = False

        # メインウィンドウ
        self.window_root = window_root
        # 　メインウィンドウサイズ指定
        self.window_root.geometry("800x600")  # 縦,横
        NWINSize = ["800", "600"]  # 縦,横
        # 　メインウィンドウタイトル
        self.window_root.title("GUI Image Editor v0.90")
        # self.window_root.bind("<Button-1>", self.ChangeWSize)
        # サブウィンドウ
        # フォルダ・ファイル選択
        self.window_sub_ctrl1 = tk.Frame(self.window_root, height=300, width=300)
        # 画像加工
        self.window_sub_ctrl2 = tk.Frame(self.window_root, height=300, width=300)
        # プレビュー
        self.window_sub_ctrl3 = tk.Frame(self.window_root, height=50, width=400)
        # 画像加工2
        self.window_sub_ctrl4 = tk.Frame(self.window_root, height=50, width=400)
        # キャンバス
        FCH = int(int(NWINSize[0]) * 0.4)
        FCW = int(int(NWINSize[1]) * 0.4)
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
        label_s2_blk1 = tk.Label(self.window_sub_ctrl2, text="")
        label_s3_blk1 = tk.Label(self.window_sub_ctrl3, text="")
        label_s3_blk2 = tk.Label(self.window_sub_ctrl3, text="")
        label_target = tk.Label(self.window_sub_ctrl1, text="[Files]")
        label_rotate = tk.Label(self.window_sub_ctrl2, text="[Rotate]")
        label_flip = tk.Label(self.window_sub_ctrl2, text="[Flip]")
        label_clip = tk.Label(self.window_sub_ctrl2, text="[Clip]")
        label_run = tk.Label(self.window_sub_ctrl4, text="[Final Edit]")
        label_Line = tk.Label(self.window_sub_ctrl4, text="[Line Edit]")

        # フォルダ選択ボタン生成
        self.button_setdir = tk.Button(
            self.window_sub_ctrl1,
            text="Set Folder",
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

        # 　切替ボタン生成
        button_next = tk.Button(
            self.window_sub_ctrl3, text=">>Next", width=10, command=self.event_next
        )
        button_prev = tk.Button(
            self.window_sub_ctrl3, text="Prev<<", width=10, command=self.event_prev
        )

        # クリップボタン生成
        button_clip_start = tk.Button(
            self.window_sub_ctrl2, text="Try", width=5, command=self.event_clip_try
        )
        button_clip_done = tk.Button(
            self.window_sub_ctrl2, text="Done", width=5, command=self.event_clip_done
        )

        # Save/Undoボタン生成
        button_Oversave = tk.Button(
            self.window_sub_ctrl4,
            text="OverSave",
            width=10,
            command=self.event_Oversave,
        )
        button_save = tk.Button(
            self.window_sub_ctrl4, text="Save", width=5, command=self.event_save
        )
        button_undo = tk.Button(
            self.window_sub_ctrl4, text="Undo", width=5, command=self.event_undo
        )

        # LineOCR起動ボタン生成
        button_LinOCR = tk.Button(
            self.window_sub_ctrl4, text="LinOCR_Open", width=10, command=self.LinOCROpen
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
        # キャンバス内クリック開始イベントに関数バインド
        self.window_sub_canvas.bind("<ButtonPress-1>", self.event_clip_start)
        # キャンバス内ドラッグイベントに関数バインド
        self.window_sub_canvas.bind("<Button1-Motion>", self.event_clip_keep)
        # キャンバス内クリック終了イベントに関数バインド
        self.window_sub_canvas.bind("<ButtonRelease-1>", self.event_clip_end)

        # ウィジェット配置
        # キャンバスを配置
        self.window_sub_canvas.pack(side=tk.TOP, fill="both", expand=True)
        # プレビューを配置
        self.window_sub_ctrl3.pack(side=tk.LEFT, fill="both", expand=True)
        # フォルダー・ファイル選択を配置
        self.window_sub_ctrl1.pack(side=tk.LEFT, fill="both", expand=True)
        # 画像編集1を配置
        self.window_sub_ctrl2.pack(side=tk.LEFT, fill="both", expand=True)
        # 画像編集2を配置
        self.window_sub_ctrl4.pack(side=tk.LEFT, fill="both", expand=True)
        # window_sub_ctrl1---------------------------------------------------
        self.button_setdir.grid(row=1, column=1, padx=5, pady=5, sticky=tk.W)
        self.entry_dir.grid(row=2, column=1, padx=5, pady=5, sticky=tk.W)
        label_target.grid(row=3, column=1, padx=5, pady=5, sticky=tk.W)
        self.combo_file.grid(row=4, column=1, padx=5, pady=5, sticky=tk.W)
        # -------------------------------------------------------------------
        # window_sub_ctrl2---------------------------------------------------
        label_s2_blk1.grid(row=1, column=1, padx=5, pady=5, sticky=tk.W)
        label_rotate.grid(row=1, column=1, padx=5, pady=5, sticky=tk.W)
        radio_rotate[0].grid(row=2, column=1, padx=5, pady=5, sticky=tk.W)
        radio_rotate[1].grid(row=2, column=2, padx=5, pady=5, sticky=tk.W)
        radio_rotate[2].grid(row=2, column=3, padx=5, pady=5, sticky=tk.W)

        label_flip.grid(row=3, column=1, padx=5, pady=5, sticky=tk.W)
        radio_flip[0].grid(row=4, column=1, padx=5, pady=5, sticky=tk.W)
        radio_flip[1].grid(row=4, column=2, padx=5, pady=5, sticky=tk.W)

        label_clip.grid(row=5, column=1, padx=5, pady=5, sticky=tk.W)
        button_clip_start.grid(row=6, column=1, padx=5, pady=5, sticky=tk.W)
        button_clip_done.grid(row=6, column=2, padx=5, pady=5, sticky=tk.W)
        label_run.grid(row=7, column=1, columnspan=2, padx=5, pady=5, sticky=tk.W)
        # -------------------------------------------------------------------
        # window_sub_ctrl4---------------------------------------------------
        button_Oversave.grid(row=1, column=1, padx=5, pady=5, sticky=tk.W)
        button_undo.grid(row=1, column=2, padx=5, pady=5, sticky=tk.W)
        button_save.grid(row=1, column=3, padx=5, pady=5, sticky=tk.W)
        label_Line.grid(row=2, column=1, columnspan=2, padx=5, pady=5, sticky=tk.W)
        button_LinOCR.grid(row=3, column=1, padx=5, pady=5, sticky=tk.W)
        # -------------------------------------------------------------------
        # window_sub_ctrl3---------------------------------------------------
        label_s3_blk1.grid(row=1, column=1, columnspan=2, padx=5, pady=5, sticky=tk.EW)
        button_prev.grid(row=1, column=3, padx=5, pady=5, sticky=tk.E)
        label_s3_blk2.grid(row=1, column=4, columnspan=2, padx=5, pady=5, sticky=tk.EW)
        button_next.grid(row=1, column=6, padx=5, pady=5, sticky=tk.W)
        # -------------------------------------------------------------------
        self.control.SetCanvas(self.window_sub_canvas)  # キャンバスをセット

    # Event Callback----------------------------------------------------------------------
    def event_set_folder(self):
        """
        フォルダー選択ボタンクリックイベント
        """
        print(sys._getframe().f_code.co_name)  # ターミナルへ表示
        self.dir_path = filedialog.askdirectory(
            initialdir=self.dir_path, mustexist=True
        )
        self.str_dir.set(self.dir_path)
        self.file_list = self.control.SetDirlist(self.dir_path)
        self.combo_file["value"] = self.file_list

    def event_updatefile(self):
        """
        ファイル選択ウィンドウクリックイベント
        """
        print(sys._getframe().f_code.co_name)  # ターミナルへ表示
        self.file_list = self.control.SetDirlist(self.dir_path)
        self.combo_file["value"] = self.file_list

    def event_selectfile(self, event):
        """
        ファイル選択後イベント
        """

        print(sys._getframe().f_code.co_name)  # ターミナルへ表示
        set_pos = self.combo_file.current()
        self.control.DrawImage("set", set_pos=set_pos)

    def event_prev(self):
        """
        prevボタンクリックイベント
        """
        print(sys._getframe().f_code.co_name)  # ターミナルへ表示
        pos = self.control.DrawImage("prev")
        self.combo_file.set(self.file_list[pos])

    def event_next(self):
        """
        nextボタンクリックイベント
        """
        print(sys._getframe().f_code.co_name)  # ターミナルへ表示
        pos = self.control.DrawImage("next")
        self.combo_file.set(self.file_list[pos])

    def event_rotate(self):
        """
        画像回転変更イベント
        """
        val = self.radio_intvar1.get()
        cmd = "rotate-" + str(val)
        self.control.EditImage(cmd)
        print("{} {} {}".format(sys._getframe().f_code.co_name, val, cmd))

    def event_flip(self):
        """
        画像反転イベント
        """
        val = self.radio_intvar2.get()
        cmd = "flip-" + str(val)
        self.control.EditImage(cmd)
        print("{} {} {}".format(sys._getframe().f_code.co_name, val, cmd))

    def event_clip_try(self):
        """
        Tryボタンイベント
        """
        print(sys._getframe().f_code.co_name)  # ターミナルへ表示
        self.clip_enable = True

    def event_clip_done(self):
        """
        Doneボタンイベント
        """
        print(sys._getframe().f_code.co_name)  # ターミナルへ表示
        if self.clip_enable:
            self.control.EditImage("clip_done")
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
        if self.clip_enable:
            self.control.DrawRectangle("clip_keep", event.y, event.x)

    def event_clip_end(self, event):
        """
        キャンバス画像左クリック範囲指定で終端まで確定後
        """
        print(sys._getframe().f_code.co_name, event.x, event.y)
        if self.clip_enable:
            self.control.DrawRectangle("clip_end", event.y, event.x)

    def event_save(self):
        """
        Saveボタンクリックイベント
        """
        print(sys._getframe().f_code.co_name)  # ターミナルへ表示
        self.control.SaveImage()

    def event_Oversave(self):
        """
        OverSaveボタンクリックイベント
        """
        print(sys._getframe().f_code.co_name)  # ターミナルへ表示
        self.control.OverSaveImage()

    def event_undo(self):
        """
        Undoボタンクリックイベント
        """
        print(sys._getframe().f_code.co_name)  # ターミナルへ表示
        self.control.UndoImage("None")
        self.radio_intvar1.set(0)
        self.radio_intvar2.set(0)

    def LinOCROpen(self):
        """
        OCROpenボタンクリックイベント
        """
        print(sys._getframe().f_code.co_name)  # ターミナルへ表示
        FDir = self.entry_dir.get()
        FN = self.combo_file.get()
        Imgurl = FDir + r"\\" + FN
        if "[select file]" in Imgurl:
            messagebox.showinfo("確認", "画像ファイルを選択してください。")
        else:
            TKCV2.Main(Imgurl)

    # ------------------------------------------------------------------------------------


if __name__ == "__main__":

    # 　Tk MainWindow 生成
    main_window = tk.Tk()

    # Viewクラス生成
    ViewGUI(main_window, "./")

    # 　フレームループ処理
    main_window.mainloop()
