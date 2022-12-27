#dictionary
a={'URL1':'https://www.google.com/','URL2':'https://demoqa.com/'}
b={1:'ANOOP',2:'BARAGI'}
print(b[1])
print(a['URL1'])
#print(b['BARAGI'])
#print(a['https://www.google.com/'])
b[3]="MYSURU"
print(b)
a['URL3']='flipkart.com'
print(a)
#print(b[4])
print(b.get(1))#getting the value using get method
print(b.setdefault(4,"MYSORE"))#adding key and value from set methos
print(b)
print(b.keys())#we get the no of keys in dictionary
print(type(a))
print(b.items())#will get the values in the tupple formate
print(b.pop(4))#will delete the particular key
print(b)
print(b.popitem())#will delete the last key value in the dictionary
print(b)
print(b.keys())
b.update({3:"MOOLYA",4:"MYSURU"})#update the dictionary
print(b)
print(b.keys())
b.clear()#will clear the dictionary
print(b)