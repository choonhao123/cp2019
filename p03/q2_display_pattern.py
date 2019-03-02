#defining function
def display_pattern(n):
    x = 1
    while x <= n:
        for i in range(x+1, n+1):
            print(" ", end="")#printing spaces in front of number
        print(x,end="")
        if x>1:
            for z in range(1, x):#printing numbers after first
                print(x-z,end="")
        print()
        x += 1

#main
number = int(input("Enter Number: "))
display_pattern(number)
