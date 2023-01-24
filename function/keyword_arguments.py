#! /usr/bin/python3

# keyword arguments

def wish(first_name, second_name):
    print(f"Hai, {first_name} {second_name}")


print("Start of prgm")

# function call
# keyword arguments
# position argument should be at the first otherwise it shows error

# wish(second_name="Smith", "John")             # error
wish(second_name="Smith", first_name="John")

print("End of prgm")
