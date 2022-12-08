import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from assets.raperos import artistas_dict1
from csvGenerator import GeneratorCSV

generator = GeneratorCSV()

artistas_result1 = {}


class SpotifyClient:

    def __init__(self):
        self.client_id = '5b0c6adf9d764c30bcf055369080e7a4'
        self.client_secret = '81fa5a3f1419487e8987b67af94f97f0'
        self.client = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(self.client_id, self.client_secret))
        self.subs = None

    def generate_csv(self):
        for artista in artistas_dict1:
            artista = self.client.artist(artista[id])
            artistas_result1[artista['name']] = artista['followers']['total']
        top = dict(sorted(artistas_result1.items(), key=lambda item: item[1], reverse=True))
        lista = top.items()
        top100 = list(lista)[:120]
        generator.create_csv(top100)
        print("csv ha sido creado")
