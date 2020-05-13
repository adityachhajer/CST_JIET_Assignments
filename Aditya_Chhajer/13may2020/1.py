n=int(input("enter the size of array:"))
l=list(map(int,input().split()))[:n]
e=0
o=0
for i in l:
    if i%2==0:
        e+=1
    else:
        o+=1
print(min(e,o))