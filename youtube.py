from pytube import YouTube


# Cole o link do vídeo que deseja baixar
video_link = "https://www.youtube.com/watch?v=tpx8VWw2FoM&ab_channel=FelipeMotaOficial"

# Cria uma instância do objeto YouTube
yt = YouTube(video_link)

# Seleciona a melhor resolução disponível
stream = yt.streams.get_highest_resolution()

# Define o diretório onde o arquivo será salvo
diretorio = '/Users/giovannileocadio/Downloads/'

# Baixa o vídeo
stream.download(output_path=diretorio)

print("Download concluído!")
