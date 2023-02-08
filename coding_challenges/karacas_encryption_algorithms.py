#! /usr/bin/python3

# karacas encryption algorithms

def vowels(a):
    k = 0
    b = []
    for i in range(len(a)):
       
        if a[i] == 'a':
            b.append('0')
        elif a[i] == 'e':
            b.append('1')
        elif a[i] == 'i':
            b.append('2')
        elif a[i] == 'o':
            b.append('3')
        elif a[i] == 'u':
            b.append('4')
        else:
            b.append(a[i])
        k += 1
    b.append("aca")
    return b


a = input("enter string")

# reverse the input string
a = a[::-1]

b = vowels(a)
b = ''.join(b)
print(b)
