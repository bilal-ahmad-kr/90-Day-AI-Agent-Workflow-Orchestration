import requests

url = "https://dummyjson.com/products"

try:
    response = requests.get(url, timeout=15)
    response.raise_for_status()

    data = response.json()

    products = data["products"]

    available_products = []

    for product in products:
        if product["stock"] > 0:
            transformed_product = {
                "name": product["title"],
                "price": product["price"],
                "stock": product["stock"]
            }

            available_products.append(transformed_product)
    print("===Available Products ===\n")
    for product in available_products:
        print(f"Name: {product['name']}")
        print(f"Price: ${product['price']}")
        print(f"Stock: {product['stock']}")
        print("-" *30)

except requests.exceptions.RequestException as e:
    print("Request failed:", e)

except (ValueError, KeyError, TypeError) as e:
    print("Error parsing JSON:", e)