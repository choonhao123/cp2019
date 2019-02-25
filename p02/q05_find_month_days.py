#leap year
def leap(year): 
    if year%4==0 and year%100!=0 or year%400==0:
        return True
    return False

#Returning values
def days(month, year):
    if month==2 and leap(year)==True:
        print("February "+str(year)+" has 29 days")
    elif month==1:
        print("January "+str(year)+" has 31 days")
    elif month==2:
        print("February "+str(year)+" has 28 days")
    elif month==3:
        print("March "+str(year)+" has 31 days")
    elif month==4:
        print("April "+str(year)+" has 30 days")
    elif month==5:
        print("May "+str(year)+" has 31 days")
    elif month==6:
        print("June "+str(year)+" has 30 days")
    elif month==7:
        print("July "+str(year)+" has 31 days")
    elif month==8:
        print("August "+str(year)+" has 31 days")
    elif month==9:
        print("September "+str(year)+" has 30 days")
    elif month==10:
        print("October "+str(year)+" has 31 days")
    elif month==11:
        print("November "+str(year)+" has 30 days")
    elif month==12:
        print("December "+str(year)+" has 31 days")
    else:
        print("not a valid month")
        
#input
y = int(input("Enter Year: "))
m = int(input("Enter Month: "))
days(m, y)
