# coding=utf-8
# 网址：http://www.mylikesz.com/
# 测试抓取目录：http://www.mylikesz.com/zhengxing/xiongbu/56_63.html
import requests
#导入requests模块
import re
#导入re模块

def getCat():
    # 定义一个获取分类页面内容的函数
    url = "http://www.mylikesz.com/zhengxing/xiongbu/56_63.html"
    headers = {"user-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36","Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.text
        #print(response.text)

def getArticle(article):
    #print(article)
    pattern = re.compile('list_page.*?href="(.*?)".*?>(.*?)</a>.*?href="(.*?)".*?>(.*?)</a>.*?href="(.*?)".*?>(.*?)</a>.*?href="(.*?)".*?>(.*?)</a>.*?href="(.*?)".*?>(.*?)</a>.*?href="(.*?)".*?>(.*?)</a>.*?href="(.*?)".*?>(.*?)</a>.*?href="(.*?)".*?>(.*?)</a>.*?href="(.*?)".*?>(.*?)</a>.*?href="(.*?)".*?>(.*?)</a>.*?href="(.*?)".*?>(.*?)</a>.*?</ul>',re.S)
    items = re.findall(pattern,article)
    print(items)
    for item in items:
        yield {
            '链接': 'http://www.mylikesz.com'+ item[0],
            '标题': item[1]
        }

def main():
    article = getCat()
    for item in getArticle(article):
        print (item)



if __name__ == "__main__":
    main()