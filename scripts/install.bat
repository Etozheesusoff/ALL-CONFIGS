@echo off
REM ALL-CONFIGS install.bat
REM Simple wrapper around install.py

SETLOCAL ENABLEDELAYEDEXPANSION

SET SCRIPT_DIR=%~dp0
CD /D "%SCRIPT_DIR%\.."

where python >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    echo Python is not installed or not in PATH.
    echo Please install Python 3 and try again.
    pause
    EXIT /B 1
)

echo === ALL-CONFIGS Installer (Windows) ===
python "scripts\install.py"

pause
ENDLOCAL
