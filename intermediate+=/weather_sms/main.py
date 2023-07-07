import requests
from datetime import datetime
from twilio.rest import Client

my_lat = 39.644207
my_long = -77.73143
key = '1d5ff10648113295967c8ddf47029d53'
account_sid = 'ACe623bfcec1d9eb7873721f4b182f20fa'
auth_token = '64c7526fb299e71c72570776258b77e8'
client = Client(account_sid, auth_token)


now = datetime.now()

response = requests.get(url=f'https://api.openweathermap.org/data/2.5/forecast?lat={my_lat}&lon={my_long}&units=imerpial&appid={key}')
response.raise_for_status()
data = response.json()
data = data['list']
raining = [{'date': datetime.fromisoformat(row['dt_txt']), 'weather': row['weather'], 'rain': row['rain']} for row in data if 'rain' in row and datetime.fromisoformat(row['dt_txt']).day == now.day]

msg = ''

for rainy_day in raining:
    if rainy_day == raining[0]:
        msg += f"{rainy_day['rain']['3h']} mm of rain are forecast from {rainy_day['date'].hour - 3} to {rainy_day['date'].hour}, "
    elif rainy_day == raining[-1]:
        msg += f"and {rainy_day['rain']['3h']} mm from {rainy_day['date'].hour - 3} to {rainy_day['date'].hour}"
    else:
        msg += f"{rainy_day['rain']['3h']} mm from {rainy_day['date'].hour - 3} to {rainy_day['date'].hour}, "

message = client.messages.create(
  from_='+18444267905',
  to='+12405208934',
  body= msg
)

print(message.status)
    

