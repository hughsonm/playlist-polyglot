# Playlist Polyglot
Create a [YouTube Music](https://music.youtube.com) playlist from a [Spotify](https://open.spotify.com/) playlist!

# Instructions
1. Install the required python packages:
    ```python
    python3 -m pip install spotipy ytmusicapi pyyaml
    ```
2. [Create app credentials in your Spotify account](https://developer.spotify.com/dashboard/applications)
3. Add those credentials to this project
    * Add your *Client ID* and *Client Secret* to `secrets.example.yaml`
    * Rename that file as `secrets.yaml`
4. [Create a `headers_auth.json` file](https://ytmusicapi.readthedocs.io/en/latest/setup.html) to enable creating playlists on YouTube Music
5. Get the id of the Spotify playlist
    * Example: `https://open.spotify.com/playlist/32O0SSXDNWDrMievPkV0Im`
    * id = `32O0SSXDNWDrMievPkV0Im`
6. Run `translate.py` and pass the id on the command line
    ```bash
    python3 translate.py 32O0SSXDNWDrMievPkV0Im
    ```
7. Open YouTube Music and listen to your playlist!
