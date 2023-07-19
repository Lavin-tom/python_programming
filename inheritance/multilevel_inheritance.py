#multilevel inheritance

class A:
    a = 10

class B(A):
    b = 20

class C(B):
    c = 30

objc = C()
print(objc.a,objc.b,objc.c)