🌟 Random Quote Generator (Python + Tkinter)

This is a simple and fun Python desktop app that shows random inspirational quotes every time you click a button.
It’s built using Tkinter for the GUI and fetches quotes from a live API — https://dummyjson.com/quotes
.

🚀 Features

💬 Displays a new random quote with every click

🧑 Saves your name locally in a file (Names.txt)

🌐 Fetches real quotes from an online API

💾 Automatically creates a file if it doesn’t exist

🎨 Simple and clean Tkinter GUI

⏳ Cool progress bar animation while setting up the file

🛠️ Tech Stack

Python 3

Tkinter – for the GUI

Requests – for fetching quotes from the API

tqdm – for the loading animation

JSON – for saving and reading user data

🧩 How It Works

When you run the program for the first time, it’ll ask for your name.

It saves the name inside Names.txt (in JSON format).

The app greets you by your name when it opens.

Every time you click “Generate Quote”, it fetches a random quote from the API and displays it in the window.

📸 Preview

(You can add a screenshot here once your GUI is open — like ![App Screenshot](screenshot.png))

▶️ How to Run

Clone this repo or download the code:

git clone https://github.com/yourusername/random-quote-generator.git
cd random-quote-generator


Install required modules:

pip install requests tqdm


Run the app:

python main.py

💡 Future Improvements

Add a “Change Name” button

Save favorite quotes locally

Add dark/light theme switch

Show author images or categories

👨‍💻 Author

Asad Ullah Khan
A passionate learner exploring Python, APIs, and GUI development ✨
