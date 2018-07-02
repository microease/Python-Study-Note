# coding=utf-8
# 导入requests和bf模块
import requests
from bs4 import BeautifulSoup

secList = ['http://www.mylikesz.com/zhengxing/xiongbu/', 'http://www.mylikesz.com/zhengxing/bibu/',
           'http://www.mylikesz.com/zhengxing/yanbu/', 'http://www.mylikesz.com/zhengxing/gailian/',
           'http://www.mylikesz.com/zhengxing/xizhi/', 'http://www.mylikesz.com/meifu/quban/',
           'http://www.mylikesz.com/meifu/jinfu/', 'http://www.mylikesz.com/meifu/meibai/',
           'http://www.mylikesz.com/meifu/tuomao/',
           'http://www.mylikesz.com/meifu/wenxiu/', ]
lastList2 = []
for url in secList:
    r = requests.get(url)
    r.encoding = 'utf-8'
    soup = BeautifulSoup(r.text, 'html.parser')
    for i in soup.find_all('div', id='warp_Content'):
        for j in i.find('div', {"class": "px_C"}):
            for k in j.find('div', {"class": "px_l"}):
                for l in k.find('div', {"class": "mod1"}):
                    for m in l.find('div', {"class": "l"}):
                        for n in m.find('div', {"class": "bd"}):
                            for o in n.find_all('ul', id='page_xb_mod1_tab'):
                                print(o)


# a
# li
# <ul class="page_xb_mod1_tab">
# <div class="bd">
# <div class="l">
# <div class="mod1 mod">
# <div class="px_l">
# <div class="px_C">
# <div class="px_warp" id="warp_Content">
