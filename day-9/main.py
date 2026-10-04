from customer import customers, show_customers, add_customer
from utils import get_customer_count
from email import send_email

print("=== Customer Automation App ===\n")

print("Current Customers:")
show_customers()

print(f"Total Customers: {get_customer_count(customers)}")

print("\nAdding new customer...")
add_customer("Aleena", "aleena@gmail.com")

print("\nUpdated Customers:")
show_customers()

print("Sending emails...\n")

for customer in customers:
    send_email(customer["name"], customer["email"])

print("\nAutomation Completed!")