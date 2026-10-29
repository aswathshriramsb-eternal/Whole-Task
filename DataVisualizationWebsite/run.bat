@echo off
title PROJECT 02: Data Visualization with Matplotlib & Seaborn
echo =====================================================================
echo  PROJECT 02: DATA VISUALIZATION WITH MATPLOTLIB ^& SEABORN
echo  Launching Flask Server and Interactive Dashboard...
echo =====================================================================
cd /d "%~dp0"

:: Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] Python is not found in your PATH.
    echo Please install Python 3.10+ from python.org or Microsoft Store.
    pause
    exit /b
)

:: Start the default web browser after 1.5 seconds
start "" http://127.0.0.1:5000

:: Run the Flask web application
python app.py

pause
