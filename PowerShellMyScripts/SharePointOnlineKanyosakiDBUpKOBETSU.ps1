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
Import-Module Microsoft.Online.SharePoint.PowerShell

# SharepointOnline用のCSOMをロードする
[System.Reflection.Assembly]::LoadWithPartialName("Microsoft.SharePoint.Client") > $null
[System.Reflection.Assembly]::LoadWithPartialName("Microsoft.SharePoint.Client.Runtime") > $null

$username = "hasegawarpa@hasegawakaikeirpa.onmicrosoft.com"
$password = "HaseK5121"
$siteUrl = "https://hasegawakaikeirpa.sharepoint.com/sites/msteams_d42518/"
#ログイン
$ctx = New-Object Microsoft.SharePoint.Client.ClientContext($siteUrl)
$Credentials = New-Object Microsoft.SharePoint.Client.SharePointOnlineCredentials($username, (ConvertTo-SecureString -String $password -asplaintext -force))
$ctx.Credentials = $Credentials

#プロキシ越え
　[System.Net.WebRequest]::GetSystemWebProxy()
　[System.Net.WebRequest]::DefaultWebProxy.Credentials = [System.Net.CredentialCache]::DefaultCredentials

# エラーが発生した場合、プログラムを終了する
$ErrorActionPreference = "Stop"

$currentTime= $(get-date).ToString("yyyyMMddHHmmss")  
$logFilePath="\\Sv05121a\e\C 作業台\RPA\ALLDataBase\BU\Log\関与先DBUpLoad\"+$currentTime+".txt"  



#書き込み不可のリスト列名を配列代入
#Import-CsvでCSV読み取り--------------------------------------------------------------------------------------------------------------------------------------
#$PSVersionTable #PSバージョン確認
#Get-PSRepository #レポジトリ確認
#Install-Module -Name ImportExcel #モジュールインストール
#Find-Module ImportExcel #インポートExcel確認
#Get-Command -module ImportExcel #コマンドレット確認
#Import-Module ImportExcel
#Import-Module Import-Csv
$FilePath =  "\\Sv05121a\e\C 作業台\RPA\ALLDataBase\関与先DBUpLoadXYZXYZ.csv"
$CsvFile = Import-Csv $FilePath -Encoding Default
$CsvRETUMEI = $CsvFile | Get-member -MemberType 'NoteProperty' | Select-Object -ExpandProperty 'Name'
#-------------------------------------------------------------------------------------------------------------------------------------------------------------
#クエリ

## Start the Transcript  
Start-Transcript -Path $logFilePath   

$queryX = New-Object Microsoft.SharePoint.Client.CamlQuery
$queryX.ViewXml=""
$ListName = "関与先DB500"
#$ListName = "社員名簿DBTEST"
# Create List object
$Lister = $ctx.Web.Lists.GetByTitle($ListName)
#$ListerFild = $Lister.Fields
$ctx.Load($Lister)
$ctx.ExecuteQuery()
$ListItems = $Lister.getItems($queryX)
$ctx.Load($ListItems)
$ctx.ExecuteQuery()

$listInfo = $Lister.Fields
$ctx.Load($listInfo)
$ctx.ExecuteQuery()

try  
{  
    foreach ($Csvitem in $CsvFile)
    {$Ls = $Ls + 1
    $CsvTitle = [Int]$Csvitem.Title
    $CsvName = $Csvitem.SyanaiCode
          $ChangeList += ListFunc
          Write-Host = $ChangeList
    } 
}
 catch [Exception]  
{  
$ErrorMessage = $_.Exception.Message         
Write-Host "Error: $ErrorMessage" -ForegroundColor Red          
}  

$ctx.ExecuteQuery()  
$ctx.Dispose()

function ListFunc() {
  foreach ($script:itemX in $ListItems)
  {
  $ShareTitle = [Int]$itemX["Title"]
  $ShareName = $itemX["SyanaiCode"]

      if (($ShareTitle -eq $CsvTitle) -and ($ShareName -eq $CsvName))
      { #SPOAddAndList
      $LsLs = $LsLs + 1

          foreach ($CsvTitles in $CsvRETUMEI)
          {
          $itemXVal = $itemX.FieldValues.$CsvTitles
          $CsvitemVal = $Csvitem.$CsvTitles
            if($null -ne $itemXVal)
            {
                if ($itemXVal -eq $CsvitemVal)
                {
                      return [Int]$itemX["Title"] 
                      break  
                }else{
                    
                }
            }else
            {
                
            }                 
      
          }        
      }
  }
}