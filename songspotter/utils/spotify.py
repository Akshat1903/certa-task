import requests
import sys

from .authentication import authenticate

def get_artists(artist_name):
    url = f"https://api.spotify.com/v1/search"
    access_token = authenticate()

    artists = requests.get(
        url,
        params = {
            "q": artist_name,
            "type": "artist",
            "limit": 3
        },
        headers = {
            "Authorization": "Bearer " + access_token
        }
    )

    if artists.status_code != 200:
        print("Some error occured, please retry")
        sys.exit()

    artists = artists.json()
    data = []

    if artists["artists"]["total"] == 0:
        print("No artist found")
        sys.exit()

    for ar in artists["artists"]["items"]:
        temp_data = {
            "name": ar["name"],
            "uri": ar["uri"],
            "href": ar["href"]
        }
        data.append(temp_data)

    return data

def get_tracks(artist_id):
    url = f"https://api.spotify.com/v1/artists/{artist_id}/top-tracks?market=IN"
    access_token = authenticate()

    tracks = requests.get(
        url,
        headers= {
            "Authorization": "Bearer " + access_token
        }
    )

    if tracks.status_code != 200:
        print("Some error occured, please retry")
        sys.exit()

    tracks = tracks.json()["tracks"]

    tracks = tracks[:3] if len(tracks) > 3 else tracks

    return tracks
