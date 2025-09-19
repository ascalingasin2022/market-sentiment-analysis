import nltk
import pandas as pd
from nltk.sentiment import SentimentIntensityAnalyzer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline

# Ensure required datasets are downloaded
nltk.download("vader_lexicon", quiet=True)
nltk.download("movie_reviews", quiet=True)

from nltk.corpus import movie_reviews
import random

class SentimentItem:
    def __init__(self, timestamp, text, symbol=None, score=None, label=None):
        self.timestamp = timestamp
        self.text = text
        self.symbol = symbol
        self.score = score
        self.label = label


def train_ml_model():
    """Train a simple ML model (Logistic Regression) on NLTK movie reviews."""
    documents = [(list(movie_reviews.words(fileid)), category)
                 for category in movie_reviews.categories()
                 for fileid in movie_reviews.fileids(category)]
    random.shuffle(documents)

    texts = [" ".join(words) for words, _ in documents]
    labels = [1 if category == "pos" else 0 for _, category in documents]

    model = make_pipeline(CountVectorizer(), LogisticRegression(max_iter=1000))
    model.fit(texts, labels)
    return model


# Train ML model once
ML_MODEL = train_ml_model()


def get_engine(engine_name="vader"):
    if engine_name == "vader":
        return SentimentIntensityAnalyzer()
    elif engine_name == "ml":
        return ML_MODEL
    else:
        raise ValueError(f"Unknown engine: {engine_name}")


def analyze_items(items, engine_name="vader"):
    engine = get_engine(engine_name)

    for it in items:
        if engine_name == "vader":
            scores = engine.polarity_scores(it.text)
            it.score = scores["compound"]
            if it.score >= 0.05:
                it.label = "positive"
            elif it.score <= -0.05:
                it.label = "negative"
            else:
                it.label = "neutral"

        elif engine_name == "ml":
            pred = engine.predict([it.text])[0]
            it.score = float(pred)  # 1 = positive, 0 = negative
            it.label = "positive" if pred == 1 else "negative"

    return items


def aggregate(items, by="D"):
    if not items:
        return pd.DataFrame()

    df = pd.DataFrame([{
        "timestamp": it.timestamp,
        "score": it.score,
        "label": it.label
    } for it in items])

    df["timestamp"] = pd.to_datetime(df["timestamp"], errors="coerce")
    grouped = df.groupby(pd.Grouper(key="timestamp", freq=by)).agg(
        score_mean=("score", "mean"),
        count=("score", "count")
    ).reset_index()
    return grouped


def read_csv(file):
    return [
        SentimentItem(row["timestamp"], row["text"], row.get("symbol", None))
        for _, row in pd.read_csv(file).iterrows()
    ]
