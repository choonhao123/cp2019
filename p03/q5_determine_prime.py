def is_prime(n):
    if n==2 or n==3:
        return True
    for i in range(2, n-1):
        if n%2==0 or n%3==0 or n%5==0:
            return False
        else:
            return True
        
q = 0
x = 1
while q<1000:
    if is_prime(x)==True:
        print(x,end=" ")
        q += 1
        if q%10==0:
            print()
    x += 1
