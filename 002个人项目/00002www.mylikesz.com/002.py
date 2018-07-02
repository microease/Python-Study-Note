# coding=utf-8
# 此文件用来采集美莱所有的最下级目录链接
# 导入requests和bf模块
import requests
from bs4 import BeautifulSoup

secList = ['http://www.mylikesz.com/zhengxing/xiongbu/',
           'http://www.mylikesz.com/zhengxing/bibu/',
           'http://www.mylikesz.com/zhengxing/yanbu/',
           'http://www.mylikesz.com/zhengxing/gailian/',
           'http://www.mylikesz.com/zhengxing/xizhi/',
           'http://www.mylikesz.com/meifu/quban/',
           'http://www.mylikesz.com/meifu/jinfu/',
           'http://www.mylikesz.com/meifu/meibai/',
           'http://www.mylikesz.com/meifu/tuomao/',
           'http://www.mylikesz.com/meifu/wenxiu/', ]
# a
# li
# <ul class="page_xb_mod1_tab">
# <div class="bd">
# <div class="l">
# <div class="mod1 mod">
# <div class="px_l">
# <div class="px_C">
# <div class="px_warp" id="warp_Content">

lastList2 = []
for url in secList:
    r = requests.get(url)
    r.encoding = 'utf-8'
    soup = BeautifulSoup(r.text, 'html.parser')
    ul = soup.find_all('ul', {"class": "page_xb_mod1_tab"})
    for i in ul:
        for l in i.find_all('a'):
            lastList2.append(l['href'])
base = 'http://www.mylikesz.com'

for m in lastList2:
    # 遍历列表，在链接前加域名
    lastList2 = [base + m if x == m else x for x in lastList2]
print(lastList2)
# 此时，我们已经获取到了所有的最下级目录的链接
# 返回信息如下：['http://www.mylikesz.com/zhengxing/xiongbu/', 'http://www.mylikesz.com/zhengxing/bibu/', 'http://www.mylikesz.com/zhengxing/yanbu/', 'http://www.mylikesz.com/zhengxing/gailian/', 'http://www.mylikesz.com/zhengxing/xizhi/', 'http://www.mylikesz.com/zhengxing/banhen/', 'http://www.mylikesz.com/zhengxing/zuichun/', 'http://www.mylikesz.com/meifu/quban/', 'http://www.mylikesz.com/meifu/jinfu/', 'http://www.mylikesz.com/meifu/qudou/', 'http://www.mylikesz.com/zhongyi/', 'http://www.mylikesz.com/meifu/meibai/', 'http://www.mylikesz.com/meifu/tuomao/', 'http://www.mylikesz.com/meifu/wenxiu/', 'http://www.mylikesz.com/meifu/heiyanquan/', 'http://www.mylikesz.com/wuchuang/suxing/', 'http://www.mylikesz.com/wuchuang/wuchuangchuzhou/', 'http://www.mylikesz.com/wuchuang/boniansuan/', 'http://www.mylikesz.com/wuchuang/shoulian/', 'http://www.mylikesz.com/wuchuang/zhushelongbi/', 'http://www.mylikesz.com/wuchuang/xd/', 'http://www.mylikesz.com/wuchuang/shouxiaotui/', 'http://www.mylikesz.com/wuchuang/chuyechou/', 'http://www.mylikesz.com/huolichike/zhongzhiya/360_1.html', 'http://www.mylikesz.comhttp://www.mylikesz.com/baidu/sszy/', 'http://www.mylikesz.com/huolichike/yachimeibai/', 'http://www.mylikesz.com/huolichike/kaociya/', 'http://www.mylikesz.com/huolichike/jiaozheng/', 'http://www.mylikesz.com/huolichike/zhiliao/', 'http://www.mylikesz.com/zhongyi/fuzhenjianfei/', 'http://www.mylikesz.com/zhongyi/zhongyimeirong/', 'http://www.mylikesz.com/meifu/qudou/', 'http://www.mylikesz.com/zhongyi/yajiankang/']
