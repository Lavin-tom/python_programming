# string length

name = "John Looeis"
print(len(name))            # return length of string
print(name.upper())         # convert into uppercase
print(name.lower())         # convert into lowerrcase
print(name.find('n'))       # return first occurance of that chara
print(name.find("Looeis"))  # return where the first occurance of the word
print(name.replace("John", "Mark"))
print(name)                 # default name variable is still constant only until we assigned to it
name = name.replace("John", "Thomas")
print(name)
