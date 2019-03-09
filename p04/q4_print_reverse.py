i = []
def reverse_int(n):
    if n == 0:
        return
    else:
        int = n%10
        i.append(int)
        return reverse_int(n//10)

num = int(input("Enter Number: "))
reverse_int(num)
for x in range(len(i)):
    print(i[x],end="")
