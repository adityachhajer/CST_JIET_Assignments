x=list(map(int,input().split()))
sum=0
for i in x:
    sum=sum^i
print(sum)