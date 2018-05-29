#coding=utf-8
# #猫眼电影TOP100：http://maoyan.com/board/4
#第二页：http://maoyan.com/board/4?offset=10
#第三页：http://maoyan.com/board/4?offset=20
import requests
def getOnePage(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        return None