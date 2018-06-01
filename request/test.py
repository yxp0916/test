# import urllib.request
# webPage=urllib.request.urlopen("http://www.baidu.com",data=None,timeout=10)
# data=webPage.read()
# data=data.decode('UTF-8')
# print(data)
# print(type(webPage))
# print(webPage.geturl())
# print(webPage.info())
# print(webPage.getcode())

import requests
response=requests.get("http://www.baidu.com",data=None,timeout=10)
print(response.headers)