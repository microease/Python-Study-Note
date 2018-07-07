# 地址：https://ziyuan.baidu.com/linksubmit/index
# https://ziyuan.baidu.com/linksubmit/url
# 需求：自动登录，批量提交链接
# coding=utf-8
import requests

url = 'https://ziyuan.baidu.com/linksubmit/urlsubmit'
testurl = {'url': 'http://www.wzxdm.com/life/88.html'}
headers = {
    "BAIDUID=8963E61E801B97D037200D8F9353D0EB:FG=1; BIDUPSID=8963E61E801B97D037200D8F9353D0EB; PSTM=1530944516; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; __cas__st__=NLI; __cas__id__=0; FP_UID=8bfde09fc0ea15ee989f540cc1f81a55; SITEMAPSESSID=rgllaec46u54786lit7nablrp4; lastIdentity=PassUserIdentity; PSINO=6; H_PS_PSSID=1449_26260_21085_18560_20883_22075; Hm_lvt_6f6d5bc386878a651cb8c9e1b4a3379a=1530969213,1530969901; Hm_lpvt_6f6d5bc386878a651cb8c9e1b4a3379a=1530970150"}
response = requests.post(url, testurl, headers=headers)
response.encoding = 'utf-8'
print(response.text)
