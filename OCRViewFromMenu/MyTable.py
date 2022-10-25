import tkinter as tk

# from tkinter import *

# from pandastable import Table, TableModel, config

from pandastable import Table, TableModel
from csv import QUOTE_NONNUMERIC

# import DataGrid as DG
import pandas as pd
import os
import numpy as np
from chardet.universaldetector import UniversalDetector
import sqlite3 as sql


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
        self.bind("<Control-z>", self.undo)

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

        self.hand_row = self.get_row_clicked(event)
        self.hand_col = self.get_col_clicked(event)
        x, y = self.getCanvasPos(self.currentrow, self.currentcol - 1)
        rmin = self.visiblerows[0]
        rmax = self.visiblerows[-1] - 2
        cmax = self.visiblecols[-1] - 1
        cmin = self.visiblecols[0]
        FirstPos = self.currentrow

        if x is None:
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
                    x = 0
                else:
                    return
            else:
                self.currentcol = self.currentcol + 1
        elif event.keysym == "Left":
            if self.currentcol == 0:
                self.currentcol = self.cols - 1
                if self.currentrow != 0:
                    self.currentrow = self.currentrow - 1
            else:
                self.currentcol = self.currentcol - 1

        if self.currentcol > cmax or self.currentcol < cmin:
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
        self.hand_coltype = self.model.getColumnType(self.currentcol)
        return

    # --------------------------------------------------------------------
    def drawCellEntry(self, row, col, text=None):
        """When the user single/double clicks on a text/number cell,
        bring up entry window and allow edits."""
        if self.editable is False:
            return
        h = self.rowheight
        self.draw_model = self.model
        text = self.model.getValueAt(row, col)
        if pd.isnull(text):
            text = ""
        x1, y1, x2, y2 = self.getCellCoords(row, col)
        w = x2 - x1
        txtvar = tk.StringVar()
        txtvar.set(text)
        self.F_stack = str(text)
        # 代入テキストウィンドウの作成-------------------------------------------------------
        self.cellentry = tk.Entry(
            self.parentframe,
            width=20,
            textvariable=txtvar,
            takefocus=1,
            font=self.thefont,
        )
        self.cellentry.delete(0, tk.END)
        self.cellentry.insert(0, text)
        self.cellentry.icursor(tk.END)
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

        if self.importpath is None:
            self.importpath = os.getcwd()
        if filename is None:
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
        if dialog is True:
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
    def childrenSearch_sub(self, m):
        f = False
        while f is False:
            m = m.master
            if m.master is None:
                m_child = m.children
                break
        f = False
        while f is False:
            for m_cItem in m_child:
                try:
                    rm = m.children[m_cItem]
                    rm = rm.children["!application"]
                    print(rm.OCR_dbname)
                    f = True
                    m = rm
                    break
                except:
                    try:
                        rm = m.children[m_cItem]
                        print(rm.OCR_dbname)
                        f = True
                        m = rm
                        break
                    except:
                        print("next")
        return m

    # --------------------------------------------------------------------
    def childrenSearch(self):
        try:
            mf = False
            m = self.master
            mf = True
            m = self.childrenSearch_sub(m)
            return m
        except:
            if mf is True:
                m = self.childrenSearch_sub(m)
            else:
                return self

    # --------------------------------------------------------------------
    def childrenSearch_sub2(self, m):
        f = False
        while f is False:
            m = m.master
            if m.master is None:
                m_child = m.children
                break
        f = False
        while f is False:
            for m_cItem in m_child:
                try:
                    rm = m.children[m_cItem]
                    rm = rm.children["!application"]
                    print(rm.RView)
                    f = True
                    m = rm
                    break
                except:
                    try:
                        rm = m.children[m_cItem]
                        print(rm.RView)
                        f = True
                        rm = rm.RView.children["!frame"]
                        rm = rm.children["!frame2"]
                        m = rm.children["!mytablesql"]
                        break
                    except:
                        print("next")
        return m

    # --------------------------------------------------------------------
    def childrenSearch2(self):
        try:
            mf = False
            m = self.master
            mf = True
            m = self.childrenSearch_sub2(m)
            return m
        except:
            if mf is True:
                m = self.childrenSearch_sub2(m)
            else:
                return self

    # --------------------------------------------------------------------
    def HCE(self, row, col):
        """Callback for cell entry"""
        value = self.cellentry.get()
        m = self.childrenSearch()
        try:
            R_DF = CreateDB.readsql(self, m.OCR_dbname, m.OCR_tbname)
        except:
            R_DF = None
        if self.filtered == 1:
            df = self.dataframe
        else:
            df = None
        self.model.setValueAt(value, row, col, df=df)
        self.L_stack = value
        self.drawText(row, col, value, align=self.align)
        # self.delete("entry")
        self.gotonextCell()
        self.focus_set()
        if self.F_stack != self.L_stack:
            if R_DF is None:
                R_DF = CreateDB.CreateDF(
                    self, m.OCR_dbname, m.OCR_tbname, self.F_stack, self.L_stack
                )
                self.HCE_sub(m, R_DF)
            else:
                self.HCE_sub(m, R_DF)
        return

    # --------------------------------------------------------------------
    def HCE_sub(self, m, R_DF):
        print(m.pt_bln.get())
        if m.pt_bln.get() is True:
            R_DF = R_DF.drop_duplicates()
            R_DF = CreateDB.pdinsert(
                self,
                m.OCR_dbname,
                m.OCR_tbname,
                self.F_stack,
                self.L_stack,
                R_DF,
            )
            CreateDB.EntDF(self, m.OCR_dbname, m.OCR_tbname, R_DF)
            R_m = self.childrenSearch2()
            R_m.model.df = R_DF
            R_m.update()
            R_m.show()
        else:
            enc = MyTable.getFileEncoding(self.importFilePath)
            self.model.df.to_csv(
                self.importFilePath,
                index=False,
                encoding=enc,
                quoting=QUOTE_NONNUMERIC,
            )

    # --------------------------------------------------------------------
    def handle_left_click(self, event):
        """Respond to a single press"""

        self.clearSelected()
        self.allrows = False
        # which row and column is the click inside?
        rowclicked = self.get_row_clicked(event)
        colclicked = self.get_col_clicked(event)
        if colclicked is None:
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

    # --------------------------------------------------------------------
    def handle_left_release(self, event):
        """Handle left mouse button release event"""

        self.endrow = self.get_row_clicked(event)
        # df = self.model.df
        # colname = df.columns[self.currentcol]
        # dtype = df.dtypes[colname]

        # if dtype.name == "category":
        #     # drop down menu for category entry
        #     row = self.get_row_clicked(event)
        #     col = self.get_col_clicked(event)
        #     x1, y1, x2, y2 = self.getCellCoords(row, col)
        #     self.dropvar = tk.StringVar()
        #     val = self.model.getValueAt(row, col)
        #     # get categories
        #     optionlist = list(df[colname].cat.categories[:50])
        #     dropmenu = tk.OptionMenu(self, self.dropvar, val, *optionlist)
        #     self.dropvar.trace("w", self.handleEntryMenu)
        #     self.create_window(
        #         x1, y1, width=120, height=30, window=dropmenu, anchor="nw", tag="entry"
        #     )
        return

    # --------------------------------------------------------------------

    # def set_xviews(self, *args):
    #     """Set the xview of table and col header"""

    #     self.xview(*args)
    #     self.colheader.xview(*args)
    #     self.redrawVisible()
    #     return

    # -------------------------------------------------------------------------------------------------------------------------------


