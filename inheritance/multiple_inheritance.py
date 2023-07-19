#multiple inheritance

class A:
    a = 10

class B :
    b = 20

class C(A,B):
    c = 30

objc = C()
print(objc.a,objc.b,objc.c)