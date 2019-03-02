def gcd(m,n):
    while n:
        m, n = n, m%n
    return m

num1 = int(input("Enter First Number: "))
num2 = int(input("Enter First Number: "))

gcd(num1, num2)
