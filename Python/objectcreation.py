class my_class:
    x,y = 4,6
    def abc(self,b,c):
        self.x=b #self is a key word use to acces the within the same class
        self.y=c
        print(b+c)
        print(self.y)

obj = my_class()
obj.abc(5,10)
obj1=my_class()
obj1.abc(20, 5)