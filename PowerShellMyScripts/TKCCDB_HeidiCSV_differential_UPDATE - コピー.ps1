function LoadDBs{　#引数の関与先がDBにないかSelect文を投げる

    [CmdletBinding()]
    param (
        [Parameter(Mandatory = $true)]
        [Object[,]]$DimArrayList
    )

    Add-Type -Path 'C:\Program Files (x86)\MySQL\MySQL Connector Net 8.0.27\Assemblies\v4.5.2\MySQL.Data.dll'
 
    [string]$mySQLHost             = 'ws77'
    [string]$mySQLPort             = '3306'
    [string]$mySQLUserName         = 'SYSTEM'
    [string]$mySQLPassword         = 'SYSTEM'
    [string]$mySQLDB               = 'kanyodb'
    [string]$mySQLConnectionString = "server='$mySQLHost';port='$mySQLPort';uid='$mySQLUserName';pwd=$mySQLPassword;database=$mySQLDB"
     
    $connection = New-Object MySql.Data.MySqlClient.MySqlConnection($mySQLConnectionString)
    $connection.ConnectionString = $mySQLConnectionString
     
    # 接続
    try
    {
        $connection.Open()
         Write-Verbose '接続OK'
     
    }
    catch
    {
        Write-Warning '接続に失敗'
        $connection.Close()
    }
     
    # SQL実行
    $command = $connection.CreateCommand()
    $command.CommandText = "SELECT * FROM kanyodb_deletelist WHERE SyanaiCode = " + $DimArrayList.SyanaiCode + " AND TKCName = '" + $DimArrayList.TKCName + "'" + " AND HoujinBangou = '" + $DimArrayList.HoujinBangou + "'"
    write-Host $command.CommandText 

    Write-Verbose 'SQL実行します'
     
    try
    {
        $result = $command.ExecuteReader()
        Write-Verbose 'SQL実行しました'
    }
    catch
    {
        Write-Warning 'SQL実行に失敗'
        $connection.Close()
    }
     
    # Datatableにデータをぶっ込む
    $dataTable = New-Object "System.Data.Datatable"
    $dataTable.Load($result)
    $Anser = $dataTable.GetList().Count
    return $Anser 
    # 終了
    $connection.Close()
    Write-Verbose '終了'
    
}
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------
function LoadDBLength{　#DeleteListの行数をMeasure-Object -Lineで数える
    Add-Type -Path 'C:\Program Files (x86)\MySQL\MySQL Connector Net 8.0.27\Assemblies\v4.5.2\MySQL.Data.dll'
    #Add-Type -Path 'C:\Program Files (x86)\MySQL\MySQL Connector Net 8.0.27\Assemblies\v4.5.2\Renci.SshNet.dll'
     
    [string]$mySQLHost             = 'ws77'
    [string]$mySQLPort             = '3306'
    [string]$mySQLUserName         = 'SYSTEM'
    [string]$mySQLPassword         = 'SYSTEM'
    [string]$mySQLDB               = 'kanyodb'
    [string]$mySQLConnectionString = "server='$mySQLHost';port='$mySQLPort';uid='$mySQLUserName';pwd=$mySQLPassword;database=$mySQLDB"
     
    $connection = New-Object MySql.Data.MySqlClient.MySqlConnection($mySQLConnectionString)
    $connection.ConnectionString = $mySQLConnectionString
     
    # 接続
    try
    {
        $connection.Open()
         Write-Verbose '接続OK'
     
    }
    catch
    {
        Write-Warning '接続に失敗'
        $connection.Close()
    }
     
    # SQL実行
    $command = $connection.CreateCommand()
    $command.CommandText = 'SELECT * FROM kanyodb_deletelist'
    Write-Verbose 'SQL実行します'
     
    try
    {
        $result = $command.ExecuteReader()
        Write-Verbose 'SQL実行しました'
    }
    catch
    {
        Write-Warning 'SQL実行に失敗'
        $connection.Close()
    }
     
    # Datatableにデータをぶっ込む
    $dataTable = New-Object "System.Data.Datatable"
    $dataTable.Load($result)
    $dataTable | Format-Table 
    # 終了
    $connection.Close()
    Write-Verbose '終了'
    
    #return $dataTable.Count
    return $dataTable | Measure-Object -Line
}
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------
function UPMySQL{　#KanyoDBの元データをUPDATE文で書き換える

    [CmdletBinding()]
    param (
        [int]$TitleX, #Title
        [string]$TKCJimusyoCodeX,  #TKCJimusyoCode
        [string]$TKCKanyoCodeX,  #TKCKanyoCode
        [int]$SyanaiCodeX,   #SyanaiCode   
        [string]$TKCNameX,  #TKCName
        [string]$TKCKokuzeiUserCodeX,    #TKCKokuzeiUserCode
        [string]$TKCTihouzeiUserIDX,    #TKCTihouzeiUserID
        [int]$TantouListTantousyaCDX,  #TantouListTantousyaCD
        [string]$TantouListKansaTantouX,  #TantouListKansaTantou
        [int]$TantouListTantoukacdX,   #TantouListTantoukacd
        [string]$TantouListTantoukaX,  #TantouListTantouka
        [string]$MailAddressX,  #MailAddress
        [string]$TKCKaijyoX,    #TKCKaijyo
        [string]$SeiriBangouX,  #SeiriBangou
        [string]$HoujinBangouX,  #HoujinBangou
        [string]$DaihyousyaX,    #Daihyousya
        [string]$KessanDukiX,  #KessanDuki
        [string]$YuubinBangouX,  #YuubinBangou
        [string]$JyuusyoX,    #Jyuusyo
        [string]$Houmonnsaki2X,    #Houmonnsaki2
        [string]$TelNoX,  #TelNo
        [string]$AccountantSoftX  #AccountantSoft
    )
[Array]$SQLPar = @([int]$TitleX, #Title
[string]$TKCJimusyoCodeX,  #TKCJimusyoCode
[string]$TKCKanyoCodeX,  #TKCKanyoCode
[int]$SyanaiCodeX,   #SyanaiCode   
[string]$TKCNameX,  #TKCName
[string]$TKCKokuzeiUserCodeX,    #TKCKokuzeiUserCode
[string]$TKCTihouzeiUserIDX,    #TKCTihouzeiUserID
[int]$TantouListTantousyaCDX,  #TantouListTantousyaCD
[string]$TantouListKansaTantouX,  #TantouListKansaTantou
[int]$TantouListTantoukacdX,   #TantouListTantoukacd
[string]$TantouListTantoukaX,  #TantouListTantouka
[string]$MailAddressX,  #MailAddress
[string]$TKCKaijyoX,    #TKCKaijyo
[string]$SeiriBangouX,  #SeiriBangou
[string]$HoujinBangouX,  #HoujinBangou
[string]$DaihyousyaX,    #Daihyousya
[string]$KessanDukiX,  #KessanDuki
[string]$YuubinBangouX,  #YuubinBangou
[string]$JyuusyoX,    #Jyuusyo
[string]$Houmonnsaki2X,    #Houmonnsaki2
[string]$TelNoX,  #TelNo
[string]$AccountantSoftX  #AccountantSoft
)
    Add-Type -Path 'C:\Program Files (x86)\MySQL\MySQL Connector Net 8.0.27\Assemblies\v4.5.2\MySQL.Data.dll'
    [string]$mySQLHost             = 'ws77'
    [string]$mySQLPort             = '3306'
    [string]$mySQLUserName         = 'SYSTEM'
    [string]$mySQLPassword         = 'SYSTEM'
    [string]$mySQLDB               = 'kanyodb'
    [string]$mySQLConnectionString = "server='$mySQLHost';port='$mySQLPort';uid='$mySQLUserName';pwd=$mySQLPassword;database=$mySQLDB"
    $DeleteDayPar = Get-Date -DisplayHint DateTime -Format "yyyy-MM-dd_hh-mm-ss" #削除した日付を今日で指定 
    $connection = New-Object MySql.Data.MySqlClient.MySqlConnection($mySQLConnectionString)
    $connection.ConnectionString = $mySQLConnectionString
    $outputFilePath="\\Sv05121a\e\C 作業台\RPA\ALLDataBase\BU\SQLLog\SQLLog" + $DeleteDayPar + ".csv"
    $HeidiURL = "\\Sv05121a\e\C 作業台\RPA\ALLDataBase\Heidi関与先DB.csv"
    $HeidiTable = Import-CSV -Encoding Default $HeidiURL
    $TitleXNo = $TitleX[0] 
    $propNames = $HeidiTable | Get-Member -MemberType Properties | Select-Object -ExpandProperty Name #引数リストの列名取得
    $propNames | ForEach-Object{$x = $x + 1 #列名分ぶんまわし
        if($x -eq $propNames.Length){ #列名数最後は,をつけない為の条件文
            if([String]$_ -eq "TKCJimusyoCode"){
                $commandValueText = $commandValueText + $_ + " = '" + $TKCJimusyoCodeX 
            }elseif([String]$_ -eq "TKCKanyoCode"){
                $commandValueText = $commandValueText + $_ + " = '" + $TKCKanyoCodeX 
            }elseif([String]$_ -eq "SyanaiCode"){
                $commandValueText = $commandValueText + $_ + " = " + $SyanaiCodeX 
            }elseif([String]$_ -eq "TKCName"){
                $commandValueText = $commandValueText + $_ + " = '" + $TKCNameX 
            }elseif([String]$_ -eq "TKCKokuzeiUserCode"){
                $commandValueText = $commandValueText + $_ + " = '" + $TKCKokuzeiUserCodeX 
            }elseif([String]$_ -eq "TKCTihouzeiUserID"){
                $commandValueText = $commandValueText + $_ + " = '" + $TKCTihouzeiUserIDX 
            }elseif([String]$_ -eq "TantouListTantousyaCD"){
                $commandValueText = $commandValueText + $_ + " = " + $TantouListTantousyaCDX 
            }elseif([String]$_ -eq "TantouListKansaTantou"){
                $commandValueText = $commandValueText + $_ + " = '" + $TantouListKansaTantouX 
            }elseif([String]$_ -eq "TantouListTantoukacd"){
                $commandValueText = $commandValueText + $_ + " = " + $TantouListTantoukacdX 
            }elseif([String]$_ -eq "TantouListTantouka"){
                $commandValueText = $commandValueText + $_ + " = '" + $TantouListTantoukaX 
            }elseif([String]$_ -eq "MailAddress"){
                $commandValueText = $commandValueText + $_ + " = '" + $MailAddressX 
            }elseif([String]$_ -eq "TKCKaijyo"){
                $commandValueText = $commandValueText + $_ + " = '" + $TKCKaijyoX 
            }elseif([String]$_ -eq "SeiriBangou"){
                $commandValueText = $commandValueText + $_ + " = '" + $SeiriBangouX 
            }elseif([String]$_ -eq "HoujinBangou"){
                $commandValueText = $commandValueText + $_ + " = '" + $HoujinBangouX 
            }elseif([String]$_ -eq "Daihyousya"){
                $commandValueText = $commandValueText + $_ + " = '" + $DaihyousyaX 
            }elseif([String]$_ -eq "KessanDuki"){
                $commandValueText = $commandValueText + $_ + " = '" + $KessanDukiX 
            }elseif([String]$_ -eq "YuubinBangou"){
                $commandValueText = $commandValueText + $_ + " = '" + $YuubinBangouX 
            }elseif([String]$_ -eq "Jyuusyo"){
                $commandValueText = $commandValueText + $_ + " = '" + $JyuusyoX 
            }elseif([String]$_ -eq "Houmonnsaki2"){
                $commandValueText = $commandValueText + $_ + " = '" + $Houmonnsaki2X 
            }elseif([String]$_ -eq "TelNo"){
                $commandValueText = $commandValueText + $_ + " = '" + $TelNoX 
            }elseif([String]$_ -eq "AccountantSoft"){
                $commandValueText = $commandValueText + $_ + " = '" + $AccountantSoftX
            }elseif(([String]$_ -eq "TantouListTantousyaCD2") -or ([String]$_ -eq "TantouListTantousyaCD3") -or 
            ([String]$_ -eq "TantouListTantousyaCD4") -or ([String]$_ -eq "TantouListTantousyaCD5") -or 
            ([String]$_ -eq "TantouListSyahoTantoukaCD") -or ([String]$_ -eq "TantouListSyahoTantouCD") -or
            ([String]$_ -eq "TantouConsulCode") -or ([String]$_ -eq "TantouConsulSubCode") -or
            ([String]$_ -eq "TantouConsulSubCode2") -or ([String]$_ -eq "TantouKyuuyoCode") -or
            ([String]$_ -eq "TantouKyuuyoSubCode") -or ([String]$_ -eq "TantouKyuuyoSubCode2") -or
            ([String]$_ -eq "TantouSyahoCode") -or ([String]$_ -eq "TantouSyahoSubCode") -or
            ([String]$_ -eq "TantouSyahoSubCode2") -or
            ([String]$_ -eq "TantouListGetujihousyuu") -or ([String]$_ -eq "TantouListKessanryou") -or
            ([String]$_ -eq "TantouListKaikeisoftRental") -or ([String]$_ -eq "TantouListPX") -or
            ([String]$_ -eq "TantouListSX") -or ([String]$_ -eq "TantouConsulhousyuu") -or
            ([String]$_ -eq "TantouKyuuyokeisan") -or ([String]$_ -eq "TantouSyahohousyuu")
            ){
                $commandValueText = $commandValueText + $_ + " = 0"
            }elseif([String]$_ -eq "Title"){
            }else{
                $commandValueText = $commandValueText + $_ + " = ''"
            }
        }else{
            if([String]$_ -eq "TKCJimusyoCode"){
                $commandValueText = $commandValueText + $_ + " = '" + $TKCJimusyoCodeX + "', "
            }elseif([String]$_ -eq "TKCKanyoCode"){
                $commandValueText = $commandValueText + $_ + " = '" + $TKCKanyoCodeX + "', "
            }elseif([String]$_ -eq "SyanaiCode"){
                $commandValueText = $commandValueText + $_ + " = " + $SyanaiCodeX + ", "
            }elseif([String]$_ -eq "TKCName"){
                $commandValueText = $commandValueText + $_ + " = '" + $TKCNameX + "', "
            }elseif([String]$_ -eq "TKCKokuzeiUserCode"){
                $commandValueText = $commandValueText + $_ + " = '" + $TKCKokuzeiUserCodeX + "', "
            }elseif([String]$_ -eq "TKCTihouzeiUserID"){
                $commandValueText = $commandValueText + $_ + " = '" + $TKCTihouzeiUserIDX + "', "
            }elseif([String]$_ -eq "TantouListTantousyaCD"){
                $commandValueText = $commandValueText + $_ + " = " + $TantouListTantousyaCDX + ", "
            }elseif([String]$_ -eq "TantouListKansaTantou"){
                $commandValueText = $commandValueText + $_ + " = '" + $TantouListKansaTantouX + "', "
            }elseif([String]$_ -eq "TantouListTantoukacd"){
                $commandValueText = $commandValueText + $_ + " = " + $TantouListTantoukacdX + ", "
            }elseif([String]$_ -eq "TantouListTantouka"){
                $commandValueText = $commandValueText + $_ + " = '" + $TantouListTantoukaX + "', "
            }elseif([String]$_ -eq "MailAddress"){
                $commandValueText = $commandValueText + $_ + " = '" + $MailAddressX + "', "
            }elseif([String]$_ -eq "TKCKaijyo"){
                $commandValueText = $commandValueText + $_ + " = '" + $TKCKaijyoX + "', "
            }elseif([String]$_ -eq "SeiriBangou"){
                $commandValueText = $commandValueText + $_ + " = '" + $SeiriBangouX + "', "
            }elseif([String]$_ -eq "HoujinBangou"){
                $commandValueText = $commandValueText + $_ + " = '" + $HoujinBangouX + "', "
            }elseif([String]$_ -eq "Daihyousya"){
                $commandValueText = $commandValueText + $_ + " = '" + $DaihyousyaX + "', "
            }elseif([String]$_ -eq "KessanDuki"){
                $commandValueText = $commandValueText + $_ + " = '" + $KessanDukiX + "', "
            }elseif([String]$_ -eq "YuubinBangou"){
                $commandValueText = $commandValueText + $_ + " = '" + $YuubinBangouX + "', "
            }elseif([String]$_ -eq "Jyuusyo"){
                $commandValueText = $commandValueText + $_ + " = '" + $JyuusyoX + "', "
            }elseif([String]$_ -eq "Houmonnsaki2"){
                $commandValueText = $commandValueText + $_ + " = '" + $Houmonnsaki2X + "', "
            }elseif([String]$_ -eq "TelNo"){
                $commandValueText = $commandValueText + $_ + " = '" + $TelNoX + "', "
            }elseif([String]$_ -eq "AccountantSoft"){
                $commandValueText = $commandValueText + $_ + " = '" + $AccountantSoftX + "', "
            }elseif(([String]$_ -eq "TantouListTantousyaCD2") -or ([String]$_ -eq "TantouListTantousyaCD3") -or 
            ([String]$_ -eq "TantouListTantousyaCD4") -or ([String]$_ -eq "TantouListTantousyaCD5") -or 
            ([String]$_ -eq "TantouListSyahoTantoukaCD") -or ([String]$_ -eq "TantouListSyahoTantouCD") -or
            ([String]$_ -eq "TantouConsulCode") -or ([String]$_ -eq "TantouConsulSubCode") -or
            ([String]$_ -eq "TantouConsulSubCode2") -or ([String]$_ -eq "TantouKyuuyoCode") -or
            ([String]$_ -eq "TantouKyuuyoSubCode") -or ([String]$_ -eq "TantouKyuuyoSubCode2") -or
            ([String]$_ -eq "TantouSyahoCode") -or ([String]$_ -eq "TantouSyahoSubCode") -or
            ([String]$_ -eq "TantouSyahoSubCode2") -or
            ([String]$_ -eq "TantouListGetujihousyuu") -or ([String]$_ -eq "TantouListKessanryou") -or
            ([String]$_ -eq "TantouListKaikeisoftRental") -or ([String]$_ -eq "TantouListPX") -or
            ([String]$_ -eq "TantouListSX") -or ([String]$_ -eq "TantouConsulhousyuu") -or
            ([String]$_ -eq "TantouKyuuyokeisan") -or ([String]$_ -eq "TantouSyahohousyuu")
            ){
                $commandValueText = $commandValueText + $_ + " = 0, "
            }elseif([String]$_ -eq "Title"){
            }else{
                $commandValueText = $commandValueText + $_ + " = '', "
            }           
        }
    }#ループ終わり
            # 接続
            try
            {
                $connection.Open()
                Write-Verbose '接続OK'
            
            }
            catch
            {
                Write-Warning '接続に失敗'
                $connection.Close()
            }
            
            # SQL実行
            $command = $connection.CreateCommand()
            $command.CommandText = "UPDATE kanyodb SET " + $commandValueText +"' WHERE Title = " + $TitleX
            write-host $command.CommandText
            Write-Verbose 'SQL実行します'
            
            try
            {
                $result = $command.ExecuteReader()
                Write-Verbose 'SQL実行しました'
            }
            catch
            {
                Write-Warning 'SQL実行に失敗'
                $connection.Close()
            }
            
            # Datatableにデータをぶっ込む
            #$dataTable = New-Object "System.Data.Datatable"
            #$dataTable.Load($SQLPar)
            
            # 終了
            $connection.Close()
            Write-Verbose '終了'
            $SQLPar | Out-File -FilePath $outputFilePath -Encoding UTF8
    } 
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------    
    function SLIDEMySQL{
    
        [CmdletBinding()]
        param (
            [Parameter(Mandatory = $true)]
            [Object[,]]$DimArrayList
        )
    
        Add-Type -Path 'C:\Program Files (x86)\MySQL\MySQL Connector Net 8.0.27\Assemblies\v4.5.2\MySQL.Data.dll'
        #Add-Type -Path 'C:\Program Files (x86)\MySQL\MySQL Connector Net 8.0.27\Assemblies\v4.5.2\Renci.SshNet.dll'
         
        [string]$mySQLHost             = 'ws77'
        [string]$mySQLPort             = '3306'
        [string]$mySQLUserName         = 'SYSTEM'
        [string]$mySQLPassword         = 'SYSTEM'
        [string]$mySQLDB               = 'kanyodb'#'kanyodb_deletelist'
        [string]$mySQLConnectionString = "server='$mySQLHost';port='$mySQLPort';uid='$mySQLUserName';pwd=$mySQLPassword;database=$mySQLDB"
         
        $connection = New-Object MySql.Data.MySqlClient.MySqlConnection($mySQLConnectionString)
        $connection.ConnectionString = $mySQLConnectionString  
        # 接続
        try
        {
            $connection.Open()
             Write-Verbose '接続OK'
         
        }
        catch
        {
            Write-Warning '接続に失敗'
            $connection.Close()
        }
         
        # SQL実行

        $command = $connection.CreateCommand()
        $TitleNo = LoadDBLength #関数で転記先リストを取得
        $TitleNo = $TitleNo.Lines #転記先のリスト行数を取得
        $DeleteDayPar = Get-Date -DisplayHint DateTime -Format "yyyy-MM-dd hh:mm:ss" #削除した日付を今日で指定
        $propNames = $DimArrayList | Get-Member -MemberType Properties | Select-Object -ExpandProperty Name #引数リストの列名取得
        $propNames | ForEach-Object{$x = $x + 1 #列名分ぶんまわし
            if($x -eq $propNames.Length){ #列名数最後は,をつけない為の条件文
                $commandMiddleText = $commandMiddleText + $_ #SQL文commandMiddleTextに列名を代入
                if(([String]$_ -eq "SyanaiCode") -Or #転記先のデータ型に準じて型変換(Int)
                ([String]$_ -eq "TantouListTantoukacd") -Or
                ([String]$_ -eq "TantouListTantousyaCD") -Or
                ([String]$_ -eq "TantouListTantousyaCD2") -Or
                ([String]$_ -eq "TantouListTantousyaCD3") -Or
                ([String]$_ -eq "TantouListTantousyaCD4") -Or
                ([String]$_ -eq "TantouListTantousyaCD5") -Or
                ([String]$_ -eq "TantouListSyahoTantoukaCD") -Or
                ([String]$_ -eq "TantouListSyahoTantouCD") -Or
                ([String]$_ -eq "TantouConsulCode") -Or
                ([String]$_ -eq "TantouConsulSubCode") -Or
                ([String]$_ -eq "TantouConsulSubCode2") -Or
                ([String]$_ -eq "TantouSyahoCode") -Or
                ([String]$_ -eq "TantouSyahoSubCode") -Or
                ([String]$_ -eq "TantouSyahoSubCode2")
                ){
                    $commandValueText = $commandValueText + [int]$DimArrayList.$_
                }elseif([String]$_ -eq "Title") #プライマリキーTitleは自動連番
                {
                $commandValueText = $commandValueText + [int]$TitleNo
                }elseif(([string]$_ -eq "TantouListGetujihousyuu") -Or #転記先のデータ型に準じて型変換(decimal)
                ([string]$_ -eq "TantouListGetujihousyuu") -Or
                ([string]$_ -eq "TantouListKessanryou") -Or
                ([string]$_ -eq "TantouListKaikeisoftRental") -Or
                ([string]$_ -eq "TantouListPX") -Or
                ([string]$_ -eq "TantouListSX") -Or
                ([string]$_ -eq "TantouConsulhousyuu") -Or
                ([string]$_ -eq "TantouKyuuyokeisan") -Or
                ([string]$_ -eq "TantouSyahohousyuu")
                ){
                    $commandValueText = $commandValueText + [decimal]$DimArrayList.$_
                }else{ #転記先のデータ型に準じて型変換(string)
                    $commandValueText = $commandValueText + [string]$DimArrayList.$_
                }
            }else{
                $commandMiddleText = $commandMiddleText + $_ + ',' #SQL文commandMiddleTextに列名を代入+,
                if(([String]$_ -eq "SyanaiCode") -Or #転記先のデータ型に準じて型変換(Int)+,
                ([String]$_ -eq "TantouListTantoukacd") -Or
                ([String]$_ -eq "TantouListTantousyaCD") -Or
                ([String]$_ -eq "TantouListTantousyaCD2") -Or
                ([String]$_ -eq "TantouListTantousyaCD3") -Or
                ([String]$_ -eq "TantouListTantousyaCD4") -Or
                ([String]$_ -eq "TantouListTantousyaCD5") -Or
                ([String]$_ -eq "TantouListSyahoTantoukaCD") -Or
                ([String]$_ -eq "TantouListSyahoTantouCD") -Or
                ([String]$_ -eq "TantouConsulCode") -Or
                ([String]$_ -eq "TantouConsulSubCode") -Or
                ([String]$_ -eq "TantouConsulSubCode2") -Or
                ([String]$_ -eq "TantouSyahoCode") -Or
                ([String]$_ -eq "TantouSyahoSubCode") -Or
                ([String]$_ -eq "TantouSyahoSubCode2")
                ){
                    $commandValueText = $commandValueText + [int]$DimArrayList.$_ + ","
                }elseif([String]$_ -eq "Title") #プライマリキーTitleは自動連番+,
                {
                $commandValueText = $commandValueText + [int]$TitleNo + ","
                }elseif(([string]$_ -eq "TantouListGetujihousyuu") -Or #転記先のデータ型に準じて型変換(decimal)+,
                ([string]$_ -eq "TantouListGetujihousyuu") -Or
                ([string]$_ -eq "TantouListKessanryou") -Or
                ([string]$_ -eq "TantouListKaikeisoftRental") -Or
                ([string]$_ -eq "TantouListPX") -Or
                ([string]$_ -eq "TantouListSX") -Or
                ([string]$_ -eq "TantouConsulhousyuu") -Or
                ([string]$_ -eq "TantouKyuuyokeisan") -Or
                ([string]$_ -eq "TantouSyahohousyuu")
                ){
                    $commandValueText = $commandValueText + [decimal]$DimArrayList.$_ + ","
                }else{ #転記先のデータ型に準じて型変換(string)+,
                    $commandValueText = $commandValueText + "'" + [string]$DimArrayList.$_ + "',"
                }
            }
            
        }
        $command.CommandText = "INSERT INTO kanyodb_deletelist (" + $commandMiddleText + ",DeleteDay)VALUES(" + $commandValueText + ",'" + [string]$DeleteDayPar +"')"
        #$command.CommandText = "INSERT INTO kanyodb_deletelist (" + $commandMiddleText + ")VALUES(" + $commandValueText +")"
    write-Host $command.CommandText 

        Write-Verbose 'SQL実行します'
         
        try
        {
            $result = $command.ExecuteReader()
            Write-Verbose 'SQL実行しました'
        }
        catch
        {
            Write-Warning 'SQL実行に失敗'
            $connection.Close()
        }
         
        # 終了
        $connection.Close()
        Write-Verbose '終了'      
    } 
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------
function SyainSQL{　#社員情報をSQLで呼出

    [CmdletBinding()]
    param (
        [Parameter(Mandatory = $true)]
        [int]$TargetSNo
    )

    Add-Type -Path 'C:\Program Files (x86)\MySQL\MySQL Connector Net 8.0.27\Assemblies\v4.5.2\MySQL.Data.dll'
     
    [string]$mySQLHost             = 'ws77'
    [string]$mySQLPort             = '3306'
    [string]$mySQLUserName         = 'SYSTEM'
    [string]$mySQLPassword         = 'SYSTEM'
    [string]$mySQLDB               = 'kanyodb'
    [string]$mySQLConnectionString = "server='$mySQLHost';port='$mySQLPort';uid='$mySQLUserName';pwd=$mySQLPassword;database=$mySQLDB" 
    $connection = New-Object MySql.Data.MySqlClient.MySqlConnection($mySQLConnectionString)
    $connection.ConnectionString = $mySQLConnectionString
      
            # 接続
            try
            {
                $connection.Open()
                Write-Verbose '接続OK'
            
            }
            catch
            {
                Write-Warning '接続に失敗'
                $connection.Close()
            }
            
            # SQL実行
            $command = $connection.CreateCommand()
            $command.CommandText = 'SELECT * FROM syainmeibo WHERE SyainNo =' + $TargetSNo
            Write-Verbose 'SQL実行します'
            
            try
            {
                $result = $command.ExecuteReader()
                Write-Verbose 'SQL実行しました'
            }
            catch
            {
                Write-Warning 'SQL実行に失敗'
                $connection.Close()
            }
            
            # Datatableにデータをぶっ込む
            $dataTable = New-Object "System.Data.Datatable"
            $dataTable.Load($result)
            return $dataTable
            
            # 終了
            $connection.Close()
            Write-Verbose '終了'
    } 
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------  

