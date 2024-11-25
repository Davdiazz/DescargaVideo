import yt_dlp as youtube_dl # importar las librerias con pip "pip install yt_dlp " abriendo la terminal 
import os

def descargar_Video(url):
    directorio_actual = os.getcwd()
    
    ydl_opts = {
        'format': 'best',
        'outtmpl': os.path.join(directorio_actual, '%(title)s.%(ext)s'),  # Guardar en el directorio donde esta el archivo
    }
    
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

# Pega la Url de la Cancion o Video que deseas descargar
url = "https://www.youtube.com/watch?v=gnMYDQf37qs"
descargar_Video(url)