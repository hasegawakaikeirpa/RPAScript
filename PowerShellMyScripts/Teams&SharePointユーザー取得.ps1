#Install-Module -Name ExchangeOnlineManagement
#Install-Module -Name Microsoft.Online.SharePoint.PowerShell
#Import-Module ExchangeOnlineManagement
#Import-Module Microsoft.Online.SharePoint.PowerShell
#-------------------------------------------------
#認証情報
#-------------------------------------------------
$user = 'hasegawarpa@hasegawakaikeirpa.onmicrosoft.com'
$pass = 'HaseK5121' | ConvertTo-SecureString -AsPlainText -Force
$credential = New-Object System.Management.Automation.PSCredential($user,$pass) 

#-------------------------------------------------
#前準備：チームをすべて取得
#-------------------------------------------------
#Connect-MicrosoftTeams -Credential $credential

#$allTeams = Get-Team

#-------------------------------------------------
#前準備：Microsoft365グループをすべて取得
#-------------------------------------------------
#Connect-ExchangeOnline -Credential $credential

#$allGroups = Get-UnifiedGroup -ResultSize Unlimited

#-------------------------------------------------
#前準備：SharePointサイトをすべて取得
#-------------------------------------------------
$SPOAdminCenter = "https://hasegawakaikeirpa-admin.sharepoint.com/_layouts/15/online/AdminHome.aspx"
#Connect-PnPOnline -Url $SPOAdminCenter -Credential $credential
Connect-SPOService -Url $SPOAdminCenter -Credential $credential
#$allSite = Get-PnPTenantSite | select Url,StorageUsageCurrent
$allGroups = Get-SPOSite -Limit ALL | ForEach {Get-SPOSiteGroup -Site $_.Url} | Format-Table
$allUser = Get-SPOSite -Limit ALL | ForEach {Get-SPOUser -Site $_.Url}
$outputFile = "D:\PythonScript\RPAScript\PowerShellMyScripts\Teams&SharePointGroups.csv"
$allUser | Export-Csv -Path $outputFile -Encoding UTF8 -NoTypeInformation -Append
$outputFile = "D:\PythonScript\RPAScript\PowerShellMyScripts\Teams&SharePointUsers.csv"
$allGroups | Export-Csv -Path $outputFile -Encoding UTF8 -NoTypeInformation -Append