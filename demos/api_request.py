"""
Simple demo showing how to make a GET request from the Spotify API.
"""

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

import os
from dotenv import load_dotenv
import pprint

if __name__ == "__main__":

    load_dotenv()

    cid = os.getenv('CLIENT_ID')
    secret = os.getenv('CLIENT_SECRET')

    client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
    spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

    track = "Fire in the Sky"
    results = spotify.search(q='track:' + track, type='track')
    pprint.pprint(results)