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
$outputFilePath="\\Sv05121a\e\C 作業台\RPA\ALLDataBase\Heidi関与先DB.csv"
 
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
$command.CommandText = 'SELECT * FROM kanyodb'
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

$dataTable | export-csv -Encoding UTF8 $outputFilePath -NoTypeInformation  
 
# 実行結果
#id name 
#-- ---- 
# 1 Maeda
# 2 kato 
# 3 Oda  