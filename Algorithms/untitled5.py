n = int(input("Enter: ").strip())
grades = []
grades_i = 0
for grades_i in range(n):
   grades_t = int(input().strip())
   grades.append(grades_t)
   
for element in grades :
    if element < 38 :
        element = element
    elif abs(element - (element%5) + 5) < 3 :
        print("boom")
        element = (element%5) + 5
    else :
        element = element
        
    grades.append(element)
    
   
print(grades)