a=int(input())
b=int(input())
c=int(input())
sum=0
f=c*b
for i in range(f,a+1,f):
    if i%b==0 and i%c==0:
        sum+=1
print(sum)
