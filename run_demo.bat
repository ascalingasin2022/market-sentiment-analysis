@echo off
echo ============================================
echo   Market Sentiment Analysis - Streamlit App
echo ============================================

REM Create virtual environment if not exists
if not exist venv (
    echo Creating virtual environment...
    python -m venv venv
)

REM Activate virtual environment
call venv\Scripts\activate

REM Upgrade pip
python -m pip install --upgrade pip

REM Install dependencies
pip install -r requirements.txt

REM Run the Streamlit app
echo Starting Streamlit app...
streamlit run app.py

pause
