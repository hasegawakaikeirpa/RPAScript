#Install-Module -Name ExchangeOnlineManagement
Import-Module ExchangeOnlineManagement
#-------------------------------------------------
#認証情報
#-------------------------------------------------
$user = 'hasegawarpa@hasegawakaikeirpa.onmicrosoft.com'
$pass = 'HaseK5121' | ConvertTo-SecureString -AsPlainText -Force
$credential = New-Object System.Management.Automation.PSCredential($user,$pass) 

#-------------------------------------------------
#前準備：Microsoft365グループをすべて取得
#-------------------------------------------------
Connect-ExchangeOnline -Credential $credential

$allGroups = Get-UnifiedGroup -ResultSize Unlimited

$Temp=foreach ($i in Get-UnifiedGroup -ResultSize Unlimited | where {$_.Grouptype -Like "Universal"}) {Get-UnifiedGroupLinks -Identity $i.PrimarySmtpAddress -ResultSize Unlimited -Linktype members | select @{n="UnifiedGroupName";e={$i.DisplayName}},@{n="UnifiedGroupMailAddress";e={$i.PrimarySmtpAddress}},DisplayName,PrimarySmtpAddress} 
$outputFile = "D:\PythonScript\RPAScript\PowerShellMyScripts\Teams&SharePointO365Users.csv"
$Temp | Export-Csv -Encoding UTF8 -NoTypeInformation -Path $outputFile 