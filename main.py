import requests
import SendMail

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
for data in content["articles"][:10]:
    # Worst case scenario
    if data["title"] is not None:
        news += '\n'
        news += data["title"] + '\n'
        news += data['description'] + '\n'
        news += data["url"] + '\n'

SendMail.sendmail(news.encode('utf-8'))
