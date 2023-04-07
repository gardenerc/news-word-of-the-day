import requests
from collections import Counter
import string
import re
import nltk
from nltk.corpus import stopwords

# Download the stop words list if you haven't already
nltk.download("stopwords")

API_KEY = "8856e4b4e7b74fa091fa9bbd2c194766"
URL = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={API_KEY}"

response = requests.get(URL)
data = response.json()

headlines = [article["title"] for article in data["articles"]]

# Load the English stop words list
stop_words = set(stopwords.words("english"))

word_frequency = Counter()

for headline in headlines:
    words = re.findall(r'\b\w+\b', headline.lower())
    filtered_words = [word for word in words if word not in stop_words]
    word_frequency.update(filtered_words)

word_of_the_day = word_frequency.most_common(1)[0][0]

print(f"Word of the day: {word_of_the_day}")
