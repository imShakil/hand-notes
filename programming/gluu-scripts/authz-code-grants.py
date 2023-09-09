__author__ = "Mobarak Hosen Shakil"


from io import RawIOBase
from os import access
import requests
import json
import subprocess
import sys

authorize_url = "https://test43u20.gluu.org/authorize"
token_url = "https://test43u20.gluu.org/token"

callback_url = "https://google.com/success"

test_api_url = __builtins__
client_id = __builtins__
client_secret = __builtins__

authorization_redirect_url = authorize_url + '?reponse_type=code&client_id='+client_id+'&redirect_uri='+ callback_url+'&scope=openid'

print("Go to the following url on the browser and enter the code from the returned url")
authorization_code = input('code: ')
data = {
    'grant_type': 'authorization_code',
    'code': authorization_code,
    'redirect_uri': callback_url
}

print('...')
access_token_response = requests.post(token_url, data=data, verify=False, allow_redirects=True, auth=(client_id, client_secret))
print(access_token_response.headers)
print('body: '+ access_token_response.text)

tokens = json.loads(access_token_response.text)
access_token = tokens['access_token']
print("access_token: " + access_token)


api_call_header = {
    'Authorization': 'Bearer' + access_token
}

api_call_response = requests.get(test_api_url, headers=api_call_header, verify=False)
print(api_call_response.text)
