# 常用Python库

## 请求库

- requests
- Selenium
- ChromDrive
- GeckoDrive
- PhantomJS
- aiohttp
- Appium

## 解析库

lxml

Beautiful Soup

pyquery

tesserocr

## 存储库

PyMySQL

PyMongo

redis-py

## 爬虫库

pyspider
Command "python setup.py egg_info" failed with error code 1 in /private/tmp/pip-install-ornagsvu/pycurl/
但是这里有一个坑：在高版本的mac系统环境变量里是找不到openssl的头文件的
因为新版本Mac的openssl版本 LibreSSL 2.2.7

pip3 uninstall pycurl# 卸载库
export PYCURL_SSL_LIBRARY=openssl
export LDFLAGS=-L/usr/local/opt/openssl/lib
export CPPFLAGS=-I/usr/local/opt/openssl/include# openssl相关头文件路径
pip3 install pycurl --compile --no-cache-dir # 重新编译安装
scrapy

## 工具

RedisDump

Charles

mitmproxy

## Web库

Flask

Tornado