import gtts

def text2speech(open_path):
    with open(open_path, 'r') as f:
        text = f.read()

    tts = gtts.gTTS(text=text, lang='en-US')
    tts.save('C:/Users/Luodai Yang/Projects/MyTest/qt test/open_img/audio/text.mp3')

if (__name__ == '__main__'):
    text2speech('C:/Users/Luodai Yang/Projects/MyTest/qt test/open_img/text/L1.txt')
