#Checking for leap
def leap(year): 
    if year%4==0 and year%100!=0 or year%400==0:
        print("Leap")
    else:
        print("Non-Leap")
        
leap(int(input("Enter year: ")))
