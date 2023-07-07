import requests

class Sheets():

    def __init__(self):
        self.url = 'https://api.sheety.co/22931923422e01a1a3cf4724a9b9bc93/flightDeals/prices'

    def get(self):
        response = requests.get(url=self.url)
        data = response.json()
        return data
    
    def put(self, field, update, row):

        put_url = f'{self.url}/{row}'
        json_data = {'price': {
                field: update
                }}
        requests.put(url=put_url, json=json_data)
        return