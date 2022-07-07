@echo off
cd /d %~dp0
:<ここから>実行権限と引数で分岐

:管理者特権で実行しないとエラーになる処理
openfiles > NUL 2>&1

:上記処理がエラー（ユーザー権限）であれば一般権限で実行する処理に移動
if NOT %ERRORLEVEL% EQU 0 goto promotion

:実行権限と引数で分岐<ここまで>


:<ここから>管理者権限で実行させたい処理を記述
"C:\Program Files (x86)\Windows Application Driver\WinAppDriver.exe" 4724
echo 管理者権限です。
pause

:管理者権限で実行させたい処理を記述<ここまで>

:↓の記述で管理者権限のときに一般権限の処理を実行しないようにしています①
goto end


:promotion

:<ここから>ユーザー権限で実行させたい処理を記述
"C:\Program Files (x86)\Windows Application Driver\WinAppDriver.exe" 4724
echo ユーザー権限です。

:ユーザー権限で実行させたい処理を記述<ここまで>

:管理者権限で自分自身を実行（昇格処理）
powershell start-process %~nx0 -verb runas


:↓の記述で管理者権限のときに一般権限の処理を実行しないようにしています②
:end