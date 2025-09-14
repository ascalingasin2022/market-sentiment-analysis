# 📊 Market Sentiment Analysis

This is a simple Streamlit project I created to analyze market sentiment from CSV files.  
Basically, you upload a CSV with text about stocks, tweets, or market news, and it will calculate sentiment scores, display charts, and show detailed results in a table.

Check it out here on GitHub: [market-sentiment-analysis](https://github.com/ascalingasin2022/market-sentiment-analysis)

---

## Features

- Upload a CSV with a `text` column (optional: `timestamp` and `symbol`).
- Automatically analyzes sentiment using **NLTK VADER**.
- Aggregates results by day.
- Displays:
  - Line chart of average sentiment score.
  - Bar chart showing number of entries.
- Detailed table of each text with its sentiment score and label.
- Color-coded labels (green = positive, red = negative, gray = neutral) for quick visualization.
- Download your results as a CSV file.
- Includes a sample CSV for easy testing.

---

## Project Structure

```

market-sentiment-analysis/
│── app.py                # Streamlit frontend
│── market\_sentiment.py   # Sentiment analysis functions
│── requirements.txt      # Python dependencies
│── run\_demo.bat          # Windows helper to launch app
│── README.md             # This file

````

---

## Requirements

- Python 3.9+  
- Libraries:
  - `streamlit`
  - `pandas`
  - `nltk`

Install all dependencies with:

```bash
pip install -r requirements.txt
````

> Note: NLTK may download the `vader_lexicon` automatically the first time you run the app.

---

## How to Run

### Windows

Double-click `run_demo.bat` or run:

```bash
streamlit run app.py
```

### Mac/Linux

```bash
python3 -m streamlit run app.py
```

Then open [http://localhost:8501](http://localhost:8501) in your browser.

---

## CSV Format

Your CSV **must** have a `text` column.
Optional columns:

* `timestamp` → If missing, the current date/time will be used.
* `symbol` → Stock or market symbol (e.g., AAPL, TSLA).

Example:

```csv
timestamp,text,symbol
2025-09-01 09:00:00,The stock is doing amazing today!,AAPL
2025-09-01 10:30:00,Investors are worried about inflation,TSLA
2025-09-02 11:00:00,This new product launch looks promising,MSFT
2025-09-02 13:15:00,The market is crashing badly,GOOG
```

If you don’t have a CSV ready, just download the **sample CSV** from the app interface.

---

## Output

* **Charts**:

  * Line chart for average sentiment over time.
  * Bar chart for number of entries per day.
* **Table**: Each row shows `timestamp`, `text`, `symbol`, `score`, `label` (color-coded).
* **Downloadable CSV**: Save all analyzed results.

---

## Credits

Developed by **Angoluan, Calingasin, Jayme, and Nagpal**.
Feel free to use, modify, or contribute to this project.

---

Check out the repo here: [https://github.com/ascalingasin2022/market-sentiment-analysis]