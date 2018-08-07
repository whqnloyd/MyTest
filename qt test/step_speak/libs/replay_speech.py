import pyaudio
import wave

def replay_speech_file(path):
    f = wave.open(path, 'r')
    p = pyaudio.PyAudio()
    stream = p.open(format=p.get_format_from_width(f.getsampwidth()), 
					channels=f.getnchannels(), 
					rate=f.getframerate(),
                    output=True)
    data = f.readframes(1024)
    while (data != b''):
        stream.write(data)
        data = f.readframes(1024)
    stream.stop_stream()
    stream.close()
    f.close()
    p.terminate()


if (__name__ == '__main__'):
    replay_speech_file('data/speech.wav')