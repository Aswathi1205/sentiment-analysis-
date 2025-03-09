# News Article Sentiment Analysis

## 📌 Overview
This project allows users to input a news article URL and get a quick summary along with a sentiment analysis report. The sentiment analysis determines whether the article's tone is **Positive, Negative, or Neutral**.

## 🚀 Features
- Fetches and processes news articles from any URL.
- Summarizes the article by extracting key sentences.
- Performs sentiment analysis to determine the overall tone.
- Displays the polarity (positive/negative) and subjectivity (factual/opinion-based).

## 🛠️ Installation
### Prerequisites
Ensure you have **Python 3.x** installed.

### Install Required Libraries
```sh
pip install newspaper3k textblob
```

Additionally, download the necessary NLTK data for text processing:
```sh
python -m textblob.download_corpora
```

## 🔧 Usage
1. **Run the script:**
```sh
python sentiment_analysis.py
```
2. **Enter the article URL** when prompted.
3. **View the results**, including:
   - Key points from the article
   - Overall sentiment (Positive, Negative, Neutral)
   - Polarity and Subjectivity scores

## 📜 Example Output
```
🔗 Enter the news article URL: https://example.com/news

📄 Article Summary:
📝 Sentence 1
📝 Sentence 2
📝 Sentence 3
📝 Sentence 4
📝 Sentence 5

🔍 Sentiment Analysis Result:
➡️ Overall Tone: Positive
🟢 Polarity Score: 0.75
📝 Subjectivity Score: 0.60
```

## 🛠️ Troubleshooting
- If the article fails to download, **check the URL** and make sure it's accessible.
- If you get a missing corpus error, **run the TextBlob data download command** again.
- If the script takes too long, **use a shorter article** or manually limit text length in the script.

## 🤝 Contributing
Feel free to suggest improvements or report issues by opening an issue or pull request.

## 📜 License
This project is licensed under the **MIT License**.

