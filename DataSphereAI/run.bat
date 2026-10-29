@echo off
title DataSphere AI - Unified Portfolio (Projects 01-05)
echo =====================================================================
echo  DataSphere AI: Unified Data Science ^& AI Portfolio
echo  Launching Streamlit Multi-Project Application...
echo =====================================================================
cd /d "%~dp0"

:: Ensure model artifact exists
if not exist "models\titanic_model.joblib" (
    echo [INFO] Training Decision Tree Classifier artifact...
    python train_model.py
)

:: Run Streamlit application directly with trusted system Python
echo [INFO] Starting Streamlit server...
python -m streamlit run app.py --server.port 8501

pause
