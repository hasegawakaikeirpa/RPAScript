import tkinter as tk
from tkinter import ttk

from PIL import Image, ImageTk

# from tkinter import messagebox
import os

# import OCRFlow as OCRF
# import toml
import customtkinter as ck

# from CV2Setting import straightlinesetting
from GCloudVision import AutoLine, LineTomlOut

# import ScrollableFrame as SF
# import tomlCreate as toml_c
from tkinter import filedialog, messagebox

# import FrameClass

from functools import wraps
import traceback

import ControlGUI
import logging.config
import os
import LineEditGUI_Frame

import Functions

import IconCode

# import threading

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


###################################################################################################
# class Application(tk.Frame):
class Application(ttk.Frame):
    def __init__(self, master, control):
        super().__init__(master)
        self.control = control
        self.control.wid_Par = self.control.width_of_window / 1459
        self.control.hei_Par = self.control.height_of_window / 820
        # # ルートウィンドウ
        self.master.window_rootFrame = tk.Frame(master=master)
        self.master.window_rootFrame.pack(fill=tk.BOTH, expand=True)
        self.control.top = tk.Toplevel(master=master)
        data = IconCode.icondata()
        self.control.top.tk.call(
            "wm",
            "iconphoto",
            self.control.top._w,
            tk.PhotoImage(data=data, master=self.control.top),
        )

        self.control.top.geometry(
            "%dx%d+%d+%d"
            % (
                self.control.width_of_window,
                self.control.height_of_window,
                self.control.x_coodinate,
                self.control.y_coodinate,
            )
        )
        self.control.top.wm_attributes("-transparentcolor", "white")  # トップWindowの白色を透過
        self.control.top.wm_attributes("-topmost", True)  # 常に一番上のウィンドウに指定
        self.control.top.window_rootFrame = tk.Frame(master=self.control.top)
        self.control.top.window_rootFrame.pack(fill=tk.BOTH, expand=True)
        self.control.top.bind("<Motion>", self.change)  # 透過ウィンドウにマウス移動関数bind
        self.master.window_rootFrame.bind("<Motion>", self.change)  # 下ウィンドウにマウス移動関数bind
        Functions.MenuCreate(self.control.top)  # メニューバー作成
        self.FrameCreate()  # フレーム作成
        self.control.top.withdraw()

    # 要素作成######################################################################################
    def FrameCreate(self):
        # サイドメニュー作成
        self.SideFrame = tk.Frame(
            self.control.top.window_rootFrame,
            width=200,
            height=self.control.height_of_window,
            bg="white",
            relief=tk.GROOVE,
        )
        # self.SideFrame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.SideFrame.grid(row=0, column=0, rowspan=2, sticky=tk.N + tk.S)
        # 透過キャンバスフレーム
        self.control.topFrame = tk.Frame(
            self.control.top.window_rootFrame,
            bg="snow",
            width=self.control.FCW,
            height=self.control.FCH,
            relief=tk.GROOVE,
            bd=2,
        )
        # self.control.topFrame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        self.control.topFrame.grid(row=0, column=1, sticky=tk.NSEW)
        # 透過キャンバス作成
        self.control.top.forward = tk.Canvas(
            self.control.topFrame,
            background="white",
            width=self.control.FCW,
            height=self.control.FCH,
        )
        self.control.top.forward.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        self.control.top.forward.bind("Enter", self.change)
        self.Transparent_Create()  # 透過キャンバス描画
        # ボトムメニュー作成
        self.bottumFrame = tk.Frame(
            self.control.top.window_rootFrame,
            width=self.control.width_of_window,
            height=self.control.Bottom_Column,
            bg="black",
            relief=tk.GROOVE,
        )
        # self.bottumFrame.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
        self.bottumFrame.grid(row=1, column=1, sticky=tk.NSEW)
        self.bottumFrame.propagate(0)
        #################################################################################
        self.ImportIMG()
        LineEditGUI_Frame.Frame1(self)
        LineEditGUI_Frame.Frame2(self)
        LineEditGUI_Frame.Frame3(self)

    # ------------------------------------------------------------------------------------
    def Transparent_Create(self):
        """
        透過キャンバス(上ウィンドウ)に罫線描画処理
        """
        # .create_line(Ⅹ座標（始点）, Ｙ座標（始点）,Ⅹ座標（終点）, Ｙ座標（終点）)
        BtagsList = []
        self.tagsList = []
        ri = 0
        for readcsv1Item in self.control.YokoList:
            ri += 1
            ripar0 = round(readcsv1Item[0] * self.control.HCW, 0)  # * CHh
            ripar1 = round(readcsv1Item[1] * self.control.HCH, 0)  # * CWw
            ripar2 = round(readcsv1Item[2] * self.control.HCW, 0)  # * CHh
            ripar3 = round(readcsv1Item[3] * self.control.HCH, 0)  # * CWw
            TName = "Line" + str(ri)
            try:
                self.control.top.forward.dtag(TName, TName)
            except:
                print("dtagErr")
            self.control.top.forward.create_line(
                ripar0,
                ripar1,
                ripar2,
                ripar3,
                tags=TName,
                width=7,
                fill="#FF0000",
                activefill="#DBDD6F",
            )
            self.control.top.forward.tag_bind(TName, "<ButtonPress-1>", self.click1)
            self.control.top.forward.tag_bind(
                TName, "<Control-Double-1>", self.EventDelete
            )
            self.control.top.forward.tag_bind(TName, "<B1-Motion>", drag1)

            self.control.top.forward.place(x=0, y=0)
            BtagsList.append([TName, ripar0, ripar1, ripar2, ripar3, "Yoko"])
        for readcsv2Item in self.control.TateList:
            ri += 1
            ripar0 = round(readcsv2Item[0] * self.control.HCW, 0)  # * CHh
            ripar1 = round(readcsv2Item[1] * self.control.HCH, 0)  # * CWw
            ripar2 = round(readcsv2Item[2] * self.control.HCW, 0)  # * CHh
            ripar3 = round(readcsv2Item[3] * self.control.HCH, 0)  # * CWw
            TName = "Line" + str(ri)
            self.control.top.forward.create_line(
                ripar0,
                ripar1,
                ripar2,
                ripar3,
                tags=TName,
                width=7,
                fill="#00FF40",
                activefill="#DBDD6F",
            )
            self.control.top.forward.tag_bind(TName, "<ButtonPress-1>", self.click1)
            self.control.top.forward.tag_bind(
                TName, "<Control-Double-1>", self.EventDelete
            )
            self.control.top.forward.tag_bind(TName, "<B1-Motion>", drag1)

            self.control.top.forward.place(x=0, y=0)
            BtagsList.append([TName, ripar0, ripar1, ripar2, ripar3, "Tate"])
        TL = len(BtagsList)
        for TTL in range(TL):
            tagsListItem = BtagsList[TTL]
            BB = self.control.top.forward.bbox(tagsListItem[0])
            BSS = [
                tagsListItem[1] - BB[0],
                tagsListItem[2] - BB[1],
                tagsListItem[3] - BB[2],
                tagsListItem[4] - BB[3],
            ]
            self.tagsList.append([tagsListItem, BSS])

    # ------------------------------------------------------------------------------------
    def ImportIMG(self):
        """
        下ウィンドウに画像をリサイズして配置
        """

        self.control.img = Image.open(self.control.imgurl)
        self.control.img = self.control.img.resize(
            (self.control.FCW, self.control.FCH)
        )  # 画像リサイズ
        self.back = tk.Canvas(
            self.master.window_rootFrame,
            background="white",
            width=self.control.FCW,
            height=self.control.FCH,
        )
        self.control.TkPhoto = ImageTk.PhotoImage(
            self.control.img, master=self.back
        )  # 下Windowに表示する画像オブジェクト
        self.back.create_image(
            0, 0, image=self.control.TkPhoto, anchor=tk.NW
        )  # 下Windowのキャンバスに画像挿入
        self.back.pack(side=tk.TOP, fill=tk.BOTH, expand=True)  # 下Windowを配置

        self.backBottom = tk.Frame(
            self.master.window_rootFrame, height=self.control.Bottom_Column
        )
        self.backBottom.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
        self.master.window_rootFrame.bind("<Configure>", self.change)

        self.back.bind("<Unmap>", self.unmap)
        self.back.bind("<Map>", self.map)
        self.back.bind("<Double-1>", self.backbind)  # 下ウィンドウにダブルクリックbind
        self.back.bind("<Double-3>", self.Right_backbind)  # 下ウィンドウにダブルクリックbind

    # 関数##############################################################################
    # 円、矩形、直線を描画＆ドラッグできるようにする【tkinter】
    def click1(self, event):
        """
        縦直線描画処理(画面クリック)
        """
        self.Line_txt.delete(0, tk.END)
        self.x2 = event.x
        self.y2 = event.y
        self.id1 = event.widget.find_closest(self.x2, self.y2)
        self.TName = event.widget.gettags(self.id1[0])[0]
        self.Line_txt.insert(tk.END, self.TName)
        self.x1 = self.x2
        self.y1 = self.y2

    # ---------------------------------------------------------------------------------------------
    def EventDelete(self, event):
        """
        線削除処理(画面ダブルクリック)
        """
        self.x2 = event.x
        self.y2 = event.y
        self.id1 = event.widget.find_closest(self.x2, self.y2)
        self.TName = event.widget.gettags(self.id1[0])[0]
        event.widget.delete(self.TName)
        r = 0
        for tagsListItem in self.tagsList:
            if self.TName == tagsListItem[0][0]:
                self.tagsList.pop(r)
                break
            r += 1
        nptag_L = LineTomlOut(self.tagsList, self.control.HCW, self.control.HCH)
        if nptag_L[0] is True:
            ####################################################################################
            F_N = os.path.splitext(os.path.basename(self.control.imgurl))[0]
            self.control.Yoko_N = F_N + "_Yoko"
            self.control.Tate_N = F_N + "_Tate"
            nptag_L[1].sort()
            nptag_L[2].sort(key=lambda x: x[1])
            self.control.tomlsetting["LineSetting"][self.control.Yoko_N] = nptag_L[1]
            self.control.tomlsetting["LineSetting"][self.control.Tate_N] = nptag_L[2]
            Functions.dump_toml(self.tomlsetting, self.control.tomlurl)
            ####################################################################################
        else:
            print("Err")
        self.Line_txt.delete(0, tk.END)

    # ---------------------------------------------------------------------------------------------
    def serchmaster(self):
        sm = False
        m = self.master
        while sm is False:
            m = m.master
            if m is not None:
                Em = m
            else:
                sm = True
        return Em

    def ReadtomlLine(self):
        """
        画像名からtoml線軸リストを取得
        """
        try:
            self.control.img_name = os.path.splitext(
                os.path.basename(self.control.imgurl)
            )[0]
            self.control.Yoko_N = self.control.img_name + "_Yoko"
            self.control.Tate_N = self.control.img_name + "_Tate"
            self.control.rep_N = self.control.img_name + "_ReplaceStr"
            self.control.YokoList = self.control.tomlsetting["LineSetting"][
                self.control.Yoko_N
            ]
            self.control.TateList = self.control.tomlsetting["LineSetting"][
                self.control.Tate_N
            ]
        except:
            self.control.YokoList = self.control.tomlsetting["LineSetting"][
                "Nomal_Yoko"
            ]
            self.control.TateList = self.control.tomlsetting["LineSetting"][
                "Nomal_Tate"
            ]

    # ---------------------------------------------------------------------------------------------
    def unmap(self, event):
        """
        上下ウィンドウ連携処理(上を隠す)
        """
        # self.control.top.master.withdraw()

    # ---------------------------------------------------------------------------------------------
    def map(self, event):
        """
        上下ウィンドウ連携処理(上を表示)
        """
        # self.lift()
        # self.control.top.master.wm_deiconify()
        # self.control.top.master.attributes("-topmost", True)

    # ---------------------------------------------------------------------------------------------
    def change(self, event):
        """
        上下ウィンドウ連携処理(ウィンドウサイズ変更)
        """
        top_geometry = self.control.top.geometry()
        sm = self.serchmaster()
        sm.geometry(top_geometry)

    # ---------------------------------------------------------------------------------------------
    def ChangeToml(self):
        """
        tomlリストを変更
        """
        try:
            typ = [("tomlファイル", "*.toml")]
            self.control.top.withdraw()
            tomlurl = filedialog.askopenfilename(filetypes=typ)
            if tomlurl != "":
                try:
                    self.control.top.destroy()
                    self.master.destroy()
                except:
                    print("")
                messagebox.showinfo("設定ファイル再読込", "設定ファイルを再読み込みします。")
                self.control.debug("tomlファイル再読込")  # Log出力
                Open()
                self.control.debug("tomlファイル再読込完了")  # Log出力
            else:
                messagebox.showinfo("確認", "設定ファイルを指定してください。")
                self.control.top.deiconify()
        except:
            self.control.debug("tomlファイル変更Err")  # Log出力
            self.control.top.deiconify()

    # ---------------------------------------------------------------------------------------------
    def backbind(self, event):
        """
        縦直線追加ダブルクリック処理
        """

        TName = "Line" + str(self.blankno())
        sm = self.control.topFrame.children["!canvas"]
        sm.create_line(
            event.x,
            0,
            event.x,
            self.control.FCH,
            tags=TName,
            width=7,
            fill="#FF0000",
            activefill="#DBDD6F",
        )
        sm.tag_bind(TName, "<ButtonPress-1>", self.click1)
        sm.tag_bind(TName, "<Control-Double-1>", self.EventDelete)
        sm.tag_bind(TName, "<B1-Motion>", drag1)
        BSS = [0, 0, 0, 0]
        TSS = [TName, event.x, 0, event.x, self.control.FCH, "Yoko"]
        self.tagsList.append([TSS, BSS])

    # ---------------------------------------------------------------------------------------------
    def Right_backbind(self, event):
        """
        横直線追加ボタン処理
        """

        TName = "Line" + str(self.blankno())
        sm = self.control.topFrame.children["!canvas"]
        sm.create_line(
            0,
            event.y,
            self.control.FCW,
            event.y,
            tags=TName,
            width=7,
            fill="#00FF40",
            activefill="#DBDD6F",
        )
        sm.tag_bind(TName, "<ButtonPress-1>", self.click1)
        sm.tag_bind(TName, "<Control-Double-1>", self.EventDelete)
        sm.tag_bind(TName, "<B1-Motion>", drag1)
        TSS = [TName, 0, event.y, self.control.FCW, event.y, "Tate"]
        BSS = [0, 0, 0, 0]
        self.tagsList.append([TSS, BSS])


