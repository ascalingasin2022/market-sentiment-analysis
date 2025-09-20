# Market Sentiment Analysis

This is a simple Streamlit project that analyzes market sentiment from CSV files. You can upload a CSV containing stock comments, tweets, or market news, and the app will automatically process the text and evaluate its sentiment. The system uses two approaches: a rule-based method (VADER), which calculates sentiment scores using a predefined lexicon, and a machine learning method (Logistic Regression), which has been trained to classify text as either positive or negative. The results are then presented through interactive charts showing sentiment trends over time, as well as a detailed table of entries that can be downloaded as a CSV file for further analysis.

Check it out here on GitHub: [market-sentiment-analysis](https://github.com/ascalingasin2022/market-sentiment-analysis)

---

## Credits

Group Members by 
- **Angoluan, Phobie Jochelle R.**
- **Calingasin, Adrian S.**
- **Jayme, Irish Anne G.**
- **Nagpal, Jaichand M.**

To be Submitted to **Mr. Michael R. Ramos**

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
│── app.py                  # Streamlit frontend
│── market\_sentiment.py    # Sentiment analysis functions
│── requirements.txt        # Python dependencies
│── run\_demo.bat           # Windows helper to launch app
│── README.md               # This file
│── sample_sentiment.csv    # Sample .csv file to upload

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

## How to Install Python

If you don’t have Python installed yet:

1. Go to the official website: [https://www.python.org/downloads/](https://www.python.org/downloads/)
2. Download the latest Python 3.x version for your operating system (Windows, macOS, or Linux).
3. During installation on Windows, make sure to check **“Add Python to PATH”**.
4. Verify installation by opening a terminal/command prompt and running:

```bash
python --version
```

It should show something like `Python 3.10.12` (version may vary).

---

## How to Run

### Option 1: Run locally after cloning

1. **Clone the repo**:

```bash
git clone https://github.com/ascalingasin2022/market-sentiment-analysis.git
cd market-sentiment-analysis
```

2. **Install dependencies**:

```bash
pip install -r requirements.txt
```

3. **Run the Streamlit app** using one of these commands:

```bash
# Standard Streamlit command
streamlit run app.py

# Python module command
python -m streamlit run app.py
```

4. Open [http://localhost:8501](http://localhost:8501) in your browser.

---

### Option 2: Run directly from GitHub (without cloning)

You can run the app straight from GitHub using Streamlit’s `run` command with a URL:

```bash
streamlit run https://raw.githubusercontent.com/ascalingasin2022/market-sentiment-analysis/main/app.py
```

> Make sure you have Python 3.9+ and required libraries installed first (`streamlit`, `pandas`, `nltk`).

---

### Option 3: Run using the Windows `.bat` file

If you are on Windows, you can run the app using the included `.bat` file. Follow these steps:

1. **Clone the repository** to your local machine:

```bash
git clone https://github.com/ascalingasin2022/market-sentiment-analysis.git
cd market-sentiment-analysis
```

2. **Install dependencies** (if not done already):

```bash
pip install -r requirements.txt
```

3. **Run the app** by double-clicking the `run_demo.bat` file inside the project folder.
   This will automatically open the Streamlit app in your default browser.

> Make sure Python is installed and added to your PATH before running the `.bat` file.

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

Check out the repo here: [https://github.com/ascalingasin2022/market-sentiment-analysis](https://github.com/ascalingasin2022/market-sentiment-analysis)

Maintained by: Adrian Calingasin GitHub: [github.com/ascalingasin2022](github.com/ascalingasin2022)