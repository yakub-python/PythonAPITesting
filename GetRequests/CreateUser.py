from jsonpath import jsonpath
import requests
import json

url = "https://reqres.in/api/users"

# read testdata
file = open(r"D:\PythonProjects\APITesting\testdata.json", "r")
test_data = file.read()
# print(test_data)

# parse test_data to json
test_data_json = json.loads(test_data)
# print(test_data_json)

# make a post request with JSON Body
response = requests.post(url, test_data_json)
print(response)
assert response.status_code == 201
print(response)
print(response.content)
response_json = json.loads(response.content)
print(jsonpath(response_json,"id")[0])