def repeated(l,a) :
    minimum = min(l)
    count = 0
    for e in l :
        if (e == minimum) :
            count+=1
    
    if (count == a):
        print(minimum)
    else :
        l.remove(minimum)
        repeated(l,a)

t = int(input())
l=list(map(int,input().split()))
a=int(input())
repeated(l,a)