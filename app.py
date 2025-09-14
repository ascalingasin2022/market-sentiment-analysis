import streamlit as st
import pandas as pd
from market_sentiment import analyze_items, aggregate, read_csv, to_csv

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
            return "background-color: #d4edda; color: #155724; font-weight: bold;"  # light green bg, dark green text
        elif val == "negative":
            return "background-color: #f8d7da; color: #721c24; font-weight: bold;"  # light red bg, dark red text
        else:
            return "background-color: #e2e3e5; color: #383d41; font-weight: bold;"  # gray bg, dark text

    styled_df = df.style.applymap(color_sentiment, subset=["label"])

    st.dataframe(styled_df, use_container_width=True)

    # Download button
    st.download_button(
        label="Download Results as CSV",
        data=df.to_csv(index=False).encode("utf-8"),
        file_name="sentiment_results.csv",
        mime="text/csv",
    )
else:
    st.info("Please upload a CSV file to begin.")

    # Provide sample CSV
    sample_csv = """timestamp,text,symbol
2025-09-01 09:00:00,The stock is doing amazing today!,AAPL
2025-09-01 10:30:00,Investors are worried about inflation,TSLA
2025-09-02 11:00:00,This new product launch looks promising,MSFT
2025-09-02 13:15:00,The market is crashing badly,GOOG
2025-09-03 09:45:00,I feel confident holding my shares,AMZN
2025-09-03 14:20:00,Uncertainty is making me nervous,NVDA
2025-09-04 10:00:00,Earnings report was fantastic,AAPL
2025-09-04 12:30:00,Global news is dragging stocks down,TSLA
2025-09-05 09:10:00,Strong momentum in the tech sector,MSFT
2025-09-05 15:45:00,This feels like the start of a recession,GOOG
"""

    st.download_button(
        label="📥 Download Sample CSV",
        data=sample_csv,
        file_name="sample_sentiment.csv",
        mime="text/csv",
    )
