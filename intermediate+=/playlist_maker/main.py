import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from bs4 import BeautifulSoup

date = input('What week would you like to get a playlist for(YYYY-MM-DD): ')
dates = date.strip().split('-')

while len(dates[0]) != 4 or len(dates[1]) != 2 or len(dates[2]) != 2 or dates[0].isalpha() or dates[1].isalpha() or dates[2].isalpha():
    print('Please enter in this exact format: YYYY-MM-DD.')
    date = input('Enter here: ')
    dates = date.strip().split('-')

response = requests.get(url=f"https://www.billboard.com/charts/hot-100/{date.strip()}/")
data = response.text

soup = BeautifulSoup(data, 'html.parser')
song = soup.select('div[class="o-chart-results-list-row-container"] ul li[class="lrv-u-width-100p"] ul h3')
artists = soup.select('div[class="o-chart-results-list-row-container"] ul li[class="lrv-u-width-100p"] ul li span[class]')

artists = [name.text for name in artists if name.get("class")[1] == 'a-no-trucate']

songs = [f"{artists[i].strip()}-{song[i].text.strip()}" for i in range(len(artists))]

client_id = '6e8733d5c93346929371e20f250ba4c1'
client_secret = '85382ad5178145afae9198ba9e8b16e3'

scope = "user-library-read"


sp = spotipy.Spotify(auth_manager=SpotifyOAuth(show_dialog=True, username='emrakh26', cache_path='intermediate+=/playlist_maker/info.text', client_id=client_id, client_secret=client_secret, redirect_uri="http://example.com", scope="playlist-modify-private"))
user = sp.current_user()
sp.user_playlist_create(name="12342", user=user['id'])

'''song_ids = []
for song in songs:
    item = sp.search(song, limit=1)
    song_ids.append(item['tracks']['items'][0]['id'])
    
sp.playlist_add_items(items=song_ids)'''