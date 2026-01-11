import nltk
import sys
from newspaper import Article
from textblob import TextBlob
from nltk.sentiment import SentimentIntensityAnalyzer
from typing import Optional, Dict, Any, List

# Ensure UTF-8 output for Windows terminals
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except AttributeError:
        pass # In case it's run in an environment where stdout is not a text stream

def ensure_nltk_data():
    """Ensure necessary NLTK data is available."""
    needed_resources = ['tokenizers/punkt', 'sentiment/vader_lexicon']
    for resource in needed_resources:
        try:
            nltk.data.find(resource)
        except LookupError:
            print(f"⬇️ Downloading necessary NLTK data: {resource}...")
            # Extract the package name from resource path (e.g. 'tokenizers/punkt' -> 'punkt')
            package = resource.split('/')[-1].replace('.zip', '')
            # Special case for vader_lexicon which is stored as sentiment/vader_lexicon.zip but package is vader_lexicon
            if 'vader' in package: 
                 package = 'vader_lexicon'
            nltk.download(package, quiet=True)

def classify_sentiment(compound_score: float) -> str:
    """
    Classifies sentiment based on VADER compound score.
    
    Args:
        compound_score (float): The VADER compound score (-1.0 to 1.0).
        
    Returns:
        str: Descriptive component of the sentiment.
    """
    if compound_score >= 0.05:
        if compound_score > 0.6:
            return "Strongly Positive"
        return "Positive"
    elif compound_score <= -0.05:
        if compound_score < -0.6:
            return "Strongly Negative"
        return "Negative"
    else:
        return "Neutral"

def fetch_article(url: str) -> Optional[Article]:
    """
    Downloads and parses an article from a URL.
    
    Args:
        url (str): The URL of the news article.
        
    Returns:
        Article: The parsed newspaper.Article object or None if failed.
    """
    print("\n🔍 Fetching and analyzing the article...")
    try:
        article = Article(url, fetch_images=False)
        article.download()
        article.parse()
        article.nlp()
        return article
    except Exception as e:
        print(f"❌ Error downloading or parsing the article: {e}")
        return None

def analyze_text(text: str) -> Dict[str, Any]:
    """
    Performs sentiment analysis on the provided text using VADER.
    
    Args:
        text (str): The text to analyze.
        
    Returns:
        Dict: A dictionary containing the analysis results.
    """
    sia = SentimentIntensityAnalyzer()
    blob = TextBlob(text) # Still use TextBlob for sentence tokenization
    
    # Analyze overall text
    scores = sia.polarity_scores(text)
    
    # Analyze per sentence
    sentences_data = []
    for sentence in blob.sentences:
        sentence_str = str(sentence)
        s_scores = sia.polarity_scores(sentence_str)
        sentences_data.append({
            "text": sentence_str,
            "compound": s_scores['compound']
        })
        
    return {
        "blob": blob, # Kept for word cloud or other textblob utils
        "vader_scores": scores,
        "compound": scores['compound'],
        "pos": scores['pos'],
        "neu": scores['neu'],
        "neg": scores['neg'],
        "sentences_data": sentences_data
    }

def display_results(article: Article, analysis: Dict[str, Any]):
    """
    Prints the analysis results to the console.
    
    Args:
        article (Article): The parsed article object.
        analysis (Dict): The analysis results from analyze_text.
    """
    print("\n" + "="*50)
    print("📄 Article Title:", article.title)
    print("\n📝 Article Summary:")
    print(article.summary)
    
    if article.keywords:
        print("\n🏷️ Keywords:", ", ".join(article.keywords))

    print("\n🧠 Sample Analyzed Sentences:")
    sentences_data = analysis["sentences_data"]
    for item in sentences_data[:3]:
        print(f"  ➡️ {item['text']} (Score: {item['compound']})")

    print("\n" + "="*50)
    print("🔍 Sentiment Analysis Result (VADER)")
    print("="*50)
    
    compound = analysis["compound"]
    print(f"➡️ Overall Tone:     {classify_sentiment(compound)}")
    print(f"🟢 Compound Score:   {compound:.2f}")
    print(f"➕ Positive:         {analysis['pos']:.2f}")
    print(f"⚪ Neutral:          {analysis['neu']:.2f}")
    print(f"➖ Negative:         {analysis['neg']:.2f}")
    
    if hasattr(article, 'meta_lang') and article.meta_lang:
        print(f"🈸 Detected Language: {article.meta_lang}")
    print("="*50 + "\n")

def main():
    ensure_nltk_data()
    
    while True:
        url = input("🔗 Enter the news article URL (or 'q' to quit): ").strip()
        if url.lower() == 'q':
            print("👋 Exiting...")
            break
            
        if not url:
            continue
            
        article = fetch_article(url)
        if not article:
            continue
            
        if not article.text.strip():
            print("❌ No content found in the article.")
            continue
            
        text_to_analyze = article.text[:5000] 
        
        analysis = analyze_text(text_to_analyze)
        display_results(article, analysis)

if __name__ == "__main__":
    main()
