@echo off
cd /d %~dp0
:<��������>���s�����ƈ����ŕ���

:�Ǘ��ғ����Ŏ��s���Ȃ��ƃG���[�ɂȂ鏈��
openfiles > NUL 2>&1

:��L�������G���[�i���[�U�[�����j�ł���Έ�ʌ����Ŏ��s���鏈���Ɉړ�
if NOT %ERRORLEVEL% EQU 0 goto promotion

:���s�����ƈ����ŕ���<�����܂�>


:<��������>�Ǘ��Ҍ����Ŏ��s���������������L�q
"C:\Program Files (x86)\Windows Application Driver\WinAppDriver.exe" 4724
echo �Ǘ��Ҍ����ł��B
pause

:�Ǘ��Ҍ����Ŏ��s���������������L�q<�����܂�>

:���̋L�q�ŊǗ��Ҍ����̂Ƃ��Ɉ�ʌ����̏��������s���Ȃ��悤�ɂ��Ă��܂��@
goto end


:promotion

:<��������>���[�U�[�����Ŏ��s���������������L�q
"C:\Program Files (x86)\Windows Application Driver\WinAppDriver.exe" 4724
echo ���[�U�[�����ł��B

:���[�U�[�����Ŏ��s���������������L�q<�����܂�>

:�Ǘ��Ҍ����Ŏ������g�����s�i���i�����j
powershell start-process %~nx0 -verb runas


:���̋L�q�ŊǗ��Ҍ����̂Ƃ��Ɉ�ʌ����̏��������s���Ȃ��悤�ɂ��Ă��܂��A
:end