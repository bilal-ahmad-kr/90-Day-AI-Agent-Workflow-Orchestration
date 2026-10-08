# import requests

# url = "https://dummyjson.com/"

# response = requests.get(url, timeout=15)

# print(response.status_code)

# import requests

# url = "https://dummyjson.com/users"

# response = requests.get(url, timeout=15)
# response.raise_for_status()
# data = response.json()

# print(data)

import requests

url = "https://dummyjson.com/products"

try:
    response = requests.get(url, timeout=15)
    response.raise_for_status()
    data = response.json()

    for product in data["products"]:
        print(F"Name: {product['title']}")
        print(f"Price: ${product['price']}")
        print("-" * 30)
except requests.exceptions.RequestException as e:
    print("Request failed:", e)
except (ValueError, KeyError, TypeError) as e:
    print("Error parsing JSON:", e)