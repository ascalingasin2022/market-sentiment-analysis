@echo off
REM ==========================================
REM Market Sentiment Analysis - Web App
REM ==========================================

echo Setting up virtual environment...
python -m venv venv

echo Activating virtual environment...
call venv\Scripts\activate.bat

echo Installing dependencies...
python -m pip install --upgrade pip
pip install -r requirements.txt

echo Launching Streamlit app...
python -m streamlit run app.py

pause
