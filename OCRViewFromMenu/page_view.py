import tkinter as tk
from tkinter import ttk


class Page(ttk.Frame):
    def _init(self, master, **kw):
        super().__init__(master, **kw)

    def verify(self):
        return True


class LanguagePage(Page):
    def _init(self, master, **kw):
        super().__init__(master, **kw)
        self.create_frame_content().pack(fill=tk.BOTH, expand=True)

    def create_frame_content(self) -> ttk.Frame:
        """
        設定のウィジェット作成
        """
        self.frame_content = ttk.Frame(self)
        lbl_title = ttk.Label(self.frame_content, text="This is the Language Page")
        lbl_title.pack()

        return self.frame_content


class AudioPage(Page):
    def _init(self, master, **kw):
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
