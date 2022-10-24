from tkinter import filedialog, messagebox
import os


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
