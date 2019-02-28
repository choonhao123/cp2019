num = int(input("Please Enter any Number: "))        

def reverse_int(n):
    Number = num
    Reverse = 0
    while(Number > 0):    
        Reminder = Number %10    
        Reverse = (Reverse *10) + Reminder    
        Number = Number //10
    return Reverse
    
print(reverse_int(num))
