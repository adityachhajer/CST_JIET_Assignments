def sub_lists(list1):
    sublist = [[]]

    for i in range(len(list1) + 1):

        for j in range(i + 1, len(list1) + 1):
            sub = list1[i:j]
            if sub not in sublist :
                sublist.append(sub)

    return len(sublist)-1


n=int(input())
l1=list(map(int,input().split()))[:n]
print(sub_lists(l1))