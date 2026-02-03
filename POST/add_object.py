# Import the requests library for making HTTP requests
import requests

# Define the API endpoint URL for creating new objects
url = "https://api.restful-api.dev/objects"

# Define the request payload with object details to be sent to the API
payLoad = {
   "name": "mango Phone",  # Product name
   "data": {
      "year": 2069,  # Year of release
      "price": 5233.99,  # Product price
      "CPU model": "Intel Core i9",  # CPU specifications
      "Hard disk size": "1 TB"  # Storage capacity
   }
}

# Set HTTP headers for the request
headers = {
    "Content-Type" : "application/json"  # Specify JSON content type
}

# Send a POST request to the API with the payload and headers
response = requests.post(url, headers = headers, json = payLoad)

# Check if the request was successful (status code 200 or 201)
if response.status_code == 200 or response.status_code == 201:
    print("Object added successfully:")
    print("Response Data:")
    print(response.json())  # Display the response data in JSON format
else:
    # If request failed, display error information
    print(f"Failed to add object. Status code: {response.status_code}")
    print(response.text)  # Display the error message