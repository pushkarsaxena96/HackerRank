n = int(input())
X = list(map(int, input().split()))
mean = sum(X)/n
variance = sum(list(map(lambda x: (x-mean)**2, X))) / n
print("%.1f" % (variance**0.5))