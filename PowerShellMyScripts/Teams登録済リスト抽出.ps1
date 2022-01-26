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

#$data | Export-Csv -Path \\Sv05121a\e\C 作業台\RPA\ALLDataBase\関与先DB.csv -Encoding ASCII -NoTypeInformation -Delimiter `t　#登録済みのTeamsサイト一覧