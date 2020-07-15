from fetch_data import get_song_id, get_audio_features, get_audio_analysis_feat
import numpy as np

def agg_audio_feat_to_2darray(title, artist):
    song_id = get_song_id(title, artist)

    feat_dict = get_audio_features(song_id)

    my_analysis_dict = get_audio_analysis_feat(song_id)

    feat_dict.update(my_analysis_dict)

    my_list = [feat_dict[k] for k,v in feat_dict.items()]

    return np.array(my_list).reshape((1,15))


