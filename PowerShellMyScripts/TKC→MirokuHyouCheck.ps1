
	#プログラムの処理
$URL = "\\Sv05121a\e\C 作業台\RPA\年調設定\年調システム登録済\処理済み\成功\syousuu\取得済"
$Folders = Get-ChildItem -Path $URL -Filter "*_*" #-Recurse
$Anthorarray = @()
$ErrMSG = @()

foreach ( $Foldersitem in $Folders){

    try {
            $KekkaURL = $Foldersitem.FullName + "\扶養情報インポート結果.csv"
            $KekkaCSV = Import-Csv $KekkaURL -Encoding Default
            [int]$KekkaCount = 0
            $Kekkaarray = @()

            foreach($KekkaCSVItem in $KekkaCSV){
                for ( $i=1 ; $i -le 10 ; $i++ )
                { 
                    $KekkaNo = [int]$KekkaCSVItem.("社員No")
                    $KekkaName = $KekkaCSVItem.("家族氏名" + $i)
                    if ($KekkaName -ne ""){[int]$KekkaCount = [int]$KekkaCount + 1}
                }
                $Kekka = [string]$KekkaNo + "_" + $KekkaCount
                $Kekkaarray += $Kekka
            }

            $NyuuryokuURL = $Foldersitem.FullName + "\扶養情報インポート用.csv"
            $NyuuryokuCSV = Import-Csv $NyuuryokuURL -Encoding Default -Header "社員No","扶養区分1","扶養区分2",
            "扶養区分3","扶養区分4","扶養区分5","扶養区分6","扶養区分7","扶養区分8","扶養区分9","扶養区分10","家族氏名1",
            "家族氏名2","家族氏名3","家族氏名4","家族氏名5","家族氏名6","家族氏名7","家族氏名8","家族氏名9","家族氏名10",
            "家族続柄1","家族続柄2","家族続柄3","家族続柄4","家族続柄5","家族続柄6","家族続柄7","家族続柄8","家族続柄9",
            "家族続柄10","家族生年月日1","家族生年月日2","家族生年月日3","家族生年月日4","家族生年月日5","家族生年月日6","家族生年月日7",
            "家族生年月日8","家族生年月日9","家族生年月日10","家族同居区分1","家族同居区分2","家族同居区分3","家族同居区分4","家族同居区分5",
            "家族同居区分6","家族同居区分7","家族同居区分8","家族同居区分9","家族同居区分10","家族障害者1","家族障害者2","家族障害者3",
            "家族障害者4","家族障害者5","家族障害者6","家族障害者7","家族障害者8","家族障害者9","家族障害者10","家族住所上段1","家族住所上段2",
            "家族住所上段3","家族住所上段4","家族住所上段5","家族住所上段6","家族住所上段7","家族住所上段8","家族住所上段9","家族住所上段10",
            "家族住所下段1","家族住所下段2","家族住所下段3","家族住所下段4","家族住所下段5","家族住所下段6","家族住所下段7","家族住所下段8",
            "家族住所下段9","家族住所下段10","家族ふりがな1","家族ふりがな2","家族ふりがな3","家族ふりがな4","家族ふりがな5","家族ふりがな6",
            "家族ふりがな7","家族ふりがな8","家族ふりがな9","家族ふりがな10","非居住区分1","非居住区分2","非居住区分3","非居住区分4","非居住区分5",
            "非居住区分6","非居住区分7","非居住区分8","非居住区分9","非居住区分10"
                    
            [int]$NyuuryokuCount = 0
            $Nyuuryokuarray = @()

            foreach($NyuuryokuCSVItem in $NyuuryokuCSV){
                for ( $i=1 ; $i -le 10 ; $i++ )
                { 
                    $NyuuryokuNo = [int]$NyuuryokuCSVItem.("社員No")
                    $NyuuryokuName = $NyuuryokuCSVItem.("家族氏名" + $i)
                    if ($NyuuryokuName -ne ""){[int]$NyuuryokuCount = [int]$NyuuryokuCount + 1}
                }
                $Nyuuryoku = [string]$NyuuryokuNo + "_" + $NyuuryokuCount
                $Nyuuryokuarray += $Nyuuryoku
            }
            $Flag = 0
            foreach ( $Nyuuryokuarrayitem in $Nyuuryokuarray){
                    foreach ( $Kekkaarrayitem in $Kekkaarray){
                        if ($Nyuuryokuarrayitem -eq $Kekkaarrayitem){
                            $Flag = 0
                            break
                        }else{
                            $Flag = 1
                        }
                    }
                if($Flag -eq 1){
                    $Anthorarray += $Foldersitem.FullName + "_" + $Nyuuryokuarrayitem + ","
                }
            }

    } catch {
        #エラーが発生した場合の処理
        $ErrMSG +=  $KekkaURL  + ","
    }
}

$Anthorarray | Out-File -FilePath "\\Sv05121a\e\C 作業台\RPA\年調設定\年調システム登録済\処理済み\成功\syousuu\登録結果一致.csv" -Encoding Default
$ErrMSG | Out-File -FilePath "\\Sv05121a\e\C 作業台\RPA\年調設定\年調システム登録済\処理済み\成功\syousuu\登録結果不一致.csv" -Encoding Default