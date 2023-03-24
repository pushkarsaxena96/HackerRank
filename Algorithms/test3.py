"""import sys

def countApplesAndOranges(s, t, a, b, apples, oranges):
    

if __name__ == "__main__":
    s, t = input().strip().split(' ')
    s, t = [int(s), int(t)]
    a, b = input().strip().split(' ')
    a, b = [int(a), int(b)]
    m, n = input().strip().split(' ')
    m, n = [int(m), int(n)]
    apple = list(map(int, input().strip().split(' ')))
    orange = list(map(int, input().strip().split(' ')))
    countApplesAndOranges(s, t, a, b, apple, orange)
    """
    
s, t = input().strip().split(' ')
s, t = [int(s), int(t)]
a, b = input().strip().split(' ')
a, b = [int(a), int(b)]
m, n = input().strip().split(' ')
m, n = [int(m), int(n)]
apple = list(map(int, input().strip().split(' ')))
orange = list(map(int, input().strip().split(' ')))

print("staring and ending point of house: ",s,t)
print("Positions of both the trees : ",a,b)
print("Number of apples thrown respectively: ",m,n)
print("Distance of apples from apple tree",apple)
print("Distance of oranges from orange tree",orange)
print(type(s))
print(type(a))
print(type(m))
print(type(apple))
Acount = 0
Bcount = 0
for i in range(m) :
    if ((a + apple[i]) >=s) and ((a + apple[i]) <=t) :
        print("Apple : Entered LOOP, i = ",i)
        Acount+=1
    else : pass

for i in range(n) :
    if ((b + orange[i]) <=t) and ((b + orange[i]) >=s):
        print("Orange: Entered loop, i =",i)
        Bcount+=1
    else : pass
        

print("A count is", Acount)
print("B count is", Bcount)