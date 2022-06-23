import os
import csv
import pandas as pd
import toml

if __name__ == "__main__":
    # toml読込------------------------------------------------------------------------------
    with open(os.getcwd() + r"/TKInterGUI/BankSetting.toml", encoding="utf-8") as f:
        Banktoml = toml.load(f)
        print(Banktoml)
    # --------------------------------------------------------------------------------------

    readcsv = []
    URL = r"D:\SouzokuOCR"
    FileName = r"D:\SouzokuOCR" + "\\ALLCSV.csv"
    for fd_path, sb_folder, sb_file in os.walk(URL):
        if fd_path == URL:
            for sb_fileItem in sb_file:
                imgurl = fd_path + "\\" + sb_fileItem
                if not FileName == imgurl:
                    with open(
                        imgurl,
                        "r",
                        newline="",
                    ) as inputfile:
                        r = 0
                        for row in csv.reader(inputfile):
                            if not r == 0:
                                if not row[7] == "":
                                    readcsv.append(row)
                            r += 1
    df = pd.DataFrame(readcsv, columns=Banktoml["JASouzoku"]["ColumnName"])
    df.to_csv(FileName, index=False, encoding="utf8")
