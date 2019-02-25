#function to convert kg to pounds
def kgtop(mass):
    p = mass*2.2
    return p

#creating table using '\t'
print("Kilograms ",'\t',"Pounds")

#input values using loop
for i in range(11):
    print(str(i),'              ',"{:.2f}".format(kgtop(i)))
