import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# Download VADER lexicon
try:
    nltk.data.find('sentiment/vader_lexicon.zip')
except LookupError:
    nltk.download('vader_lexicon', quiet=True)

sia = SentimentIntensityAnalyzer()

texts = [
    "The horrific crash caused the death of five people.",
    "Five people died in a car crash on Tuesday.",
    "The vehicle collided with a barrier on the highway.",
    "Three others were injured and taken to the hospital.",
    # Factual negative combined
    """
    Five people died in a car crash on Tuesday. 
    The vehicle collided with a barrier on the highway.
    Police are investigating the cause of the incident.
    Three others were injured and taken to the hospital.
    """
]

print("--- VADER Analysis ---")
for text in texts:
    scores = sia.polarity_scores(text)
    print(f"\nText: {text.strip()[:50]}...")
    print(f"Scores: {scores}")
    if scores['compound'] >= 0.05:
        print("Result: POSITIVE")
    elif scores['compound'] <= -0.05:
        print("Result: NEGATIVE")
    else:
        print("Result: NEUTRAL")
