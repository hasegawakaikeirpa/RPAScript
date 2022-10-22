import tkinter as tk
import FrameClass
import ViewGUI_obj as V_obj


class ViewGUI(tk.Toplevel):
    """
    概要: TKinterメインWindowクラス
    """

    def __init__(self, window_root, Control):
        self.window_root = FrameClass.Frame(window_root, f"{Control.Toptitle}-画像編集-")
        # self.MenuCreate()
        self.FrameCreate()  # フレーム作成
        V_obj.ElementCreate(self)  # Element作成

    # 要素作成######################################################################################
    # def MenuCreate(self):
    #     """
    #     メニューバー作成
    #     """
    #     try:
    #         self.window_root.config(bg="#60cad1")
    #         # メニューバー作成
    #         self.men = tk.Menu(self.window_root, tearoff=0)
    #         # メニューバーを画面にセット
    #         self.window_root.config(menu=self.men)
    #         # ファイルメニューを作成する
    #         self.menu_file = tk.Menu(self.men)
    #         self.men.add_command(label="ファイル", command=self.event_set_file)
    #         # 保存メニューを作成する
    #         self.savemenu = tk.Menu(self.window_root, tearoff=False)
    #         self.men.add_cascade(label="保存", menu=self.savemenu)
    #         self.savemenu.add_command(label="上書保存", command=self.event_save)
    #         self.savemenu.add_separator()  # 仕切り線
    #         self.savemenu.add_command(label="別名保存", command=self.event_Searchsave)

    #         # OCRメニューを作成する
    #         self.OCR_men = tk.Menu(self.men)
    #         self.men.add_command(label="OCR起動", command=self.LinOCROpen)
    #     except:
    #         self.logger.debug("メニューバー作成失敗")  # Log出力

    # ----------------------------------------------------------------------------------
    def FrameCreate(self):
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
            self.FCW = int(self.width_of_window * 0.4)
            self.FCH = int(self.height_of_window * 0.4)
            self.window_sub_FrameCanvas = tk.Frame(
                self.window_rootFrame, height=self.FCH, width=self.FCW
            )
        except:
            self.logger.debug("Frame作成失敗")  # Log出力

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


# ------------------------------------------------------------------------------------
