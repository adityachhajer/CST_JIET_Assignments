m = int(input())
count = [[0 for x in range(m)] for y in range(m)]

for j in range(m):
    for i in range(m):
        count[j][0] = 1
        if(i<=j):
            count[j][i]=count[j-1][i]+count[j][i-1]
        else:
            break

print(count[m-1][m-1])
