import cv2
import os

import numpy as np

# from numpy import fromfile, uint8
import csv
from tkinter import messagebox, filedialog

# from tkinter import ttk, filedialog


class mouse_event_handler:
    """
    概要: マウスイベントクラス
    """

    def __init__(self):
        self.Tpoints = []
        self.Ypoints = []

    # マウスイベント時に処理を行う
    def mouse_event(self, event, x, y, flags, param, img):
        height, width = img.shape[:2]
        # 左クリック + Shiftキーで白い縦線を生成
        if event == cv2.EVENT_LBUTTONUP and flags & cv2.EVENT_FLAG_SHIFTKEY:
            self.Ypoints += [[x, y, x, height]]
            cv2.line(img, (x, y), (x, height), (255, 255, 255), 3)
        # 右クリック + Shiftキーで白い横線を生成
        elif event == cv2.EVENT_RBUTTONUP and flags & cv2.EVENT_FLAG_SHIFTKEY:
            self.Tpoints += [[x, y, width, y]]
            cv2.line(img, (x, y), (width, y), (255, 255, 255), 3)
        # 左クリックで赤い縦線を生成
        elif event == cv2.EVENT_LBUTTONUP:
            self.Ypoints += [[x, y, x, height]]
            cv2.line(img, (x, y), (x, height), (0, 0, 255), 3)
        # 右クリックで緑の横線を生成
        elif event == cv2.EVENT_RBUTTONUP:
            self.Tpoints += [[x, y, width, y]]
            cv2.line(img, (x, y), (width, y), (0, 255, 0), 3)


class CanvasOval:
    """
    概要: キャンバスクラス
    """

    canvas = None

    def __init__(self, x0, y0, x1, y1, **key):
        self.id = self.canvas.create_oval(x0, y0, x1, y1, **key)
        self.canvas.tag_bind(self.id, "<1>", self.drag_start)
        self.canvas.tag_bind(self.id, "<Button1-Motion>", self.dragging)

    def drag_start(self, event):
        self.x = event.x
        self.y = event.y

    def dragging(self, event):
        self.canvas.move(self.id, event.x - self.x, event.y - self.y)
        self.x = event.x
        self.y = event.y


def imread(filename, flags=cv2.IMREAD_COLOR, dtype=np.uint8):
    """
    概要: cv2imread代替関数(日本語対応)
    @param filename: ファイルURL
    @return cv2画像インスタンス
    """
    try:
        n = np.fromfile(filename, dtype)
        img = cv2.imdecode(n, flags)
        return img
    except Exception as e:
        print(e)
        return None


def imwrite(filename, img, params=None):
    """
    概要: cv2imwrite代替関数(日本語対応)
    @param filename: ファイルURL
    @return bool
    """
    try:
        ext = os.path.splitext(filename)[1]
        result, n = cv2.imencode(ext, img, params)

        if result:
            with open(filename, mode="w+b") as f:
                n.tofile(f)
            return True
        else:
            return False
    except Exception as e:
        print(e)
        return False


def straightlinesetting(imgurl):
    """
    概要: CV2で直線を描画し、縦軸と横軸リストを返す
    @param imgurl: 画像URL(str)
    @return bool,横軸リスト,縦軸リスト
    """
    try:
        m = mouse_event_handler()
        # 画像の読み込み
        img = imread(imgurl, 1)
        height, width = img.shape[:2]
        widPar = 1480 / width
        heiPar = 750 / height
        HE = int(750)
        WD = int(1480)
        img = cv2.resize(img, (WD, HE))
        # ウィンドウのサイズを変更可能にする
        cv2.namedWindow("img", cv2.WINDOW_AUTOSIZE)  # cv2.WINDOW_NORMAL)
        # cv2.setWindowProperty("img", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
        # マウスイベント時に関数mouse_eventの処理を行う
        # cv2.setMouseCallback("img", mouse_event)
        cv2.setMouseCallback(
            "img",
            lambda event, x, y, flags, param: m.mouse_event(
                event, x, y, flags, param, img
            ),
        )

        # 「Q」が押されるまで画像を表示する
        while True:
            cv2.imshow("img", img)
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break
        # 元画像に対する直線設定
        TpList = []
        for TpointsItem in m.Tpoints:
            TpList.append(
                [
                    round(TpointsItem[0] / widPar),
                    round(TpointsItem[1] / heiPar),
                    round(TpointsItem[2] / widPar),
                    round(TpointsItem[3] / heiPar),
                ]
            )
        YpList = []
        for YpointsItem in m.Ypoints:
            YpList.append(
                [
                    round(YpointsItem[0] / widPar),
                    round(YpointsItem[1] / heiPar),
                    round(YpointsItem[2] / widPar),
                    round(YpointsItem[3] / heiPar),
                ]
            )
        TP = sorted(TpList, key=lambda x: x[1])
        YP = sorted(YpList, key=lambda x: x[0])

        msg = messagebox.askokcancel("確認", "画像を保存しますか？(直線削除の際は保存してください。)")
        if msg is True:
            save_path = filedialog.asksaveasfilename(initialdir=imgurl)
            img = cv2.resize(img, (width, height))
            imwrite(save_path, img)
            cv2.destroyAllWindows()
            return True, "直線削除", "直線削除"
        else:
            cv2.destroyAllWindows()
            return True, YP, TP
        # imwrite(imgurl, img)
    except:
        return False, "m.Ypoints", "m.Tpoints"


if __name__ == "__main__":

    imgurl = r"D:\OCRTESTPDF\PDFTEST\PDF1_1page.png"
    YURL = r"D:\PythonScript\RPAScript\RPAPhoto\PDFeTaxReadForList\StraightListYoko.csv"
    TURL = r"D:\PythonScript\RPAScript\RPAPhoto\PDFeTaxReadForList\StraightListTate.csv"
    # ####################################################################################
    readcsv1 = []
    with open(
        r"D:\PythonScript\RPAScript\RPAPhoto\PDFeTaxReadForList\StraightListYoko.csv",
        "r",
        newline="",
    ) as inputfile:
        for row in csv.reader(inputfile):
            for rowItem in row:
                rsp = (
                    rowItem.replace("[", "")
                    .replace("]", "")
                    .replace(" ", "")
                    .split(",")
                )
                readcsv1.append([int(rsp[0]), int(rsp[1]), int(rsp[2]), int(rsp[3])])
    readcsv2 = []
    with open(
        r"D:\PythonScript\RPAScript\RPAPhoto\PDFeTaxReadForList\StraightListTate.csv",
        "r",
        newline="",
    ) as inputfile:
        for row in csv.reader(inputfile):
            for rowItem in row:
                rsp = (
                    rowItem.replace("[", "")
                    .replace("]", "")
                    .replace(" ", "")
                    .split(",")
                )
                readcsv2.append([int(rsp[0]), int(rsp[1]), int(rsp[2]), int(rsp[3])])
    COLArray = True, readcsv1, readcsv2
    # ####################################################################################
    straightlinesetting(imgurl)
