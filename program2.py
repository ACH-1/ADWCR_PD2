import requests

response = requests.get("http://127.0.0.1:5000/")
print("Status:", response.status_code)
print("Odpowiedź:", response.json())