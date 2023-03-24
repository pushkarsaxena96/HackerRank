import sys

def divisibleSumPairs(n, k, ar):
    count = 0
    for elements in ar :
        for ele in ar :
            if ((elements + ele)%k == 0) and (ar.index(elements) < ar.index(ele)) :
               # print("entered if")
                count += 1
                
            
    return count

n, k = input().strip().split(' ')
n, k = [int(n), int(k)]
ar = list(map(int, input().strip().split(' ')))
result = divisibleSumPairs(n, k, ar)
print(result)