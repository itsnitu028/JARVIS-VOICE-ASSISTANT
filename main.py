import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
from dotenv import load_dotenv
import os
import requests
import pygame
from gtts import gTTS

load_dotenv()

newsapi = os.getenv("NEWS_API_KEY")


def speak_old(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    engine.stop()

def speak(text):
    tts = gTTS(text)
    tts.save('temp.mp3') 

    # Initialize Pygame mixer
    pygame.mixer.init()

    # Load the MP3 file
    pygame.mixer.music.load('temp.mp3')

    # Play the MP3 file
    pygame.mixer.music.play()

    # Keep the program running until the music stops playing
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    
    pygame.mixer.music.unload()
    os.remove("temp.mp3") 

def processCommand(c):
        if "open google" in c.lower():
            webbrowser.open("https://google.com")
        elif "open facebook" in c.lower():
            webbrowser.open("https://facebook.com")
        elif "open youtube" in c.lower():
            webbrowser.open("https://youtube.com")
        elif "open linkedin" in c.lower():
            webbrowser.open("https://linkedin.com")
        elif c.lower().startswith("play"):
            song = c[5:].strip().lower()      # removes "play "
            found = False

            for name, link in musicLibrary.music.items():
                if song in name:
                    webbrowser.open(link)
                    found = True
                    break

            if not found:
                speak("Song not found")
        elif "news" in c.lower():
             newsapi = os.getenv("NEWS_API_KEY")
             r = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}")
             if r.status_code == 200:
                # Parse the JSON response
                data = r.json()
                
                # Extract the articles
                articles = data.get('articles', [])
                print(articles)
                # Print the headlines
                for article in articles:
                    speak(article['title'])

                
        else:
            speak("I don't have this functionality")
             
    


if __name__== "__main__" :
   speak("Initializing Jarvis..... ")
#    listen for the wake word jarvis
   while True:
        r = sr.Recognizer()
        print("recognizing...")
        try:
                with sr.Microphone() as source:
                    print("Listening...")
                    audio = r.listen(source, timeout=2, phrase_time_limit=2)
                word = r.recognize_google(audio)
                print(word)

                if("jarvis" in word.lower()):
                    speak("Yes sir")   
                    with sr.Microphone() as source:
                        print("Jarvis Active...")
                        print("Listening...")
                        audio = r.listen(source)
                        command = r.recognize_google(audio)

                        print(command)   
                        processCommand(command)


        except Exception as e:
                print("Error; {0}".format(e))