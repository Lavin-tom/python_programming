#   A
#B     C
#   D

class A:
    a = 1

class B(A):
    #a = 11
    b = 2

class C(A):
    a = 22
    c = 3

class D(B,C):
    d = 4

obja = A()
print(obja.a)

objb = B()
print(objb.a,objb.b)

objc = C()
print(objc.a,objc.c)

objd = D()
print(objd.a,objd.b,objd.c,objd.d)

#to print MRO
print(D.__mro__)