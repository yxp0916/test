import urllib.request

re=urllib.request.urlopen('http://www.baidu.com',data=None,timeout=10)
print(re.info())