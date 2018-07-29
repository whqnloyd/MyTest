import google.cloud.texttospeech
import os

def text2speech(open_path):
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'C:/Users/Luodai Yang/Projects/MyTest/qt test/open_img/libs/key.json'

    with open(open_path, 'r') as f:
        text = f.read()

    client = google.cloud.texttospeech.TextToSpeechClient()

    synthesis_input = google.cloud.texttospeech.types.SynthesisInput(text=text)

    voice = google.cloud.texttospeech.types.VoiceSelectionParams(
        language_code='en-US',
        ssml_gender=google.cloud.texttospeech.enums.SsmlVoiceGender.FEMALE)

    audio_config = google.cloud.texttospeech.types.AudioConfig(
        audio_encoding=google.cloud.texttospeech.enums.AudioEncoding.LINEAR16)

    response = client.synthesize_speech(synthesis_input, voice, audio_config)

    with open('C:/Users/Luodai Yang/Projects/MyTest/qt test/open_img/audio/output.wav', 'wb') as outs:
        outs.write(response.audio_content)


if __name__ == '__main__':
    text2speech('C:/Users/Luodai Yang/Projects/MyTest/qt test/open_img/text/L1.txt')