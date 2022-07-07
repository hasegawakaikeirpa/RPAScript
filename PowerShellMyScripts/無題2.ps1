$inPath = "\\Sv05121a\e\電子ファイル\elTaxメッセージボックス\ダウンロード履歴.csv"
$incv = Import-csv -path $inPath -encoding default
$incv | Get-member -Mem

berType 'NoteProperty' | Select-Object -ExpandProperty 'Name'