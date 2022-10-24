import tkinter as tk
from tkinter import ttk
import ViewGUI
import ImageViewer


class Page(ttk.Frame):
    def __init__(self, master, **kw):
        super().__init__(master, **kw)

    def verify(self):
        return True


class LanguagePage(Page):
    def __init__(self, master, **kw):
        super().__init__(master, **kw)
        self.control = controlSerach(self)
        self.create_frame_content().pack(fill=tk.BOTH, expand=True)

    def create_frame_content(self) -> ttk.Frame:
        """
        設定のウィジェット作成
        """
        # self.frame_content = ttk.Frame(self)

        # self.FCW = int(self.control.width_of_window * 0.4)
        # self.FCH = int(self.control.height_of_window * 0.4)

        # self.window_sub_FrameCanvas = ImageViewer.Application(
        #     tk.Frame(
        #         master=self.frame_content,
        #         height=self.FCH,
        #         width=self.FCW,
        #     )
        # )
        # self.window_sub_FrameCanvas.master.pack(side=tk.TOP, fill="both", expand=True)
        self.fr = ttk.Frame(
            self,
            width=self.control.width_of_window,
            height=self.control.height_of_window,
        )
        self.fr.pack(fill=tk.BOTH, expand=True)
        self.frame_content = ViewGUI.ViewGUI(self.fr, self.control)
        # lbl_title = ttk.Label(self.frame_content, text="This is the Language Page")
        # lbl_title.pack()

        return self.frame_content


class AudioPage(Page):
    def __init__(self, master, **kw):
        super().__init__(master, **kw)
        self.create_frame_content().pack(fill=tk.BOTH, expand=True)

    def create_frame_content(self) -> ttk.Frame:
        """
        設定のウィジェット作成
        """
        self.frame_content = ttk.Frame(self)
        lbl_title = ttk.Label(self.frame_content, text="This is the Audio Page")
        lbl_title.pack()

        return self.frame_content


def controlSerach(self):
    master_f = True
    m = self.master
    while master_f is True:
        try:
            m = m.master
            if m is None:
                break
            else:
                Em = m
        except:
            master_f = False
    return Em.children["!settingsview"].control


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("640x480")

    LanguagePage(root)

    root.mainloop()
