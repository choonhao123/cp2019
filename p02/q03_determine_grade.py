#input
score = int(input("Enter Number: "))

#Checking score
if score<1 or score >100:
    print("Invalid! Score must be within 0 - 100")
elif 70<=score<= 100:
    print("A")
elif 60<=score<=69:
    print("B")
elif 55<=score<=59:
    print("C")
elif 50<=score<=54:
    print("D")
elif 45<=score<=49:
    print("E")
elif 35<=score<=44:
    print("S")
else:
    print("U")
