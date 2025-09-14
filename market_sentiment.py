import pandas as pd
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from dataclasses import dataclass
from typing import List, Optional
from datetime import datetime

# Ensure VADER lexicon is available
try:
    nltk.data.find("sentiment/vader_lexicon.zip")
except LookupError:
    nltk.download("vader_lexicon")


@dataclass
class SentimentItem:
    text: str
    timestamp: datetime
    symbol: Optional[str] = None
    score: Optional[float] = None
    label: Optional[str] = None


def get_engine():
    """Return the VADER sentiment analyzer."""
    return SentimentIntensityAnalyzer()


def analyze_items(items: List[SentimentItem]) -> List[SentimentItem]:
    """Run sentiment analysis on a list of SentimentItems."""
    engine = get_engine()
    for it in items:
        scores = engine.polarity_scores(it.text)
        it.score = scores["compound"]
        if it.score >= 0.05:
            it.label = "positive"
        elif it.score <= -0.05:
            it.label = "negative"
        else:
            it.label = "neutral"
    return items


def aggregate(items: List[SentimentItem], by: str = "D") -> pd.DataFrame:
    """Aggregate sentiment scores by a resampling period (D=day, H=hour, W=week)."""
    df = pd.DataFrame([
        {"timestamp": it.timestamp, "score": it.score, "label": it.label}
        for it in items if it.score is not None
    ])

    if df.empty:
        return pd.DataFrame()

    df = df.set_index("timestamp").sort_index()
    agg = df.resample(by).agg({"score": "mean"})
    agg = agg.rename(columns={"score": "score_mean"})  # ensures "score_mean" exists
    agg = agg.reset_index()
    agg["count"] = df.resample(by).size().values
    return agg


def read_csv(file) -> List[SentimentItem]:
    """Read a CSV file into a list of SentimentItems."""
    df = pd.read_csv(file)

    # Handle missing timestamp - use current time
    if "timestamp" not in df.columns:
        df["timestamp"] = datetime.now()

    # Convert timestamps
    df["timestamp"] = pd.to_datetime(df["timestamp"], errors="coerce").fillna(datetime.now())

    items = [
        SentimentItem(
            text=row["text"],
            timestamp=row["timestamp"],
            symbol=row["symbol"] if "symbol" in df.columns else None,
        )
        for _, row in df.iterrows()
    ]
    return items


def to_csv(items: List[SentimentItem]) -> str:
    """Convert SentimentItems into CSV string."""
    df = pd.DataFrame([{
        "timestamp": it.timestamp,
        "text": it.text,
        "symbol": it.symbol,
        "score": it.score,
        "label": it.label
    } for it in items])
    return df.to_csv(index=False)
