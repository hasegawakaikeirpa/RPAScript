echo off

rem �T�[�r�X����ݒ�
set SERVICENAME=Print Spooler

rem ��ɂ���t�H���_�p�X��ݒ�
set FOLDERPATH=C:\Windows\System32\spool\PRINTERS

rem �T�[�r�X���f
echo stopping %SERVICENAME%
net stop "%SERVICENAME%"

rem �t�H���_����ɂ���
echo emptying %FOLDERPATH%\*.*
del "%FOLDERPATH%\*.*"

rem �T�[�r�X�N��
echo starting %SERVICENAME%
net start "%SERVICENAME%"

rem pause

echo on