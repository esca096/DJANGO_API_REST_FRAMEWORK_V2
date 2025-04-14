import requests

endpoint = "http://localhost:8000/api/product/"

data = {
    'name':'Pomme',
    'price': 1700,
    'description': 'pomme is a fruit',
    'email': 'pomme@gmail.com',
    }

response = requests.post(endpoint, json=data)

print(response.json())
print(response.status_code)