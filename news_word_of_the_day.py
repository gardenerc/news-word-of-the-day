import requests
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import io
import time
import threading

# Function to fetch news headlines
def fetch_news():
    url = "https://newsapi.org/v2/top-headlines?country=us&apiKey=8856e4b4e7b74fa091fa9bbd2c194766"
    response = requests.get(url)
    data = response.json()
    headlines = [article["title"] for article in data["articles"]]
    return headlines

# Function to extract the word of the day and its context
def word_of_the_day(headlines):
    # Add your code to process the headlines, find the word of the day and its context
    # ...

# Function to update the label with the word of the day and its context
def update_label():
    headlines = fetch_news()
    word, context = word_of_the_day(headlines)
    word_label.config(text=f"Word of the day: {word}")
    context_label.config(text=f"Context: {context}")

    # Schedule the function to run again after 60 seconds
    root.after(60000, update_label)

# Function to load and display the animated GIF
def update_gif(ind):
    frame = frames[ind]
    ind += 1
    if ind == frame_count:
        ind = 0
    gif_label.config(image=frame)
    root.after(100, update_gif, ind)

root = Tk()
root.title("News Word of the Day")
root.geometry("400x400")

canvas = Canvas(root, width=400, height=400)
canvas.pack(fill=BOTH, expand=True)

gradient = ttk.Style()
gradient.configure("Grad.TFrame", background="#ADD8E6")

frame = ttk.Frame(root, style="Grad.TFrame")
frame.place(relx=0.5, rely=0.5, anchor=CENTER)

word_label = ttk.Label(frame, text="")
word_label.pack(pady=10)
context_label = ttk.Label(frame, text="")
context_label.pack(pady=10)

# Load and display the animated GIF
url = "https://j.gifs.com/KYo5qo.gif"
response = requests.get(url)
gif_data = response.content
gif = Image.open(io.BytesIO(gif_data))
frames = [ImageTk.PhotoImage(gif.copy()) for i in range(gif.n_frames)]
frame_count = len(frames)

gif_label = ttk.Label(frame)
gif_label.pack(pady=10)

update_label()
update_gif(0)

root.mainloop()
