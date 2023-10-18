import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Step 1: Set up your Spotify Developer credentials
client_id = 'd3f16a00c7c344d88953f96a3bc04e66'
client_secret = 'b87120c44b14432bb90e0a6dd13234af'

# Step 2: Authenticate your application
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id,
                     client_secret=client_secret, redirect_uri='http://localhost:3000'))

# Step 3: Retrieve a list of genres
genres = sp.recommendation_genre_seeds()

# Step 4: Fetch the top 200 songs in each genre
top_tracks = {}

for genre in genres['genres']:
    top_tracks[genre] = sp.recommendations(
        seed_genres=[genre], limit=200)['tracks']


print("what")

# Now, top_tracks is a dictionary where each key is a genre, and the value is a list of the top 200 tracks in that genre.
# You can process this data further as needed.
