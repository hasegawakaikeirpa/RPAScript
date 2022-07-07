﻿#ヘッダー無のCSV結合
$URL = "\\Sv05121a\e\C 作業台\RPA\年調設定\抽出リスト"
$filetype = "*扶養情報インポート結果.csv"
$outputFile = $URL + "/扶養登録結果集計.csv"

# ヘッダー
$header = $confdir + "\\Sv05121a\e\C 作業台\RPA\年調設定\抽出リスト\扶養情報ヘッダー.txt"

# 本処理
# inフォルダ配下のファイルを読み取り
$files = Get-ChildItem $URL -include $filetype -Recurse
# マージファイルにヘッダを追加
Get-Content -Encoding UTF8 $header | Out-File $outputFile
# マージファイルに1行目（ヘッダ）を抜かしてファイル出力
#$files | Foreach-Object { $_ | Get-Content -Encoding Default | Out-File $outputFile -Append }
$filesRow = 0
$files | Foreach-Object {    
    $GetCSV = $_ |Get-Content -Encoding Default 
    $GetCSV | Select-Object *,@{Name='ファイル名';Expression={$files[$filesRow]}}
    $MargeCSV = @()
    $GetCSV | Foreach-Object {
        $MargeCSV += $_ + "," + $files[$filesRow]
    }
    $MargeCSV  | Select-Object -Skip 1  | Out-File $outputFile -Append
    $filesRow = $filesRow + 1 
    }
exit