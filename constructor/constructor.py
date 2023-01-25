#! /usr/bin/python3

class Student:

    def __init__(self):
        print('objected created')

    def __del__(self):
        print('object destroyed')


obj = Student()
