def median(data):
    if len(data)%2 == 0:
        return int(sum(data[len(data)//2-1:len(data)//2+1])/2)
    else:
        return data[len(data)//2]

def quartiles(N,data):
    Q1 = median(data[:len(data)//2])
    Q2 = median(data)
    if N%2 == 0:
        Q3 = median(data[len(data)//2:])
    else:
        Q3 = median(data[len(data)//2+1:])
    return Q1,Q2,Q3

n = int(input())
x = list(map(int, input().split()))
y = list(map(int, input().split()))
data = []

for i in range(len(x)):
    for j in range(y[i]) :
        data.append(x[i])

data=sorted(data)
Q1,Q2,Q3 = quartiles(n,data)
print("{0:0.1f}".format(Q3-Q1))
        
