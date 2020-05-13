def minXOR(arr, n):
    arr.sort()
    min_xor = 100000
    val = 0
    for i in range(0, n - 1):
        for j in range(i + 1, n ):
            val = arr[i] ^ arr[j]
            min_xor = min(min_xor, val)
    return min_xor


arr = [9, 5, 3]
n = len(arr)

print(minXOR(arr, n))
