# Python data types
# Customer data processor
customer_name = "Bilal Hassan"
customer_age = 23
customer_budget = 2000.0
is_premium_customer = True
country = "Pakistan"
projects_completed = 5


customer_skills = [
    "Python",
    "JavaScript",
    "React",
    "Node.js",
    "Git",
    "Docker",
    "AWS",
]

customer = {
    "name": customer_name,
    "age": customer_age,
    "budget": customer_budget,
    "premium": is_premium_customer,
    "country": country,
    "projects": projects_completed,
    "skills": customer_skills,
}

print("Customer Information")

print(f"Name: {customer['name']}")
print(f"Age: {customer['age']}")
print(f"Budget: ${customer['budget']}")
print(f"Premium Customer: {customer['premium']}")
print(f"Country: {customer['country']}")
print(f"Projects Completed: {customer['projects']}")

print("\nSkills:")
for skill in customer['skills']:
    print(f"- {skill}")

print("\nData Types")

print(type(customer_name))
print(type(customer_age))
print(type(customer_budget))
print(type(is_premium_customer))
print(type(customer_skills))
print(type(customer))