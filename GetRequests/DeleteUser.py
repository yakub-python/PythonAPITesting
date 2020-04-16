import requests

url = "https://reqres.in/api/users?page=2"

# 204 Delete response code
response = requests.delete(url)
print(response)