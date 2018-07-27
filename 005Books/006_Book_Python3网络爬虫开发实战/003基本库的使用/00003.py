import requests

r = requests.get('https://github.com/favicon.ico')
f = open('favicon.ico', 'wb')
f.write(r.content)