class CreateDB:
    """
    dbを作成する
    """

    def __init__(self, dbname, tbname):
        # すでに存在していれば、それにアスセスする。
        conn = sql.connect(dbname)

        # データベースへのコネクションを閉じる。(必須)
        conn.close()

    def CreateTable(self, dbname, tbname):

        conn = sql.connect(dbname)
        # sqliteを操作するカーソルオブジェクトを作成
        cur = conn.cursor()

        # personsというtableを作成してみる
        # 大文字部はSQL文。小文字でも問題ない。
        cur.execute("CREATE TABLE IF NOT EXISTS " + tbname + "(変更前 STRING,変更後 STRING)")

        # データベースへコミット。これで変更が反映される。
        conn.commit()
        conn.close()

    def CreateDF(self, dbname, tbname, F_stack, L_stack):
        List = [F_stack, L_stack]
        dfList = []
        dfList.append(List)
        df = pd.DataFrame(dfList, columns=["変更前", "変更後"])
        CreateDB.EntDF(self, dbname, tbname, df)
        return df

    def TableInsert(self, dbname, tbname, text):

        conn = sql.connect(dbname)
        cur = conn.cursor()

        # Insert文
        cur.execute("INSERT INTO " + tbname + "(変更前, 変更後) values(" + text + ")")
        # 同様に
        conn.commit()

        cur.close()
        conn.close()

    def CheckTable(self, dbname, tbname):

        conn = sql.connect(dbname)
        cur = conn.cursor()

        # terminalで実行したSQL文と同じようにexecute()に書く
        cur.execute("SELECT * FROM " + tbname)

        # 中身を全て取得するfetchall()を使って、printする。
        print(cur.fetchall())

        cur.close()
        conn.close()

    def readsql(self, dbname, tbname):

        conn = sql.connect(dbname)
        cur = conn.cursor()

        # terminalで実行したSQL文と同じようにexecute()に書く
        df = pd.read_sql_query("SELECT * FROM " + tbname, conn)

        cur.close()
        conn.close()

        return df

    def EntDF(self, dbname, tbname, df):

        conn = sql.connect(dbname)
        cur = conn.cursor()

        # データの投入
        df.to_sql(tbname, conn, if_exists="replace", index=False)
        cur.close()
        conn.close()

    def pdinsert(self, dbname, tbname, F_stack, L_stack, R_DF):
        List = [F_stack, L_stack]
        dfList = []
        dfList.append(List)
        df = pd.DataFrame(dfList, columns=["変更前", "変更後"])
        df_conc = pd.concat([R_DF, df], axis=0)
        return df_conc

    def CsvConvert(self, csv_url, dbname, tbname):
        # pandasでカレントディレクトリにあるcsvファイルを読み込む
        # csvには、1列目にyear, 2列目にmonth, 3列目にdayが入っているとする。
        enc = MyTable.getFileEncoding(csv_url)
        df = pd.read_csv(csv_url, encoding=enc)

        # カラム名（列ラベル）を作成。csv file内にcolumn名がある場合は、下記は不要
        # pandasが自動で1行目をカラム名として認識してくれる。
        # df.columns = ["year", "month", "day"]

        conn = sql.connect(dbname)
        cur = conn.cursor()

        # dbのnameをsampleとし、読み込んだcsvファイルをsqlに書き込む
        # if_existsで、もしすでにexpenseが存在していたら、書き換えるように指示
        df.to_sql(tbname, conn, if_exists="replace", index=False)

        # 作成したデータベースを1行ずつ見る
        select_sql = "SELECT * FROM " + tbname
        for row in cur.execute(select_sql):
            print(row)

        cur.close()
        conn.close()
