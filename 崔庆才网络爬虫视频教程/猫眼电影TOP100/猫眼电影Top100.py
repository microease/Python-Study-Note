#coding=utf-8
from requests.exceptions import RequestException
#导入异常处理模块
import requests
import re
import json
from multiprocessing import Pool
#看教程时，此处并没有加headers信息，但是不加就会造成爬取失败，猫眼电影的访问限制，所以只能加这个。
headers = {"user-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36","Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8"}
def getOnePage(url):
    response = requests.get(url,headers = headers)
    #用request方法获取页面内容
    try:
        if response.status_code == 200:
            return response.text
        #返回页面内容
        else:
            return None
    except RequestException:
        return None
def parseOnePage(html):
    pattern = re.compile('<dd>.*?board-index.*?>(\d+)</i>.*?data-src="(.*?)".*?name"><a.*?>(.*?)</a>.*?star">(.*?)</p>.*?releasetime">(.*?)</p>.*?integer">(.*?)</i>.*?fraction">(.*?)</i>.*?</dd>',re.S)
#用正则表达式获取页面所需要的内容
    items = re.findall(pattern,html)
    for item in items:
        yield{
            '排名': item[0],
            '图片地址': item[1],
            '标题': item[2],
            '演员': item[3].strip()[3:],
            '上映时间': item[4].strip()[5:],
            '评分': item[5] + item[6]
        }
        #yield是python的语法糖，实现迭代器
def writeToFile(content):
    with open('result.txt','a',encoding='utf-8') as f:
        #此处必须加上编码处理，否则打印16进制
        f.write(json.dumps(content,ensure_ascii=False)+ '\n')
        f.close()
#已知总共10个页面，一个页面10个电影，offset值从0到90，递增10
def main(offset):
    url = "http://maoyan.com/board/4?offset=" + str(offset)
    #引入offset参数，从而获取10个top100页面的电影数据
    html = getOnePage(url)
    #从所有的url里面获取页面内容
    #print(html)
    for item in parseOnePage(html):
        print(item)
        #获取页面所需要的内容，打印
        writeToFile(item)
        #写入内容

if __name__ == "__main__":
    pool = Pool()
    #多进程处理
    pool.map(main,[i*10 for i in range(10)])