# coding=utf-8
import requests
from bs4 import BeautifulSoup

# 文章很多，此处仅仅放上五篇测试
article = ['http://www.mylikesz.com/html/78935.html', 'http://www.mylikesz.com/html/78937.html',
           'http://www.mylikesz.com/html/78952.html', 'http://www.mylikesz.com/html/78957.html',
           'http://www.mylikesz.com/html/78959.html']
for i in article:
    r = requests.get(i)
    r.encoding = 'utf-8'
    soup = BeautifulSoup(r.text, 'html.parser')
    titles = soup.find_all('h1')
    times = soup.find_all('div',{"class": "essay_xb_info"})
    for j in times:
        for k in j.find_all('span'):
            print(type(k))