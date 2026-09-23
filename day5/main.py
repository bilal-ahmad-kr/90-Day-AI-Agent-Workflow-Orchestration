# Customer manager
customers = [
    { "name": "Bilal", "age": 23, "budget": 3000},
    { "name": "Ali", "age": 12, "budget": 2000},
    { "name": "Hassan", "age": 14, "budget": 1000},
]

search_name = input("Enter customer name:")

customer_found = False

for customer in customers:
    if customer["name"].lower() == search_name.lower():
        customer_found = True
        print(f"Customer {customer['name']} found!")
        print(f"Age: {customer['age']}")
        print(f"Budget: {customer['budget']}")
        break

if not customer_found:
    print(f"Customer {search_name} not found")