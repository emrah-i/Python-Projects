import requests
from datetime import datetime

# Create a user
'''
url = 'https://pixe.la/v1/users'

params = {
    'token': 'j12jhl3blhb34j23n4s4rfq1',
    'username': 'emrah26',
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes'
}

response = requests.post(url=url, json=params)'''

# Creating a graph
'''
url = f'https://pixe.la/v1/users/{username}/graphs'

graph_config = {
    'id': 'graph1',
    'name': 'Workout Graph',
    'unit': 'times',
    'type': 'int',
    'color': 'momiji'
}

response = requests.post(url=url, json=graph_config, headers=headers)
print(response.text)'''

'''url = f'https://pixe.la/v1/users/{username}/graphs/{graph}'

response = requests.post(url=url, headers=headers, json=config)
print(response.text)'''

now = datetime.now()
today = datetime.strftime(now, '%Y%m%d')

username = 'emrah26'
token = 'j12jhl3blhb34j23n4s4rfq1'
graph = 'graph1'

headers = {
    'X-USER-TOKEN': token
}

config = {
    'quantity': '4'
}

url = f'https://pixe.la/v1/users/{username}/graphs/{graph}/{today}'

response = requests.put(url=url, headers=headers, json=config)
print(response.text)