import tkinter as tk
from tkinter import messagebox
import Functions


class Frame(tk.Toplevel):
    """
    概要: TKinterメインWindowクラス
    """

    def __init__(self, window_root, Title):
        # super().__init__(window_root)
        # メインウィンドウ
        self.window_root = window_root
        self.width_of_window = int(int(self.window_root.winfo_screenwidth()) * 0.95)
        self.height_of_window = int(int(self.window_root.winfo_screenheight()) * 0.85)
        self.x_coodinate = self.width_of_window / 2
        self.y_coodinate = self.height_of_window / 2
        self.padx = self.x_coodinate / 4
        self.pady = self.y_coodinate / 4
        self.window_root.geometry(
            "%dx%d+%d+%d"
            % (
                self.width_of_window,
                self.height_of_window,
                0,
                0,
            )
        )
        self.window_root.minsize(self.width_of_window, self.height_of_window)
        # 　メインウィンドウタイトル
        self.window_root.title(Title)
        self.window_root.protocol("WM_DELETE_WINDOW", self.click_close)  # 閉じる処理設定
        self.window_root.HeaderCol_c = 0  # ページ追加時の列数
        self.window_rootFrame = tk.Frame(
            self.window_root,
            width=self.width_of_window,
            height=self.height_of_window,
            bg="#60cad1",
        )
        self.window_rootFrame.pack(fill=tk.BOTH, expand=True)
        self.MenuCreate()

    # 要素作成######################################################################################
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
            self.men.add_command(
                label="ファイル", command=lambda: Functions.event_set_file(self)
            )
            # 保存メニューを作成する
            self.savemenu = tk.Menu(self.window_root, tearoff=False)
            self.men.add_cascade(label="保存", menu=self.savemenu)
            self.savemenu.add_command(
                label="上書保存", command=lambda: Functions.event_save(self)
            )
            self.savemenu.add_separator()  # 仕切り線
            self.savemenu.add_command(
                label="別名保存", command=lambda: Functions.event_Searchsave(self)
            )

            # OCRメニューを作成する
            self.OCR_men = tk.Menu(self.men)
            self.men.add_command(label="OCR起動", command=self.LinOCROpen)
        except:
            self.logger.debug("メニューバー作成失敗")  # Log出力

    # セルフ関数#####################################################################################
    def click_close(self):
        """
        ウィンドウ×ボタンクリック
        """
        if messagebox.askokcancel("確認", "終了しますか？"):
            self.logger.debug(f"{self.title}完了")  # Log出力
            self.window_root.destroy()

    ################################################################################################


def Open(title_n):
    main_window = tk.Tk()
    # Viewクラス生成
    Frame(main_window, title_n)
    # 　フレームループ処理
    # main_window.mainloop()
    return


if __name__ == "__main__":
    Open("OCR読取 Ver:0.9")
    # 　Tk MainWindow 生成
    main_window = tk.Tk()
    # Viewクラス生成
    Frame(main_window, "./")

    # 　フレームループ処理
    main_window.mainloop()
