import speech_recognition as sr

mic = sr.Recognizer()

with sr.Microphone as source:
    mic.adjust_for_ambient_noise(source)

    print('Vamos começar, fale alguma coisa')
