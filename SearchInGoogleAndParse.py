import re
import requests
from bs4 import BeautifulSoup


response = requests.get('http://google.com/search', params={'q': 'joomshaper.com email'})
soup = BeautifulSoup(response.text, 'lxml')

# print(response.headers)
# print(response.history)
# print(response)

for tag in soup.findAll(text=re.compile('@')):
    print(tag)

