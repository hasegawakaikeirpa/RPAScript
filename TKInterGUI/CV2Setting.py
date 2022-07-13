import cv2
import csv


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
