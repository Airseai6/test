rem call %~dp0..\setenv.bat

pyside2-uic %~dp0main.ui -o %~dp0main_UI.py
pyside2-rcc "%~dp0main.qrc" -o "%~dp0..\main_rc.py"
