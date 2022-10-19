import customtkinter as ck
import IconCode
from tkinter import PhotoImage, messagebox


def WindowSet(window_root, theme, width_of_window, height_of_window, title, logger):
    try:
        logger.debug("WindowSet起動")  # Log出力
        #####################################################
        # customtkスタイル
        ck.set_appearance_mode("System")  # Modes: system (default), light, dark
        ck.set_default_color_theme(theme)  # Themes: blue (default), dark-blue, green
        ######################################################
        w_root = window_root  # ルートウィンドウ
        w_root.columnconfigure(0, weight=1)
        w_root.rowconfigure(0, weight=1)
        w_root_width = w_root.winfo_screenwidth()  # ルートウィンドウ幅(画面解像度)
        w_root_height = w_root.winfo_screenheight()  # ルートウィンドウ高さ(画面解像度)
        data = IconCode.icondata()
        w_root.tk.call(
            "wm",
            "iconphoto",
            w_root._w,
            PhotoImage(data=data, master=w_root),
        )
        x_coodinate = (w_root_width / 2) - (width_of_window / 2)
        y_coodinate = (w_root_height / 2) - (height_of_window / 2)
        w_root.geometry(
            "%dx%d+%d+%d"
            % (
                width_of_window,
                height_of_window,
                x_coodinate,
                y_coodinate,
            )
        )
        w_root.title(title)
        w_root.protocol(
            "WM_DELETE_WINDOW", lambda: click_close(w_root, logger)
        )  # 閉じる処理設定
        return w_root
    except:
        messagebox.showinfo("確認", "WindowSet失敗に失敗しました。")
        logger.debug("WindowSet失敗")  # Log出力
        return False


def click_close(w_root, logger):
    """
    ウィンドウ×ボタンクリック
    """
    if messagebox.askokcancel("確認", "終了しますか？"):
        logger.debug("Close完了")  # Log出力
        w_root.destroy()