def LoadImg(self, Wwidth, Wheight):
    """
    画像ファイル読込
    """
    self.control.img = Image.open(self.control.imgurl)
    self.control.MaxW, self.control.MaxH = (
        self.control.img.width,
        self.control.img.height,
    )
    CW, CH = int(Wwidth), int(Wheight)
    self.control.HCW, self.control.HCH = (
        CW / self.control.MaxW,
        CH / self.control.MaxH,
    )  # リサイズ比率
    self.control.img = self.control.img.resize((CW, CH))  # 画像リサイズ
    self.control.TkPhoto = ImageTk.PhotoImage(self.control.img)  # 下Windowに表示する画像オブジェクト


# ---------------------------------------------------------------------------------------------
def drag1(event):
    """
    縦直線移動処理(ドラッグ)
    """
    global x1
    global y1
    global id1

    x2 = event.x
    y2 = event.y
    del_x1 = x2 - x1
    del_y1 = y2 - y1
    x0, y0, x1, y1 = event.widget.coords(id1)
    event.widget.coords(id1, x0 + del_x1, y0 + del_y1, x1 + del_x1, y1 + del_y1)
    x1 = x2
    y1 = y2


@log_decorator()
def Open():
    control = ControlGUI.ControlGUI("./", logger)  # セルフコントローラー
    main_window = tk.Tk()
    top = tk.Toplevel()
    Application(top, control)
    main_window.mainloop()


if __name__ == "__main__":
    Open()
