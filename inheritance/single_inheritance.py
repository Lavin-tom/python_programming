#single inheritance

class A:
    a = 10

class B (A):
    b = 20

obja = A()
objb = B()
print(obja.a)
print(objb.a,objb.b)