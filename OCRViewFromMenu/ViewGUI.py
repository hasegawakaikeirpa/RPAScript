import tkinter as tk
import customtkinter as ck
import FrameClass
import Functions
from tkinter import filedialog, messagebox
import ImageViewer
from functools import wraps
import logging.config
import os

# ロガー########################################################################################
logging.config.fileConfig(os.getcwd() + r"\LogConf\logging_debug.conf")
logger = logging.getLogger(__name__)
# デコレーター##################################################################################
def log_decorator():
    def _log_decorator(func):
        def wrapper(*args, **kwargs):
            try:
                logger.info("処理を開始します")
                return func(*args, **kwargs)

            except Exception as e:
                logger.error("エラーが発生しました")
                raise e

            finally:
                logger.info("処理を終了します")

        return wrapper

    return _log_decorator


# ###############################################################################################


class ViewGUI(tk.Toplevel):
    """
    概要: TKinterメインWindowクラス
    """

    def __init__(self, window_root, control):
        self.control = control
        self.window_root = FrameClass.Frame(
            window_root, f"{control.Toptitle}-画像編集-", self.control
        )
        # self.MenuCreate()
        self.FCW = int(self.window_root.width_of_window * 0.4)
        self.FCH = int(self.window_root.height_of_window * 0.4)
        self.FrameCreate()  # フレーム作成

    # 要素作成######################################################################################
    def FrameCreate(self):
        """
        Frame作成
        """
        try:
            # Frame = tk.Frame(
            #     self.window_root.window_rootFrame,
            #     bg="#60cad1",
            #     relief=tk.GROOVE,
            #     bd=1,
            #     height=self.FCH,
            #     width=self.FCW,
            # )

            # ImageViewer.call("", Frame)

            self.window_sub_FrameCanvas = ImageViewer.Application(
                tk.Frame(
                    master=self.window_root.window_rootFrame,
                    height=self.FCH,
                    width=self.FCW,
                )
            )
            self.window_sub_FrameCanvas.master.pack(
                side=tk.TOP, fill="both", expand=True
            )
            # フォルダ・ファイル選択
            self.window_sub_ctrl1 = self.SubFrame1()
            # 画像加工
            self.window_sub_ctrl2 = self.SubFrame2()
            self.window_sub_ctrl3 = self.SubFrame3()
            return
        except:
            return

    # ----------------------------------------------------------------------------------
    # def CanvasCreate(self):
    #     """
    #     キャンバス作成
    #     """
    #     try:
    #         # キャンバス
    #         self.window_sub_canvas = tk.Canvas(
    #             self.window_root.window_rootFrame,
    #             height=self.FCH,
    #             width=self.FCW,
    #             bg="gray",
    #         )
    #         # キャンバス内クリック開始イベントに関数バインド
    #         self.window_sub_canvas.bind("<ButtonPress-1>", Functions.event_clip_start)
    #         # キャンバス内ドラッグイベントに関数バインド
    #         self.window_sub_canvas.bind("<Button1-Motion>", Functions.event_clip_keep)
    #         # キャンバス内クリック終了イベントに関数バインド
    #         self.window_sub_canvas.bind("<ButtonRelease-1>", Functions.event_clip_end)
    #         # キャンバスを配置
    #         self.window_sub_canvas.pack(side=tk.TOP, fill="both", expand=True)
    #         self.control.SetCanvas(self.window_sub_canvas)  # キャンバスをセット
    #     except:
    #         self.control.logger.debug("キャンバス作成失敗")  # Log出力

    # ------------------------------------------------------------------------------------
    def SubFrame1(self):
        """
        フレーム1作成
        """
        BtnWidth, BtnHeight = 50, 50
        EntWidth, EntHeight = 50, 50
        LabelWidth, LabelHeight = 50, 50
        self.str_dir = tk.StringVar()
        # IntVar生成
        self.radio_intvar1 = tk.IntVar()
        self.radio_intvar2 = tk.IntVar()

        Frame = tk.Frame(
            self.window_root.window_rootFrame,
            height=300,
            width=300,
            bg="#60cad1",
            relief=tk.GROOVE,
            bd=1,
        )
        # フォルダー・ファイル選択を配置
        Frame.pack(side=tk.LEFT, padx=5, fill=tk.BOTH, expand=True)
        # フォルダ選択ボタン生成
        self.button_setdir = ck.CTkButton(
            master=Frame,
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
        self.button_setdir.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W + tk.E)
        self.button_prev = ck.CTkButton(
            master=Frame,
            text="前画像<<",
            command=Functions.event_prev,
            width=BtnWidth,
            height=BtnHeight,
            border_width=2,
            corner_radius=8,
            text_color="snow",
            border_color="snow",
        )
        self.button_prev.grid(row=0, column=1, padx=5, pady=5, sticky=tk.W + tk.E)
        # 切替ボタン生成
        self.button_next = ck.CTkButton(
            master=Frame,
            text=">>次画像",
            command=Functions.event_next,
            width=BtnWidth,
            height=BtnHeight,
            border_width=2,
            corner_radius=8,
            text_color="snow",
            border_color="snow",
        )
        self.button_next.grid(row=0, column=2, padx=5, pady=5, sticky=tk.W + tk.E)
        # 　テキストエントリ生成
        self.entry_dir = ck.CTkEntry(
            master=Frame,
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
            row=1, column=0, columnspan=3, padx=5, pady=5, sticky=tk.W + tk.E
        )
        # ラベル
        self.label_target = ck.CTkLabel(
            master=Frame,
            text="[ファイル]",
            width=LabelWidth,
            height=LabelHeight,
            corner_radius=8,
        )
        self.label_target.grid(
            row=2, column=0, columnspan=3, padx=5, pady=5, sticky=tk.W
        )
        # コンボBOX生成
        self.combo_file = ck.CTkComboBox(
            master=Frame,
            # text="combo_file",
            # value=self.file_list,
            values=self.control.file_list,
            state="readonly",
            width=EntWidth,
            command=Functions.event_updatefile,
        )
        self.combo_file.set(self.control.file_list[0])
        self.combo_file.grid(
            row=3, column=0, columnspan=3, padx=5, pady=5, sticky=tk.W + tk.E
        )

    # ------------------------------------------------------------------------------------
    def SubFrame2(self):
        """
        フレーム2作成
        """
        BtnWidth, BtnHeight = 50, 50
        EntWidth, EntHeight = 50, 50
        LabelWidth, LabelHeight = 50, 50
        Frame = tk.Frame(
            self.window_root.window_rootFrame,
            height=300,
            width=300,
            bg="#60cad1",
            relief=tk.GROOVE,
            bd=1,
        )
        Frame.pack(side=tk.LEFT, padx=5, fill=tk.BOTH, expand=True)
        self.label_rotate = ck.CTkLabel(
            master=Frame,
            text="[画像回転]",
            width=LabelWidth,
            height=LabelHeight,
            corner_radius=8,
        )
        self.label_rotate.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        # 回転角度ラジオボックス生成
        self.radio_intvar1 = tk.IntVar()
        self.radio_intvar2 = tk.IntVar()
        self.radio_intvar1.set(0)  # 0:No select
        self.radio_intvar2.set(0)  # 0:No select
        self.radio_rotate = []
        for val, text in enumerate(
            ["90°", "180°", "270°"]
        ):  # 1:rot90 2:rot180 3:rot270
            self.radio_rotate.append(
                tk.Radiobutton(
                    Frame,
                    text=text,
                    value=val + 1,
                    variable=self.radio_intvar1,
                    command=Functions.event_rotate,
                    bg="#60cad1",
                )
            )
        self.radio_rotate[0].grid(row=1, column=0, padx=5, pady=5, sticky=tk.W + tk.E)
        self.radio_rotate[1].grid(row=1, column=1, padx=5, pady=5, sticky=tk.W + tk.E)
        self.radio_rotate[2].grid(row=1, column=2, padx=5, pady=5, sticky=tk.W + tk.E)

        self.label_flip = ck.CTkLabel(
            master=Frame,
            text="[反転]",
            width=LabelWidth,
            height=LabelHeight,
            corner_radius=8,
        )
        self.label_flip.grid(row=3, column=0, padx=5, pady=5, sticky=tk.W)
        self.radio_flip = []
        for val, text in enumerate(["U/D", "L/R"]):  # 1:Flip U/L 2:Flip L/R
            self.radio_flip.append(
                tk.Radiobutton(
                    Frame,
                    text=text,
                    value=val + 1,
                    variable=self.radio_intvar2,
                    command=Functions.event_flip,
                    bg="#60cad1",
                )
            )
        self.radio_flip[0].grid(row=4, column=0, padx=5, pady=5, sticky=tk.W + tk.E)
        self.radio_flip[1].grid(row=4, column=1, padx=5, pady=5, sticky=tk.W + tk.E)

    # ------------------------------------------------------------------------------------
    def SubFrame3(self):
        """
        フレーム2作成
        """
        BtnWidth, BtnHeight = 50, 50
        EntWidth, EntHeight = 50, 50
        LabelWidth, LabelHeight = 50, 50
        Frame = tk.Frame(
            self.window_root.window_rootFrame,
            height=300,
            width=300,
            bg="#60cad1",
            relief=tk.GROOVE,
            bd=1,
        )
        Frame.pack(side=tk.LEFT, padx=5, fill=tk.BOTH, expand=True)
        self.label_clip = ck.CTkLabel(
            master=Frame,
            text="[トリミング・削除]",
            width=LabelWidth,
            height=LabelHeight,
            corner_radius=8,
        )
        self.label_clip.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        # クリップボタン生成
        self.button_clip_start = ck.CTkButton(
            master=Frame,
            text="選択開始",
            command=Functions.event_clip_try,
            width=BtnWidth,
            height=BtnHeight,
            border_width=2,
            corner_radius=8,
            text_color="snow",
            border_color="snow",
            fg_color="#7eb000",
        )
        self.button_clip_start.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W + tk.E)
        self.button_clip_done = ck.CTkButton(
            master=Frame,
            text="範囲トリミング",
            command=Functions.event_clip_done,
            width=BtnWidth,
            height=BtnHeight,
            border_width=2,
            corner_radius=8,
            text_color="snow",
            border_color="snow",
            fg_color="#6100b0",
        )
        self.button_clip_done.grid(row=1, column=1, padx=5, pady=5, sticky=tk.W + tk.E)
        self.button_clip_Erace = ck.CTkButton(
            master=Frame,
            text="範囲削除",
            command=Functions.event_clip_Erace,
            width=BtnWidth,
            height=BtnHeight,
            border_width=2,
            corner_radius=8,
            text_color="snow",
            border_color="snow",
            fg_color="#c7048c",
        )
        self.button_clip_Erace.grid(row=1, column=2, padx=5, pady=5, sticky=tk.W + tk.E)
        self.label_run = ck.CTkLabel(
            master=Frame,
            text="[編集確定]",
            width=LabelWidth,
            height=LabelHeight,
            corner_radius=8,
        )
        self.label_run.grid(row=2, column=0, columnspan=2, padx=5, pady=5, sticky=tk.W)
        # Save/Undoボタン生成
        self.button_Oversave = ck.CTkButton(
            master=Frame,
            text="上書保存",
            command=Functions.event_Oversave,
            width=BtnWidth,
            height=BtnHeight,
            border_width=2,
            corner_radius=8,
            text_color="snow",
            border_color="snow",
            fg_color="#cf94ff",
        )
        self.button_Oversave.grid(row=3, column=0, padx=5, pady=5, sticky=tk.W + tk.E)
        self.button_undo = ck.CTkButton(
            master=Frame,
            text="編集取消",
            command=Functions.event_undo,
            width=BtnWidth,
            height=BtnHeight,
            border_width=2,
            corner_radius=8,
            text_color="snow",
            border_color="snow",
            fg_color="gray",
        )
        self.button_undo.grid(row=3, column=1, padx=5, pady=5, sticky=tk.W + tk.E)
        self.button_save = ck.CTkButton(
            master=Frame,
            text="別名保存",
            command=Functions.event_save,
            width=BtnWidth,
            height=BtnHeight,
            border_width=2,
            corner_radius=8,
            text_color="snow",
            border_color="snow",
            fg_color="hotpink1",
        )
        self.button_save.grid(row=3, column=2, padx=5, pady=5, sticky=tk.W + tk.E)
        # LineOCR起動ボタン生成
        self.button_LinOCR = ck.CTkButton(
            master=Frame,
            text="OCR起動",
            # command=self.LinOCROpen,
            width=BtnWidth,
            height=BtnHeight,
            border_width=2,
            corner_radius=8,
            text_color="snow",
            border_color="snow",
            fg_color="tomato",
        )
        self.button_LinOCR.grid(row=4, column=0, padx=5, pady=5, sticky=tk.W + tk.E)
        # # Exposeイベントbind
        # for event_type in EventType.__members__.keys():
        #     if event_type == "Expose":
        #         event_seq = "<" + event_type + ">"
        #         try:
        #             self.window_root.window_rootFrame.bind_all(
        #                 event_seq, self.event_handler
        #             )
        #             # print(event_type)
        #         except TclError:
        #             # print("bind error:", event_type)
        #             pass
        # -------------------------------------------------------------------

    # ボタンクリックイベント#######################################################################
    def event_set_folder(self):
        """
        フォルダ選択ボタンクリックイベント
        """
        self.control.dir_path = filedialog.askdirectory(
            title="関与先フォルダを開く",
            initialdir=r"C:\Users\もちねこ\Desktop\GitHub\RPAScript\OCRView\CompanyData\1869",
        )
        self.control.Kanyosaki_name = os.path.basename(self.control.dir_path)
        self.Dir.insert(0, self.control.dir_path)
        self.control.file_list = self.control.SetDirlist(self.control.dir_path)

    # ----------------------------------------------------------------------------------
    def event_save(self):
        """
        Saveボタンクリックイベント
        """
        try:
            if self.control.Kanyosaki_name != "":
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

    # #######################################################################################


def Open():
    import ControlGUI
    import logging.config
    import os

    logging.config.fileConfig(os.getcwd() + r"\LogConf\logging_debug.conf")
    logger = logging.getLogger(__name__)
    control = ControlGUI.ControlGUI("./", logger)  # セルフコントローラー
    main_window = tk.Tk()
    top = tk.Toplevel()
    ViewGUI(top, control)
    main_window.mainloop()


if __name__ == "__main__":
    Open()
