# 📰 News Article Sentiment Analyzer

A real-time web application that analyzes the sentiment of news articles using Natural Language Processing (NLP). It provides detailed insights into the emotional tone, polarity, and key themes of any article URL provided.

## 🚀 Features

*   **Instant Analysis**: Fetch and analyze articles directly from a URL.
*   **Accurate Sentiment**: Uses the **VADER** model for robust sentiment classification (Positive, Negative, Neutral).
*   **Visual Dashboard**:
    *   **Word Cloud**: Visualize frequent terms.
    *   **Sentiment Trend**: Track how sentiment changes sentence-by-sentence.
    *   **Key Metrics**: Compound scores and subjectivity analysis.
*   **User-Friendly Interface**: Built with [Streamlit](https://streamlit.io/) for a clean and responsive experience.

## 🛠️ Installation

1.  **Clone the repository** (if applicable) or navigate to the project directory.

2.  **Install dependencies**:
    Ensure you have Python 3.8+ installed. Run the following command:
    ```bash
    pip install streamlit newspaper3k nltk textblob wordcloud matplotlib
    ```

3.  **Download NLTK Data**:
    The app automatically checks for and downloads necessary NLTK data (punkt, vader_lexicon) on the first run.

## 🏃‍♂️ Usage

1.  **Run the Application**:
    Execute the following command in your terminal:
    ```bash
    streamlit run app.py
    ```

2.  **Analyze an Article**:
    *   The app will open in your web browser (usually http://localhost:8501).
    *   Paste a valid News Article URL into the input field.
    *   Click **"Analyze Article"**.

## 📂 Project Structure

*   `app.py`: The main Streamlit application script.
*   `sentiment_article_analyzer.py`: The core NLP analysis logic (helper functions).
*   `PROJECT_REPORT.md`: Detailed documentation on the project's working, use cases, and accuracy.

## 🧠 Technical Details

This project utilizes:
*   **Newspaper3k**: For article scraping and parsing.
*   **NLTK VADER**: For lexicon and rule-based sentiment analysis.
*   **TextBlob**: For additional text processing.



For a deep dive into the architecture and use cases, please refer to the [Project Report](PROJECT_REPORT.md).
