import tekore as tk
from dotenv import load_dotenv
import os
import math

load_dotenv()

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")
redirect_uri = os.getenv("REDIRECT")

conf = (client_id, client_secret, redirect_uri)
token = tk.prompt_for_user_token(*conf, scope=tk.scope.every)

spotify = tk.Spotify(token)

song_to_add = "4OhqsmPMreC0EFCo3OmDSm"
playlist_to_add_to = "6Sr56E01Q59vytGaN3uG2W"
hours = 100

song = spotify.track_audio_features(song_to_add)
print(song)
playlist = spotify.playlist(playlist_to_add_to)

number_of_times = (hours * 60 * 60 * 1000 % song.duration_ms) / 100

print(f"need to add the song times : {number_of_times}")

for i in range(math.floor(number_of_times)):
    print(i)
    spotify.playlist_add(playlist_to_add_to, [song.uri] * 100)

