@echo off
echo ========================================================
echo   RetinaVision AI - Liquid Glass Diagnostic Suite
echo ========================================================
echo Starting local web server on port 8000...
start "" "http://localhost:8000"
python -m http.server 8000
pause

