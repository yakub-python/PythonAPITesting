import requests
import json
from jsonpath import jsonpath

# uri
uri = "https://reqres.in/api/users?page=2"

# getting response
response = requests.get(uri)

# # print response -  prints 200
# print(response)
#
# # print response content
# print(response.content)
#
# # print response headers
# print(response.headers)
# print(response.headers.get("Date"))
# print(response.headers.get("Server"))

# load response into string
json_response = json.loads(response.content)
# print(json_response)
# print(json_response["data"][0])
# print(json_response["data"])

# using json path to print results, it returns list
jsonpath_response = jsonpath(json_response,'total_pages')
# print(jsonpath_response)

# print all the first names
for i in range(0,3):
    jsonpath_response = jsonpath(json_response, "data["+str(i)+"].first_name")
    print(jsonpath_response)