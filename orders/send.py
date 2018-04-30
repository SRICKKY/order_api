import requests

headers = {}
headers['Authorization'] = 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTI1MDg3MTI1LCJqdGkiOiIwM2E0ZDg4ZjYwNDc0OGQ2OTBiY2I0MWM1MjRkYjM5YiIsInVzZXJfaWQiOjF9.nAgKjseknRqqIj6Lxtdid1k72NdSNiXKQUQLNOYNahw'

r = requests.get('http://127.0.0.1:8000/orders/', headers=headers)

print(r.text)