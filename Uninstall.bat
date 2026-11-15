@echo off
setlocal
title Tab Colour Organizer - Uninstaller

set "TARGET=%APPDATA%\Notepad++\plugins\Config\PythonScript\scripts"

echo ==========================================
echo      Tab Colour Organizer Uninstaller
echo          Create By DiabloRDK
echo ==========================================
echo.
echo This removes the two Tab Colour Organizer scripts.
echo Your saved colour order will be kept.
echo.

if exist "%TARGET%\TabColourOrganizer.py" del "%TARGET%\TabColourOrganizer.py"
if exist "%TARGET%\ConfigureTabColourOrder.py" del "%TARGET%\ConfigureTabColourOrder.py"

echo Uninstallation completed.
echo Restart Notepad++ to remove the commands from the PythonScript Scripts menu.
echo Your settings file has not been deleted.
echo.
pause
