#coding=utf-8
import requests
from bs4 import BeautifulSoup
r = requests.get('http://www.mylikesz.com/')
r.encoding='utf-8'
print(r.text)
getContent = soup.find('div',class='nav').find('div',class='Con').find('div',class='nav_a')
print(getContent)