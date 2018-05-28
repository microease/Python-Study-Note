#coding=utf-8
import requests
reponse = requests.get("http://www.baidu.com")
print(reponse.text)
print(reponse.headers)
print(reponse.status_code)
image = requests.get("http://www.wzxdm.com/wp-content/uploads/2018/05/path.jpg")
with open("huyankai.png","wb") as f:
    f.write(image.content)
    f.close()