import spotipy.util as util
import requests
import pandas as pd
import spotipy

import ast
from typing import List
from os import listdir


def get_streamings(path: str = './Data/') -> List[dict]:

    files = ['./Data//' + x for x in listdir(path)
             if x.split('.')[0][:-1] == 'StreamingHistory']

    all_streamings = []

    for file in files:
        with open(file, 'r', encoding='UTF-8') as f:
            new_streamings = ast.literal_eval(f.read())
            all_streamings += [streaming for streaming
                               in new_streamings]
    return all_streamings


username = '6bd0a5olhzd0b06kn41l2sxb7'
client_id = '44c08017661d496a999b0d2b191e9dfd'
client_secret = 'dace2ad7d4ab41ff94c9f78295c13ff5'
redirect_uri = 'http://localhost:8888/callback'
scope = 'user-read-recently-played'

token = util.prompt_for_user_token(username=username,
                                   scope=scope,
                                   client_id=client_id,
                                   client_secret=client_secret,
                                   redirect_uri=redirect_uri)

print(token)

streamings = get_streamings()
unique_tracks = list(set([streaming['trackName']
                          for streaming in streamings]))


def get_id(track_name: str, token: str) -> str:
    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': f'Bearer ' + token,
    }
    params = [
        ('q', track_name),
        ('type', 'track'),
    ]
    try:
        response = requests.get('https://api.spotify.com/v1/search',
                                headers=headers, params=params, timeout=5)
        json = response.json()
        first_result = json['tracks']['items'][0]
        track_id = first_result['id']
        return track_id
    except:
        return None


def get_features(track_id: str, token: str) -> dict:
    sp = spotipy.Spotify(auth=token)
    try:
        features = sp.audio_features([track_id])
        return features[0]
    except:
        return None


all_features = {}
for track in unique_tracks:
    track_id = get_id(track, token)
    features = get_features(track_id, token)
    if features:
        all_features[track] = features

with_features = []
for track_name, features in all_features.items():
    with_features.append({'name': track_name, **features})

df = pd.DataFrame(with_features)
df.to_csv('./Data/spotify_streaming_history.csv')