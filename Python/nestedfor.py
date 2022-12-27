# a=["Anoop","BARAGI","MYSURU"]
# for x in a:
#     for y in x:
#         #print(y)#nested forloop for printing each charecter in the list
#
# str = "MOOLYA"
# for s in str:
#     #print(s)
# b=[["MYSURU","BARAGI","ANOOP"],[1,5,3,4,6]]
# for z in  b:
#     for c in z:
#         print(c)
list4=[['india','MYSURU'],['usa','new jersy'],['canada','vancouver']]
# for s,t in list4:
#      print("my country name is ",s," and i live in ",t)#concatinating can be done by both +&,
#typecaste
#list5=[['india','MYSURU']]
#print(type(list5))
dict = dict(list4)#converting list to dictionary
for x,y in dict.items():
    for y in x:
        print(x,y)
print(type(list4))
# print(type(dict))
# print(dict)
# list6=['india','MYSURU']
# set = set(list6)
# print(type(set))
# print(set)
# tuple = tuple(list5)
# print(type(list5))
# print(tuple)