# import tkinter as tk
from tkinter import *

# from pandastable import Table, TableModel, config

from pandastable import Table, TableModel
from csv import QUOTE_NONNUMERIC

# import DataGrid as DG
import pandas as pd
import os
from CSVOut import getFileEncoding


class MyTable(Table):
    """
    pandastableのTableクラスの継承サブクラス設定
    クリックイベント等を書き換える事ができる
    """

    def __init__(self, parent=None, **kwargs):
        Table.__init__(self, parent, **kwargs)
        return

    # --------------------------------------------------------------------
    def doBindings(self):
        """Bind keys and mouse clicks, this can be overriden"""

        self.bind("<Button-1>", self.handle_left_click)

        self.bind("<Key-F2>", self.handle_double_click)

        self.bind("<Double-Button-1>", self.handle_double_click)
        self.bind("<Control-Button-1>", self.handle_left_ctrl_click)
        self.bind("<Shift-Button-1>", self.handle_left_shift_click)

        self.bind("<ButtonRelease-1>", self.handle_left_release)
        if self.ostyp == "darwin":
            # For mac we bind Shift, left-click to right click
            self.bind("<Button-2>", self.handle_right_click)
            self.bind("<Shift-Button-1>", self.handle_right_click)
        else:
            self.bind("<Button-3>", self.handle_right_click)

        self.bind("<B1-Motion>", self.handle_mouse_drag)
        # self.bind('<Motion>', self.handle_motion)

        self.bind("<Control-c>", self.copy)
        # self.bind("<Control-x>", self.deleteRow)
        # self.bind_all("<Control-n>", self.addRow)
        self.bind("<Delete>", self.clearData)
        self.bind("<Control-v>", self.paste)
        self.bind("<Control-a>", self.selectAll)
        self.bind("<Control-f>", self.findText)

        self.bind("<Right>", self.handle_arrow_keys)
        self.bind("<Left>", self.handle_arrow_keys)
        self.bind("<Up>", self.handle_arrow_keys)
        self.bind("<Down>", self.handle_arrow_keys)
        self.parentframe.master.bind_all("<KP_8>", self.handle_arrow_keys)
        self.parentframe.master.bind_all("<Return>", self.handle_arrow_keys)
        self.parentframe.master.bind_all("<Tab>", self.handle_arrow_keys)
        # if 'windows' in self.platform:
        self.bind("<MouseWheel>", self.mouse_wheel)
        self.bind("<Button-4>", self.mouse_wheel)
        self.bind("<Button-5>", self.mouse_wheel)
        self.focus_set()
        return

    # --------------------------------------------------------------------
    def handle_arrow_keys(self, event):
        """Handle arrow keys press"""
        # print event.keysym

        row = self.get_row_clicked(event)
        col = self.get_col_clicked(event)
        x, y = self.getCanvasPos(self.currentrow, self.currentcol - 1)
        rmin = self.visiblerows[0]
        rmax = self.visiblerows[-1] - 2
        cmax = self.visiblecols[-1] - 1
        cmin = self.visiblecols[0]
        FirstPos = self.currentrow

        if x == None:
            return

        if event.keysym == "Up":
            if self.currentrow == 0:
                return
            else:
                # self.yview('moveto', y)
                # self.rowheader.yview('moveto', y)
                self.currentrow = self.currentrow - 1
        elif event.keysym == "Down":
            if self.currentrow >= self.rows - 1:
                return
            else:
                self.currentrow = self.currentrow + 1
        elif event.keysym == "Right" or event.keysym == "Tab":
            if self.currentcol >= self.cols - 1:
                if self.currentrow < self.rows - 1:
                    self.currentcol = 0
                    self.currentrow = self.currentrow + 1
                else:
                    return
            else:
                self.currentcol = self.currentcol + 1
        elif event.keysym == "Left":
            if self.currentcol > 0:
                self.currentcol = self.currentcol - 1

        if self.currentcol > cmax or self.currentcol <= cmin:
            # print (self.currentcol, self.visiblecols)
            self.xview("moveto", x)
            self.colheader.xview("moveto", x)
            self.redraw()

        if self.currentrow < rmin and FirstPos == 0:
            # we need to shift y to page up enough
            vh = len(self.visiblerows) / 2
            x, y = self.getCanvasPos(self.currentrow - vh, 0)

        if self.currentrow >= rmax or self.currentrow <= rmin:
            self.yview("moveto", y)
            self.rowheader.yview("moveto", y)
            self.redraw()

        self.drawSelectedRect(self.currentrow, self.currentcol)
        coltype = self.model.getColumnType(self.currentcol)
        return

    # --------------------------------------------------------------------
    def drawCellEntry(self, row, col, text=None):
        """When the user single/double clicks on a text/number cell,
        bring up entry window and allow edits."""
        if self.editable == False:
            return
        h = self.rowheight
        model = self.model
        text = self.model.getValueAt(row, col)
        if pd.isnull(text):
            text = ""
        x1, y1, x2, y2 = self.getCellCoords(row, col)
        w = x2 - x1
        txtvar = StringVar()
        txtvar.set(text)
        # 代入テキストウィンドウの作成-------------------------------------------------------
        self.cellentry = Entry(
            self.parentframe,
            width=20,
            textvariable=txtvar,
            takefocus=1,
            font=self.thefont,
        )
        self.cellentry.delete(0, END)
        self.cellentry.insert(0, text)
        self.cellentry.icursor(END)
        self.cellentry.focus_set()
        self.cellentry.bind("<Return>", lambda x: self.HCE(row, col))

        self.entrywin = self.create_window(
            x1, y1, width=w, height=h, window=self.cellentry, anchor="nw", tag="entry"
        )
        # ---------------------------------------------------------------------------------
        return

    # --------------------------------------------------------------------
    def importCSV(self, filename=None, dialog=False, **kwargs):
        """Import from csv file"""

        if self.importpath == None:
            self.importpath = os.getcwd()
        if filename == None:
            filename = self.model.filedialog.askopenfilename(
                parent=self.master,
                defaultextension=".csv",
                initialdir=self.importpath,
                filetypes=[
                    ("csv", "*.csv"),
                    ("tsv", "*.tsv"),
                    ("txt", "*.txt"),
                    ("All files", "*.*"),
                ],
            )
        if not filename:
            return
        if dialog == True:
            impdialog = self.model.ImportDialog(self, filename=filename)
            df = impdialog.df
            if df is None:
                return
        else:
            df = pd.read_csv(filename, **kwargs)
        model = TableModel(dataframe=df)
        self.updateModel(model)
        self.redraw()
        self.importpath = os.path.dirname(filename)
        self.importFilePath = filename
        return

    # --------------------------------------------------------------------

    def HCE(self, row, col):
        """Callback for cell entry"""
        value = self.cellentry.get()
        if self.filtered == 1:
            df = self.dataframe
        else:
            df = None
        self.model.setValueAt(value, row, col, df=df)
        self.drawText(row, col, value, align=self.align)
        # self.delete("entry")
        self.gotonextCell()
        self.focus_set()
        enc = getFileEncoding(self.importFilePath)
        self.model.df.to_csv(
            self.importFilePath, index=False, encoding=enc, quoting=QUOTE_NONNUMERIC
        )
        return

    # --------------------------------------------------------------------
    def handle_left_click(self, event):
        """Respond to a single press"""

        self.clearSelected()
        self.allrows = False
        # which row and column is the click inside?
        rowclicked = self.get_row_clicked(event)
        colclicked = self.get_col_clicked(event)
        if colclicked == None:
            return
        self.focus_set()

        if hasattr(self, "cellentry"):
            self.cellentry.destroy()
        # ensure popup menus are removed if present
        if hasattr(self, "rightmenu"):
            self.rightmenu.destroy()
        if hasattr(self.colheader, "rightmenu"):
            self.colheader.rightmenu.destroy()

        self.startrow = rowclicked
        self.endrow = rowclicked
        self.startcol = colclicked
        self.endcol = colclicked
        # reset multiple selection list
        self.multiplerowlist = []
        self.multiplerowlist.append(rowclicked)
        if 0 <= rowclicked < self.rows and 0 <= colclicked < self.cols:
            self.setSelectedRow(rowclicked)
            self.setSelectedCol(colclicked)
            self.drawSelectedRect(self.currentrow, self.currentcol)
            self.drawSelectedRow()
            self.rowheader.drawSelectedRows(rowclicked)
            self.colheader.delete("rect")
        if hasattr(self, "cellentry"):
            self.cellentry.destroy()
        return

    # --------------------------------------------------------------------
    def handle_double_click(self, event):
        """Do double click stuff. Selected row/cols will already have
        been set with single click binding"""
        # "比較ファイルMain"
        if event.widget._name == "OCR抽出結果表Main":
            row = self.get_row_clicked(event)
            col = self.get_col_clicked(event)
            if event.widget.model.df.columns[col] == "比較対象行番号":
                # 比較対象DF検索--------------------------------------
                Dif_t = event.widget
                for i in range(100):
                    Dif_t = Dif_t.master
                    try:
                        print(Dif_t._name)
                    except:
                        Dif_t = Dif_t.children["!application"]
                        Dif_t = Dif_t.pt2
                        break
                # ---------------------------------------------------
                ewm = event.widget.model.df.iloc[row]
                ewm = int(ewm["比較対象行番号"]) - 1
                Dif_t.setSelectedRow(ewm)
                Dif_t.setSelectedCol(0)
                Dif_t.drawSelectedRect(ewm, 0)
                Dif_t.drawSelectedRow()
                return
            else:
                self.drawCellEntry(self.currentrow, self.currentcol)
                return
        else:
            row = self.get_row_clicked(event)
            col = self.get_col_clicked(event)
            self.drawCellEntry(self.currentrow, self.currentcol)
            return
