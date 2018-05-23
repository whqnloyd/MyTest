"""
Created on Fri May 22, 2018
@author: Yifeng He

This file contains the APIs of speak() and listen().

"""

import speech_recognition as sr
from gtts import gTTS
import time
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from pygame import mixer


def speak(audioString):
    mixer.init()
    tts = gTTS(text=audioString, lang='en')
    tts.save("./data/tmp.mp3")
    mixer.music.load("./data/tmp.mp3")
    mixer.music.play()


def listen():
    mixer.init()
    response = ''
    while (True == True):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source, duration=1)
            print("Please start to say:")
            audio = r.listen(source, phrase_time_limit=5)

        try:
            # response = r.recognize_sphinx(audio)
            response = r.recognize_google(audio)
            print(response)
            print("I think you said  '" + response + "'")
            tts = gTTS(text="I think you said " + str(response), lang='en')
            tts.save("./data/temp_response.mp3")
            mixer.music.load('./data/temp_response.mp3')
            mixer.music.play()
            if response != '':
                break
        except sr.UnknownValueError:
            print("Sorry. I could not understand. Can you say it again?")
            speak("Sorry. I could not understand. Can you say it again?")
            time.sleep(6)
        except sr.RequestError as e:
            print("Sphinx error; {0}".format(e))
    return response


if __name__ == '__main__':
    speak('Hello, John. Welcome to Anew learning school. My name is Salina. I am your teacher. What topic are you interested in today?')
    time.sleep(9)
    response = listen()
    print(response)
