import requests
import json
import webbrowser

from pprint import pprint

# response = requests.get('http://jsonplaceholder.typicode.com/todos/1')
# data = json.loads(response.text)
# pprint(data)

wiki_search_url = 'https://en.wikipedia.org/wiki/Special:Search'
query_params = {'search': 'requests'}

response = requests.get(url=wiki_search_url, params=query_params)
# pprint(response.text)
# print(response.url)


def print_response_history(response):
    if response.history:
        print('History')
        for r in response.history:
            print(r.status_code, r.url)

        print('Finally')
        print(response.status_code, response.url)

    else:
        print('Request was not redirected')


print_response_history(response)



