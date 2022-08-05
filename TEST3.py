import Function.MJSSPOPDFMarge as PDFM


Url = r"C:/Users/soumu/Desktop/RPAScript\RPAPhoto\MJS_SystemPrintOut\\All\\ListNumber.csv"
PDFUrl = r"C:/Users/soumu/Desktop/RPAScript\\RPAPhoto\\MJS_SystemPrintOut\\PDF"
SerchURL = r"\\nas-sv\B_監査etc\B2_電子ﾌｧｲﾙ\03_法人決算"
Title = r"792_ＲＲ\\u3000合同会社_RPA決算書"
No = 792
YearT = "2022"
PDFM.PDFMarge(Url, PDFUrl, SerchURL, Title, No, YearT)
