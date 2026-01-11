from textblob import TextBlob

# Factual reporting of a negative event, often found in news
factual_negative = """
Five people died in a car crash on Tuesday. 
The vehicle collided with a barrier on the highway.
Police are investigating the cause of the incident.
Three others were injured and taken to the hospital.
"""

blob = TextBlob(factual_negative)
print(f"Text: {factual_negative.strip()}")
print(f"Polarity: {blob.sentiment.polarity}")
print(f"Subjectivity: {blob.sentiment.subjectivity}")

if blob.sentiment.polarity > 0:
    print("Result: POSITIVE (Incorrect/Unexpected)")
elif blob.sentiment.polarity < 0:
    print("Result: NEGATIVE (Correct)")
else:
    print("Result: NEUTRAL (Potentially misleading)")
