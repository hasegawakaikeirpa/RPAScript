#======================SPO子リスト登録ファンクション==========================
function SPOAddAndList{
#SPO子リスト要素数ループ

#SPO親リストのTitle($Nos)と子リストTitle($NosX)の一致判定

                            #子リストのアイテムが親リストアイテムと一致したら親リストの列数分ループ
                            foreach ($field in $listInfo) 
                            {
                                $Str = $itemX[$field.Title]#親リストの値
                                $coln = $field.StaticName#親リストの列名
                                $Aruyo = 0　#$fieldアイテムが書き込みエラーになる列名なら1になる
                                #書き込みエラーになる列名を代入した配列要素分ループ
                                foreach($Arrayitem in $TitleArray)
                                {
                                    if($coln -eq $Arrayitem)
                                    {$Aruyo = 1　#$fieldアイテムが書き込みエラーになる列名なら1になる
                                    break　#$Arrayitemループ抜ける
                                    }else{　#書き込みエラーにならない列名ならなにもしない                            
                                    }
                                }
                                #書き込みエラーになる列名配列ループ終了後＄Aruyoフラグを判定
                                if (-not($Aruyo -eq 1))
                                {　#書き込みエラーになる列名ならなにもしない                                
                                    try {
                                    $ErrorActionPreference = "silentlycontinue"
                                        #書き込みエラーにならない列名なら読込んだ子リストの値を親リストからコピー
                                            #if(-not($ChildListItem[$coln] -eq $itemX[$coln]))
                                            #{
                                                $ListerX[$coln] = $itemX[$coln]
                                            #}
                                        }catch{ #スクリプトエラー等のキャッチ
                                        write-host $coln
                                        }
                                }
                            }
                            $ListerX.Update()
                            $Ctx.ExecuteQuery()
                            break
           }


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

#書き込み不可のリスト列名を配列代入
$TitleArray =(
"LinkTitleNoMenu",
"LinkTitle",
"LinkTitle2",
"ID",
"ContentType",
"Modified",
"Created",
"Author",
"Editor",
"_HasCopyDestinations",
"_CopySource",
"owshiddenversion",
"WorkflowVersion",
"_UIVersion",
"_UIVersionString",
"Attachments",
"_ModerationStatus",
"Edit",
"SelectTitle",
"InstanceID",
"Order",
"GUID",
"WorkflowInstanceID",
"FileRef",
"FileDirRef",
"Last_x0020_Modified",
"Created_x0020_Date",
"FSObjType",
"SortBehavior",
"PermMask",
"PrincipalCount",
"FileLeafRef",
"UniqueId",
"SyncClientId",
"ProgId",
"ScopeId",
"HTML_x0020_File_x0020_Type",
"_EditMenuTableStart",
"_EditMenuTableStart2",
"_EditMenuTableEnd",
"LinkFilenameNoMenu",
"LinkFilename",
"LinkFilename2",
"DocIcon",
"ServerUrl",
"EncodedAbsUrl",
"BaseName",
"MetaInfo",
"_Level",
"_IsCurrentVersion",
"ItemChildCount",
"FolderChildCount",
"Restricted",
"OriginatorId",
"NoExecute",
"ContentVersion",
"_ComplianceFlags",
"_ComplianceTag",
"_ComplianceTagWrittenTime",
"_ComplianceTagUserId",
"_IsRecord",
"AccessPolicy",
"_VirusStatus",
"_VirusVendorID",
"_VirusInfo",
"AppAuthor",
"AppEditor",
"SMTotalSize",
"SMLastModifiedDate",
"SMTotalFileStreamSize",
"SMTotalFileCount",
"_CommentFlags",
"_CommentCount")

#クエリ

$NothingFlag = 0

$queryX = New-Object Microsoft.SharePoint.Client.CamlQuery
$queryX.ViewXml=""
$ListName = "関与先DB"
# Create List object
$Lister = $ctx.Web.Lists.GetByTitle($ListName)
$ListerFild = $Lister.Fields
$ctx.Load($Lister)
$ctx.ExecuteQuery()
$ListItems = $Lister.getItems($queryX)
$ctx.Load($ListItems)
$ctx.ExecuteQuery()

$listInfo = $Lister.Fields
$ctx.Load($listInfo)
$ctx.ExecuteQuery()

foreach ($itemX in $ListItems)
{
$Nos = [int]$itemX["Title"]
Write-Host $Nos
    #if(($Nos -igt 500) -and ($Nos -ilt 1000))
    if($Nos -le 500){

#==========================================================================================
    }elseif(($Nos -gt 3000) -and ($Nos -le 3500)){
    write-host "3500未満"
#===================================リスト指定=============================================
        $query = New-Object Microsoft.SharePoint.Client.CamlQuery
        $query.ViewXml=""
        $ListNameX = "関与先DB3500"
        # Create List object
        $ListerX = $ctx.Web.Lists.GetByTitle($ListNameX)
        $ctx.Load($ListerX)
        $ctx.ExecuteQuery()
        $ListerFildX = $ListerX.getItems($query)
        $ListItemInfo = New-Object Microsoft.SharePoint.Client.ListItemCreationInformation  
        $ListItem = $ListerX.AddItem($ListItemInfo)
#==========================================================================================
#===================================リスト登録=============================================
        SPOAddAndList
#==========================================================================================
    }elseif(($Nos -gt 3500) -and ($Nos -le 4000)){
    write-host "4000未満"
#===================================リスト指定=============================================
        $query = New-Object Microsoft.SharePoint.Client.CamlQuery
        $query.ViewXml=""
        $ListNameX = "関与先DB4000"
        # Create List object
        $ListerX = $ctx.Web.Lists.GetByTitle($ListNameX)
        $ctx.Load($ListerX)
        $ctx.ExecuteQuery()
        $ListerFildX = $ListerX.getItems($query)
        $ListItemInfo = New-Object Microsoft.SharePoint.Client.ListItemCreationInformation  
        $ListItem = $ListerX.AddItem($ListItemInfo)
#==========================================================================================
#===================================リスト登録=============================================
        SPOAddAndList
#==========================================================================================
    }else{
    }
        #foreach ($field in $listInfo) 
        #{
            #$coln = $itemX[$field.Title]
            #Write-Host $coln         # こっちがタイトル
            #Write-Host $Nos
        #}
}

$ErrorActionPreference = "continue"

$ctx.Dispose()