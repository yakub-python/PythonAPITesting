import requests

url = "https://httpbin.org/get"
header_data = {'t1': 'header1', 't2': 'header2'}
response = requests.get(url, headers=header_data)
print(response.content)
