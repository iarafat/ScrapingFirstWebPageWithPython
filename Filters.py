import re
from bs4 import BeautifulSoup

with open('files/TomJerry_Story.html') as html_code:
    soup = BeautifulSoup(html_code, 'lxml')

# print(soup.prettify())

# print(soup.p)

# print(soup.find('p'))
# print(soup.findAll('p'))
# print(soup.findAll(src='TomAndJerry.jpg'))
# print(soup.find(re.compile('^a')))

# for tag in soup.findAll(re.compile('^a')):
#     print(tag)

# print(soup.find('a', attrs={'class': re.compile('^cre')}))
#
# for tag in soup.findAll('a', attrs={'class': re.compile('^cre')}):
#     print(tag)

# for tag in soup.findAll('a', attrs={'class': re.compile('c')}):
#     print(tag)

# for tag in soup.findAll(id=re.compile('i')):
#     print(tag)


# print(soup.find(text=re.compile('@')))

# for tag in soup.findAll(text=re.compile('@')):
#     print(tag)




