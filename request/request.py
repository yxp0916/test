import requests
from bs4 import  BeautifulSoup
if __name__=='__main__':
    # target='http://www.biqukan.com/1_1094/5403177.html'
    # req=requests.get(url=target)
    # print(req.text)
    target='http://www.biqukan.com/1_1094/5403177.html'
    req=requests.get(url=target)
    html=req.text
    bf=BeautifulSoup(html,"html.parser")
    texts=bf.find_all('div',id='content')
    # print(texts)
    print(texts[0].text.replace('\xa0'*8,'\n\n'))