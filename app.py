import streamlit as st
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from sentiment_article_analyzer import fetch_article, analyze_text, classify_sentiment, ensure_nltk_data

# --- Page Config ---
st.set_page_config(
    page_title="News Sentiment Analyzer",
    page_icon="📰",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Custom CSS for Polish ---
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        color: #4B4B4B;
        text-align: center;
        font-weight: 700;
        margin-bottom: 2rem;
    }
    .sub-header {
        font-size: 1.2rem;
        color: #666;
        text-align: center;
        margin-bottom: 2rem;
    }
    .metric-card {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 0.5rem;
        text-align: center;
    }
</style>
""", unsafe_allow_html=True)

# --- Sidebar ---
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/2965/2965879.png", width=100)
    st.title("About")
    st.info(
        """
        This app uses **VADER (Valence Aware Dictionary and sEntiment Reasoner)** to analyze the sentiment of news articles.
        
        **Libraries used:**
        - `newspaper3k`: For article extraction
        - `nltk (VADER)`: For accurate sentiment analysis
        - `wordcloud`: For visual representation
        - `streamlit`: For the web interface
        """
    )
   

# --- Main Content ---
ensure_nltk_data()

st.markdown('<div class="main-header">📰 News Article Sentiment Analyzer</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">Uncover the hidden emotional tone of any news article in seconds.</div>', unsafe_allow_html=True)

# Input Section
url = st.text_input("🔗 Paste the News Article URL here:", placeholder="https://example.com/article")

if st.button("Analyze Article", type="primary"):
    if not url:
        st.warning("⚠️ Please execute with a valid URL.")
    else:
        with st.spinner("🔍 Fetching and analyzing article..."):
            article = fetch_article(url)

        if article:
            # Analyze
            text_to_analyze = article.text
            if len(text_to_analyze) > 5000:
                 text_to_analyze = text_to_analyze[:5000] 

            analysis = analyze_text(text_to_analyze)
            
            # Extract VADER metrics
            compound = analysis["compound"]
            pos = analysis["pos"]
            neu = analysis["neu"]
            neg = analysis["neg"]
            sentences_data = analysis["sentences_data"]
            
            # --- Results Dashboard ---
            st.success("Analysis Complete!")
            
            st.markdown("### 📊 Sentiment Overview")
            col1, col2, col3, col4 = st.columns(4)
            
            with col1:
                st.metric("Overall Tone", classify_sentiment(compound))
            with col2:
                st.metric("Compound Score", f"{compound:.2f}", help="-1 (Neg) to +1 (Pos)")
            with col3:
                st.metric("Positive Content", f"{pos*100:.1f}%")
            with col4:
                st.metric("Negative Content", f"{neg*100:.1f}%")

            st.divider()

            # --- Visualizations ---
            col_viz1, col_viz2 = st.columns(2)
            
            with col_viz1:
                st.markdown("### ☁️ Word Cloud")
                if article.text:
                    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(article.text)
                    fig, ax = plt.subplots(figsize=(10, 5))
                    ax.imshow(wordcloud, interpolation='bilinear')
                    ax.axis("off")
                    st.pyplot(fig)
                else:
                    st.info("Not enough text for Word Cloud.")
            
            with col_viz2:
                st.markdown("### 📈 Sentiment Trend")
                # Calculate sentiment for each sentence to show flow
                sentence_scores = [item['compound'] for item in sentences_data]
                if sentence_scores:
                    st.line_chart(sentence_scores, use_container_width=True)
                    st.caption("Sentiment compound score fluctuating sentence by sentence.")
                else:
                    st.info("Not enough sentences to chart trend.")

            st.divider()

            # --- Detailed Content ---
            st.markdown("### 📝 Article Details")
            
            with st.expander("📄 Full Summary"):
                st.write(article.summary if article.summary else "No summary available.")

            with st.expander("🏷️ Keywords"):
                st.write(", ".join(article.keywords))

            st.markdown("### 🔍 Key Sentences & Values")
            # Display first 5 sentences with their scores
            for i, item in enumerate(sentences_data[:5]):
                 score_color = "red" if item['compound'] < -0.05 else "green" if item['compound'] > 0.05 else "grey"
                 st.markdown(f"**{i+1}.** {item['text']} *(Score: :{score_color}[{item['compound']:.2f}])*")

        else:
            st.error("❌ Failed to fetch the article. Please check the URL and try again.")
