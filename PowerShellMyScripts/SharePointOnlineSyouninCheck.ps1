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

#-----------------------------------------------------------------------------------------------------
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

    #クエリ

    $NothingFlag = 0

$queryX = New-Object Microsoft.SharePoint.Client.CamlQuery
$queryX.ViewXml=""
$ListName = "社員名簿DB"
# Create List object
$SyainMeibo = $ctx.Web.Lists.GetByTitle($ListName)
$ctx.Load($SyainMeibo)
$ctx.ExecuteQuery()

$SyainMeiboItem = $SyainMeibo.getItems($queryX)
$ctx.Load($SyainMeiboItem)
$ctx.ExecuteQuery()
#-----------------------------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------------------------
$username = "hasegawarpa@hasegawakaikeirpa.onmicrosoft.com"
$password = "HaseK5121"
$siteUrl = "https://hasegawakaikeirpa.sharepoint.com/sites/msteams_4e2bee/"
#ログイン
$ctx = New-Object Microsoft.SharePoint.Client.ClientContext($siteUrl)
$Credentials = New-Object Microsoft.SharePoint.Client.SharePointOnlineCredentials($username, (ConvertTo-SecureString -String $password -asplaintext -force))
$ctx.Credentials = $Credentials

#プロキシ越え
　[System.Net.WebRequest]::GetSystemWebProxy()
　[System.Net.WebRequest]::DefaultWebProxy.Credentials = [System.Net.CredentialCache]::DefaultCredentials

    #クエリ

    $NothingFlag = 0

$queryX = New-Object Microsoft.SharePoint.Client.CamlQuery
$queryX.ViewXml=""
$ListName = "試算表承認一覧"
# Create List object
$Lister = $ctx.Web.Lists.GetByTitle($ListName)
$ctx.Load($Lister)
$ctx.ExecuteQuery()

$ListItems = $Lister.getItems($queryX)
$ctx.Load($ListItems)
$ctx.ExecuteQuery()

$ctx.Dispose()
#-----------------------------------------------------------------------------------------------------
#try {
$ErrorActionPreference = "silentlycontinue"
    foreach($itemX in $ListItems + 1)
    {
        $id = $itemX.Id.ToString()
        $Tantou = $itemX["Title"]
        $FiNames = $itemX["FileName"]
        $Tantouka = righters
        #Write-Output ($id + $Tantou + $FiNames)
        $ll = $ll + 1
        #If($ll -eq $ListItems.Count){
        #Pause
        #}
                #ドキュメント配下のファイル情報取得
                $objList = $ctx.Web.Lists.GetByTitle("ドキュメント")
                $ctx.Load($objList)
                $ctx.ExecuteQuery()

                $query = New-Object Microsoft.SharePoint.Client.CamlQuery
                $query.ViewXml="<View Scope='RecursiveAll'><Query><Where><Eq><FieldRef Name='FSObjType'/><Value Type='string'>0</Value></Eq></Where></Query></View>"
                $objListItems = $objList.getItems($query)
                $ctx.Load($objListItems)
                $ctx.ExecuteQuery()

                #クエリ指定のItemループ
                foreach($item in $objListItems)
                {
                    $Fileid = $item.Id.ToString()
                    $Filename = $item["FileLeafRef"]
                    $FilePath = $item["FileRef"].Replace('/sites/msteams_4e2bee/Shared Documents/承認待ち/', '').Replace('/' + $Filename , '')
                    $Editor = $item["Editor"].LookupValue
                    $Modified = $item["Modified"]
                    $Size = $item["File_x0020_Size"]

                    foreach($SMItem in $SyainMeiboItem)
                    {
                        if ($Tantou -eq $SMItem["Name"])
                        {
                            $TantoukaNo = $SMItem["Genhaizokucd"]
                            foreach($SMHItem in $SyainMeiboItem)
                            {
                                if ($TantoukaNo -eq $SMHItem["SyainNo"])
                                {   
                                $Tantouka = $SMHItem["Name"]
                                break
                                }
                            }                            
                        }
                    }

                    #Write-Output ($id + "," + $Filename + "," +  $FilePath)

                if ( $Tantou + $FiNames  -eq  $FilePath + $Filename ){
                    $NothingFlag = 0
                    Write-Output ($FilePath + $Filename  + $Tantou + $FiNames + $Tantouka)
                    break
                }
                else{
                    $NothingFlag = 1 
                }

            }
            if ( $NothingFlag -eq 1 ){
                $DelItem = $ListItems.GetById($id)
                $DelItem.DeleteObject()
            }else{
            $itemX["Haizoku"] = $Tantouka
            $itemX.Update()
            }
    }

$ErrorActionPreference = "continue"

$ctx.Dispose()