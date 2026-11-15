@echo off
setlocal
title Tab Colour Organizer - Installer

echo ==========================================
echo       Tab Colour Organizer Installer
echo          Create By DiabloRDK
echo ==========================================
echo.

set "PLUGIN_DIR=%APPDATA%\Notepad++\plugins\Config\PythonScript"
set "TARGET=%PLUGIN_DIR%\scripts"

if not exist "%PLUGIN_DIR%" (
    echo PythonScript's configuration folder was not found:
    echo %PLUGIN_DIR%
    echo.
    echo Make sure Notepad++ and the PythonScript plugin are installed.
    echo Open Notepad++ ^> Plugins ^> Plugins Admin and install PythonScript.
    echo Then run this installer again.
    echo.
    echo If you use a portable or custom Notepad++ installation,
    echo copy the two .py files from the scripts folder in this package
    echo into that installation's PythonScript scripts folder.
    echo.
    pause
    exit /b 1
)

if not exist "%TARGET%" mkdir "%TARGET%"

copy /Y "%~dp0scripts\TabColourOrganizer.py" "%TARGET%\TabColourOrganizer.py" >nul
if errorlevel 1 goto failed

copy /Y "%~dp0scripts\ConfigureTabColourOrder.py" "%TARGET%\ConfigureTabColourOrder.py" >nul
if errorlevel 1 goto failed

echo.
echo Installation completed.
echo.
echo Restart Notepad++ (or reload PythonScript scripts).
echo Then open:
echo Plugins ^> PythonScript ^> Scripts
echo.
echo Run ConfigureTabColourOrder first, then TabColourOrganizer.
echo.
echo Your colour-order settings are stored separately and are not overwritten.
echo.
pause
exit /b 0

:failed
echo.
echo Installation failed. Check folder permissions and try again.
pause
exit /b 1
