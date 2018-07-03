# coding=utf-8
import requests
from bs4 import BeautifulSoup
import os
import sys
# 文章很多，此处仅仅放上五篇测试
article = ['http://www.mylikesz.com/html/78935.html', 'http://www.mylikesz.com/html/78937.html',
           'http://www.mylikesz.com/html/78952.html', 'http://www.mylikesz.com/html/78957.html',
           'http://www.mylikesz.com/html/78959.html']


def txt(name, txt):
    b = os.getcwd() + '/articles/'
    print(b)
    if not os.path.exists(b):
        os.makedirs(b)
    mktxt = b + name + '.txt'
    file = open(mktxt, 'wb+')
    file.write(txt)
    file.close()
    print('ok')


titles = []
contents = []
for i in article:
    r = requests.get(i)
    r.encoding = 'utf-8'
    soup = BeautifulSoup(r.text, 'html.parser')
    titles.append(soup.find('h1').get_text())
    contents.append(soup.find('div', {"class": "text_C"}))
    # for j in times:
    #     for k in j.find_all('span'):
    #         print(k)
    # contents.append() soup.find('div', {"class": "essay_xb_info"})
    # txt(str(titles), str(contents))
for l in titles:
    index = titles.index(l)
    txt(str(titles[index]), str(contents[index]).encode('utf-8'))

    # print(str(contents[index]))
