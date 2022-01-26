function Load-SPOnlineCSOMAssemblies
{
Load-SPOnlineCSOMAssembly "Microsoft.SharePoint.Client.dll"
Load-SPOnlineCSOMAssembly "Microsoft.SharePoint.Client.Publishing.dll"
Load-SPOnlineCSOMAssembly "Microsoft.SharePoint.Client.Runtime.dll"
Load-SPOnlineCSOMAssembly "Microsoft.SharePoint.Client.Search.dll"
}

Load-SPOnlineCSOMAssemblies

$siteUrl = "https://hasegawakaikeirpa.sharepoint.com/sites/msteams_d42518"

$ctx = New-Object Microsoft.SharePoint.Client.ClientContext($siteUrl)
$Credentials = New-Object Microsoft.SharePoint.Client.SharePointOnlineCredentials("hasegawarpa@hasegawakaikeirpa.onmicrosoft.com", (ConvertTo-SecureString -String "HaseK5121" -asplaintext -force))
$ctx.Credentials = $Credentials

　[System.Net.WebRequest]::GetSystemWebProxy()
　[System.Net.WebRequest]::DefaultWebProxy.Credentials = [System.Net.CredentialCache]::DefaultCredentials

$objList = $ctx.Web.Lists.GetByTitle("ドキュメント")
$ctx.Load($objList)
$ctx.ExecuteQuery

$query = New-Object Microsoft.SharePoint.Client.CamlQuery
$query.ViewXml="<View Scope='RecursiveAll'><Query><Where><Eq><FieldRef Name='FSObjType'/><Value Type='Integer'>0</Value></Eq></Where></Query></View>"

$objListItems = $objList.getItems($query)
$ctx.Load($objListItems)
$ctx.ExecuteQuery

foreach($item in $objListItems)
{
    $id = $item.Id.ToString()
    $Filename = $item["FileLeafRef"]
    $FilePath = $item["FileRef"]
    $Editor = $item["Editor"].LookupValue
    $Modified = $item["Modified"]
    $Size = $item["File_x0020_Size"]
    Write-Output ($id + "," + $Filename + "," + $Size + "," + $FilePath)
}

$ctx.Dispose()