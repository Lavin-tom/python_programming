#! /usr/bin/python3

source = open("sample.txt", 'r')
destination = open("destination.txt", 'w')

content = source.read()
destination.write(content)

source.close()
destination.close()