$TKCCDBURL = "\\Sv05121a\e\C 作業台\RPA\ALLDataBase\DB連結用関与形態区分入り重複対策.CSV"
$HeidiURL = "\\Sv05121a\e\C 作業台\RPA\ALLDataBase\Heidi関与先DB.csv"

$CDBTable = Import-CSV -Encoding Default $TKCCDBURL
$HeidiTable = Import-CSV -Encoding Default $HeidiURL

foreach($CDBItem in $CDBTable) {
if($CDBItem.事務所コード -eq "05121"){
    $CDBSyanaiCD =  [int]$CDBItem.関与先コード
}elseif ($CDBItem.事務所コード -eq "05371") {
    $CDBSyanaiCD =  "4" + $CDBItem.関与先コード
    $CDBSyanaiCD = [int]$CDBSyanaiCD    
}elseif ($CDBItem.事務所コード -eq "15180") {
    $CDBSyanaiCD =  "1" + $CDBItem.関与先コード
    $CDBSyanaiCD = [int]$CDBSyanaiCD    
}elseif ($CDBItem.事務所コード -eq "99999") {
    $CDBSyanaiCD =  "9" + $CDBItem.関与先コード
    $CDBSyanaiCD = [int]$CDBSyanaiCD
}else{}

    $HeidiRecord = $HeidiTable | Where-Object {$_.SyanaiCode -eq $CDBSyanaiCD} | Select-Object 
    if($CDBItem.商号 -ne $HeidiRecord.TKCName){
        $SyainSQLRecord = SyainSQL $CDBItem.担当者コード
        $HeidiTitleNo = [int]$HeidiRecord.Title
        UPMySQL -TitleX $HeidiTitleNo -TKCJimusyoCodeX $CDBItem.事務所コード -TKCKanyoCodeX $CDBItem.関与先コード -SyanaiCodeX $CDBSyanaiCD -TKCNameX $CDBItem.商号 -TKCKokuzeiUserCodeX $CDBItem.利用者識別番号 -TKCTihouzeiUserIDX $CDBItem.("利用者ＩＤ＿地方税") -TantouListTantousyaCDX $CDBItem.担当者コード -TantouListKansaTantouX $CDBItem.監査担当者名 -TantouListTantoukacdX $SyainSQLRecord.Genhaizokucd -TantouListTantoukaX $SyainSQLRecord.Genhaizoku -MailAddressX $CDBItem.Ｅメール -TKCKaijyoX $CDBItem.関与終了年月日 -SeiriBangouX $CDBItem.整理番号 -HoujinBangouX $CDBItem.法人番号 -DaihyousyaX $CDBItem.代表者 -KessanDukiX $CDBItem.決算月１ -YuubinBangouX $CDBItem.郵便番号 -JyuusyoX $CDBItem.住所１ -Houmonnsaki2X $CDBItem.住所２ -TelNoX $CDBItem.本店電話番号 -AccountantSoftX $CDBItem.自計ｼｽﾃﾑ名 

        #try #DeleteListへ転記済みの関与先でないか突合して処理分け
        #{
        #    $ObjFind = LoadDBs $HeidiRecord
        #    Write-Verbose 'SQL実行しました'
        #    if($ObjFind -eq 0){SLIDEMySQL $HeidiRecord}
        #}
        #catch
        #{
        #    Write-Warning 'SQL実行に失敗'
        #}

    }
}