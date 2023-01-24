#! /usr/bin/python3

# with help of key associated we can access the data
# we can modify the data of dictionaries

customer = {
        "name": "John Smith",
        "age": 30,
        "is_varified": True
        }
print(customer["name"])
customer["name"] = "Thomas"
print(customer["name"])
print(customer.get("DOB", "Jan 1st"))
