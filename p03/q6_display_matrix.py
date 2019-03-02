from random import randint

def print_matrix(n):
    for i in range(n):
        for i in range(n):
            print(f"{randint(0,1)}",end=" ")
        print()

n = int(input("Enter Number: "))
print_matrix(n)
