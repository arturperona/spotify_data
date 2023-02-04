
import os


import utils
from auth import Auth
from UserTop import UserTop
from playlist import Playlist


class SpotifyRequest:
    def __init__(self):
       base_url = 'https://api.spotify.com/v1/'
       auth = Auth()
       auth.generate_token()
       token =  auth.get_token()
       headers = {
            'Authorization': f'Bearer {token}',
            "Accept": "application/json"
        }
       self.__usertop = UserTop(token,base_url,headers)
       self.__playlist = Playlist(token,base_url,headers)

    def run_requests(self):
        #self.create_folder('/results')

        self.__usertop.get_top_artists()
        self.__usertop.get_top_tracks()

        self.__playlist.get_playlist_cover()
        self.__playlist.get_playlist_followers()
        self.__playlist.get_playlists_tracks()
        df = self.__playlist.get_audio_features()
        df_avg = df.mean(axis=0,numeric_only=True)
        utils.write_csv(df_avg,'average_features',True)
        
    
    def create_folder(self,path):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        print(dir_path+path)
        if not os.path.exists(path):
            os.makedirs(path)









#get_top_artists()
#write_csv(get_top_tracks(),'top_tracks')
#print(get_playlist_followers(playlist_ID))
#get_playlist_cover(playlist_ID)
#df = get_playlists_tracks(playlist_ID)


#df2 = get_audio_features(df)
#write_csv(df2,'track_features')
#df_avg = df2.mean(axis=0, numeric_only=True)
#write_csv(df_avg,'average_features',True)
