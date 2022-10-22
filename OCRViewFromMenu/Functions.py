from tkinter import filedialog, messagebox
import os

# ----------------------------------------------------------------------------------
def event_set_file(self):
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
