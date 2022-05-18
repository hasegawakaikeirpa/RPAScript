import os
import csv

MeUrl = os.getcwd().replace("\\", "/")  # 自分のパス
# 列名追記------------------------------------------------------------------------------
with open(
    MeUrl + r"/RPAPhoto/PDFReadForList/ColumnList.CSV",
    "a",
    encoding="utf-8",
) as Colup:
    ColupList = [
        "Test",
        "Test",
        "Test",
        "Test",
        "Test",
        "Test",
        "Test",
    ]
    writer = csv.writer(Colup)
    writer.writerow(ColupList)
# ----------------------------------------------------------------------------------------
