import requests

API_KEY="e8a671df9ab341c7902781b1d1089627"
url=f"https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey={API_KEY}"

# Make request
req = requests.get(url)

# Store data as dictionary
content = req.json()

# Organising the Data
for data in content["articles"]:
    print(data["title"])
    print(data["description"])
