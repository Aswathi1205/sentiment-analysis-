# 📰 Sentiment Article Analyzer - README

## 🔍 Overview

This Python script analyzes the sentiment of news articles by extracting text content from a given URL and performing sentiment analysis using **TextBlob**. It provides a detailed breakdown of the article's tone, polarity, subjectivity, and other key metrics.

## ✨ Features

* 📄 Fetches and parses articles using the `newspaper3k` library
* 🧠 Performs sentiment analysis on the article text
* 🎯 Classifies sentiment into 5 categories:

  * 💚 **Strongly Positive** (polarity > 0.5)
  * 🙂 **Positive** (polarity > 0)
  * 😐 **Neutral** (polarity = 0)
  * 🙁 **Negative** (polarity > -0.5 and ≤ 0)
  * 💔 **Strongly Negative** (polarity ≤ -0.5)
* 📊 Provides additional article insights:

  * 📰 Title
  * ✍️ Summary
  * 🏷️ Keywords
  * 💬 Sample sentences
  * 🌐 Language detection

## ⚙️ Requirements

* 🐍 Python 3.x
* 📦 Required packages:

  * `newspaper3k`
  * `textblob`

📥 Install requirements with:

```bash
pip install newspaper3k textblob
```

> 🧾 **Note:** To use TextBlob, you might need to download additional NLTK corpora. Run this once in your Python environment:

```python
import nltk
nltk.download('punkt')
```

## ▶️ Usage

1. Run the script:

```bash
python sentiment_article_analyzer.py
```

2. When prompted, enter the URL of the news article you want to analyze.
3. 📺 View the analysis results in your terminal.

## 📌 Output Example

```
🔍 Fetching and analyzing the article...

📄 Article Title: Example News Article Title  
📝 Article Summary:  
This is an automatically generated summary of the article content...  
🏷️ Keywords: keyword1, keyword2, keyword3

🧠 Analyzed Sentences:  
➡️ This is the first analyzed sentence.  
➡️ Here's another important sentence from the article.

========================================  
🔍 Sentiment Analysis Result  
========================================  
➡️ Overall Tone: Positive  
🟢 Polarity Score: 0.35  
📝 Subjectivity Score: 0.65  
🈸 Detected Language: en
```

## 🧾 Notes

* ⚡ The script analyzes only the first 2000 characters of the article to maintain performance.
* 🚫 Some websites may block automated scraping attempts or require headers/user-agent spoofing.
* 🤖 Sentiment analysis results are approximate and based on linguistic patterns.
* 🌍 Language detection is based on the article text and may not be 100% accurate.

## 🪪 License

This project is open-source and available for public use.

---

