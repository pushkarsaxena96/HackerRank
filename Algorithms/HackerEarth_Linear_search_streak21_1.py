
def place(case):
    case = list(map(int, str(case)))
    for i in range(0,len(case)-1):
            if case[i]==2 and case[i+1]==1 :
                return "The streak is broken!"

def streak(case):
    if case%21==0 :
        print("The streak is broken!")
        exit
    
    elif place(case) == "The streak is broken!" :
        print("The streak is broken!")
    
    else:
        print("The streak lives still in our heart!")
                

t = int(input())
for i in range(0,t) :
    case = int(input())
    streak(case)