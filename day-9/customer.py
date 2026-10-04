customers = [
    { "name": "Bilal", "email": "bilal@gmail.com" },
    { "name": "Hamza", "email": "hamza@gmail.com" },
    { "name": "Hassan", "email": "hassan@gmail.com" },
]

def show_customers():
    for customer in customers:
        print(f"Name: {customer['name']}")
        print(f"Email: {customer['email']}")
        print()

def add_customer(name, email):
    new_customer = {
        "name": name,
        "email": email,
    }

    customers.append(new_customer)
    print(f"{name} added successfully!")