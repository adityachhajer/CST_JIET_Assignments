def gcd(a, b):
    if (a == 0):
        return b
    if (b == 0):
        return a
    if (a == b):
        return a
    if (a > b):
        return gcd(a - b, b)
    return gcd(a, b - a)


a=int(input())
b=int(input())

print("gcd: ",gcd(a,b))
print("lcm is:",(a*b) / gcd(a,b))