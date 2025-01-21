import spotipy
from spotipy.oauth2 import SpotifyOAuth
from config import SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET, SPOTIPY_REDIRECT_URI


# Set up authentication with Spotify
scope = 'playlist-modify-public playlist-modify-private'  # Scope for modifying public playlists

# Create a Spotipy client
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID,
                                               client_secret=SPOTIPY_CLIENT_SECRET,
                                               redirect_uri=SPOTIPY_REDIRECT_URI,
                                               scope=scope))

def create_playlist(playlist_name, description=''):
    """Create a new playlist for the user."""
    user_id = sp.current_user()['id'] # Dynamically get the user ID
    playlist = sp.user_playlist_create(user=user_id, name=playlist_name, description=description)
    return playlist['id']  # Return the playlist ID

def add_tracks_to_playlist(playlist_id, track_uris):
    """Add tracks to a specified playlist in chunks of 100."""
    chunk_size = 100
    for i in range(0, len(track_uris), chunk_size):
        # Get a chunk of up to 100 tracks
        track_chunk = track_uris[i:i + chunk_size]
        try:
            sp.playlist_add_items(playlist_id, track_chunk)
            print(f"Added {len(track_chunk)} tracks to playlist {playlist_id}.")
        except Exception as e:
            print(f"Error adding tracks: {e}")

def search_track(track_name, artist_name):
    """Search for a track by name and artist."""
    num_artists = len(artist_name.split(';'))
    query = f'track:{track_name} artist:{artist_name}'
    results = sp.search(q=query, type='track', limit=1)
    tracks = results['tracks']['items']
    if tracks:
        return tracks[0]['uri']  # Return the track URI
    elif not tracks and (num_artists>1):
        Query = f'track:{track_name} artist:{artist_name.split(";")[0]}'
        Results = sp.search(q=Query, type='track', limit=1)
        Tracks = Results['tracks']['items']
        if tracks:
            return Tracks[0]['uri']  # Return the track URI
        else:
            print(f"Track '{track_name}' by '{artist_name}' not found.")
            return None
    else:
        print(f"Track '{track_name}' by '{artist_name}' not found.")
        return None
    
#you could add error handling for buggy requests
#exact track matches may not be found in certain cases, think about fuzzy matching?