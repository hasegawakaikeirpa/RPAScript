import cv2
import numpy as np
import csv
import tkinter


class mouse_event_handler:
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


class Frame(tkinter.Frame):
    def __init__(self, master=None):
        tkinter.Frame.__init__(self, master)
        self.cvs = tkinter.Canvas(self, width="960", height="960", bg="white")
        self.cvs.grid(row=0, column=0)

        CanvasOval.canvas = self.cvs
        CanvasOval(40, 40, 50, 50, fill="red", width=0)
        CanvasOval(130, 130, 170, 170, fill="red", width=0)


def straightlinesetting(imgurl):
    """
    概要: CV2で直線を描画し、縦軸と横軸リストを返す
    @param imgurl: 画像URL(str)
    @return bool,横軸リスト,縦軸リスト
    """
    try:
        m = mouse_event_handler()
        # 画像の読み込み
        img = cv2.imread(imgurl, 1)
        height, width = img.shape[:2]
        HE = int(height / 2)
        WD = int(width / 2)
        cv2.resize(img, (WD, HE))
        # ウィンドウのサイズを変更可能にする
        cv2.namedWindow("img", cv2.WINDOW_NORMAL)
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
        TP = sorted(m.Tpoints, key=lambda x: x[1])
        YP = sorted(m.Ypoints, key=lambda x: x[0])
        cv2.destroyAllWindows()
        # cv2.imwrite(imgurl, img)
        return True, YP, TP
    except:
        return False, "m.Ypoints", "m.Tpoints"


def straightlineImport(imgurl, Yoko, Tate):
    """
    概要: CV2で直線を描画し、縦軸と横軸リストを返す
    @param imgurl: 画像URL(str)
    @return bool,横軸リスト,縦軸リスト
    """
    try:
        m = mouse_event_handler()
        # 画像の読み込み
        img = cv2.imread(imgurl, 1)
        height, width = img.shape[:2]
        img_white = np.ones((height, width, 3), np.uint8) * 255
        HE = int(height / 2)
        WD = int(width / 2)
        cv2.resize(img_white, (WD, HE))

        f = Frame()

        TKimg = tkinter.PhotoImage(file=imgurl, width=200, height=200)
        f.create_image(30, 30, image=TKimg, anchor=tkinter.NW)

        f.pack()
        f.mainloop()

        for YokoItem in Yoko[0]:
            YI = YokoItem.replace("[", "").replace("]", "").replace(" ", "").split(",")
            # 左クリックで赤い縦線を生成
            cv2.line(
                img_white,
                (int(YI[0]), int(YI[1])),
                (int(YI[2]), int(YI[3])),
                (0, 0, 255),
                3,
            )
            cv2.drawMarker(
                img_white,
                (int(YI[0]), 0),
                (0, 0, 255),
                markerType=cv2.MARKER_TILTED_CROSS,
                markerSize=100,
            )
        for TateItem in Tate[0]:
            TI = TateItem.replace("[", "").replace("]", "").replace(" ", "").split(",")
            # 右クリックで緑の横線を生成
            cv2.line(
                img_white,
                (int(TI[0]), int(TI[1])),
                (int(TI[2]), int(TI[3])),
                (0, 255, 0),
                3,
            )
            cv2.drawMarker(
                img_white,
                (0, int(TI[1])),
                (0, 255, 0),
                markerType=cv2.MARKER_TILTED_CROSS,
                markerSize=100,
            )
        # ウィンドウのサイズを変更可能にする
        cv2.namedWindow("img_white", cv2.WINDOW_NORMAL)
        cv2.setMouseCallback(
            "img_white",
            lambda event, x, y, flags, param: m.mouse_event(
                event, x, y, flags, param, img
            ),
        )

        # 「Q」が押されるまで画像を表示する
        while True:
            cv2.imshow("img_white", img_white)
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break

        # ウィンドウのサイズを変更可能にする
        cv2.namedWindow("img", cv2.WINDOW_NORMAL)
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
        TP = sorted(m.Tpoints, key=lambda x: x[1])
        YP = sorted(m.Ypoints, key=lambda x: x[0])
        cv2.destroyAllWindows()
        # cv2.imwrite(imgurl, img)
        return True, YP, TP
    except:
        return False, "m.Ypoints", "m.Tpoints"


if __name__ == "__main__":

    imgurl = r"D:\PythonScript\RPAScript\RPAPhoto\PDFeTaxReadForList\OCR0.png"
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
    straightlineImport(imgurl, readcsv1, readcsv2)
