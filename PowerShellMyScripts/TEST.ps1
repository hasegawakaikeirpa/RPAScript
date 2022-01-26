#Sharepointリスト読み取り------------------------------------------------------------------------------------------------------------------------------------
#モジュール確認
#Get-Module -Name Microsoft.Online.SharePoint.PowerShell -ListAvailable | Select Name,Version
#Office365に接続
#Connect-SPOService -Url "https://hasegawakaikeirpa-admin.sharepoint.com/" -Credential "hasegawarpa@hasegawakaikeirpa.onmicrosoft.com"
#Office365管理者URL
#https://hasegawakaikeirpa.sharepoint.com-admin.sharepoint.com/
#コマンド確認
#Get-Command -Module Microsoft.Online.SharePoint.PowerShell
#Install-Package Microsoft.SharePointOnline.CSOM -Version 16.0.20912.12000
#Install-Package Microsoft.SharePointOnline.CSOM -Force
#Import-Module Microsoft.Online.SharePoint.PowerShell

# エラーが発生した場合、プログラムを終了する
$ErrorActionPreference = "Stop"

#書き込み不可のリスト列名を配列代入
#Import-CsvでCSV読み取り--------------------------------------------------------------------------------------------------------------------------------------
#$PSVersionTable #PSバージョン確認
#Get-PSRepository #レポジトリ確認
#Install-Module -Name ImportExcel #モジュールインストール
#Find-Module ImportExcel #インポートExcel確認
#Get-Command -module ImportExcel #コマンドレット確認
#Import-Module ImportExcel
#Import-Module Import-Csv
$FilePath =  "D:\HeidiCSVTEST.csv"
$CsvFile = Import-Csv $FilePath -Encoding Default
#CSVオブジェクトの列名を配列代入
$CsvRETUMEI = $CsvFile | Get-member -MemberType 'NoteProperty' | Select-Object -ExpandProperty 'Name'
#-------------------------------------------------------------------------------------------------------------------------------------------------------------
#クエリ

foreach ($Csvitem in $CsvFile)
{
    foreach ($CsvTitle in $CsvRETUMEI)
    {
        write-host $CsvTitle
        write-host $Csvitem.$CsvTitle
    }
}
