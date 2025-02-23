@echo off
setlocal enabledelayedexpansion
set "PYTHON_INTERPRETER=python"
set "SCRIPT=main.py"
set "LOG_FILE=script.log"
:log
echo %date% %time% - %1 >> "%LOG_FILE%"
exit /b
where %PYTHON_INTERPRETER% >nul 2>&1
if errorlevel 1 (
    call :log "Error: Python interpreter '%PYTHON_INTERPRETER%' is not installed."
    exit /b 1
)
if not exist "%SCRIPT%" (
    call :log "Error: Script '%SCRIPT%' not found."
    exit /b 1
)
call :log "Starting the Python script '%SCRIPT%'..."
%PYTHON_INTERPRETER% "%SCRIPT%" >> "%LOG_FILE%" 2>&1
if errorlevel 1 (
    call :log "Error: Python script '%SCRIPT%' failed."
    exit /b 1
)
call :log "Python script '%SCRIPT%' executed successfully."
call :log "Script completed."
endlocal
