# coding=utf-8
# 此文件用来采集美莱的文章链接
# 通过前面的几个文件，我们已经拿到了所有的最下级目录链接，此时，就需要采集所有的文章链接了，但是在这里，我发现了一个问题，就是美莱的这个目录是用的两个不同的模板，所以需要区分操作，
import requests
from bs4 import BeautifulSoup

lastList1 = ['http://www.mylikesz.com/zhengxing/banhen/',
             'http://www.mylikesz.com/zhengxing/zuichun/',
             'http://www.mylikesz.com/meifu/heiyanquan/',
             'http://www.mylikesz.com/wuchuang/suxing/',
             'http://www.mylikesz.com/wuchuang/wuchuangchuzhou/',
             'http://www.mylikesz.com/wuchuang/shoulian/',
             'http://www.mylikesz.com/wuchuang/zhushelongbi/',
             'http://www.mylikesz.com/wuchuang/shouxiaotui/',
             'http://www.mylikesz.com/wuchuang/chuyechou/',
             'http://www.mylikesz.com/zhongyi/fuzhenjianfei/',
             'http://www.mylikesz.com/zhongyi/zhongyimeirong/',
             'http://www.mylikesz.com/zhongyi/yajiankang/',
             'http://www.mylikesz.com/zhengxing/yanbu/151_1.html',
             'http://www.mylikesz.com/meifu/quban/86_1.html']

