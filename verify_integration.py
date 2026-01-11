from sentiment_article_analyzer import analyze_text, classify_sentiment, ensure_nltk_data

ensure_nltk_data()

# Factual negative text that TextBlob struggled with
negative_text = """
Five people died in a car crash on Tuesday. 
The vehicle collided with a barrier on the highway.
Police are investigating the cause of the incident.
Three others were injured and taken to the hospital.
"""

print(f"Analyzing Text:\n{negative_text.strip()}")
analysis = analyze_text(negative_text)

print("\n--- Results ---")
print(f"Compound Score: {analysis['compound']}")
print(f"Classification: {classify_sentiment(analysis['compound'])}")
print(f"Pos: {analysis['pos']}")
print(f"Neu: {analysis['neu']}")
print(f"Neg: {analysis['neg']}")

if analysis['compound'] < -0.05:
    print("\n✅ SUCCESS: Correctly classified as NEGATIVE.")
else:
    print("\n❌ FAILURE: Failed to classify as NEGATIVE.")
