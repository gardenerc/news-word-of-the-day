import requests
from collections import Counter
import tkinter as tk
from tkinter import ttk

def fetch_headlines(api_key):
    url = f'https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key}'
    response = requests.get(url)
    data = response.json()
    headlines = [article['title'] for article in data['articles']]
    return headlines

def extract_interesting_words(headlines):
    common_words = {'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'have', 'in', 'is', 'it', 'of', 'on', 'or', 'that', 'the', 'to', 'with'}
    news_outlet_names = {'abc', 'cbs', 'cnn', 'fox', 'nbc', 'nyt', 'reuters', 'wsj'}
    generic_business_terms = {'business', 'company', 'market', 'stock', 'economy', 'economic', 'trade', 'finance', 'financial', 'industry', 'sector', 'product', 'service', 'consumer', 'job', 'employment', 'unemployment', 'growth', 'decline', 'rate', 'percentage', 'price', 'cost', 'value', 'profit', 'loss', 'revenue', 'sales', 'income', 'tax', 'budget', 'deficit', 'surplus'}

    words_to_exclude = common_words | news_outlet_names | generic_business_terms

    words = []
    for headline in headlines:
        for word in headline.split():
            word = word.lower().strip('.,;:!?"()[]{}<>')
            if word not in words_to_exclude and word.isalpha():
                words.append(word)

    return words

def find_most_common_words(words, n=4):
    counter = Counter(words)
    most_common_words = counter.most_common(n)
    return most_common_words

def main(api_key):
    headlines = fetch_headlines(api_key)
    words = extract_interesting_words(headlines)
    most_common_words = find_most_common_words(words)

    # Create a tkinter window
    root = tk.Tk()
    root.title("News Word of the Day")

    bg_color = "#1A73E8"
    root.configure(background=bg_color)

    label = ttk.Label(root, text="Today's most frequent interesting words in the news:", background=bg_color, foreground="white", font=("Arial", 14))
    label.pack(pady=10)

    for word, count in most_common_words:
        word_label = ttk.Label(root, text=f"{word} ({count} times)", background=bg_color, foreground="white", font=("Arial", 12))
        word_label.pack()

    root.mainloop()

if __name__ == '__main__':
    api_key = '8856e4b4e7b74fa091fa9bbd2c194766'
    main(api_key)
