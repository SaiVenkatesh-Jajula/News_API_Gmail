import requests
import SendMail
from nltk.sentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()
API_KEY = "e8a671df9ab341c7902781b1d1089627"
sources = "techcrunch"
url = f"https://newsapi.org/v2/top-headlines?sources={sources}&apiKey={API_KEY}&language=en"

# Make request
req = requests.get(url)

# Store data as dictionary
content = req.json()

# News sending to mail
news = "Subject: Today's News from Venkatesh Jajula"

# Organising the Data
no_of_news=0
for data in content["articles"]:
    positive_value = analyzer.polarity_scores(data['description'])['pos']
    negative_value = analyzer.polarity_scores(data['description'])['neg']
    # Worst case scenario
    if data["title"] is not None and positive_value >= negative_value and no_of_news != 5:
        news += '\n'
        news += data["title"] + '\n'
        news += data['description'] + '\n'
        news += data["url"] + '\n'
        no_of_news += 1

SendMail.sendmail(news.encode('utf-8'))
