import httplib2
import webbrowser
from pprint import pprint

bin_url = 'https://httpbin.org/'

# webbrowser.open(bin_url)

http = httplib2.Http()
response, data = http.request(bin_url+'get', method='GET')
pprint(response)
pprint(data)
print(type(data))