#profit&loss
sp=[60,4,60,8,100]
cp=[40,60,20,30,1]
np=zip(sp,cp)
for a,b in np:
    if b<a:
        print("profit",a-b)
    elif a<b:
        print("loss",b-a)