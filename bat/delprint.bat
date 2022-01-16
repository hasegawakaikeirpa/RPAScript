echo off

rem サービス名を設定
set SERVICENAME=Print Spooler

rem 空にするフォルダパスを設定
set FOLDERPATH=C:\Windows\System32\spool\PRINTERS

rem サービス中断
echo stopping %SERVICENAME%
net stop "%SERVICENAME%"

rem フォルダを空にする
echo emptying %FOLDERPATH%\*.*
del "%FOLDERPATH%\*.*"

rem サービス起動
echo starting %SERVICENAME%
net start "%SERVICENAME%"

rem pause

echo on