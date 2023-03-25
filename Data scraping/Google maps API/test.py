import requests

# Set up the API endpoint and parameters
url = 'https://maps.googleapis.com/maps/api/place/textsearch/json'
params = {
    'query': 'food in Bangalore',
    'key': 'YOUR_API_KEY',
}

# Retrieve the list of restaurants in Bangalore that serve pizza
response = requests.get(url, params=params)
data = response.json()

if 'results' in data:
    results = data['results']
    
    # Filter the results by category or keyword
    pizza_results = [result for result in results if 'pizza' in result['types']]
    
    # Print the name and address of each pizza restaurant
    for restaurant in pizza_results:
        print(f"Name: {restaurant['name']}")
        print(f"Address: {restaurant['formatted_address']}")
        print()
