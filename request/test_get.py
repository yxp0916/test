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

if __name__=='__main__':
    requset_method()
