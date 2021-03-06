#coding=utf-8
from urllib.parse import urlencode
import requests
from requests.exceptions import  RequestException
def getPage(offset,keyword):
    data = {
        'offset': offset,
        'format': 'json',
        'keyword': keyword,
        'autoload': 'true',
        'count': '20',
        'cur_tab': 1,
        'from': 'search_tab'
    }
    url = 'https://www.toutiao.com/search_content/?' + urlencode(data)
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        else:
            return None
    except RequestException:
        print("请求索引页错误")
        return None
def main():
    html = getPage(0,'街拍')
    print(html)

if __name__ == "__main__":
    main()