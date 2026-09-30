customers = [
    { "name": "Bilal", "email": "bilal@gmail.com" },
    { "name": "Hamza", "email": "hamza@gmail.com" },
    { "name": "Hassan", },
    { "name": "Aleena", "email": "aleena@gmail.com" },
    { "name": "Raza", "email": "raza@gmail.com" }
]

def process_customer(customer):
    try:
        name = customer["name"]
        email = customer["email"]

        print(f"Processing {name}...")
        print(f"Sending email to {email}...")
        print("Customer processed successfully!\n")
    except KeyError as error:
        print(f"Error: Missing field {error}")
        print("Skipping this customer... \n")

print("Starting customer processing... \n")

for customer in customers:
    process_customer(customer)

print("All customers processed!")