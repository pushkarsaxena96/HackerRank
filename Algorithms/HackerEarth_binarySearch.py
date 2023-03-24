

def power(l,a) :
    count = 0
    for element in l :
        if element <= a :
            count=count+element
        else : pass
    
    print(a,count)


t = int(input())
l=list(map(int,input().split()))
q = int(input())
for i in range(0,q-1):
    a = int(input())
    power(l,a)