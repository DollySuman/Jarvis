
import musiclibrary
import webbrowser
import speech_recognition as sr
import pyttsx3
import subprocess 

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processcomand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")

    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")

    elif "open instagram" in c.lower():
        webbrowser.open("https://instagram.com")

    elif "open pinterest" in c.lower():
        webbrowser.open("https://pinterest.com")

    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")

    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")

    elif "open chatgpt" in c.lower():
        webbrowser.open("https://chatgpt.com")

    elif c.lower().startswith("play"):
        song=c.lower().split(" ")[1]
        link = musiclibrary.music[song]
        webbrowser.open(link)
    
    elif "run calculator" in c.lower():
        subprocess.Popen(["open", "/System/Applications/Calculator.app"])

    elif "run telegram" in c.lower():
        subprocess.Popen(["open", "/Applications/Telegram.app"])

    elif "run spotify" in c.lower():
        subprocess.Popen(["open", "/Applications/Spotify.app"])

    elif "run facetime" in c.lower():
        subprocess.Popen(["open", "/System/Applications/FaceTime.app"])

    elif "run terminal" in c.lower():
        subprocess.Popen(["open", "/System/Applications/Utilities/Terminal.app"])

    elif "run photobooth" in c.lower():
        subprocess.Popen(["open", "/System/Applications/Photo Booth.app"])

    elif "run mail" in c.lower():
        subprocess.Popen(["open", "/System/Applications/Mail.app"])

    elif "run appstore" in c.lower():
        subprocess.Popen(["open", "/System/Applications/App Store.app"])

    else: 
        pass
        
if __name__ == "__main__":
    speak("Initializing Jarvis...")
    while True:
        #Listen for Jarvis
        #Obtain audio from microphone
        r = sr.Recognizer()
        print("recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source,timeout=2, phrase_time_limit=4)
                word = r.recognize_google(audio)
            if(word.lower()=="jarvis"):
                speak("Yes, hello")
                #Listen for command
                with sr.Microphone() as source:
                    print("Working on it...")
                    audio = r.listen(source)
                    command =r.recognize_google(audio) 

                    processcomand(command)

            
        except Exception as e:
            print(f"Eroor{e}")
