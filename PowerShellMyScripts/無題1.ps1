# Client Side Object Model の読み込み
Add-Type -Path "C:\Program Files\PackageManagement\NuGet\Packages\Microsoft.SharePointOnline.CSOM.16.1.21012.12000\lib\net40-full\Microsoft.SharePoint.Client.dll"
Add-Type -Path "C:\Program Files\PackageManagement\NuGet\Packages\Microsoft.SharePointOnline.CSOM.16.1.21012.12000\lib\net40-full\Microsoft.SharePoint.Client.Runtime.dll"
 
$WebUrl = 'https://hasegawakaikeirpa.sharepoint.com/'
$loginUser = "hasegawarpa@hasegawakaikeirpa.onmicrosoft.com"
$Password = "HaseK5121"
 
$securePassword = ConvertTo-SecureString $Password -AsPlainText -Force
 
# コンテキストを作成
$Context =New-Object Microsoft.SharePoint.Client.ClientContext($WebUrl)
$credentials = New-Object Microsoft.SharePoint.Client.SharePointOnlineCredentials($loginUser, $securePassword) 
$Context.Credentials = $credentials
 
if (!$Context.ServerObjectIsNull.Value) 
{ 
    Write-Host $WebUrl " に接続完了" -ForegroundColor Green 
} 
 
$web = $Context.Web
$Context.Load($web)
$Context.ExecuteQuery()
 
Write-Host $web.title
Write-Host $web.Url
 
# SiteCheck というリストの内容を抽出
$listName = "SiteCheck"
 
$list = $web.Lists.GetByTitle($listName) 
$Context.Load($list)
$Context.ExecuteQuery()
 
Write-Host $list.Title
Write-Host $list.Description
 
$query = New-Object Microsoft.SharePoint.Client.CamlQuery
$query.ViewXml = ""
 
$listItems = $list.getItems($query)
$Context.Load($listItems)
$Context.ExecuteQuery()
$query.ListItemCollectionPosition = $listItems.ListItemCollectionPosition
 
foreach($item in $listItems)
{
        Write-Host  $item["Title"]
}