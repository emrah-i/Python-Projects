import requests
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

for i in range(len(artists)):
   print(i, artists[i].strip(), "-", song[i].text.strip())
