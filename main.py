from gtts import gTTS
from os import system
# from random_words import RandomWords
import requests

#Aqui va tu API_KEY de https://newsapi.org/
API_KEY = '5929ee224a0c46ef87152b19e791adc1'

#Este es el url para obtener los datos, cambia la categoria para obtener otros tipos de noticias
url = "https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey={0}".format(API_KEY)

#Esta variable nos dará el control sobre el bucle
active = False

#Aqui cambias al nombre de tu reproductor accesible desde la terminal
reproductor = 'xplayer'

#Bucle principal para obtener noticias con descripciones
while not active:
    #Hacemos la petición de tipo get al servidor
    response = requests.get(url)

    try:
        for i in range(len(response.json()['articles'])):
            if not active:
                if str(response.json()['articles'][i]['description']) != 'None':
                    active = True
                    word = "Title: " + response.json()['articles'][i]['source']['name']
                    word += "Description: " + str(response.json()['articles'][i]['description'])

    except Exception:
        print("Ha ocurrido un error")

#Mostramos los resultados en la terminal
print("La noticia es: {0}".format(word))

#Configuramos la sintesis de voz
tts = gTTS(word, lang='en')
#Lo guardamos en el archivo audio.mp3
tts.save("audio.mp3")


system("{0} audio.mp3".format(reproductor))
