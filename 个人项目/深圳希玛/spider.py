#coding=utf-8
#网址：http://www.cmersz.com/
#测试抓取目录：http://www.cmersz.com/huangbanjibinglanmu/huangbanbingbian/list_131_18.html
import requests
def getCat():
    #定义一个获取分类页面内容的函数
    url = "http://www.cmersz.com/huangbanjibinglanmu/huangbanbingbian/list_131_18.html"
    headers = {"user-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36","Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8"}
    response = requests.get(url,headers=headers)
    if response.status_code == 200:
        return response.text
        #print(response.text)
def getArticle():


def main():
    getCat()
if __name__ == "__main__":
    main()
