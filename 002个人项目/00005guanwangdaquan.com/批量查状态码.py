# coding=utf-8
import urllib, time
from io import StringIO
import pycurl
import certifi
def get_http_status(url):
    html = StringIO()
    c = pycurl.Curl()
    myurl = url
    c.setopt(pycurl.CAINFO, certifi.where())
    c.setopt(pycurl.URL, myurl)
    c.setopt(pycurl.WRITEFUNCTION, html.write)
    c.setopt(pycurl.FOLLOWLOCATION, 1)
    c.setopt(pycurl.MAXREDIRS, 5)
    c.setopt(pycurl.CONNECTTIMEOUT, 60)
    c.setopt(pycurl.TIMEOUT, 300)
    c.setopt(c.HEADER, True)
    c.setopt(pycurl.USERAGENT, "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322)")
    ret = c.perform()
    ret = html.getvalue()
    if "200" in ret:
        print(url, c.getinfo(c.HTTP_CODE))
        return 1
    elif "404" in ret:
        print
        url, c.getinfo(c.HTTP_CODE)
        f = open('text.txt', 'a')
        f.write(url + '\n')
        f.close()
        return 0


if __name__ == "__main__":
    urls = open('text.txt', 'r').readlines()
    oknum = 0
    lostnum = 0
    for url in urls:
        if get_http_status(url.strip()):
            oknum += 1
        else:
            lostnum += 1