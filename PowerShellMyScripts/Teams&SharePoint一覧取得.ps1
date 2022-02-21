Install-Module -Name ExchangeOnlineManagement
Import-Module ExchangeOnlineManagement
#-------------------------------------------------
#認証情報
#-------------------------------------------------
$user = 'hasegawarpa@hasegawakaikeirpa.onmicrosoft.com'
$pass = 'HaseK5121' | ConvertTo-SecureString -AsPlainText -Force
$credential = New-Object System.Management.Automation.PSCredential($user,$pass) 

#-------------------------------------------------
#前準備：チームをすべて取得
#-------------------------------------------------
Connect-MicrosoftTeams -Credential $credential

$allTeams = Get-Team

#-------------------------------------------------
#前準備：Microsoft365グループをすべて取得
#-------------------------------------------------
Connect-ExchangeOnline -Credential $credential

$allGroups = Get-UnifiedGroup -ResultSize Unlimited

#-------------------------------------------------
#前準備：SharePointサイトをすべて取得
#-------------------------------------------------
$SPOAdminCenter = "https://hasegawakaikeirpa.sharepoint.com/"
Connect-PnPOnline -Url $SPOAdminCenter -Credential $credential

$allSite = Get-PnPTenantSite | select Url,StorageUsageCurrent

#-------------------------------------------------
#主処理：チームの情報をCSVに出力する
#-------------------------------------------------
$outputFile = "D:\PythonScript\RPAScript\PowerShellMyScripts\Teams&SharePointOutput.csv"

foreach($team in $allTeams)
{
    #SharePointサイトの容量を取得
    $group = $allGroups | where ExternalDirectoryObjectId -eq $team.GroupId
    $site  = $allSite   | where Url -EQ $group.SharePointSiteUrl
    $sharePointSiteSizeMB = $site.StorageUsageCurrent

    #チームの情報をCSVに出力
    $obj = New-Object PSObject
    $obj | Add-Member -MemberType NoteProperty -Name DisplayName -Value $team.DisplayName
    $obj | Add-Member -MemberType NoteProperty -Name Visibility  -Value $team.Visibility
    $obj | Add-Member -MemberType NoteProperty -Name Archived    -Value $team.Archived
    $obj | Add-Member -MemberType NoteProperty -Name SiteURL     -Value $group.SharePointSiteUrl
    $obj | Add-Member -MemberType NoteProperty -Name SiteSizeMB  -Value $sharePointSiteSizeMB

    $obj | Export-Csv -Path $outputFile -Encoding UTF8 -NoTypeInformation -Append
}