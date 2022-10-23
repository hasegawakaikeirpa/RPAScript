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
    self.Dir.insert(0, self.control.dir_path)
    self.control.file_list = self.control.SetDirlist(self.control.dir_path)


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


def event_prev(self):
    """
    prevボタンクリックイベント
    """
    pos = self.control.DrawImage("prev")
    self.combo_file.set(self.file_list[pos])


def event_next(self):
    """
    nextボタンクリックイベント
    """
    pos = self.control.DrawImage("next")
    self.combo_file.set(self.file_list[pos])


def event_rotate(self):
    """
    画像回転変更イベント
    """
    val = self.radio_intvar1.get()
    cmd = "rotate-" + str(val)
    self.control.EditImage(cmd)


def event_flip(self):
    """
    画像反転イベント
    """
    val = self.radio_intvar2.get()
    cmd = "flip-" + str(val)
    self.control.EditImage(cmd)


def event_clip_try(self):
    """
    Tryボタンイベント
    """
    self.clip_enable = True


def event_clip_done(self):
    """
    Doneボタンイベント
    """
    if self.clip_enable:
        self.control.EditImage("clip_done")
        self.clip_enable = False


def event_clip_Erace(self):
    """
    Eraceボタンイベント
    """
    if self.clip_enable:
        self.control.EditImage("clip_Erace")
        self.clip_enable = False


def event_clip_start(self, event):
    """
    画像処理Saveイベント
    """
    if self.clip_enable:
        self.control.DrawRectangle("clip_start", event.y, event.x)


def event_clip_keep(self, event):
    """
    画像処理Undoイベント
    """
    if self.clip_enable:
        self.control.DrawRectangle("clip_keep", event.y, event.x)


def event_clip_end(self, event):
    """
    キャンバス画像左クリック範囲指定で終端まで確定後
    """
    if self.clip_enable:
        self.control.DrawRectangle("clip_end", event.y, event.x)


def event_save(self):
    """
    Saveボタンクリックイベント
    """
    self.control.SaveImage()


def event_Oversave(self):
    """
    OverSaveボタンクリックイベント
    """
    self.control.OverSaveImage()


def event_undo(self):
    """
    Undoボタンクリックイベント
    """
    self.control.UndoImage("None")
    self.radio_intvar1.set(0)
    self.radio_intvar2.set(0)


def event_updatefile(self):
    """
    ファイル選択ウィンドウクリックイベント
    """
    self.file_list = self.control.SetDirlist(self.dir_path)
    self.combo_file["value"] = self.file_list


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
