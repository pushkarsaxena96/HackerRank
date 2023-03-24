

def power(l,a) :
    total = 0
    count = 0
    for element in l :
        if element <= a :
            total=total+element
            count=count+1
        else : pass
    
    print(count,total)


t = int(input())
l=list(map(int,input().split()))
q = int(input())
for i in range(0,q):
    a = int(input())
    power(l,a)