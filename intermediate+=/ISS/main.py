import requests
import smtplib
import time
from datetime import datetime

my_email = 'emrakhibragimov5@gmail.com'
password = 'rgbzaerhvevmdoou'
my_lat = 39.639580,
my_long = -77.718941

def overhead():
    response = requests.get(url='http://api.open-notify.org/iss-now.json')
    response.raise_for_status()
    data = response.json()['iss_position']

    long = data['longitude']
    lat = data['latitude']

    if my_lat - 5 <= lat <= my_lat + 5 and my_long - 5 <= long <= my_long + 5:
        return True

def night():
    response = requests.get(url=f"https://api.sunrise-sunset.org/json?lat={my_lat}&lng={my_long}&formatted=0")
    response.raise_for_status()
    data = response.json()
    sunrise = data['results']['sunrise']
    sunset = data['results']['sunset']

    rise = datetime.fromisoformat(sunrise)
    set = datetime.fromisoformat(sunset)
    now = datetime.now()

    if rise < now  or now > set:
        return True

while True:
    if overhead() and night():
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(my_email, password)
        connection.sendmail(from_addr=my_email, to_addrs=my_email, msg='Subject: Look Up!!\n\nThe ISS is overhead!')
        connection.close()
    
    time.sleep(60)