import requests

# API endpoint
url = "https://api.restful-api.dev/objects?id=3&id=5&id=10"

# send GET request
response = requests.get(url)

# Pasre JSON response
data = response.json()

# Print the data
print("Fetched Data from RESTful API:")
print(data)