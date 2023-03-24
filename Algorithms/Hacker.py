

def name(case) :
    case = str(case.upper())
    half = 0
    full = 0

    for i in range(0,len(case)):

        if (case[i]=="S") and (case[i+1] == "U") and (case[i+2] =="V") and (case[i+3] == "O") and (case[i+4]== "J") and (case[i+5]=="I")  and (case[i+6]=="T") :
            print("FULL")
            full+=1
        if (case[i]=="S") and (case[i+1]== "U") and (case[i+2]=="V") and (case[i+3] == "O"):
            print("HALF")
            half+=1
        if i++6 == len(case):
            break
    
    print("SUVO = {}, SUVOJIT = {}".format(half, full))
            

t = int(input())
for i in range(0,t) :
    case = input()
    name(case)