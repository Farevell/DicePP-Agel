@echo off
Title DicePP������ - v1.4.2��
:start
set GIT_PYTHON_REFRESH=quiet
set PYTHON_EXE=..\Python\python.exe
if exist %PYTHON_EXE% (
	%PYTHON_EXE% bot.py
) else (
	python bot.py
)
echo ��ʼ����
goto start