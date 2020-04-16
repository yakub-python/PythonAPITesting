import json

import requests
from jsonpath import jsonpath
from requests.auth import HTTPBasicAuth

#
# def test_git_hub():
#     request_uri = 'https://www.google.com/users'
#     response = requests.get('https://api.github.com/user', auth=HTTPBasicAuth('yakub-pasha', 'Yasmin@789'))
#     print(response)
#
#
# def test_oAuth_verification():
#     token_url = "http://thetestingworldapi.com/Token"
#     data = {"grant_type": "password", "username": "admin", "password": "password"}
#     response = json.loads(requests.post(token_url, data))
#     token = jsonpath(response, 'access_token')[0]
#
#     auth = {"authoriztion": "Bearer" + token}
#     application_url = "http://thetestingworldapi.com/api/stDetails/1104"
#     response = requests.get(application_url, headers=auth)
#     print(response)



