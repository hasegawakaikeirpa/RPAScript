@echo off

rem if not exist Z: (net use Z: "\\Sv05121a\e\C 作業台\試算表メール転送フォルダ\承認待ち");

rem cd /d Z

rem \\Sv05121a\e\CをP:D:\税理士法人にバックアップ

robocopy "\\Sv05121a\e\C 作業台\試算表メール転送フォルダ\承認待ち" "D:\税理士法人　長谷川会計\税理士法人 長谷川会計 - ドキュメント\承認待ち" /mir

rem 完了メッセージを表示する
echo.処理を完了する