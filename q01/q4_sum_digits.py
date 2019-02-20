n = int(input("number: "))
a=0
while len(str(n))>1:
    o = n%10
    a = a+o
    n = n//10
print(a+n)
