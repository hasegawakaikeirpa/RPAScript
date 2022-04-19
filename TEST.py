import Function.GCloudVision as GCV

filein = r"D:\PythonScript\RPAScript\RPAPhoto\PDFeTaxReadForList\OCR0.png"
fileout = r"D:\PythonScript\RPAScript\RPAPhoto\PDFeTaxReadForList\OCRrender.png"
# GCV.render_doc_text(filein, fileout)
GF = GCV.rentxtver(filein, 500, 5, 100, "::")  # 画像URL,横軸閾値,縦軸閾値,ラベル配置間隔,ラベル(str)
print(GF[1])
