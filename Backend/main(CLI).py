import lastfm_api as fm
import spotify_api as spo
def main():
    # 1. Define Playlist Name and Description
    playlist_name = "Last.fm Loved Tracks"
    playlist_description = "Tracks loved on Last.fm, converted effortlessly to spotify playlist"

    # 2. Fetch Loved Tracks from Last.fm
    print("Fetching loved tracks from Last.fm...")
    loved_tracks = fm.get_loved_tracks()

    if not loved_tracks:
        print("No loved tracks found. Exiting.")
        return

    # 3. Search for Tracks on Spotify
    print("Searching for tracks on Spotify...")
    track_uris = []
    for track_name, artist_name in loved_tracks:
        print(f"Searching for '{track_name}' by '{artist_name}'...")
        track_uri = spo.search_track(track_name, artist_name)
        if track_uri:
            track_uris.append(track_uri)



    if not track_uris:
        print("No tracks could be found on Spotify. Exiting.")
        return

    # 4. Create a Playlist on Spotify
    print("Creating playlist on Spotify...")
    playlist_id = spo.create_playlist(playlist_name, playlist_description)

    # 5. Add Tracks to Playlist
    print(f"Adding {len(track_uris)} tracks to the playlist...")
    spo.add_tracks_to_playlist(playlist_id, track_uris)
    print(f"Successfully added {len(track_uris)} tracks to the playlist '{playlist_name}'.")

if __name__ == "__main__":
    main()

# need to figure out how to add 3 missed tracks (lonerism trakcs; maybe fuzzy matching? but probably simpler)
# after that, we finally, start work on deployment
# integrate git tracking