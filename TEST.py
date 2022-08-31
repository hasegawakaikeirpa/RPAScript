import pandas as pd
import numpy as np
from chardet.universaldetector import UniversalDetector


def getFileEncoding(file_path):  # .format( getFileEncoding( "sjis.csv" ) )
    detector = UniversalDetector()
    with open(file_path, mode="rb") as f:
        for binary in f:
            detector.feed(binary)
            if detector.done:
                break
    detector.close()
    return detector.result["encoding"]


C_url = r"D:\PythonScript\RPAScript\RPAPhoto\TKC_DensiSinkoku\HoujinSyouhizeiJyusinMaster.CSV"
SerchEnc = format(getFileEncoding(C_url))
C_Master = pd.read_csv(C_url, encoding=SerchEnc)
C_np = np.array(C_Master)
ind = np.unique(C_np[:, 2], return_index=True)
ind = np.sort(ind[1])
C_np = C_np[ind]
