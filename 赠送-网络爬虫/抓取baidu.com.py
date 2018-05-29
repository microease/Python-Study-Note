#coding=utf-8
import requests
#抓取网页
reponse = requests.get("http://www.baidu.com")
print(reponse.text)
print(reponse.headers)
print(reponse.status_code)
#保存图片
image = requests.get("http://www.wzxdm.com/wp-content/uploads/2018/05/path.jpg")
with open("huyankai.png","wb") as f:
    f.write(image.content)
    f.close() 