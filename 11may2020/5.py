#using binary search
num=int(input())
if num == 0:
    print("0")
elif num == 1:
    print("1")
else:
    l = 2
    u = (num // 2) + 1
    while (l <= u):
        mid = (l + u) // 2
        if (mid * mid == num):
            print(mid)
            break
        else:
            if (mid * mid) > num:
                u = mid - 1
            else:
                l = mid + 1

