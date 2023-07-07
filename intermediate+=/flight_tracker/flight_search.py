import requests

class FlightSearch():

    def __init__(self):
        self.headers = {
            "apikey": 'pOdyFSFzZr3Jo9tyNUwpn94cQKuXBUwu'
            }
        self.fly_to = "",
        self.fly_from = "IAD"
        self.date_from = "17/07/2023"
        self.date_to = "17/08/2023"
        self.nights_in_dst_from = 7
        self.nights_in_dst_to = 28
        self.curr = 'USD'
        self.price_from = ''

    # Search throguh all fligths depending on 4 factors
    def search_flights(self):
        url=f'https://api.tequila.kiwi.com/v2/search?fly_to={self.fly_to}&fly_from={self.fly_from}&date_from={self.date_from}&date_to{self.date_to}&nights_in_dst_from{self.nights_in_dst_from}&nights_in_dst_to{self.nights_in_dst_to}&curr{self.curr}'
        response = requests.get(url=url, headers=self.headers)
        data = response.json()
        return data
    
    # Find IATA codes
    def search_code(self, city):
        url=f'https://api.tequila.kiwi.com/locations/query?term={city}&location_types=city'
        response = requests.get(url=url, headers=self.headers)
        data = response.json()
        return data['locations'][0]['code']
