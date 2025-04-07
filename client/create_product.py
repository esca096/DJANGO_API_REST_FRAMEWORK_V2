import requests

endpoint = "http://localhost:8000/api/"

data = {
    'name':'Orange',
    'price': 1500,
    'description': 'Orange is a fruit',
}

response = requests.get(endpoint, json=data)

print(response.json())
print(response.status_code)