# Market Sentiment Analysis

This is a small Streamlit project I put together for analyzing market sentiment from CSV data.  
Basically, you upload a CSV file with some text (like stock comments, tweets, or news), and the app will run sentiment analysis on it using NLTK’s VADER. Then it shows you charts and a table with results.

---

## What it does
- Upload a CSV with a `text` column (other columns like `timestamp` and `symbol` are optional).
- Runs sentiment scoring (positive, negative, neutral, compound).
- Aggregates the results by day.
- Shows:
  - A line chart of the average sentiment score.
  - A bar chart of how many entries there were.
- Lets you download the analyzed results as CSV.
- Includes a sample CSV in case you just want to try it quickly.

---

## Project Structure

market-sentiment-analysis/
│── app.py # Streamlit app (the frontend)
│── market_sentiment.py # Functions for analyzing sentiment
│── requirements.txt # Dependencies list
│── run_demo.bat # Windows helper to run the app
│── README.md # This file

---

## Requirements
- Python 3.9+ (should work on newer versions too)
- Libraries: `streamlit`, `pandas`, `nltk`

Install them with:

```bash
pip install -r requirements.txt

Note: the first time you run it, NLTK might need to download the vader_lexicon. The code already tries to handle that automatically.

---

## How to run

On Windows
Just double-click run_demo.bat, or run: streamlit run app.py

On Mac/Linux
python3 -m streamlit run app.py
Then go to: http://localhost:8501

---

## CSV Format

Your file must have a text column.
Other optional ones:

    - timestamp → if missing, today’s date will be used
    - symbol → e.g., AAPL, TSLA, etc.

Example:

    timestamp,text,symbol
    2025-09-01 09:00:00,The stock is doing amazing today!,AAPL
    2025-09-01 10:30:00,Investors are worried about inflation,TSLA
    2025-09-02 11:00:00,This new product launch looks promising,MSFT
    2025-09-02 13:15:00,The market is crashing badly,GOOG

If you don’t have your own CSV yet, just grab the sample CSV from inside the app (there’s a download button).

Output
    Two charts side by side:
        - Average sentiment score (line chart).
        - Number of rows per day (bar chart).
    - A full table of results (timestamp, text, symbol, score, label).
    -Option to download the results as CSV.