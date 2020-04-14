@echo off
set PYTHONPATH=%~dp0\TotoroScripting\;%PYTHONPATH%
python.exe TotoroScripting/totoro/mergefiles.py
pause