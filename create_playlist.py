import json
import requests
import os

from secrets import spotify_user_id, spotify_token
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors


class CreatePlaylist:
    def __init__(self):
        self.user_id = spotify_user_id
        self.spotify_token = spotify_token

    # log into youtube
    def get_youtube_client(self):
        pass

    # grab the video from the spotify playlist
    def get_liked_video(self):
        pass

    # create a new playlist
    def create_playlist(self):
        request_body = json.dumps({
            "name": "liked videos from Youtube",
            "description": "pfft getting good good from youtube through the internet",
            "public": True
        })
        query = "https://api.spotify.com/v1/users/{}/playlists".format(self.user_id)
        response = requests.post(
            query,
            data=request_body, headers={
                "Content-Type": "application/json",
                "Authorization": "Bearer {}".format(spotify_token)
            }
        )
        response_json = response.json()

        # playlist id
        return response_json["id"]

    # search for the song
    def get_spotify_uri(self, song_name, artist):
        query = "https://api.spotify.com/v1/search?query=track%3A{}+artist%3A{}&type=track&offset=0&limit=20".format(
            song_name, artist
        )
        response = requests.get(
            query,
            data=query, headers={
                "Content-Type": "application/json",
                "Authorization": "Bearer {}".format(spotify_token)
            }
        )
        response_json = response.json()
        songs = response_json["tracks"]["items"]

        #only first song
        uri = songs[0]["uri"]

        return uri



    # Add the song to  the spotify playlist
    def add_song_to_playlist(self):
        pass
