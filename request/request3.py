from bs4 import  BeautifulSoup
import requests
if __name__=='__main__':
    # target='http://www.biqukan.com/1_1094/5403177.html'
    # req=requests.get(url=target)
    # print(req.text)
    target='http://www.biqukan.com/1_1094/'
    req=requests.get(url=target)
    html=req.text
    div_bf=BeautifulSoup(html,"html.parser")
    div=div_bf.find_all('div',class_='listmain')
    a_bf=BeautifulSoup(div[0],"html.parser")
    a=a_bf.find_all('a')
    for each in a:
        print(each.string,server+each.get('herf'))