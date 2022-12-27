import math
'''a = 4
print("sq root",a*2)

def sq(x):
    if(x>=0):
        sqroot= int(math.sqrt(x))
        return(sqroot*sqroot == x)
        return False
x = 64
if (sq(x)):
    print("Yes")
else:
    print("No")

def sqr(x,y):
    print(x+y)
    def sqr(x,y,z):
        print(x*y*z)
        def sqr(a,b,c,d):
         v=a*b*c*d
        print(v)
        root=math.isqrt(v)
        if root*2 == x:
            print("Perfect SquareRoot",x)
        else:
            print("Not a Perfect SquareRoot",x)
        sqr(5, 2, 4, 6)
    sqr(2, 4, 6)
sqr(1, 4, 1)'''
from multipledispatch import dispatch
@dispatch(int)
def sum(a):
    print("Square Root of:",a**2)
@dispatch(int,int)
def sum(a,b):
    print(a+b)
@dispatch(int,int,int)
def sum(a,b,c):
    print(a*b*c)
@dispatch(int,int,int,int)
def sum(p,q,r,s):
    t=p*q*r*s
    print(t)
    if t<0:
        print("Not possible")
    else:
        r=math.isqrt(t)
        print(r)
        if r**2==t:
            print("This is perfect square")
        else:
            print("This is not a perfect square")
sum(7)
sum(4,3)
sum(2,6,3)
sum(1,3,3,3)