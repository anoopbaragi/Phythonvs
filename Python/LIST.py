#LIST
v=["ANOOP",4395,True]
print(type(v))
print(v[2])
print(v[-2])
#print(v[3])//out of range
b=[10,5,'BARAGI','MYSURU','BARAGI']#list can accept the duplicate value
print(b)
print(b[1:5:2])
#[Startingvalue : Stoping value : step]
#LIST METHODS
print(b.count('MYSURU'))
b.append("ANOOP")
print(b)#append
b.insert(1,'MOOLYA')
print(b)#insertthe value
b.pop(2)#delete the value in that index
print(b)
b.reverse()#reverse the list
print(b)
print(b.count("BARAGI"))
b1=["MOOLYA","INDIA","MYSURU","ANOOP","KARNATAKA","BARAGI"]
b1.sort()#sorting the list
print(b1)
b2=[40,10,80,60,50]
#b2.sort(reverse=True)
b2.sort()
b2.reverse()
print(b2)
print(b)
b.clear()
print(b)
#set it does not accept the duplicate value & prints in unorderd
b3={"MOOLYA","INDIA","MYSURU","ANOOP",25082,7885,"ANOOP"}
print(type(b3))
print(b3)
print(len(b3))
b3.add(100)
print(b3)
#set
print("SETS")
t={'a','b','c','d','e'}
t1 ={"Anoop","Baragi","Mysuru","a"}
z=t.intersection(t1)
z1=t.union(t1)
z2=t.issubset(t1)
z3=t.symmetric_difference(t1)
print(z)
print(z1)
print(z2)
print(z3)