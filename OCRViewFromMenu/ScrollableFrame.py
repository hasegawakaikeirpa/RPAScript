import tkinter as tk
import tkinter.ttk as ttk


class ScrollableFrame(ttk.Frame):
    def __init__(self, container, wid, hei, bar_x=True, bar_y=True):
        super().__init__(container)
        self.canvas = tk.Canvas(
            self,
            width=int(wid / 5),
            height=int(hei / 5),
            bg="#ecb5f5",
        )
        self.scrollable_frame = tk.Frame(
            self.canvas,
            bg="#ecb5f5",
            relief=tk.GROOVE,
            width=int(wid / 5),
            bd=2,
        )
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")),
        )
        self.canvas.create_window(
            (0, 0), window=self.scrollable_frame, anchor="nw", width=int(wid / 5)
        )
        if bar_y:
            self.scrollable_frame.bind("<MouseWheel>", self.mouse_y_scroll)
            self.scrollbar_y = ttk.Scrollbar(
                self.scrollable_frame, orient="vertical", command=self.canvas.yview
            )
            self.scrollbar_y.grid(row=0, column=3, sticky=tk.S + tk.N)
            self.canvas.configure(yscrollcommand=self.scrollbar_y.set)
        if bar_x:
            self.scrollable_frame.bind("<MouseWheel>", self.mouse_x_scroll)
            self.scrollbar_x = ttk.Scrollbar(
                self.scrollable_frame, orient="horizontal", command=self.canvas.xview
            )
            self.scrollbar_x.grid(sticky=tk.E + tk.W)
            self.canvas.configure(xscrollcommand=self.scrollbar_x.set)
        self.canvas.grid(sticky=tk.S + tk.N)

    def mouse_y_scroll(self, event):
        if event.delta > 0:
            self.canvas.yview_scroll(-1, "units")
        elif event.delta < 0:
            self.canvas.yview_scroll(1, "units")

    def mouse_x_scroll(self, event):
        if event.delta > 0:
            self.canvas.xview_scroll(-1, "units")
        elif event.delta < 0:
            self.canvas.xview_scroll(1, "units")


class ScrollableFrameDG(ttk.Frame):
    def __init__(self, container, bar_x=True, bar_y=True):
        super().__init__(container)
        self.canvas = tk.Canvas(self, width=730)
        # self.scrollable_frame = ttk.Frame(
        #     self.canvas,
        #     borderwidth=2,
        #     relief=tk.GROOVE,
        #     bg="gray",
        # )
        self.scrollable_frame = tk.Frame(
            self.canvas,
            bg="gray94",
            relief=tk.GROOVE,
            bd=2,
        )
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")),
        )
        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        if bar_y:
            self.scrollable_frame.bind("<MouseWheel>", self.mouse_y_scroll)
            self.scrollbar_y = ttk.Scrollbar(
                self.scrollable_frame, orient="vertical", command=self.canvas.yview
            )
            # self.scrollbar_y.pack(side=tk.RIGHT, fill="y")
            self.scrollbar_y.grid(row=0, column=3, sticky=tk.S + tk.N)
            self.canvas.configure(yscrollcommand=self.scrollbar_y.set)
        if bar_x:
            self.scrollable_frame.bind("<MouseWheel>", self.mouse_x_scroll)
            self.scrollbar_x = ttk.Scrollbar(
                self.scrollable_frame, orient="horizontal", command=self.canvas.xview
            )
            self.scrollbar_x.grid(sticky=tk.E + tk.W)
            # self.scrollbar_x.pack(side=tk.BOTTOM, fill="x")
            self.canvas.configure(xscrollcommand=self.scrollbar_x.set)
        # self.canvas.pack(side=tk.LEFT, fill="both", expand=True)
        self.canvas.grid(sticky=tk.S + tk.N + tk.E + tk.W)

    def mouse_y_scroll(self, event):
        if event.delta > 0:
            self.canvas.yview_scroll(-1, "units")
        elif event.delta < 0:
            self.canvas.yview_scroll(1, "units")

    def mouse_x_scroll(self, event):
        if event.delta > 0:
            self.canvas.xview_scroll(-1, "units")
        elif event.delta < 0:
            self.canvas.xview_scroll(1, "units")


