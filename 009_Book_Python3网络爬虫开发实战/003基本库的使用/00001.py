import urllib.request

response = urllib.request.urlopen('http://www.python.org')
# print(response.read())
print(response.status)
print(response.getheaders())
print(response.getheader('Server'))