from tkinter import *
import tkinter.ttk as ttk
import threading


class ProgressBar(ttk.Frame):
    def __init__(self, app):
        super().__init__(app)
        self.pack()
        self.l_text = StringVar()
        self.l_text.set("実行中:0%")
        self.label = ttk.Label(self, textvariable=self.l_text)
        self.label.pack(side="left")
        self.wint = 0
        self.pbDeterminateVer = ttk.Progressbar(
            self, orient=HORIZONTAL, length=500, mode="determinate"
        )
        self.pbDeterminateVer.pack(side="left")
        self.update_idletasks()
        # startbutton = ttk.Button(self, text="start", command=self.startDeterminateVer)
        # startbutton.pack(side="left")

        # stopbutton = ttk.Button(self, text="stop", command=self.stopDeterminateVer)
        # stopbutton.pack(side="left")

    # stepを実行する
    def startDeterminateVer(self):
        self.step()

    # stopを実行することで初期化される
    def stopDeterminateVer(self):
        self.pbDeterminateVer.stop()

    # stepの引数にどれだけ進捗を進めるかを指定する
    def step(self, wint):
        self.wint += wint
        self.l_text.set("実行中:" + str(int(self.wint)) + "%")
        threading.Thread(target=self.pbDeterminateVer.step(wint))
        self.update_idletasks()


class PB_indeterminate(ttk.Frame):
    def __init__(self, app):
        super().__init__(app)
        self.pack()

        label = ttk.Label(self, text="読込中")
        label.pack(side="left")

        self.pbDeterminateVer = ttk.Progressbar(
            self, orient=HORIZONTAL, length=500, mode="indeterminate"
        )
        self.pbDeterminateVer.pack(side="left")
        self.pbDeterminateVer.start(100)
        self.update_idletasks()
        # startbutton = ttk.Button(self, text="start", command=self.startDeterminateVer)
        # startbutton.pack(side="left")

        # stopbutton = ttk.Button(self, text="stop", command=self.stopDeterminateVer)
        # stopbutton.pack(side="left")

    # stepを実行する
    def startDeterminateVer(self):
        self.step()

    # stopを実行することで初期化される
    def stopDeterminateVer(self):
        self.pbDeterminateVer.stop()

    # stepの引数にどれだけ進捗を進めるかを指定する
    def step(self, int):
        threading.Thread(target=self.pbDeterminateVer.step(int))
        self.update_idletasks()


# 引数オブジェクトにどれだけ進捗を進めるかを指定する
def Open(app):
    SB = app
    # 画面サイズ検出----------------------
    SW = SB.winfo_screenwidth()
    SW = str(int(SW / 2) - 275)
    SH = SB.winfo_screenheight()
    SH = str(int(SH / 2) - 15)
    # ------------------------------------
    SB.geometry("650x30+" + SW + "+" + SH)  # 画面中央に表示
    SB.wm_attributes("-topmost", True)  # 常に一番上のウィンドウに指定
    SB.overrideredirect(True)  # ウィンドウのタイトル部分を消去

    # #フレームを作成する
    PBAR = threading.Thread(target=ProgressBar(SB))
    return PBAR


# 引数オブジェクトにどれだけ進捗を進めるかを指定する
def Open_IN(app):
    SB = app
    # 画面サイズ検出----------------------
    SW = SB.winfo_screenwidth()
    SW = str(int(SW / 2) - 275)
    SH = SB.winfo_screenheight()
    SH = str(int(SH / 2) - 15)
    # ------------------------------------
    SB.geometry("650x30+" + SW + "+" + SH)  # 画面中央に表示
    SB.wm_attributes("-topmost", True)  # 常に一番上のウィンドウに指定
    SB.overrideredirect(True)  # ウィンドウのタイトル部分を消去

    # #フレームを作成する
    PBAR = threading.Thread(target=PB_indeterminate(SB))
    return PBAR


if __name__ == "__main__":
    # Tkインスタンスを作成し、app変数に格納する
    app = Tk()
    # 縦幅400横幅300に画面サイズを変更します。
    app.geometry("650x30")
    # タイトルを指定
    app.title("ProgressBar Sample Program")
    # #フレームを作成する
    frame = ProgressBar(app)
    # 格納したTkインスタンスのmainloopで画面を起こす
    app.mainloop()
