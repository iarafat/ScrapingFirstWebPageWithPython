import requests
import webbrowser
import lxml

from bs4 import BeautifulSoup

# response = requests.get('https://google.com')
# soup = BeautifulSoup(response.text, 'lxml')
# print(soup)

with open('files/GiantPanda.html') as html_code:
    soup = BeautifulSoup(html_code, 'lxml')

# print(soup.prettify())
# print(soup.title)

# print(soup.a)
# print(soup.a.name)
# print(soup.a['href'])
# print(soup.a.attrs)

print(soup.img)
print(soup.img['src'])
print(soup.img.attrs)