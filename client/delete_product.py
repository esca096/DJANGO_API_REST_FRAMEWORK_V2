import requests

endpoint = "http://localhost:8000/api/product/9/"

response = requests.delete(endpoint)


print(f"Status Code: {response.status_code}")

# Vérifie si le serveur a renvoyé du JSON
try:
    data = response.json()
    print("Response JSON:", data)
except requests.exceptions.JSONDecodeError:
    print("No JSON response received.")
    print("Raw response text:", response.text)