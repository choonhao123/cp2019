scores = {}
#defining function to add to dict
def grades(name, score):
    scores[name] = score
    
#getting number of students
num_student = int(input("Number of Students: "))

x = 0

#appending dictionary
while x < num_student:
    n = input("Name: ")
    s = input("Score:")
    grades(n,s)
    x = x+1

#printing max score name
print(max(scores))
scores.pop(max(scores))
print(max(scores))
