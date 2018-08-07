import pyaudio
import wave

def record_audio_file(time, path):
    #setup
    chunk = 1024
    format = pyaudio.paInt16
    channels = 2
    rate = 44100
    p = pyaudio.PyAudio()
    frames = []

    #load
    stream = p.open(format= format, channels= channels, rate= rate, input= True, frames_per_buffer= chunk)
    print("recording")

    for i in range(0, int(rate / chunk * time)):
        data = stream.read(chunk)
        frames.append(data)
    print("done recording")

    stream.stop_stream()
    stream.close()
    p.terminate()

    f = wave.open(path, 'wb')
    f.setnchannels(channels)
    f.setsampwidth(p.get_sample_size(format))
    f.setframerate(rate)
    f.writeframes(b''.join(frames))
    f.close()

#self test
if (__name__ == '__main__'):
    record_audio_file(5, 'data/speech.wav')
    f = wave.open('data/speech.wav', 'r')
    p = pyaudio.PyAudio()
    stream = p.open(format= p.get_format_from_width(f.getsampwidth()), channels= f.getnchannels(), rate= f.getframerate(), output= True)
    data = f.readframes(1024)
    while (data != ''):
        stream.write(data)
        data = f.readframes(1024)
    stream.stop_stream()
    stream.close()
    f.close()
    p.terminate()