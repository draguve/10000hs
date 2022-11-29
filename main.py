import tekore as tk
from dotenv import load_dotenv
import os

load_dotenv()

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")
redirect_uri = os.getenv("REDIRECT")

conf = (client_id, client_secret, redirect_uri)
token = tk.prompt_for_user_token(*conf, scope=tk.scope.every)

spotify = tk.Spotify(token)
tracks = spotify.current_user_top_tracks(limit=10)
for item in tracks.items:
    print(item.name)