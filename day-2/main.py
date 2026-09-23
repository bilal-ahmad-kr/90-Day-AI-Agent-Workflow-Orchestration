customers = [
    {
        "name" : "Bilal Hassan",
        "age" : 23,
        "budget": 3000,
        "email": "bilalhassan@gmail.com",
        "country": "Pakistan",
        "projects": 5,
        "skills": ["Python", "JavaScript", "SQL"],
        "interests": ["AI", "Web Development", "Data Science"]
    },
    {
        "name" : "Aleena Zahra",
        "age" : 21,
        "budget": 2500,
        "email": "aleenazahra@gmail.com",
        "country": "Pakistan",
        "projects": 3,
        "skills": ["Python", "ML", "AI"],
        "interests": ["Machine Learning", "AI", "Data Analysis"]
    },
    {
        "name" : "Ahmed Khan",
        "age" : 25,
        "budget": 4000,
        "email": "ahmad@gmail.com",
        "country": "Pakistan",
        "projects": 7,
        "skills": ["Python", "Django", "Flask"],
        "interests": ["Web Development", "API Development", "DevOps"]
    }
]

for index, customer in enumerate(customers):
    print(f"Customer {index} information:")
    print(f"Name: {customer['name']}")
    print(f"Age: {customer['age']}")
    print(f"Budget: {customer['budget']}")
    print(f"Email: {customer['email']}")
    print(f"Country: {customer['country']}")
    print(f"Projects: {customer['projects']}")
    print(f"Skills: {', '.join(customer['skills'])}")
    print(f"Interests: {', '.join(customer['interests'])}")

    print("\nData Types:")
    print(f"List of Customers Type: {type(customers)}")
    print(f"Individual Customer Type: {type(customers[0])}")