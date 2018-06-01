import requests
import json

URL='https://api.github.com'

def bulid_url(endpoint):
    return '/'.join([URL,endpoint])

def better_output(json_str):
    return json.dumps(json.loads(json_str), indent=4)

def request_methon():
    response=requests.post(bulid_url('user/emails'),auth=('xx@msn.com','password'),json=['5xxxxx1@qq.com'])
    print(better_output(response.text))
    print(response.request.headers)
    print(response.request.body)

if __name__=='__main__':
    request_methon()