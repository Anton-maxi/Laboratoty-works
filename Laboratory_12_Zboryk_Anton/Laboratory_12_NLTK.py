from nltk.sentiment import SentimentIntensityAnalyzer

sia = SentimentIntensityAnalyzer()


def get_vader_sentiment(text):
    scores = sia.polarity_scores(text)
    compound = scores['compound']
    if compound >= 0.05:
        return 'positive'
    elif compound <= -0.05:
        return 'negative'
    else:
        return 'neutral'


sample_text1 = "I love this product! It's amazing."
print(get_vader_sentiment(sample_text1))

sample_text2 = "I don't like this product!."
print(get_vader_sentiment(sample_text2))