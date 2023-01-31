#! /usr/bin/python3


# file append

file = open("sample.txt", 'a')

content = input("enter content to be added : ")
file.write(content)
file.close()
