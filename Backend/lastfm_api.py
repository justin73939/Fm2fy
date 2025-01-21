from config import API_KEY, USERNAME
import requests

def get_loved_tracks():
    tracks = []
    page = 1
    while True:
        url = f"http://ws.audioscrobbler.com/2.0/?method=user.getlovedtracks&user={USERNAME}&api_key={API_KEY}&format=json&page={page}" 
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            if 'lovedtracks' in data and 'track' in data['lovedtracks']:
                page_tracks = data['lovedtracks']['track']
                tracks.extend([(track['name'], track['artist']['name']) for track in page_tracks])

                if len(page_tracks) < 50:  # Assuming 50 is the number of tracks per page
                    break #if we've reached the last page
                page += 1  
            else:
                print("No loved tracks found or error in response.")
                break
        else:
            print(f"Error fetching loved tracks: {response.status_code}")
            break

    return tracks
    
# for debugging purposes alone; nothing else
if __name__ == "__main__":
    loved_tracks = get_loved_tracks()
    for track in loved_tracks:
        print(track)

