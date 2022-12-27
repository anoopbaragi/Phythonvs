a=5
b=8
c=3
print(a>b and c<b)
print(a>b or  c<b)
#list,tuples,dictionaries
a=(2,7,8)#tuples
#membership operator
print(8 in a)
a=2
print(a ** 3)#Exponetialoperator
#presidanceofoperator
print(5-8+2)
#Stringmanupulation
#string aare immutable
#operationstring
s = "anoop"
print(len(s))
print(s[4])
x=3456
c=str(x)
print(type(c))
#find()
print(s.find("o"))
print(s.find("q"))#-1 if the caracter not present
#upper/lowecase
print(s.upper())
print(s)
print(s.count("o"))
print(s.isupper())
z = "  MYSURU "
print(z)
print(z.strip())#triming the space
m = "visakhapatnam"
print(m)
print(m.replace("a","B").upper())
n = " ANOOP   "
print(n)
print(n.lstrip())
print(n.rstrip())
#splitoperation
sl = "Since Selenium is a collection of different tools, it also had different developers."
print(sl.split())
print(sl.replace(" ",""))
#print(sl.split("is"))
sl1="ANOOP\"BARAGI"#escape character
print(sl1)
#multiline/paragraph
sl2='''
MYSURU ANOOP BARAGI
'''
print(sl2)
print('ANOOP'in  sl2)
print(sl)
print(sl[::-1])#reverse the string
print(sl[::1])
print(sl[0:])#print hthe whole string
print(sl[0])#firstcharacter
print(sl[-1])#lastsecondcharacter
print(sl[0:5])#slice
print(sl[20:30])
print(sl[-11:-1])#printing from the last words
print(sl[-15:-3])#removes last 2 characters
print(sl.find("Since"))#find the index of the first word
print(sl[0:5])

