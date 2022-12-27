#ifelse
marks=35
if marks>=90:
    print("FCD")
elif marks >70 and marks<90:
    print("FC")
else:
    print("Second Class")
#maxmin
list1 = [10,20,30,50,5,800]
l= list1[0]
for i in list1: #iterator
    if i >= l:
        l = i
print(l)