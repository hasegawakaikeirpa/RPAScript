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

#プロキシ越え
　[System.Net.WebRequest]::GetSystemWebProxy()
　[System.Net.WebRequest]::DefaultWebProxy.Credentials = [System.Net.CredentialCache]::DefaultCredentials

#サイトURL
$siteUrl ="https://hasegawakaikeirpa.sharepoint.com/sites/msteams_d42518/"

#ユーザー
$username = "hasegawarpa@hasegawakaikeirpa.onmicrosoft.com"
$password = "HaseK5121"

#インスタンス生成
$context = New-Object Microsoft.SharePoint.Client.ClientContext($siteUrl)

#認証情報
$credentials = New-Object Microsoft.SharePoint.Client.SharePointOnlineCredentials($username, (ConvertTo-SecureString -String $password -asplaintext -force))
$context.Credentials = $credentials

$TitleArray =("関与先DB500")#,"関与先DB1000","関与先DB1500","関与先DB2000","関与先DB2500","関与先DB3000","関与先DB3500","関与先DB4000")

foreach($ListTitleName in $TitleArray)
{
#リスト名
$listName = $ListTitleName 
try
    {
        $counter=0
       
        $spQuery = New-Object Microsoft.SharePoint.Client.CamlQuery
        $spQuery.ViewXml = "<View><Query></Query><ViewFields><FieldRef Name='Id' /></ViewFields><RowLimit>100</RowLimit></View>"

        $list = $Context.Web.Lists.GetByTitle($listName)

        do
        {
            $items = $list.GetItems($spQuery);
            $Context.Load($items)

            $Context.ExecuteQuery()

            $count = $items.Count
            Write-Host "残りアイテム" $count "件" -ForegroundColor Yellow

            while ($items.Count -gt 0)
            {
                $items[0].DeleteObject()
            }

            $spQuery.ListItemCollectionPosition = $items.ListItemCollectionPosition
        }
        while ($spQuery.ListItemCollectionPosition -ne $null)

        $Context.ExecuteQuery()
        Write-Host "アイテム削除完了" -ForegroundColor Yellow
    }
catch
    {
        Write-Host -ForegroundColor Red $_.Exception.ToString()
    }
}