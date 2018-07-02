import requests


url = 'https://httpbin.org/post'
data = dict(title='Learn Python Programming')


resp = requests.post(url, data=data)
print('Response for POST')
print(resp.json())
