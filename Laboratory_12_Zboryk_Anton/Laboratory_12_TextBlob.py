from textblob import TextBlob

def sentiment_textblob(text):
    blob = TextBlob(text)
    c = blob.sentiment.polarity
    if c >= 0.05:
        result = "positive"
    elif c <= -0.05:
        result = "negative"
    else:
        result = "neutral"
    print(f"Sentiment degree:{result}")
    print(blob.sentiment)
text1 = "Mix is very amazing and simple to use. What a great tool!"
text2 = "Shweta played well in the match as usual."
text3 = "I am feeling sad today."
sentiment_textblob(text1)
sentiment_textblob(text2)
sentiment_textblob(text3)