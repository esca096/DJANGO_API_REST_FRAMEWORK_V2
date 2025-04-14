import requests

endpoint = "http://localhost:8000/api/product/1/"

data = {
    'name':'Mangues',
    'price': 3000,
    }

response = requests.patch(endpoint, json=data)

print(response.json())
print(response.status_code)