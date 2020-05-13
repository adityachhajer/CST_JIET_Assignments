x=int(input())
y=0
for i in range(1,x):
    x=x-i
    if x<0:
        print(y)
        break
    else:
        y=y+1
