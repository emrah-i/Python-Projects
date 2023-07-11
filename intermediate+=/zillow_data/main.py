from bs4 import BeautifulSoup
import requests

url = 'https://www.zillow.com'
headers = {
    'User-Agent': 'User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
    'Referer': 'https://www.google.com/',
    'Connection': 'keep-alive'
    }

response = requests.get(url=url, headers=headers)
data = response.text
print(data)

soup = BeautifulSoup(data, "html.parser")
items = soup.select('#search-page-list-container div ul')
for item in items:
    print(item)