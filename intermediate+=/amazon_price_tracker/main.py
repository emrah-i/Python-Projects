from bs4 import BeautifulSoup
import smtplib
import requests

my_email = 'emrakhibragimov5@gmail.com'
password = 'rgbzaerhvevmdoou'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    'Accept-Language': 'en-US,en;q=0.8'
}

response = requests.get(url='https://www.amazon.com/dp/B08N5LNQCX/ref=fs_a_mbt2_us1', headers=headers)
data = response.text

soup = BeautifulSoup(data, 'html.parser')
price = soup.select('div[class="a-section a-spacing-none aok-align-center"] span[class="a-price-whole"]')[0].text
price = price[:-1]

with open('intermediate+=/amazon_price_tracker/price.txt') as file:
    curr = file.read()

if int(price) < int(curr):
    with open('intermediate+=/amazon_price_tracker/price.txt', 'w') as file:
        file.write(price)

    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(my_email, password)
    connection.sendmail(from_addr=my_email, to_addrs=my_email, msg=f'Subject: Macbook Price\n\nThe price of the macbook is now ${price}. This is below your asking price.')
    connection.close()
    