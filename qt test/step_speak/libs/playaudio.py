import pyaudio
import wave

def play_speech():
    f = wave.open('C:/Users/Luodai Yang/Projects/MyTest/qt test/open_img/audio/output.wav')
    p = pyaudio.PyAudio()
    stream = p.open(format=p.get_format_from_width(f.getsampwidth()), channels=f.getnchannels(), rate=f.getframerate(),
                    output=True)
    data = f.readframes(1024)
    while (data != b''):
        stream.write(data)
        data = f.readframes(1024)
    stream.stop_stream()
    stream.close()
    f.close()
    p.terminate()


#self test
if __name__ == '__main__':
    play_speech()
