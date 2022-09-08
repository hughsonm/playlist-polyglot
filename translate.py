import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import sys
import yaml
from ytmusicapi import YTMusic


def GetYTMusicIdFromTitleArtist(title, artist, ytmusic):
    results = ytmusic.search('{} - {}'.format(title, artist), limit=10)
    if len(results) == 0:
        return None
    songs = [result for result in results if result['resultType'] == 'song']
    if len(songs) == 0:
        return None
    return(songs[0]['videoId'])


def CreateSpotifyConnection(secretsFileName):
    secretsFile = open(secretsFileName, 'r')
    secrets = yaml.safe_load(secretsFile)
    auth_manager = SpotifyClientCredentials(
        client_id=secrets['Spotify']['Client ID'],
        client_secret=secrets['Spotify']['Client Secret'])
    spotify = spotipy.Spotify(auth_manager=auth_manager)
    return(spotify)


def CreatYTMusicConnection():
    ytmusic = YTMusic('headers_auth.json')
    return(ytmusic)


def NewYTMusicPlaylistFromSpotifyPlaylist(spPlaylist, ytmusic):
    playlist = ytmusic.create_playlist(
        spPlaylist['name'], spPlaylist['description'])
    return(playlist)


def PopulateYTMusicPlaylistFromSpotifyPlaylist(ytPlaylist, spPlaylist, ytmusic):
    playlistItems = []
    for item in spPlaylist['tracks']['items']:
        track = item['track']
        title = track['name']
        artist = track['artists'][0]['name']
        trackString = '{} - {}'.format(title, artist)
        idToAdd = GetYTMusicIdFromTitleArtist(title, artist, ytmusic)
        if idToAdd:
            playlistItems.append(idToAdd)
        print('|{: >7}|{: >7}| {}'.format('Added' if idToAdd else '',
              '' if idToAdd else 'Failed', trackString))
    if len(playlistItems) != 0:
        ytmusic.add_playlist_items(ytPlaylist, playlistItems)


if __name__ == "__main__":
    ytConnection = CreatYTMusicConnection()
    spConnection = CreateSpotifyConnection('secrets.yaml')

    spotifyId = sys.argv[1]
    spPlaylist = spConnection.playlist(spotifyId)
    ytPlaylist = NewYTMusicPlaylistFromSpotifyPlaylist(
        spPlaylist, ytConnection)
    PopulateYTMusicPlaylistFromSpotifyPlaylist(
        ytPlaylist, spPlaylist, ytConnection)
