import requests
import pandas as pd
import numpy as np

import utils


class UserTop:
    def __init__(self,token,base_url,headers):
        self.__token = token
        self.__headers = headers
        self.__base_url = base_url
        self.__params = {
            'limit' : 10,
            'time_range' : "long_term"
        }
        self.__df_top_genre = pd.DataFrame()
        self.__df_top_artist = pd.DataFrame()

    def get_top_artists(self):
        _endpoint = 'me/top/artists'

        response = requests.get(self.__base_url+_endpoint, headers=self.__headers,params=self.__params)   
        dic_json = response.json()
        top_artists = dic_json['items']
        list_artist = []
        list_top_genre = []
        for a in range(len(top_artists)):
            list_artist.append(top_artists[a]['name']) 
            if top_artists[a]['genres'][0] not in list_top_genre and len(list_top_genre) < 5:
                list_top_genre.append(top_artists[a]['genres'][0])
        self.__df_top_genre['genre'] = list_top_genre
        self.__df_top_artist['artists'] = list_artist
        utils.write_csv(self.__df_top_artist,'top_artist')
        utils.write_csv(self.__df_top_genre,'top_genre')

    def get_top_tracks(self):
        _endpoint = 'me/top/tracks'
        response = requests.get(self.__base_url+_endpoint, headers=self.__headers,params=self.__params)   
        dic_json = response.json()
        top_tracks = dic_json['items']
        list_tracks = []
        list_track_artist= []
        for a in range(len(top_tracks)):
            list_tracks.append(top_tracks[a]['name']) 
            list_track_artist.append(top_tracks[a]['artists'][0]['name'])
        df = pd.DataFrame(np.column_stack([list_tracks,list_track_artist]),columns= ['Tracks','Artists']) 
        utils.write_csv(df,'top_tracks')   
