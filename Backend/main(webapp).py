from flask import Flask, render_template, request, jsonify
import lastfm_api as fm
import spotify_api as spo

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create_playlist', methods=['POST'])
def create_playlist():
    # 1. Define Playlist Name and Description
    playlist_name = "Last.fm Loved Tracks"
    playlist_description = "Tracks loved on Last.fm, converted effortlessly to Spotify playlist"

    # 2. Fetch Loved Tracks from Last.fm
    loved_tracks = fm.get_loved_tracks()

    if not loved_tracks:
        return jsonify({"message": "No loved tracks found."}), 400

    # 3. Search for Tracks on Spotify
    track_uris = []
    for track_name, artist_name in loved_tracks:
        track_uri = spo.search_track(track_name, artist_name)
        if track_uri:
            track_uris.append(track_uri)

    if not track_uris:
        return jsonify({"message": "No tracks could be found on Spotify."}), 400

    # 4. Create a Playlist on Spotify
    playlist_id = spo.create_playlist(playlist_name, playlist_description)

    # 5. Add Tracks to Playlist
    spo.add_tracks_to_playlist(playlist_id, track_uris)
    return jsonify({"message": f"Successfully added {len(track_uris)} tracks to the playlist '{playlist_name}'."})

if __name__ == "__main__":
    app.run(debug=True)

#i need to look at chat and figure out wtf going on, need to update index.html and need to figure out wtf chat is telling me about static and templates