import ContextTimeOut as CTO
import Function.PDFCellsImport as FPDF

SCode = "1026"
path_pdf = "//Sv05121a/e/電子ファイル/メッセージボックス/TEST/el/1026_和炎_広島市（償却資産・中区）_税務部固定資産税課償却資産係_申告受付完了通知.pdf"
PageVol = "1"
y = 0

tables = CTO.camelotTimeOut(path_pdf, PageVol, "")
tCells = FPDF.CellsImport(SCode, path_pdf, tables, y)
