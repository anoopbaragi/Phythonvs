"""def a(x):
    x=10
    global x1
    print(x)

def b(d,e):
    x1=15
    print(x1)"""
x=10
def mul():
    x=20
    print(x)
    def sub():
        print(x)
    def add():
        print(x)
    add()
    sub()
mul()