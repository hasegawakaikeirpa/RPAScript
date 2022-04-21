import Function.GCloudVision as GCV

filein = r"D:\PythonScript\RPAScript\RPAPhoto\PDFeTaxReadForList\OCR0.png"
fileout = r"D:\PythonScript\RPAScript\RPAPhoto\PDFeTaxReadForList\OCRrender.png"
# GCV.render_doc_text(filein, fileout)
GF = GCV.rentxtver(
    filein, 1100, 5, 400, "::", 10
)  # 画像URL,横軸閾値,縦軸閾値,ラベル配置間隔,ラベル(str),同行として扱う縦間隔
print(GF[1])
