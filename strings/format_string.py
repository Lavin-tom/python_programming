#! /usr/bin/python3

# string format

quantity = 2
price = 343
item_no = 123

my_order = "i want {} of item no {} for the price of {}"
print(my_order.format(quantity, item_no, price))
print(f"i want {quantity} of item no {item_no} for the price of {price}")
