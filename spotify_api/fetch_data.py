import sp_config
import spotipy
import re

client_id = sp_config.my_dict['client_id']
client_secret = sp_config.my_dict['client_secret']

def get_song_id(title, artist):
    client = spotipy.SpotifyClientCredentials(client_id, client_secret)
    s_client = spotipy.Spotify(client_credentials_manager=client)
    
    results = s_client.search(q= artist.lower())

    for i in range(len(results['tracks']['items'])):
        if re.match(title.lower(), results['tracks']['items'][i]['name'].lower()):
            print(results['tracks']['items'][i]['name'])
            song_id = results['tracks']['items'][i]['id']
    return song_id

