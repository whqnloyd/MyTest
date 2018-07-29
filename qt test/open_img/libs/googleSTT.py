import speech_recognition as sr

def speech_to_txt():
    #load
    r = sr.Recognizer()
    with sr.AudioFile('C:/Users/Luodai Yang/Projects/MyTest/qt test/open_img/audio/speech.wav') as src:
        audio = r.record(src)

    #get results
    text = r.recognize_google(audio, key = None, language = 'en-US')
    print(text)

    #save
    with open('C:/Users/Luodai Yang/Projects/MyTest/qt test/open_img/text/speech.txt', 'w') as f:
        f.write(text)


if __name__ == '__main__':
    speech_to_txt()