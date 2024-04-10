import speech_recognition as sr
import re
import pyttsx3
import os

nome = ''


while(True):

    mic = sr.Recognizer()

    with sr.Microphone() as source:
        engine = pyttsx3.init()
        engine.setProperty('voice','com.apple.speech.synthesis.voice.luciana')
        mic.adjust_for_ambient_noise(source)

        print('Vamos começar, fale alguma coisa..')

        audio = mic.listen(source)

        try:
            frase = mic.recognize_google(audio, language = 'pt-BR')

            if re.search(r'\b' + "ajuda" + r'\b', frase):
                engine.say('Ajuda')
                engine.runAndWait()
                print('Algo relacionado a ajuda.')

            elif re.search(r'meu nome é (.*)', frase):
                nome = re.search(r'meu nome é (.*)', frase).group(1)
                print('Seu nome é ' + nome)
                engine.say('O nome falado foi ' + nome)
                engine.runAndWait()

            elif re.search(r'\b' + 'Abrir navegador' + r'\b', frase):
                os.system('start chrome')


            print('Você falou: '+frase)


        except sr.UnknownValueError:
            print('Ops.. Algo deu errado.')