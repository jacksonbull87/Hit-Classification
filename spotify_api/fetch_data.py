import spotipy
import re
import numpy as np
import pickle
import xgboost
import sklearn
from sklearn.preprocessing import LabelEncoder 

client_id = 'fde423d9c3454b2b87726f5afab15cb4'
client_secret = '9a5747edc5c043c8bed9c8ba3b04c6bf'

def get_song_id(title, artist):
    client = spotipy.SpotifyClientCredentials(client_id, client_secret)
    s_client = spotipy.Spotify(client_credentials_manager=client)
    
    results = s_client.search(q= artist.lower())

    for i in range(len(results['tracks']['items'])):
        if re.match(title.lower(), results['tracks']['items'][i]['name'].lower()):
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

def get_audio_analysis_feat(song_id):
    #returns the start of the chorus in the 3rd section and number of sections as a dictionary
    client = spotipy.SpotifyClientCredentials(client_id, client_secret)
    s_client = spotipy.Spotify(client_credentials_manager=client)
    analysis = s_client.audio_analysis(song_id)
    my_analysis_dict = {key:value for key,value in analysis['sections'][2].items() if key == 'start'}
    my_analysis_dict.update({'sections': len(analysis['sections'][2])})
    new_key = "chorus_hit"
    old_key = "start"
    my_analysis_dict[new_key] = my_analysis_dict.pop(old_key)
    return my_analysis_dict

def agg_audio_feat_to_2darray(title, artist):
    song_id = get_song_id(title, artist)

    feat_dict = get_audio_features(song_id)

    my_analysis_dict = get_audio_analysis_feat(song_id)

    feat_dict.update(my_analysis_dict)

    my_list = [feat_dict[k] for k,v in feat_dict.items()]

    return np.array(my_list).reshape((1,15))



def make_prediction(title, artist):
    array = agg_audio_feat_to_2darray(title, artist)
    model = pickle.load(open("spotify_api/model.pickle.dat", "rb"))
    
    prediction = model.predict(array)
    
    return prediction[0]

