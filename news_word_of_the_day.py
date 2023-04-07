import requests
from collections import Counter
import re
import tkinter as tk
from tkinter import font as tkfont

def fetch_headlines(api_key):
    url = f'https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key}'
    response = requests.get(url)
    data = response.json()
    headlines = [article['title'] for article in data['articles']]
    return headlines

def find_interesting_words(headlines):
    common_words = {
    'a', 'an', 'the', 'and', 'of', 'to', 'in', 'on', 'for', 'with', 'as', 'at', 'by', 'from', 'that', 'which', 'who', 'whom',
    'whose', 'this', 'these', 'those', 'there', 'where', 'when', 'how', 'why', 'or', 'but', 'so', 'if', 'then', 'else',
    'while', 'than', 'either', 'each', 'any', 'all', 'some', 'one', 'two', 'three', 'four', 'five', 'first', 'next', 'last',
    'many', 'much', 'several', 'few', 'less', 'own', 'other', 'out', 'old', 'new', 'good', 'bad', 'high', 'low', 'best',
    'least', 'own', 'other', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'hundred',
    'thousand', 'first', 'second', 'third', 'next', 'last', 'many', 'several', 'few', 'less', 'own', 'other', 'former',
    'latter', 'own', 'other', 'off', 'often', 'likely', 'so', 'such', 'own', 'other', 'own', 'other', 'news', 'cbs', 'says',
    'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'january', 'february', 'march', 'april',
    'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december'
}

# Add the new categories of common words here
days_of_the_week = {'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'}
months = {'january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december'}
numbers_in_words = {'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten'}
generic_political_terms = {'government', 'president', 'senate', 'congress', 'court', 'law', 'bill', 'vote', 'election', 'party', 'republican', 'democrat', 'policy', 'leader', 'official', 'administration', 'state', 'federal', 'local', 'city', 'country', 'national', 'international', 'global'}
generic_business_terms = {'business', 'company', 'market', 'stock', 'economy', 'economic', 'trade', 'finance', 'financial', 'industry', 'sector', 'product', 'service', 'consumer', 'job', 'employment', 'unemployment', 'growth', 'decline', 'rate', 'percentage', 'price', 'cost', 'value', 'profit', 'loss', 'revenue', 'sales', 'income', 'tax', 'budget', 'deficit', 'sur

    words = [word.lower() for headline in headlines for word in re.findall(r'\b\w+\b', headline) if word.lower() not in common_words]
    word_counts = Counter(words)
    interesting_words = word_counts.most_common(4)
    return interesting_words

def find_example_headlines(interesting_words, headlines):
    example_headlines = []
    for word, _ in interesting_words:
        for headline in headlines:
            if word in headline.lower():
                example_headlines.append((word, headline))
                break
    return example_headlines

def create_gui(example_headlines):
    root = tk.Tk()
    root.title("News Word of the Day")
    root.configure(bg='#1DA1F2')

    bold_font = tkfont.Font(weight='bold')

    description_label = tk.Label(root, text="The 4 most frequent interesting words in today's news headlines:", bg='#1DA1F2', font=bold_font)
    description_label.pack(pady=10)

    for word, headline in example_headlines:
        word_label = tk.Label(root, text=f"{word}:", bg='#1DA1F2', font=bold_font)
        word_label.pack(anchor='w')

        example_label = tk.Label(root, text=headline, bg='#1DA1F2', wraplength=600, justify='left')
        example_label.pack(anchor='w', padx=20)

    root.mainloop()

def main():
    api_key = '8856e4b4e7b74fa091fa9bbd2c194766'
    headlines = fetch_headlines(api_key)
    interesting_words = find_interesting_words(headlines)
    example_headlines = find_example_headlines(interesting_words, headlines)
    create_gui(example_headlines)

if __name__ == '__main__':
    main()
