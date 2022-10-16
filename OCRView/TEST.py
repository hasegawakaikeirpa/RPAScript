import pandas as pd
import numpy as np

dl = [["OCRテキスト", "元帳テキスト"]]
df = pd.DataFrame(
    dl,
    columns=["OCRテキスト", "元帳テキスト"],
    index=None,
)
print(df)
