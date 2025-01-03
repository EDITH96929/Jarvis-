

 
import pyttsx3 # type: ignore
import speech_recognition as sr # type: ignore
import datetime

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def greet():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good morning!")
    elif 12 <= hour < 18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")
    speak("Hello sunil! I'm Jarvis, your virtual assistant. How can I help you today?")

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
        return query
    except sr.UnknownValueError:
        print("Sorry, I didn't catch that. Can you please repeat?")
        return None
    except sr.RequestError:
        print("Sorry, I couldn't access the Google API. Please check your internet connection.")
        return None

if __name__ == "__main__":
    greet()
    while True:
        command = listen()
        if command:
            # Perform actions based on the command
            # For now, let's just print the command
            print("Performing action for:", command)
            # Implement your logic for different commands here
            # Add a condition to break the loop if the user wants to exit
            if "exit" in command:
                speak("Goodbye! Have a great day!")
                break
