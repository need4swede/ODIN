import platform, simpleaudio, os
import speech_recognition as sr
global voiceCommand
global nameFreya
nameFreya = 'freya'

def freya():
    if platform.system() == "Darwin":
        r = sr.Recognizer()
        mic = sr.Microphone()
        try:
            with mic as source:
                r.adjust_for_ambient_noise(source)
                print('Listening!')
                audio = r.listen(source)
                voiceCommand = r.recognize_google(audio)
                if 'hello' in voiceCommand:
                    print('You said hello')
                    root_dir = os.path.dirname(os.path.abspath(__file__))
                    sounds_dir = root_dir + "/sounds/"
                    greeting_matt = simpleaudio.WaveObject.from_wave_file(sounds_dir + 'greeting_matt.wav')
                    play_obj = greeting_matt.play()
                else:
                    print(f"You said no")
        except:
            print("Can't hear you")

freya()
