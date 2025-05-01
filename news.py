import nltk
import re
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from collections import Counter
from nltk.sentiment import SentimentIntensityAnalyzer


# nltk.download('punkt')
# nltk.download('stopwords')
# nltk.download('vader_lexicon')


newsletter_text = """
Welcome to our weekly newsletter! We are excited to introduce our new eco-friendly product line.
Enjoy a 20% discount this weekend! Read testimonials from happy customers and stay updated with the latest trends.
Our mission is to provide sustainable solutions.
"""

def preprocess_text(text):
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    return text.lower()

clean_text = preprocess_text(newsletter_text)

words = word_tokenize(clean_text)
sentences = sent_tokenize(newsletter_text)

stop_words = set(stopwords.words("english"))
filtered_words = [word for word in words if word not in stop_words]


keyword_counts = Counter(filtered_words)
top_keywords = keyword_counts.most_common(5)


sia = SentimentIntensityAnalyzer()
sentiment_score = sia.polarity_scores(newsletter_text)


print("Top Keywords:", top_keywords)
print("Total Sentences:", len(sentences))
print("Sentiment Analysis:", sentiment_score)

