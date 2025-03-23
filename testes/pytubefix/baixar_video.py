from pytubefix import YouTube
from pathlib import Path
import platform

sistema = platform.system()
# > Seleciona a pasta (Vídeos) de acordo com o sistema operacional
if sistema == 'Windows': # ? Windowns
    pasta_videos = Path.home() / "Videos" 
elif sistema == 'Darwin': # ? macOS
    pasta_videos = Path.home() / "Movies"
else: # ? Linux e outros Unix-like
    pasta_videos = Path.home() / "Videos" 

pasta_destino = pasta_videos / "youtube_downloads" # > Cria uma pasta (youtube_downloads) dentro da pasta vídeos
pasta_destino.mkdir(parents=True, exist_ok=True) # > Confirma se a pasta existe

url = input("Digite a url do vídeo que deseja baixar: ").strip()

try:
    yt = YouTube(url) # > Cria o objeto Youtube
    
    stream = yt.streams.get_highest_resolution() # > Seleciona o stream com a melhor resolução
    stream.download(output_path=pasta_destino) # > Baixa o vídeo para o diretório atual
    
    print("Download completo!")
except Exception as error:
    print("Download falhou")
    print(f"Erro: {error}")