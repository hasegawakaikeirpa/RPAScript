import pandas as pd
import numpy as np

l = np.array(
    [
        [0, 0, 0, 0, "Tate"],
        [0, 0, 0, 0, "Yoko"],
        [1, 1, 1, 1, "Tate"],
        [1, 1, 1, 1, "Yoko"],
    ]
)
ind = [x for x in range(l.shape[0])]
df = pd.DataFrame(
    data=l,
    columns=["x1", "y1", "x2", "y2", "LineName"],
    index=ind,
)

ExtractColumn = np.full(df.shape[0], "")
ExtractColumn.astype(str)
print(ExtractColumn[0])

ExtractColumn[0] = ""
