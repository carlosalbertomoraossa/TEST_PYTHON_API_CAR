@echo off
setlocal

set "FNAME=function"

rem Change working directory to the script's directory
cd /d "%~dp0"

rem Remove existing function.zip if it exists
if exist "%FNAME%.zip" (
    del /q "%FNAME%.zip"
)

rem Create and activate a virtual environment
python -m venv vEnvTemp
call vEnvTemp\Scripts\Activate
pip install -r requirements.txt
call Deactivate

cd vEnvTemp\Lib\site-packages

7z a ..\..\..\%FNAME%.zip *

rem Change working directory to the project's root directory
cd /d "%~dp0"

rmdir /s /q vEnvTemp

rem Compress the contents of the site-packages directory to %FNAME%.zip
7z a -tzip -mx9 "%FNAME%.zip" "lambda_function.py"

rem Recursively add the app directory to the %FNAME%.zip archive
7z a -tzip -mx9 "%FNAME%.zip" "app\"

endlocal
