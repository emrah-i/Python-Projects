import requests
from datetime import datetime, timedelta
from twilio.rest import Client

stock = "TSLA"
cmpny = "Tesla"
news_api_key = 'b1ee1a9d861a41999b417954e6e2e0de'
time_series = 'TIME_SERIES_DAILY_ADJUSTED'
stock_api_key = 'DLRC08HBOHI6IKV3'
account_sid = 'ACe623bfcec1d9eb7873721f4b182f20fa'
auth_token = '64c7526fb299e71c72570776258b77e8'
client = Client(account_sid, auth_token)

response = requests.get(f'https://www.alphavantage.co/query?function={time_series}&symbol={stock}&apikey={stock_api_key}')
raw = response.json()
data = raw['Time Series (Daily)']
all_keys = list(data.keys())

open = float(data[all_keys[0]]['1. open'])
close = float(data[all_keys[1]]['4. close'])

change = round(((close - open) / close * 100), 2)
abs_change = abs(change) 

if change > 0:
    text_change = f"🔺 {abs_change}"
elif change < 0:
    text_change = f"🔻 {abs_change}"
else:
    text_change = "~0"

if abs_change >= 5:
    resp = requests.get(url=f"https://newsapi.org/v2/everything?q={cmpny}&sortby=popularity&from={all_keys[1]}&to={all_keys[0]}&language=en&pageSize=3&page=1&apiKey={news_api_key}")
    resp.raise_for_status()
    data = resp.json()

    for article in data['articles']:
        msg = f"Stock: {stock}\nChange: {text_change}\nPublisher: {article['source']['name']}\nHeadline: {article['title']}\nContent: {article['description']}\nPublished:, {datetime.fromisoformat(article['publishedAt'])}"
        message = client.messages.create(
            from_='+18444267905',
            to='+12405208934',
            body= msg
            )

else: 
    msg = f"Stock: {stock}\nChange: {text_change}"
    message = client.messages.create(
        from_='+18444267905',
        to='+12405208934',
        body= msg
        )

