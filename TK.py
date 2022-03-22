import tkinter as tk
import numpy as np
import SQLConnect as sc
import numpy as np
from pandas import DataFrame
class App(tk.Tk):
    def __init__(self,FMSDF):
        super().__init__()
        self.title("Display DataFrame")
        
        self.df = FMSDF
        SQLDataRow = np.array(FMSDF).shape[0]#DF行数取得
        SQLDataCol = np.array(FMSDF).shape[1]#DF列数取得
        for r in range(50):
            for c in range(20):
                e = tk.Entry(self)
                e.insert(0,self.df.iloc[r,c])
                e.grid(row=r,column=c)
                e.bind("<KeyPress>",lambda event, row=r, column=c: self.change(event,row,column))
    def change(self,event,row,column):
        value = event.widget.get()
        self.df.iloc[row,column] = value
        print(self.df)
if __name__ == '__main__':
    WithA = "WITH SubFMS AS (SELECT * FROM m_kfmsmail WHERE cr_RecKbn = '0' GROUP BY vc_FMSKnrCd),"
    WithB = "SubKan AS (SELECT * FROM m_kkanyo WHERE cr_RecKbn = '0' GROUP BY vc_KnrCd)"
    SelectStr = "SELECT F.vc_KnrCd,F.vc_KanKojinNo_pk,F.vc_FMSKnrCd,F.vc_Name,K.vc_Name AS 'Yago',K.vc_HaizokuNo,K.vc_Haizoku,K.vc_KansaTantouNo,K.vc_KansaTantou,\
                K.vc_SubTantouNo,K.vc_SubTantou,K.vc_Sub_SubTantouNo,K.vc_Sub_SubTantou,F.vc_Hakkou,F.vc_PDFName,F.vc_SousinK,F.vc_Mail,F.vc_SousinK2,F.vc_Mail2,\
                F.vc_SousinK3,F.vc_Mail3,F.vc_SousinK4,F.vc_Mail4,F.vc_SousinK5,F.vc_Mail5 FROM SubFMS F INNER JOIN SubKan K ON F.vc_KnrCd = K.vc_KnrCd"
    sql = WithA + WithB + SelectStr
    FMSDF = sc.MySQLHeaderTo_df('ws77','SYSTEM','SYSTEM',3306,'test_db','utf8',sql)[1]
    app = App(FMSDF)
    app.mainloop()