lastList2 = ['http://www.mylikesz.com/meifu/qudou/'
             'http://www.mylikesz.com/wuchuang/boniansuan/',
             'http://www.mylikesz.com/wuchuang/xd/',
             'http://www.mylikesz.com/meifu/qudou/',
             'http://www.mylikesz.com/zhengxing/xiongbu/56_1.html',
             'http://www.mylikesz.com/zhengxing/xiongbu/61_1.html',
             'http://www.mylikesz.com/zhengxing/xiongbu/150_1.html',
             'http://www.mylikesz.com/zhengxing/xiongbu/60_1.html',
             'http://www.mylikesz.com/zhengxing/xiongbu/57_1.html',
             'http://www.mylikesz.com/zhengxing/xiongbu/59_1.html',
             'http://www.mylikesz.com/zhengxing/xiongbu/335_1.html',
             'http://www.mylikesz.com/zhengxing/bibu/48_1.html',
             'http://www.mylikesz.com/zhengxing/bibu/49_1.html',
             'http://www.mylikesz.com/zhengxing/bibu/51_1.html',
             'http://www.mylikesz.com/zhengxing/bibu/53_1.html',
             'http://www.mylikesz.com/zhengxing/bibu/54_1.html',
             'http://www.mylikesz.com/zhengxing/bibu/55_1.html',
             'http://www.mylikesz.com/zhengxing/bibu/149_1.html',
             'http://www.mylikesz.com/zhengxing/yanbu/62_1.html',
             'http://www.mylikesz.com/zhengxing/yanbu/63_1.html',
             'http://www.mylikesz.com/zhengxing/yanbu/64_1.html',
             'http://www.mylikesz.com/zhengxing/yanbu/65_1.html',
             'http://www.mylikesz.com/zhengxing/yanbu/ylax/list_435_1.html',
             'http://www.mylikesz.com/zhengxing/yanbu/ybxf/list_436_1.html',
             'http://www.mylikesz.com/zhengxing/gailian/357_1.html',
             'http://www.mylikesz.com/zhengxing/gailian/mianbuzhifangtianchong/',
             'http://www.mylikesz.com/zhengxing/gailian/qujiazhidian/',
             'http://www.mylikesz.com/zhengxing/xizhi/66_1.html',
             'http://www.mylikesz.com/zhengxing/xizhi/67_1.html',
             'http://www.mylikesz.com/zhengxing/xizhi/68_1.html',
             'http://www.mylikesz.com/zhengxing/xizhi/70_1.html',
             'http://www.mylikesz.com/zhengxing/xizhi/152_1.html',
             'http://www.mylikesz.com/meifu/quban/77_1.html',
             'http://www.mylikesz.com/meifu/quban/78_1.html',
             'http://www.mylikesz.com/meifu/quban/79_1.html',
             'http://www.mylikesz.com/meifu/quban/80_1.html',
             'http://www.mylikesz.com/meifu/quban/82_1.html',
             'http://www.mylikesz.com/meifu/quban/81_1.html',
             'http://www.mylikesz.com/meifu/quban/83_1.html',
             'http://www.mylikesz.com/meifu/quban/84_1.html',
             'http://www.mylikesz.com/meifu/quban/85_1.html',
             'http://www.mylikesz.com/meifu/jinfu/93_1.html',
             'http://www.mylikesz.com/meifu/jinfu/94_1.html',
             'http://www.mylikesz.com/meifu/jinfu/95_1.html',
             'http://www.mylikesz.com/meifu/jinfu/96_1.html',
             'http://www.mylikesz.com/meifu/jinfu/97_1.html',
             'http://www.mylikesz.com/meifu/jinfu/98_1.html',
             'http://www.mylikesz.com/meifu/jinfu/99_1.html',
             'http://www.mylikesz.com/meifu/jinfu/154_1.html',
             'http://www.mylikesz.com/meifu/meibai/87_1.html',
             'http://www.mylikesz.com/meifu/meibai/88_1.html',
             'http://www.mylikesz.com/meifu/meibai/89_1.html',
             'http://www.mylikesz.com/meifu/meibai/90_1.html',
             'http://www.mylikesz.com/meifu/meibai/91_1.html',
             'http://www.mylikesz.com/meifu/meibai/153_1.html',
             'http://www.mylikesz.com/meifu/tuomao/104_1.html',
             'http://www.mylikesz.com/meifu/tuomao/105_1.html',
             'http://www.mylikesz.com/meifu/tuomao/106_1.html',
             'http://www.mylikesz.com/meifu/tuomao/107_1.html',
             'http://www.mylikesz.com/meifu/tuomao/156_1.html',
             'http://www.mylikesz.com/meifu/tuomao/108_1.html',
             'http://www.mylikesz.com/meifu/wenxiu/100_1.html',
             'http://www.mylikesz.com/meifu/wenxiu/101_1.html',
             'http://www.mylikesz.com/meifu/wenxiu/102_1.html',
             'http://www.mylikesz.com/meifu/wenxiu/103_1.html',
             'http://www.mylikesz.com/meifu/wenxiu/155_1.html',
             'http://www.mylikesz.com/meifu/wenxiu/442_1.html',
             'http://www.mylikesz.com/meifu/wenxiu/yjs/']
article = []
for i in lastList1:
    r = requests.get(i)
    r.encoding = 'utf-8'
    soup = BeautifulSoup(r.text, 'html.parser')
    listDiv = soup.find_all('div', {"class": "list"})
    for j in listDiv:
        for k in j.find_all('div', {"class": "hd"}):
            for l in k.find_all('h2'):
                for m in l.find_all('a'):
                    article.append(m['href'])
# 此时，第一类列表中的所有文章链接数据我们已经拿到了。
article2 = []
for n in lastList2:
    r1 = requests.get(n)
    r1.encoding = 'utf-8'
    soup1 = BeautifulSoup(r1.text, 'html.parser')
    listDiv1 = soup1.find_all('div', {"class": "list_page"})
    for o in listDiv1:
        for p in o.find_all('ul'):
            for q in p.find_all('li'):
                for r in q.find_all('a'):
                    article2.append(r['href'])
base = 'http://www.mylikesz.com'

for s in article2:
    article2 = [base + s if x == s else x for x in article2]
for t in article:
    article = [base + t if x == t else x for x in article]
print(sorted(article))
print(sorted(article2))
# 此时，我们已经获取到了所有的目录的第一页文章，即最新文章
