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
    common_words = {'the', 'and', 'in', 'a', 'to', 'of', 'on', 'for', 'with'}
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
