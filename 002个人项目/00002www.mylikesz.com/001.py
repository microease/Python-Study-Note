# coding=utf-8
# 导入requests和bf模块
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