class ScrollableFrameFS(ttk.Frame):
    def __init__(self, container, bar_x=True, bar_y=True):
        super().__init__(container)
        self.canvas = tk.Canvas(self, width=350)
        # self.scrollable_frame = ttk.Frame(
        #     self.canvas,
        #     borderwidth=2,
        #     relief=tk.GROOVE,
        #     bg="gray",
        # )
        self.scrollable_frame = tk.Frame(
            self.canvas,
            bg="gray94",
            relief=tk.GROOVE,
            bd=2,
        )
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")),
        )
        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        if bar_y:
            self.scrollable_frame.bind("<MouseWheel>", self.mouse_y_scroll)
            self.scrollbar_y = ttk.Scrollbar(
                self.scrollable_frame, orient="vertical", command=self.canvas.yview
            )
            # self.scrollbar_y.pack(side=tk.RIGHT, fill="y")
            self.scrollbar_y.grid(row=0, column=3, sticky=tk.S + tk.N)
            self.canvas.configure(yscrollcommand=self.scrollbar_y.set)
        if bar_x:
            self.scrollable_frame.bind("<MouseWheel>", self.mouse_x_scroll)
            self.scrollbar_x = ttk.Scrollbar(
                self.scrollable_frame, orient="horizontal", command=self.canvas.xview
            )
            self.scrollbar_x.grid(sticky=tk.E + tk.W)
            # self.scrollbar_x.pack(side=tk.BOTTOM, fill="x")
            self.canvas.configure(xscrollcommand=self.scrollbar_x.set)
        # self.canvas.pack(side=tk.LEFT, fill="both", expand=True)
        self.canvas.grid(sticky=tk.S + tk.N + tk.E + tk.W)

    def mouse_y_scroll(self, event):
        if event.delta > 0:
            self.canvas.yview_scroll(-1, "units")
        elif event.delta < 0:
            self.canvas.yview_scroll(1, "units")

    def mouse_x_scroll(self, event):
        if event.delta > 0:
            self.canvas.xview_scroll(-1, "units")
        elif event.delta < 0:
            self.canvas.xview_scroll(1, "units")


class SubScrollableFrame(ttk.Frame):
    def __init__(self, container, wid, hei, mrow, bar_x=True, bar_y=True):
        super().__init__(container)
        self.canvas = tk.Canvas(
            self, width=int(wid / 5) - 10, height=(hei / 5), bg="gray94"
        )
        # self.scrollable_frame = ttk.Frame(
        #     self.canvas,
        #     borderwidth=2,
        #     relief=tk.GROOVE,
        #     bg="gray",
        # )
        self.scrollable_frame = tk.Frame(
            self.canvas,
            bg="gray94",
            width=int(wid / 5) - 10,
            height=(hei / 5),
            relief=tk.GROOVE,
            bd=2,
        )
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")),
        )
        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="center")
        if bar_y:
            self.scrollable_frame.bind("<MouseWheel>", self.mouse_y_scroll)
            self.scrollbar_y = ttk.Scrollbar(
                self.scrollable_frame, orient="vertical", command=self.canvas.yview
            )

            self.scrollbar_y.grid(row=0, column=4, rowspan=mrow + 1, sticky=tk.S + tk.N)
            self.canvas.configure(yscrollcommand=self.scrollbar_y.set)
        if bar_x:
            self.scrollable_frame.bind("<MouseWheel>", self.mouse_x_scroll)
            self.scrollbar_x = ttk.Scrollbar(
                self.scrollable_frame, orient="horizontal", command=self.canvas.xview
            )
            self.scrollbar_x.grid(
                row=mrow + 1, column=0, columnspan=4, sticky=tk.E + tk.W
            )

            self.canvas.configure(xscrollcommand=self.scrollbar_x.set)
        self.canvas.pack(expand=True, fill=tk.BOTH)
        # self.canvas.grid(row=0, sticky=tk.NSEW)

    def mouse_y_scroll(self, event):
        if event.delta > 0:
            self.canvas.yview_scroll(-1, "units")
        elif event.delta < 0:
            self.canvas.yview_scroll(1, "units")

    def mouse_x_scroll(self, event):
        if event.delta > 0:
            self.canvas.xview_scroll(-1, "units")
        elif event.delta < 0:
            self.canvas.xview_scroll(1, "units")


class ScrollableUnderFrame(ttk.Frame):
    def __init__(self, container, wid, bar_x=False, bar_y=True):
        super().__init__(container)
        self.canvas = tk.Canvas(
            self,
            width=wid,
            bg="gray94",
        )
        self.scrollable_frame = tk.Frame(
            self.canvas,
            bg="gray94",
            width=wid,
            relief=tk.GROOVE,
            bd=2,
        )
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")),
        )
        self.canvas.create_window(
            (0, 0), window=self.scrollable_frame, anchor="nw", width=wid
        )
        if bar_y:
            self.scrollable_frame.bind("<MouseWheel>", self.mouse_y_scroll)
            self.scrollbar_y = ttk.Scrollbar(
                self.scrollable_frame, orient="vertical", command=self.canvas.yview
            )
            self.scrollbar_y.grid(row=0, column=4, sticky=tk.S + tk.N)
            self.canvas.configure(yscrollcommand=self.scrollbar_y.set)
        if bar_x:
            self.scrollable_frame.bind("<MouseWheel>", self.mouse_x_scroll)
            self.scrollbar_x = ttk.Scrollbar(
                self.scrollable_frame, orient="horizontal", command=self.canvas.xview
            )
            self.scrollbar_x.grid(sticky=tk.E + tk.W)
            self.canvas.configure(xscrollcommand=self.scrollbar_x.set)
        self.canvas.grid(sticky=tk.S + tk.N)

    def mouse_y_scroll(self, event):
        if event.delta > 0:
            self.canvas.yview_scroll(-1, "units")
        elif event.delta < 0:
            self.canvas.yview_scroll(1, "units")

    def mouse_x_scroll(self, event):
        if event.delta > 0:
            self.canvas.xview_scroll(-1, "units")
        elif event.delta < 0:
            self.canvas.xview_scroll(1, "units")
