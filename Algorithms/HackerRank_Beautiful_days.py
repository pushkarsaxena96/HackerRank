

#!/bin/python3

import sys

def beautifulDays(i, j, k):
    beautiful = 0
    non = 0
    for a in range(i,j):
        if abs(a-int(str(a)[::-1]))%k==0 :
            beautiful+=1
        else : 
            non+=1
            
if __name__ == "__main__":
    i, j, k = input().strip().split(' ')
    i, j, k = [int(i), int(j), int(k)]
    result = beautifulDays(i, j, k)
    print(result)


