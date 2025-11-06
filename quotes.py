import os
import json
import random
import requests
from tqdm import tqdm
import time
import tkinter as tk
from tkinter import messagebox




# File and API setup
file_name = "Names.txt"
Quote_API = "https://dummyjson.com/quotes"

# Create the file if it doesn't exist
if not os.path.exists(file_name):
    print("File does not exist, creating the file first...")
    for i in tqdm(range(100), desc="Progress", ncols=70):
        time.sleep(0.025)

    user_name = input("Enter your name to save in the file: ")
    with open(file_name, "w") as f:
        data = {"Name": user_name}  # ✅ store as dictionary
        json.dump(data, f)

    print(f"File has been created: {file_name}")

# Read the name from the file
with open(file_name, "r") as f:
    try:
        user_data = json.load(f)
        Name = user_data.get("Name", "Unknown User")
    except json.JSONDecodeError:
        Name = "Unknown User"

# Function to get one random quote


def get_quote():
    try:
        response = requests.get(Quote_API)
        response.raise_for_status()
        data = response.json()
        quote = random.choice(data["quotes"])
        return f'"{quote["quote"]}"\n\n— {quote["author"]}'
    except Exception as e:
        return f"Error fetching quote: {e}"

# Function for button click


def show_quote():
    quote = get_quote()
    quote_label.config(text=quote)


# Setup Tkinter window
root = tk.Tk()
root.title("Random Quote Generator 💬")
root.geometry("700x450")
root.config(bg="#2b2b2b")

# Main title

title_label = tk.Label(root, text="✨ Welcome to my first quote generetor✨", font=(
    "Arial", 18, "bold"), bg="#2b2b2b", fg="white")
title_label.pack(pady=10)

# Title label
title_label = tk.Label(root, text="✨ Random Quote App ✨", font=(
    "Arial", 18, "bold"), bg="#2b2b2b", fg="white")
title_label.pack(pady=10)

# Show user name
name_label = tk.Label(root, text=f"Welcome, {Name} 👋", font=(
    "Arial", 14, "bold"), bg="#2b2b2b", fg="#00ff99")
name_label.pack(pady=5)

# Quote label
quote_label = tk.Label(root, text="Click the button to get a quote!", wraplength=400, justify="center",
                       font=("Arial", 12), bg="#2b2b2b", fg="#00ff99")
quote_label.pack(pady=30)

# Button
btn = tk.Button(root, text="Generate Quote", font=(
    "Arial", 12, "bold"), bg="#00ff99", fg="black", command=show_quote)
btn.pack(pady=10)

# Start app
root.mainloop()
