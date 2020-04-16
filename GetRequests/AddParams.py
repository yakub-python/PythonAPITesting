import requests

url = "https://httpbin.org/get"
params_data = {'param1': 'xyz', 'param2': '123'}

response = requests.get(url, params=params_data)
print(response.status_code)
print(response.content)
