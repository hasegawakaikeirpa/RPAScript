from tkinter import filedialog, messagebox
import tkinter as tk
import os
import numpy as np
from chardet.universaldetector import UniversalDetector

# -----------------------------------------------------------------------------------
def getFileEncoding(file_path):  # .format( getFileEncoding( "sjis.csv" ) )
    if os.path.isfile(file_path) is True:
        detector = UniversalDetector()
        with open(file_path, mode="rb") as f:
            for binary in f:
                detector.feed(binary)
                if detector.done:
                    break
        detector.close()
        return detector.result["encoding"]
    else:
        messagebox.showinfo("確認", file_path + "\nが存在しません。")
        return ""


# -----------------------------------------------------------------------------------
def blankno(List):
    if len() != 0:
        TN_List = [int(str(t[0][0]).replace("Line", "")) for t in List]
        TN_List.sort()
        N_TN_r = 0
        for TN_r in TN_List:
            if N_TN_r == 0:
                N_TN_r = TN_r + 1
            else:
                if N_TN_r == TN_r:
                    N_TN_r = TN_r + 1
                else:
                    return N_TN_r
        N_TN_r = TN_r + 1
        return N_TN_r
    else:
        return 1


# ----------------------------------------------------------------------------------
def event_set_folder(self):
    """
    フォルダ選択ボタンクリックイベント
    """
    self.control.dir_path = filedialog.askdirectory(
        title="関与先フォルダを開く",
        initialdir=r"C:\Users\もちねこ\Desktop\GitHub\RPAScript\OCRView\CompanyData\1869",
    )
    self.control.Kanyosaki_name = os.path.basename(self.control.dir_path)
    self.entry_dir.insert(0, self.control.dir_path)
    self.control.file_list = self.control.SetDirlist(self.control.dir_path)
    self.combo_file.configure(values=self.control.file_list)


# ----------------------------------------------------------------------------------
def event_set_file(self):
    """
    ファイル選択ボタンクリックイベント
    """
    # event_Searchsave(self)  # 編集履歴判定後上書き
    self.control = self.children["!settingsview"].control

    typ = [("PNG", "*.png"), ("PDF", "*.pdf")]
    self.control.imgurl = filedialog.askopenfilename(
        title="画像ファイルを開く", filetypes=typ, initialdir="./"
    )
    self.control.dir_path = os.path.dirname(self.control.imgurl)
    FN = os.path.basename(self.control.imgurl)
    # self.str_dir.set(self.control.dir_path)
    self.control.file_list = self.control.SetDirlist(self.control.dir_path)

    if (
        ".PDF" == os.path.splitext(os.path.basename(FN))[1]
        or ".pdf" == os.path.splitext(os.path.basename(FN))[1]
    ):
        msg = messagebox.askokcancel(
            "確認", "PDFが選択されています。PNGに変換しますか？\n10ページ以上の処理は処理時間が長時間になる可能性があります。"
        )
        if msg is True:
            # プログレスバーの起動
            # PBAR = PB.Open(tk.Toplevel())  # サブWindow作成
            PBAR = ""
            spd = self.control.pdf_image(FN, "png", 300, PBAR)
            if spd is True:
                f_r = 0
                for f_l in self.control.file_list:
                    if f_l == FN:
                        set_pos = f_r
                        break
                    f_r += 1
                msg = messagebox.askokcancel("確認", "PNG変換完了しました。")
                self.control.DrawImage("set", set_pos=set_pos)
            else:
                f_r = 0
                for f_l in self.control.file_list:
                    if f_l == FN:
                        set_pos = f_r
                        break
                    f_r += 1
                msg = messagebox.askokcancel("確認", "PNG変換に失敗しました。指定DPIが高すぎる可能性があります。")
                self.control.DrawImage("set", set_pos=set_pos)
    else:
        f_r = 0
        for f_l in self.control.file_list:
            if f_l == FN:
                set_pos = f_r
                break
            f_r += 1
        self.control.DrawImage("set", set_pos=set_pos)


