# エラーが発生した場合、プログラムを終了する
$ErrorActionPreference = "Stop"

$env:PNPPOWERSHELL_UPDATECHECK="false"
#Install-Module -Name PnP.PowerShell
Update-Module -Name PnP.PowerShell
Import-Module PnP.PowerShell
Get-PnPChangeLog -Release 1.5.0

$url="https://hasegawakaikeirpa.sharepoint.com/sites/msteams_d42518"  
$listName="KanyoDB"  
$currentTime= $(get-date).ToString("yyyyMMddHHmmss")  
$logFilePath="\\Sv05121a\e\C 作業台\RPA\ALLDataBase\BU\Log\関与先DB\"+$currentTime+".txt"  
# Fields that has to be retrieved  
$Global:selectProperties=@(
"Title",
"MirokuCode",
"TKCJimusyoCode",
"TKCKanyoCode",
"TKCKojinCode",
"SyanaiCode",
"MirokuName",
"TKCName",
"MAddressListName",
"MirokuKokuzeiUserCode",
"MirokuTihouzeiUserID",
"TKCKokuzeiUserCode",
"TKCTihouzeiUserID",
"etaxPass",
"TantousyaCode",
"Tantousya",
"TantoukaCode",
"Tantouka",
"MailAddress",
"SeikyuuHantei",
"TKCKaijyo",
"SeiriBangou",
"HoujinBangou",
"Daihyousya",
"MirokuYagou",
"SharePointURL",
"TantouMA",
"MirokuTantou",
"TKCTantou",
"SharePointListId",
"TeamsTouroku",
"KessanDuki",
"KanyoKeitai",
"GyousyuCode",
"Gyousyu",
"Gyousyu2",
"TantouhyouName",
"HoujinKojin",
"YuubinBangou",
"Jyuusyo",
"Houmonnsaki2",
"TelNo",
"AccountantSoft",
"TantouListTantouka",
"TantouListTantousyaCD",
"TantouListKansaTantou",
"TantouListTantousyaCD2",
"TantouListKaikeiIkousaki",
"TantouListTantousyaCD3",
"TantouListKaikeiSub",
"TantouListTantousyaCD4",
"TantouListKaikeiSub2",
"TantouListSyahoTantouka",
"TantouListSyahoTantouCD",
"TantouListSyahoTantou",
"TantouListGetujihousyuu",
"TantouListKessanryou",
"TantouListKaikeisoftRental",
"TantouListPX",
"TantouListSX",
"TantouConsulhousyuu",
"TantouConsulnaiyou",
"TantouKyuuyokeisan",
"TantouKyuuyoSimebi",
"TantouKyuuyoSiharaibi",
"TantouKyuuyoNinzuu",
"TantouSyahohousyuu",
"TantouConsulCode",
"TantouConsulName",
"TantouConsulSubCode",
"TantouConsulSubName",
"TantouConsulSubCode2",
"TantouConsulSubName2",
"TantouKyuuyoCode",
"TantouKyuuyoName",
"TantouKyuuyoSubCode",
"TantouKyuuyoSubName",
"TantouKyuuyoSubCode2",
"TantouKyuuyoSubName2",
"TantouSyahoCode",
"TantouSyahoName",
"TantouSyahoSubCode",
"TantouSyahoSubName",
"TantouSyahoSubCode2",
"TantouSyahoSubName2",
"KanyosakiRank",
"tikuwari",
"MAddress0",
"elTaxTouroku",
"Keiyakujyoukyou2",
"TKChurigana",
"TantouListGyousyuBunrui",
"TantouListGyousyumoku",
"TantouListTantousyaCD5",
"TantouListKaikeiSub3",
"MSAccount",
"MSPass",
"MSTouroku",
"MSFolder",
"etaxDay",
"eltaxDay",
"eltaxPass"
);  
 			
## Start the Transcript  
Start-Transcript -Path $logFilePath   
 
 
## Export List to CSV ##  
function ExportList  
{  
    try  
    {  
        # Get all list items using PnP cmdlet  
        $listItems=(Get-PnPListItem -List $listName -Fields $Global:selectProperties).FieldValues
        #$listItems=(Get-PnPListItem -List $listName -Fields "Jyuusyo").FieldValues    
        $outputFilePath="\\Sv05121a\e\C 作業台\RPA\ALLDataBase\関与先DB.csv"  
  
        $hashTable=@()  
 
        # Loop through the list items  
        foreach($listItem in $listItems)  
        {  
            $obj=New-Object PSObject              
            $listItem.GetEnumerator() | Where-Object { $_.Key -in $Global:selectProperties }| ForEach-Object{ $obj | Add-Member Noteproperty $_.Key $_.Value}  
            $hashTable+=$obj;  
            $obj=$null;  
        }  
  
        $hashtable | export-csv -Encoding UTF8 $outputFilePath -NoTypeInformation  
     }  
     catch [Exception]  
     {  
        $ErrorMessage = $_.Exception.Message         
        Write-Host "Error: $ErrorMessage" -ForegroundColor Red          
     }  
}
$SiteURL = "https://hasegawakaikeirpa.sharepoint.com/sites/msteams_d42518"
$AdminAccount = 'hasegawarpa@hasegawakaikeirpa.onmicrosoft.com'
$AdminPass = 'HaseK5121'
$application = "b6d4cd5c-e3c2-49fa-a8e2-68829df9672a"
$path = "C:\Windows\System32\AzureADプリンシパル.pfx"
$tenantname = "hasegawakaikeirpa.onmicrosoft.com"

## Connect to SharePoint Online site  
#Connect-PnPOnline –Url $SiteURL -Interactive 

#Connect-PnPOnline -ClientId $application -CertificatePath $path -CertificatePassword (ConvertTo-SecureString -AsPlainText AdminPass -Force) -Url SiteURL -Tenant "f8cd21a0-3f1e-4378-ab3a-5d366d1a0d8f"
Connect-PnPOnline -ClientId $application -CertificatePath $path -CertificatePassword (ConvertTo-SecureString -AsPlainText $AdminPass -Force) -Url $SiteURL -Tenant $tenantname
## Call the Function  
ExportList  
 
## Disconnect the context  
Disconnect-PnPOnline  
 
## Stop Transcript  
Stop-Transcript    