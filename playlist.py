
import pandas as pd
import numpy as np
import requests



class Playlist():
    
    def __init__(self, auth, base_url,headers):
        self.__headers = headers
        self.__base_url = base_url
        playlistID = '37i9dQZF1DWWGFQLoP9qlv'
        __playlist_endpoint = f'playlists/{playlistID}'
        __playlist_response = requests.get(base_url+__playlist_endpoint,headers=self.__headers)
        self.__playlist_object =__playlist_response.json()
        self.__df = pd.DataFrame(columns=['track','id'])

    def get_playlist_followers(self):
        followers = [self.__playlist_object['followers']['total']]
        df_followers = pd.DataFrame(followers,columns=['followers'])
        df_followers.to_csv('followers.csv')


    def get_playlist_cover(self):
        img_url = self.__playlist_object['images'][0]['url']
        img_data = requests.get(img_url).content
        with open('playlist_cover.png','wb') as f:
            f.write(img_data)

    def get_playlists_tracks(self):
        
        self.__df['track'] = [self.__playlist_object['tracks']['items'][t]['track']['name'] for t in range(len(self.__playlist_object['tracks']['items']))]
        self.__df['id'] = [self.__playlist_object['tracks']['items'][t]['track']['uri'] for t in range(len(self.__playlist_object['tracks']['items']))]
        return self.__df
            
    def get_audio_features(self):
        acous,dance,energy,instru,temp,val,loud,live = [],[],[],[],[],[],[],[]
        for t in range(len(self.__df)):
            track_id = self.__df['id'][t][14:]
            _endpoint = f'audio-features/{track_id}'
            response = requests.get(self.__base_url+_endpoint,headers=self.__headers)
            audio_feat = response.json()
            acous.append(audio_feat['acousticness'])
            dance.append(audio_feat['danceability'])
            energy.append(audio_feat['energy'])
            instru.append(audio_feat['instrumentalness'])
            temp.append(audio_feat['tempo'])
            val.append(audio_feat['valence'])
            loud.append(audio_feat['loudness'])
            live.append(audio_feat['liveness'])
        self.__df['acousticness'] = acous
        self.__df['danceability'] = dance
        self.__df['energy'] = energy
        self.__df['instrumentalness'] = instru
        self.__df['tempo'] = temp
        self.__df['valence'] = val
        self.__df['loudness'] = loud
        self.__df['liveness'] = live
        return self.__df