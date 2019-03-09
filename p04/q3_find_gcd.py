def gcd(a,b):
    if a % b == 0:
       return b
    return gcd(b, a % b)

print(gcd(255,25))
print(gcd(24,16))
