#Install-Module -Name MSOnline -Force
#Install-Module -Name ExchangeOnlineManagement -Force
#Install-Module -Name Microsoft.Online.SharePoint.PowerShell -Force
#Install-Module -Name AzureAD -Force
#Install-Module -Name MicrosoftTeams -Force
Import-Module -Name ExchangeOnlineManagement
Import-Module -Name Microsoft.Online.SharePoint.PowerShell
Import-Module -Name AzureAD
Import-Module -Name MicrosoftTeams
Import-Module -Name MSOnline

# hasegawarpa@hasegawakaikeirpa.onmicrosoft.com

#認証情報設定--------------------------------------------------------------------------------------------
$user = 'hasegawarpa@hasegawakaikeirpa.onmicrosoft.com'
$pass = 'HaseK5121' | ConvertTo-SecureString -AsPlainText -Force
$credential = New-Object System.Management.Automation.PSCredential($user,$pass) 
#--------------------------------------------------------------------------------------------------------

try {
    # インプットボックスを表示し、登録か削除を選択---------------------------------------------------------
    #　アセンブリの読み込み
    [void][System.Reflection.Assembly]::Load("Microsoft.VisualBasic, Version=8.0.0.0, Culture=Neutral, PublicKeyToken=b03f5f7f11d50a3a")
    #　インプットボックスの表示
    $userAc = [Microsoft.VisualBasic.Interaction]::InputBox("どちらか入力してください。登録=t 削除=s", "登録・削除選択")
    #--------------------------------------------------------------------------------------------------------
    #SharePoint管理センターにコネクト-----------------------------------------------------------------------------------------------------------------
    $CurrentDir = Split-Path $MyInvocation.MyCommand.Path
    $SPOAdminCenter = "https://hasegawakaikeirpa-admin.sharepoint.com/_layouts/15/online/AdminHome.aspx"
    Connect-MSOLService
    $CSVName = $CurrentDir + "\Teams&SharePointUsersEntry.csv"
    $user = Import-Csv $CSVName #user登録csvを読込み
    #-------------------------------------------------------------------------------------------------------------------------------------------------
    if ($userAc -eq "t"){
        #パイプラインでCSV項目を指定してユーザー登録[$_.UserPrincipalName]等がCSV側パラメーター-----------------------------------------------------------
        $user | ForEach-Object {New-MsolUser -UserPrincipalName $_.UserPrincipalName -FirstName $_.FirstName -LastName $_.LastName -DisplayName $_.DisplayName -Title $_.Title -Department $_.Department -Country $_.Country -UserType $_.UserType -Password $_.Password -alternateEmailAddress $_.alternateEmailAddress}
        #-------------------------------------------------------------------------------------------------------------------------------------------------
        # インプットボックスを表示し、登録か削除を選択---------------------------------------------------------
        #　アセンブリの読み込み
        [void][System.Reflection.Assembly]::Load("Microsoft.VisualBasic, Version=8.0.0.0, Culture=Neutral, PublicKeyToken=b03f5f7f11d50a3a")
        #　インプットボックスの表示
        $GroupAc = [Microsoft.VisualBasic.Interaction]::InputBox($_.UserPrincipalName + "グループ登録を行いますか？はい=y いいえ=n", "グループ登録選択")
        #--------------------------------------------------------------------------------------------------------
        if ($GroupAc -eq "y"){
            foreach($userItem in $user){
                $SyanaiCode = $userItem.GroupCode
                $UsPrName = $userItem.UserPrincipalName
                if([string]::IsNullOrEmpty($SyanaiCode)){
                    # インプットボックスを表示し、関与先コードを入力---------------------------------------------------------
                    #　アセンブリの読み込み
                    [void][System.Reflection.Assembly]::Load("Microsoft.VisualBasic, Version=8.0.0.0, Culture=Neutral, PublicKeyToken=b03f5f7f11d50a3a")
                    #　インプットボックスの表示
                    $SyanaiCode = [Microsoft.VisualBasic.Interaction]::InputBox("GroupCodeが空白です。登録する関与先コードを入力してください。", "関与先コード入力")
                    #--------------------------------------------------------------------------------------------------------
                    #AzureGroupにユーザー追加---------------------------------------------
                    $CA = get-azureadgroup -SearchString  "$SyanaiCode"　#関与先コードを含むAzureADGroupを抽出
                    $AZUser = Get-AzureADUser -Filter "userPrincipalName eq '$UsPrName'"　#Azureに追加したユーザーを抽出
                    Add-AzureADGroupMember -ObjectId $CA.ObjectId -RefObjectId $AZUser.ObjectId　#グループとユーザーのObjectIdを指定してグループにメンバー登録
                }else{
                    #AzureGroupにユーザー追加---------------------------------------------
                    $CA = get-azureadgroup -SearchString  "$SyanaiCode"　#関与先コードを含むAzureADGroupを抽出
                    $AZUser = Get-AzureADUser -Filter "userPrincipalName eq '$UsPrName'"　#Azureに追加したユーザーを抽出
                    Add-AzureADGroupMember -ObjectId $CA.ObjectId -RefObjectId $AZUser.ObjectId　#グループとユーザーのObjectIdを指定してグループにメンバー登録
                }
            }
        }
        #-------------------------------------------------------------------------------------------------------------------------------------------------
    }else{
        #Azureからユーザー削除----------------------------------------------------------------------------------------------------------------------------
        $user | ForEach-Object {Remove-MsolUser -UserPrincipalName $_.UserPrincipalName}　#全てのユーザーリストから削除
        $DelList = Get-MsolUser -ReturnDeletedUsers -All　#削除済みユーザーリストを抽出
        $DelList | ForEach-Object {Remove-MsolUser -UserPrincipalName $_.UserPrincipalName -RemoveFromRecycleBin}　#削除済みユーザーリストを削除(全削除)
        #-------------------------------------------------------------------------------------------------------------------------------------------------
        #[GroupCode]←関与先コード列名
    }
}
catch{
Write-Output ('Error message is ' + $_.Exception.Message)
}