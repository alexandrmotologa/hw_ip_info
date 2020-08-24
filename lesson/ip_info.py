import json
import requests
query = input("Enter an IP or DOMAIN name: ")
endpoint = f"http://ip-api.com/json/{query}"

response = requests.get(endpoint)
data = json.loads(response.text)

country = data['country']
city = data['city']

print(f"The domain is located in {country} / {city}")
