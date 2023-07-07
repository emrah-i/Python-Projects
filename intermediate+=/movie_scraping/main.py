from bs4 import BeautifulSoup
import requests 
import re

response = requests.get(url='https://www.empireonline.com/movies/features/best-movies-2/')
tags = response.text

pattern = re.compile('^Read Empire')
soup = BeautifulSoup(tags, "html.parser")
elements = [p.text for p in soup.select('p a') if p.text.strip().startswith('Read Empire')]

item = 1

for element in elements:

    string = element.split(' ')
    print(f"{item}/100", " ".join(string[4:]))
    item += 1


