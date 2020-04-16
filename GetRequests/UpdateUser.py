from jsonpath import jsonpath
import requests
import json

url = "https://reqres.in/api/users/2"

# read test data
file = open(r"D:\PythonProjects\APITesting\testdata.json", "r")
test_data = file.read()
# print(test_data)

# parse test_data to json
test_data_json = json.loads(test_data)
# print(test_data_json)

# make a post request with JSON Body
response = requests.put(url, test_data_json)
print(response.status_code)
assert response.status_code == 200


print(response.text)
print(response.headers)
response_json = json.loads(response.content)
