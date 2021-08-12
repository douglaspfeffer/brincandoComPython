#pip install pytube
from pytube import YouTube

#Cria objeto com URL do vídeo a ser baixado
video=YouTube('https://www.youtube.com/watch?v=culn2wKBoKI')

#Configura a melhor qualidade de vídeo
stream=video.streams.get_highest_resolution()

#Faz o Download do vídeo e salva na pasta "saída"
stream.download(output_path='./saida')
