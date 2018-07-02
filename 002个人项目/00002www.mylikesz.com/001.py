# coding=utf-8
# 导入requests和bf模块
# 此文件用来采集美莱所有的目录链接
import requests
from bs4 import BeautifulSoup

# 指定采集链接
url = 'http://www.mylikesz.com'
# 开始采集
r = requests.get(url)
# 转换采集下来的内容编码格式
r.encoding = 'utf-8'
# 用bf4解析内容
soup = BeautifulSoup(r.text, 'html.parser')
# 只需要id为nav下面的class为Con的内容
con =  soup.find('div', id='nav').find('div', {"class": "Con"})
# 创建一个空列表，这个列表用来保存所有的H2标签
# allH2 = []
# # 循环遍历所有的class为nav_a的div
# for i in con.find_all('div', {"class": "nav_a"}):
#     # 循环遍历所有的h2下面的a标签
#     for j in i.find('h2').find_all('a'):
#         # 保存链接到allH2
#         allH2.append(j['href'])
# for l in allH2:
#     # 遍历列表，在链接前加域名
#     allH2 = [url + l if x == l else x for x in allH2]
# print(allH2)
# 创建一个空列表，这个列表用来保存所有的a标签
allA = []
# 循环遍历所有的class为nav_a的div
for i in con.find_all('div', {"class": "nav_a"}):
    # 循环遍历所有的h2下面的ul标签
    for j in i.find_all('ul'):
        # 循环遍历所有的h2下面的li标签
        for k in j.find_all('li'):
            # 循环遍历所有的h2下面的a标签
            for l in k.find_all('a'):
                # 保存链接到allA
                allA.append(l['href'])
for m in allA:
    # 遍历列表，在链接前加域名
    allA = [url + m if x == m else x for x in allA]
print(allA)
# 此时，我们已经获取到了所有的目录链接
# 返回信息如下：['http://www.mylikesz.com/zhengxing/xiongbu/', 'http://www.mylikesz.com/zhengxing/bibu/', 'http://www.mylikesz.com/zhengxing/yanbu/', 'http://www.mylikesz.com/zhengxing/gailian/', 'http://www.mylikesz.com/zhengxing/xizhi/', 'http://www.mylikesz.com/zhengxing/banhen/', 'http://www.mylikesz.com/zhengxing/zuichun/', 'http://www.mylikesz.com/meifu/quban/', 'http://www.mylikesz.com/meifu/jinfu/', 'http://www.mylikesz.com/meifu/qudou/', 'http://www.mylikesz.com/zhongyi/', 'http://www.mylikesz.com/meifu/meibai/', 'http://www.mylikesz.com/meifu/tuomao/', 'http://www.mylikesz.com/meifu/wenxiu/', 'http://www.mylikesz.com/meifu/heiyanquan/', 'http://www.mylikesz.com/wuchuang/suxing/', 'http://www.mylikesz.com/wuchuang/wuchuangchuzhou/', 'http://www.mylikesz.com/wuchuang/boniansuan/', 'http://www.mylikesz.com/wuchuang/shoulian/', 'http://www.mylikesz.com/wuchuang/zhushelongbi/', 'http://www.mylikesz.com/wuchuang/xd/', 'http://www.mylikesz.com/wuchuang/shouxiaotui/', 'http://www.mylikesz.com/wuchuang/chuyechou/', 'http://www.mylikesz.com/huolichike/zhongzhiya/360_1.html', 'http://www.mylikesz.comhttp://www.mylikesz.com/baidu/sszy/', 'http://www.mylikesz.com/huolichike/yachimeibai/', 'http://www.mylikesz.com/huolichike/kaociya/', 'http://www.mylikesz.com/huolichike/jiaozheng/', 'http://www.mylikesz.com/huolichike/zhiliao/', 'http://www.mylikesz.com/zhongyi/fuzhenjianfei/', 'http://www.mylikesz.com/zhongyi/zhongyimeirong/', 'http://www.mylikesz.com/meifu/qudou/', 'http://www.mylikesz.com/zhongyi/yajiankang/']