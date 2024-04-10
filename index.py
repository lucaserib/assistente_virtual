import speech_recognition as sr
import re
import pyttsx3
import os
import subprocess
import webbrowser

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
                engine.say('Abrindo navegador')
                engine.runAndWait()
                os.system('start chrome')

            elif re.search(r'\b' + 'Abrir YouTube' + r'\b', frase):
                engine.say('Abrindo youtube')
                engine.runAndWait()
                webbrowser.open("https://www.youtube.com")
            
            elif re.search(r'\b' + 'Abrir Spotify' + r'\b', frase):
                engine.say('Abrindo Spotify')
                engine.runAndWait()
                os.system('start C:\\Users\\lucas\\AppData\\Roaming\\Spotify\\Spotify.exe')


            


            print('Você falou: '+frase)


        except sr.UnknownValueError:
            print('Ops.. Algo deu errado.')