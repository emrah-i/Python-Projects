import requests

my_lat = 39.644207
my_long = -77.73143
key = '1d5ff10648113295967c8ddf47029d53'


response = requests.get(url=f'https://api.openweathermap.org/data/2.5/weather?lat={my_lat}&lon={my_long}&appid={key}')
response.raise_for_status()
data = response.json()
print(data)