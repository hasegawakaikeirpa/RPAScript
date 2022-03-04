$TargetFolder = "\\Sv05121a\e\C 作業台\RPA\ウィルス対策\KasperskyLog"

# 詳細プロパティの取得

# シェルオブジェクトを作成
$Shell = New-Object -ComObject Shell.Application

# フォルダの指定
$Folder = $Shell.NameSpace($TargetFolder)
$Folders = Get-ChildItem $TargetFolder
# ファイルの指定

#for ($i=0; $i -lt 200; $i++){
#$File = $Folder.parseName('162.txt')
#$GET = $Folder.GetDetailsOf($File,10)
#Write-Host $GET
#}

foreach($FolderItem in $Folders){
$FN = $FolderItem.Name
$File = $Folder.parseName($FN)
$GET = $Folder.GetDetailsOf($File,10)
Write-Host $GET,",",$FN
}