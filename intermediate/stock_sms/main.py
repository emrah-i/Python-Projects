import requests
from datetime import datetime
from twilio.rest import Client

stock = "TSLA"
cmpny = "Tesla Inc"
time_series = 'TIME_SERIES_DAILY_ADJUSTED'
stock_api_key = 'DLRC08HBOHI6IKV3'

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
'''response = requests.get(f'https://www.alphavantage.co/query?function={time_series}&symbol={stock}&interval=5min&apikey={stock_api_key}')
raw = response.json()
data = raw['Time Series (Daily)']
all_keys = list(data.keys())

for i in range(len(data)):
    open = float(data[all_keys[i]]['1. open'])
    close = float(data[all_keys[i+1]]['4. close'])

    change = round(((close - open) / close * 100), 2)

    if change > 0:
        change = f"🔺 {abs(change)}"
    elif change < 0:
        change = f"🔻 {abs(change)}"
    else:
        change = "~0"

    print(f"TSLA shares {change}% from {all_keys[i]} to {all_keys[i+1]}")   

    if i == 7:
        exit()'''

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 
news_api_key = 'b1ee1a9d861a41999b417954e6e2e0de'

resp = requests.get(url=f"https://newsapi.org/v2/top-headlines?q={cmpny}&pageSize=3&page=1&country=us&apiKey=")
data = resp.json()
print(data)

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

