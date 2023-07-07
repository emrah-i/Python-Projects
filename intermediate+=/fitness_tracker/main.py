import requests
from datetime import datetime
from twilio.rest import Client

url = 'https://trackapi.nutritionix.com/v2/natural/exercise'

headers = {
    'x-app-id': '43a3bdd8',
    'x-app-key': '99d24d3ad622575da3262cdc778719a2',
    'x-remote-user-id': 'Emrah'
    }

entry = input('What exercises did you do today? ')

params = {
    "query": f"{entry}",
    "gender": "male",
    "weight_kg": 84,
    "height_cm": 180,
    "age": 23
    }

response = requests.post(url=url, headers=headers, json=params)
data = response.json()
print(data)

now = datetime.now()
today_date = f"{now.day}/{now.month}/{now.year}"
today_time = f"{now.hour}:{now.minute}:{now.second}"

json_data = {}

for i in range(len(data['exercises'])):
    json_data['workout'] = {
        'date': today_date,
        'time': today_time,
        'exercise': data['exercises'][i]['name'].title(),
        'duration': data['exercises'][i]['duration_min'],
        'calories': data['exercises'][i]['nf_calories']
    }
    sheety = 'https://api.sheety.co/22931923422e01a1a3cf4724a9b9bc93/copyOfMyWorkouts/workouts'

    resp = requests.post(url=sheety, json=json_data)
    print(resp.text)