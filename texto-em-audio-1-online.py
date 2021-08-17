#pip install gTTS pyttsx3 playsound
from playsound import playsound
import gtts

texto=""" Olá! Seja muito bem vindo! Utilizamos a biblioteca gtts (Google Text to Speech) para esse objetivo """

#Configura o objeto gTTS com texto e idioma
tts=gtts.gTTS(texto,lang='pt-br')

#Salva o arquivo de áudio
tts.save('audio.mp3')

#Toca o arquivo de áudio
playsound('audio.mp3')
