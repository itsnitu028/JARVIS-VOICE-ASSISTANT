

https://github.com/user-attachments/assets/b96363a1-f8d8-4244-82a8-9b2e71b9202a



https://github.com/user-attachments/assets/bdf9895d-e5bc-45ac-a1d6-4f69107a6e21

# 🎙️ JARVIS - Voice Assistant

A Python-based voice assistant inspired by JARVIS that can recognize voice commands, open websites, play music, and read the latest news.

## ✨ Features

- 🎤 Wake word detection ("Jarvis")
- 🌐 Open popular websites
  - Google
  - YouTube
  - Facebook
  - LinkedIn
- 🎵 Play songs from a custom music library
- 📰 Read the latest news using NewsAPI
- 🗣️ Text-to-Speech responses
- 🎧 Speech Recognition using Google's Speech Recognition API

---

## 🛠️ Technologies Used

- Python 3.12
- SpeechRecognition
- PyAudio
- gTTS / pyttsx3
- pygame
- requests
- python-dotenv

---

## 📂 Project Structure

```
JARVIS/
│── main.py
│── musicLibrary.py
│── requirements.txt
│── .env.example
│── .gitignore
└── README.md
```

---

## 🚀 Installation

### Clone the repository

```bash
git clone https://github.com/itsnitu028/JARVIS-VOICE-ASSISTANT.git
cd JARVIS-VOICE-ASSISTANT
```

### Create a virtual environment

```bash
python -m venv .venv
```

### Activate the virtual environment

#### Windows

```bash
.venv\Scripts\activate
```

#### Linux / macOS

```bash
source .venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file in the project root.

```env
NEWS_API_KEY=YOUR_NEWS_API_KEY
```

Get your API key from:

https://newsapi.org

---

## ▶️ Run the Project

```bash
python main.py
```

Say:

```
Jarvis
```

Then give commands like:

```
Open Google
Open YouTube
Play Drivers License
Play Double Take
News
```

---

## 🎵 Music Library

Songs are stored inside `musicLibrary.py`.

Example:

```python
music = {
    "drivers license": "YouTube Link",
    "double take": "YouTube Link"
}
```

You can easily add more songs.

---

## 📌 Future Improvements

- ChatGPT integration
- Weather updates
- WhatsApp messaging
- Email support
- AI conversation
- Volume and brightness control
- System automation
- Desktop application (GUI)

---

## 📷 Demo

*(Add screenshots or a demo GIF here.)*

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository.
2. Create a new branch.
3. Commit your changes.
4. Open a Pull Request.

---

## 📄 License

This project is for learning and educational purposes.

---

## 👩‍💻 Author

**Nitika Arora**

GitHub: https://github.com/itsnitu028
