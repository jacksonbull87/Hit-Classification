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

def get_audio_features(song_id):
    #returns audio features: danceability, energy, key, loudness, mode, speechiness, acoustiness, 
    # instrumentalness, livenes, valence, temo, duration, time_siganature
    client = spotipy.SpotifyClientCredentials(client_id, client_secret)
    s_client = spotipy.Spotify(client_credentials_manager=client)
    features = s_client.audio_features(song_id)
    feature_dict = features[0]
    my_features = {key:value for key, value in feature_dict.items() if key not in ['type', 'id', 'uri', 'track_href','analysis_url']}
    return my_features 

