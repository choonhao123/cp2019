#input
s1 = int(input("Enter side 1: "))
s2 = int(input("Enter side 2: "))
s3 = int(input("Enter side 3: "))

#checking for lengths
if s1>=s2+s3 or s2>=s1+s3:
    print("Invalid triangle!")
else: 
    print(str(s1+s2+s3))
