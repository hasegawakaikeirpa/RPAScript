$excelFile = "\\Sv05121a\e\C 作業台\RPA\ALLDataBase\試算表作成依頼\試算表作成一覧.xlsm"
#$sheetName = "Sheet1"

$excelFile = (Get-ChildItem $excelFile).FullName
$excel = New-Object -ComObject Excel.Application
$excel.Visible = $false
$book = $excel.Workbooks.Open($excelFile, 0, $true)
$sheet = $book.Worksheets.Item(1)

#Write-Host $sheet.Cells.Item(1, 1).Text
$start = $sheet.Range("A1")
echo $start.Row     # ⇒ 6
echo $start.Column  # ⇒ 4
Write-Host $start.Row
Write-Host $start.Column