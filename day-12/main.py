data = {
    "customers":[
        {
            "first_name": "bilal",
            "email": "bilal56@gmail.com",
            "status": "active"
        },
        {
            "first_name": "ali",
            "email": "ali123@gmail.com",
            "status": "inactive"
        },
        {
            "first_name": "ahmad",
            "email": "ahmad32@gmail.com",
            "status": "active"
        }
    ]
}

active_customers = []

for customers in data["customers"]:
    if customers["status"] == "active":
        active_customers.append({
            "first_name": customers["first_name"],
            "email": customers["email"]
        })
print(active_customers)