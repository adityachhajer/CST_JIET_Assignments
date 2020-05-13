def magic(num):
    c=0
    while num>0:
        a=num%10
        c=c+a
        num=num//10
    if c==1:
        return True
    elif(c>1 and c<10):
        return False
    else:
        return magic(c)

for i in range(1,1001):
    a=magic(i)
    if a==True:
        print(i,end=" ")


