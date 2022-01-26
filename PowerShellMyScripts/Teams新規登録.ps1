#関与先DBのTeamsTourokuが〇でないもので試算表提出がメールの関与先のTeamsサイトを作る

#サイトURL、アカウント、パスワード設定(多要素なのでInteractiveで認証)
$SiteURL = "https://hasegawakaikeirpa.sharepoint.com/sites/msteams_d42518"
$AdminAccount = 'hasegawarpa@hasegawakaikeirpa.onmicrosoft.com'
$AdminPass = 'HaseK5121'
Connect-PnPOnline –Url $SiteURL -Interactive
#-------------------------------------------------------------------------
$ListID = '2b326542-007f-4484-a799-c9a8bd32d86c'#リストIDを変数代入
Import-Module PnP.PowerShell
$data = @()#空配列作成
$data =(Get-PnPListItem -List $ListID).FieldValues#リストデータを全て配列代入
#$data#リスト見たいならここ 
Import-Module MicrosoftTeams
Connect-MicrosoftTeams #Teamsにログイン
#Get-Team#登録済みのTeamsサイト一覧
#以下を実行後SharePointURLとLISTIDが必要なので-le "10"を調整して少しづつ回す
for($i=1000; $i -le 4000; $i++) {
[string]$dataMirokuCode = $data[$i].MirokuCode
[string]$dataTKCJimusyoCode = $data[$i].TKCJimusyoCode
[string]$dataTKCKanyoCode = $data[$i].TKCKanyoCode
[string]$dataTKCKojinCode = $data[$i].TKCKojinCode
[string]$dataSyanaiCode = $data[$i].SyanaiCode
[string]$dataMirokuName = $data[$i].MirokuName
[string]$dataTKCName = $data[$i].TKCName
[string]$dataMAddressListName = $data[$i].MAddressListName
[string]$dataTeamsTouroku = $data[$i].TeamsTouroku
[string]$dataTeamsSakusei = $data[$i].elTaxTouroku #TeamsSakuseiKibou←Lists上はこれだがなぜかShell上ではelTaxTourokuになってる
[string]$dataMailHantei = $data[$i].SeikyuuHantei
[string]$dataTeamsURL = $data[$i].TeamsURL
[string]$DisplayNames = "$dataSyanaiCode" + "-" + "$dataTKCKojinCode" + " " + "$dataTKCName"　+ " 様" 
[string]$NickNames = $dataSyanaiCode + "-" + $dataTKCKojinCode
[string]$DataID = $data[$i].ID
#----------Temas登録済リスト抽出------------
    If($dataTeamsTouroku -ne "〇" -and $dataSyanaiCode -ne $null -and $dataTeamsSakusei -eq 1){
            New-Team -DisplayName $DisplayNames `
            -MailNickName $NickNames `
            -Owner $AdminAccount `
            -Visibility Private `
            -Description $DisplayNames

            Set-PnPListItem -List "$ListID" -Identity $DataID -Values @{"TeamsTouroku" = "〇"}

        }Else {
            #"登録済み" 

        }
#-----------------------------------------
}