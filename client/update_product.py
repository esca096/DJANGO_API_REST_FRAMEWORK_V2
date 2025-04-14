import requests

endpoint = "http://localhost:8000/api/product/1/"

data = {
    'name':'Mangues from africa',
    'price': 2500,
    'description': 'mangues is a fruit',
    'email': 'mangues@gmail.com',
    }

response = requests.put(endpoint, json=data)

print(response.json())
print(response.status_code)