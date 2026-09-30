import json

FILE_NAME = "customers.json"


# Read customers from JSON file
def read_customers():
    with open(FILE_NAME, "r") as file:
        customers = json.load(file)

    return customers


# Display customers
def show_customers(customers):
    for customer in customers:
        print(
            f"ID: {customer['id']}, "
            f"Name: {customer['name']}, "
            f"Email: {customer['email']}, "
            f"Status: {customer['status']}"
        )


# Add new customer
def add_customer(customers, name, email):
    new_customer = {
        "id": len(customers) + 1,
        "name": name,
        "email": email,
        "status": "active"
    }

    customers.append(new_customer)

    with open(FILE_NAME, "w") as file:
        json.dump(customers, file, indent=4)

    print(f"Customer {name} added successfully!")


# Main program
customers = read_customers()

print("Current Customers:")
show_customers(customers)

print("\nAdding a new customer...")
add_customer(customers, "Aleena", "aleena@gmail.com")

print("\nUpdated Customers:")
show_customers(customers)