# ----------------------------------------------------------------------------------
def event_save(self):
    """
    Saveボタンクリックイベント
    """
    try:
        if self.control.Kanyosaki_name != "":
            self.logger.debug("Saveボタン起動")  # Log出力
            # 一時保存ファイルを確認
            if self.control.model.stock_url != "":
                os.remove(self.control.model.stock_url)
            self.Newfilename = filedialog.asksaveasfilename(
                filetypes=[("PNG", ".png"), ("JPEG", ".jpg")]
            )
            self.control.SaveImage(self.Newfilename)
            self.control.file_list = self.control.SetDirlist(
                self.dir_path
            )  # ファイルリストリロード
            for F_r in range(len(self.control.file_list)):
                if self.control.file_list[F_r] in self.Newfilename:
                    self.control.model.stock_url = ""
                    self.combo_file.set(self.control.file_list[F_r])
        else:
            messagebox.showinfo("確認", "画像ファイルが選択されていません。")
    except:
        messagebox.showinfo("確認", "画像ファイルが選択されていません。")


# ----------------------------------------------------------------------------------
def MenuCreate(self):
    """
    メニューバー作成
    """
    try:
        self.config(bg="#60cad1")
        # メニューバー作成
        self.men = tk.Menu(self, tearoff=0)
        # メニューバーを画面にセット
        self.config(menu=self.men)
        # ファイルメニューを作成する
        self.menu_file = tk.Menu(self.men)
        self.men.add_command(label="ファイル", command=lambda: event_set_file(self))
        # 保存メニューを作成する
        self.savemenu = tk.Menu(self, tearoff=False)
        self.men.add_cascade(label="保存", menu=self.savemenu)
        self.savemenu.add_command(label="上書保存", command=lambda: event_save(self))
        self.savemenu.add_separator()  # 仕切り線
        self.savemenu.add_command(label="別名保存", command=lambda: event_Searchsave(self))
    except:
        print("メニューバー作成失敗")  # Log出力


# -------------------------------------------------------------------------------------
def Pandas_mem_usage(df):
    """
    Pandasデータフレームのメモリ最適化
    """
    start_mem = df.memory_usage().sum() / 1024**2
    print("Memory usage of dataframe is {:.2f} MB".format(start_mem))

    for col in df.columns:
        col_type = df[col].dtype

        if col_type != object:
            c_min = df[col].min()
            c_max = df[col].max()
            if str(col_type)[:3] == "int":
                if c_min > np.iinfo(np.int8).min and c_max < np.iinfo(np.int8).max:
                    df[col] = df[col].astype(np.int8)
                elif c_min > np.iinfo(np.int16).min and c_max < np.iinfo(np.int16).max:
                    df[col] = df[col].astype(np.int16)
                elif c_min > np.iinfo(np.int32).min and c_max < np.iinfo(np.int32).max:
                    df[col] = df[col].astype(np.int32)
                elif c_min > np.iinfo(np.int64).min and c_max < np.iinfo(np.int64).max:
                    df[col] = df[col].astype(np.int64)
            else:
                if (
                    c_min > np.finfo(np.float16).min
                    and c_max < np.finfo(np.float16).max
                ):
                    # df[col] = df[col].astype(np.float16)
                    df[col] = df[col].astype("object")
                elif (
                    c_min > np.finfo(np.float32).min
                    and c_max < np.finfo(np.float32).max
                ):
                    # df[col] = df[col].astype(np.float32)
                    df[col] = df[col].astype("object")
                else:
                    # df[col] = df[col].astype(np.float64)
                    df[col] = df[col].astype("object")
        else:
            df[col] = df[col].astype("object")
            # df[col] = df[col].astype("category")

    end_mem = df.memory_usage().sum() / 1024**2
    print("Memory usage after optimization is: {:.2f} MB".format(end_mem))
    print("Decreased by {:.1f}%".format(100 * (start_mem - end_mem) / start_mem))

    return df


# def LinOCROpen(self):
#     """
#     OCROpenボタンクリックイベント
#     """
#     typ = [("tomlファイル", "*.toml")]
#     self.tomlPath = tk.filedialog.askopenfilename(
#         filetypes=typ, initialdir=self.dir_path
#     )

#     FDir = self.entry_dir.get()
#     FN = self.combo_file.get()
#     Imgurl = FDir + r"\\" + FN
#     Imgurl = Imgurl.replace("/", r"\\")
#     if "[select file]" in Imgurl:
#         tk.messagebox.showinfo("確認", "画像ファイルを選択してください。")
#     else:
#         Main(main_window, Imgurl, self.tomlPath)
