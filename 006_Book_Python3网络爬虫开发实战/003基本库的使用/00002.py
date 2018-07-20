import urllib.parse
import urllib.request

data1 = bytes(urllib.parse.urlencode({'word':'hello huyankai'}),encoding='utf-8')
response = urllib.request.urlopen('http://httpbin.org/post',data = data1)
print(response.read())