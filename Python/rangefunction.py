# a = [1,2,3,4,5,6,7,8,9,10]
# for x in a:
#     print(x)
# for x in range(1,11):
#     print(x)
# even and odd
for x in range(1,10):
    if(x%2 == 0):
        print(x, "Even")
    else:
        print(x,"Odd")
#table of 23
for y in range(1,11):
    print("23 * " ,y, " = ", 23*y)
#even and odd using only range not condition satement
for z in range(1,10,2):
    print(z,end=' ')
print("\n")
for c in range(2,10,2):
    print(c,end=' ')