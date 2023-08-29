import requests

# URL for the JSONPlaceholder API
BASE_URL = 'https://jsonplaceholder.typicode.com'

# GET request to retrieve user data
user_id = 1
final_url = BASE_URL + "/users/" + str(user_id)
user_response = requests.get(final_url)
user_data = user_response.json()

if user_response.status_code == 200:
    print("User Data:")
    print("Name:", user_data['name'])
    print("Email:", user_data['email'])
    print("City:", user_data['address']['city'])
else:
    print("Failed to retrieve user data.")

