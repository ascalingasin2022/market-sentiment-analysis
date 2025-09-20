# app.py
# --- Robust import block: put this at the VERY TOP of app.py ---
import os
import sys
import traceback
import importlib.util

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

print("=== Debug start ===")
print("App file:", os.path.join(HERE, os.path.basename(__file__)))
print("Current working dir:", os.getcwd())
print("App dir listing:", os.listdir(HERE))
print("sys.path[0:6]:", sys.path[:6])

# Try to import the module in a safe way and bind only needed functions
_analyze_items = None
_aggregate = None
_read_csv = None
_to_csv = None  # optional

# Try normal import first
try:
    import market_sentiment as ms
    print("Imported market_sentiment as module.")
    _analyze_items = getattr(ms, "analyze_items", None)
    _aggregate = getattr(ms, "aggregate", None)
    _read_csv = getattr(ms, "read_csv", None)
    _to_csv = getattr(ms, "to_csv", None)  # may be None
except Exception as e:
    print("Normal import failed:", repr(e))
    traceback.print_exc()

# If any required function missing, attempt fallback load from file
if not (_analyze_items and _aggregate and _read_csv):
    module_path = os.path.join(HERE, "market_sentiment.py")
    print("Attempting fallback load from:", module_path)
    if os.path.exists(module_path):
        try:
            spec = importlib.util.spec_from_file_location("market_sentiment", module_path)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            _analyze_items = getattr(module, "analyze_items", None)
            _aggregate = getattr(module, "aggregate", None)
            _read_csv = getattr(module, "read_csv", None)
            _to_csv = getattr(module, "to_csv", None)  # optional
            print("Successfully loaded market_sentiment.py via importlib.")
        except Exception as e2:
            print("Failed to load/execute market_sentiment.py:", repr(e2))
            traceback.print_exc()
            raise
    else:
        raise ModuleNotFoundError(f"market_sentiment.py not found at {module_path}")

# Validate required functions
missing = []
if not callable(_analyze_items):
    missing.append("analyze_items")
if not callable(_aggregate):
    missing.append("aggregate")
if not callable(_read_csv):
    missing.append("read_csv")
if missing:
    raise AttributeError(f"market_sentiment.py is missing required functions: {', '.join(missing)}")

# bind to friendly names used below
analyze_items = _analyze_items
aggregate = _aggregate
read_csv = _read_csv
to_csv = _to_csv  # may be None

# --- End robust import block ---

import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Market Sentiment Analysis",
    page_icon="📊",
    layout="wide"
)

st.title("Market Sentiment Analysis")
st.write("Upload a CSV file with at least a **`text`** column to analyze sentiment.")
st.caption("Developed by Angoluan, Calingasin, Jayme, and Nagpal.")

# File uploader (CSV only)
uploaded_file = st.file_uploader("Upload CSV", type=["csv"])

if uploaded_file is not None:
    # read_csv in the module should accept a file path or file-like (we expect it to handle file-like)
    items = read_csv(uploaded_file)     # Read CSV into SentimentItem list
    analyzed = analyze_items(items)     # Run sentiment analysis
    agg = aggregate(analyzed, by="D")   # Aggregate results

    # Show results
    st.subheader("Aggregated Sentiment Over Time")
    if not agg.empty:
        col1, col2 = st.columns(2)

        with col1:
            st.markdown("**Average Sentiment Score**")
            st.line_chart(agg.set_index("timestamp")["score_mean"])

        with col2:
            st.markdown("**Number of Entries**")
            st.bar_chart(agg.set_index("timestamp")["count"])
    else:
        st.warning("No sentiment scores available. Please check your CSV format.")

    # Show table of analyzed items with colored labels
    st.subheader("Detailed Results")
    df = pd.DataFrame([{
        "timestamp": it.timestamp,
        "text": it.text,
        "symbol": it.symbol,
        "score": it.score,
        "label": it.label
    } for it in analyzed])

    # Coloring function
    def color_sentiment(val):
        if val == "positive":
            return "background-color: #d4edda; color: #155724; font-weight: bold;"
        elif val == "negative":
            return "background-color: #f8d7da; color: #721c24; font-weight: bold;"
        else:
            return "background-color: #e2e3e5; color: #383d41; font-weight: bold;"

    styled_df = df.style.applymap(color_sentiment, subset=["label"])

    st.dataframe(styled_df, use_container_width=True)

    # Download button (we use pandas DataFrame.to_csv here; module's to_csv is optional)
    st.download_button(
        label="Download Results as CSV",
        data=df.to_csv(index=False).encode("utf-8"),
        file_name="sentiment_results.csv",
        mime="text/csv",
    )
else:
    st.info("Please upload a CSV file to begin.")

    # Provide download link to sample_sentiment.csv (must be in the same directory)
    sample_path = os.path.join(HERE, "sample_sentiment.csv")
    if os.path.exists(sample_path):
        with open(sample_path, "rb") as f:
            st.download_button(
                label="📥 Download Sample CSV",
                data=f,
                file_name="sample_sentiment.csv",
                mime="text/csv",
            )
    else:
        st.warning("Sample CSV file (sample_sentiment.csv) not found in the app directory.")

    # st.download_button(
    #     label="📥 Download Sample CSV",
    #     data=sample_csv,
    #     file_name="sample_sentiment.csv",
    #     mime="text/csv",
    # )
