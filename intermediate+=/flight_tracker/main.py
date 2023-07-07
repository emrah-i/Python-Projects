from twilio.rest import Client
from datetime import datetime, timedelta
from flight_search import *
from sheets import *
import requests

# Initialize flights
FS = FlightSearch()
FS.date_from = datetime.now().strftime('%d/%m/%Y')
FS.date_to = (datetime.now() + timedelta(days=180)).strftime('%d/%m/%Y')

# Initialize twilio
account_sid = 'ACe623bfcec1d9eb7873721f4b182f20fa'
auth_token = '64c7526fb299e71c72570776258b77e8'
client = Client(account_sid, auth_token)

# Get all google sheets data
GS = Sheets()
data = GS.get()

# Add IATA codes for each city 
for i in range(len(data['prices'])):
    item = data['prices'][i]

    if item['iataCode'] == '':
        code = FS.search_code(item['city'])
        GS.put('iataCode', code, i+2)

    FS.fly_to = item['iataCode']
    flights = FS.search_flights()
    rows = flights['data']
    min = rows[0]['price']
    for row in rows:
        if row['price'] < min:
            min = row['price']

    if min < item['lowestPrice']:
        GS.put('lowestPrice', min, i+2)
        msg = f"Flight from {FS.fly_from} to {FS.fly_to} ({item['city']}) is at ${min}."
        message = client.messages.create(
            from_='+18444267905',
            to='+12405208934',
            body= msg
            )

Client()




