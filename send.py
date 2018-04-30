import requests

headers = {}
headers['Authorization'] = 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTI1MDg2NDIwLCJqdGkiOiJkYWE4MTQ2NjBkZDQ0OGVlYjczNjQwYjUxZDM1ODRjNSIsInVzZXJfaWQiOjF9.mr5FHmDOOdtSmXY5Nux3b56s0XP7loNJ1YZUxBCNqwM'

r = requests.get('http://127.0.0.1:8000/orders', headers=headers)

print(r.text)