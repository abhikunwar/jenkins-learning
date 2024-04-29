import requests
import json
def getPetdata(url,headers=None,params=None):
    response = requests.get(url,verify=False,headers=headers,params=params)
    print("Request url:",url)
    print("request header:",response.request.headers)
    print("response header:",response.headers)
    return response

def postPetdata(url,body):
    headers = {'Content-Type':'application/json'}
    print("reqUrl:",url)
    print("reqBody:",json.dumps(body))
    response = requests.post(url,verify=False,json = body,headers = headers)
    return response


