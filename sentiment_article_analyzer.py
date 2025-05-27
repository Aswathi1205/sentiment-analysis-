
from newspaper import Article
from textblob import TextBlob

def classify_sentiment(polarity):
    if polarity > 0.5:
        return "Strongly Positive"
    elif polarity > 0:
        return "Positive"
    elif polarity == 0:
        return "Neutral"
    elif polarity > -0.5:
        return "Negative"
    else:
        return "Strongly Negative"

def analyze_article_sentiment(url):
    print("\n🔍 Fetching and analyzing the article...")

    try:
        article = Article(url, fetch_images=False)
        article.download()
        article.parse()
        article.nlp()
    except Exception as e:
        print(f"❌ Error downloading or parsing the article: {e}")
        return

    if not article.text.strip():
        print("❌ No content found in the article.")
        return

    text_to_analyze = article.text[:2000]
    blob = TextBlob(text_to_analyze)
    sentiment = blob.sentiment

    print("\n📄 Article Title:", article.title)
    print("📝 Article Summary:")
    print(article.summary)
    print("🏷️ Keywords:", ", ".join(article.keywords))

    print("\n🧠 Analyzed Sentences:")
    for sentence in blob.sentences[:5]:
        print("➡️", sentence)

    print("\n" + "="*40)
    print("🔍 Sentiment Analysis Result")
    print("="*40)
    print(f"➡️ Overall Tone: {classify_sentiment(sentiment.polarity)}")
    print(f"🟢 Polarity Score: {sentiment.polarity:.2f}")
    print(f"📝 Subjectivity Score: {sentiment.subjectivity:.2f}")
    print(f"🈸 Detected Language: {article.meta_lang}")

if __name__ == "__main__":
    url = input("🔗 Enter the news article URL: ").strip()
    analyze_article_sentiment(url)
