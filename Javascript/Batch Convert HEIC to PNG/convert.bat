@echo off
setlocal

rem Set the path to Photoshop
set "PHOTOSHOP=C:\Program Files\Adobe\Adobe Photoshop 2024\Photoshop.exe"

rem Check if Photoshop exists
if not exist "%PHOTOSHOP%" (
    echo Photoshop not found! Update the script with the correct path.
    pause
    exit /b
)

rem Run the Photoshop script
"%PHOTOSHOP%" -scripting "%~dp0convert_heic_to_png.jsx"

endlocal
pause
