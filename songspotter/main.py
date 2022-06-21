from utils.spotify import *

print("***** Welcome to Spotify search. Search for an artist and get their top tracks! *****")

input_artist = input("Enter artist name: ")

artists = get_artists(input_artist)

print('\n')
print("These are the top 3 search results - ")
for i, e in enumerate(artists):
    print(f"{i + 1} - {e['name']}")

print('\n')

while True:
    option = input("Choose artist index to see his/her top tracks - ")

    try:
        option = int(option)
        if option > 0 and option <= 3:
            break
        print("Please choose a valid index !!")
    except:
        print("Please choose a valid index !!")

print('\n')
print(f"These are the top 3 tracks of {artists[option - 1]['name']} - ")
artist_id = artists[option - 1]["uri"].split(":")[2]

tracks = get_tracks(artist_id)

for i, t in enumerate(tracks):
    print(f"{i + 1} - {t['name']}: {t['external_urls']['spotify']}")

print('\n')
print("***** Thank you for using the program! *****")