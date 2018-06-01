import requests
import json

URL='https://api.github.com'

def bulid_url(endpoint):
    return '/'.join([URL,endpoint])

def better_output(json_str):
    return json.dumps(json.loads(json_str), indent=4)

def requset_method():
    response=requests.get(bulid_url('users/Anthonyliu86'))
    print(better_output(response.text))

def params_method():
    response=requests.get(bulid_url('users'),params={'since':11})
    print(better_output(response.text))
    print(response.headers)
    print(response.url)

def json_methon():
    # response=requests.patch(bulid_url('user'),auth=('your_account','your_password'),json={'email':'abc@msn.com','name':'Anthony_tester'})
    respone = requests.patch(bulid_url('user'),auth=('your_account','you_password'),json={'email':'abc@msn.com','name':'Anthony_tester'})
    print(better_output(respone.text))
    print(respone.headers)
    print(respone.url)

if __name__=='__main__':
    json_methon()