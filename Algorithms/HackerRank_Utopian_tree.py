#!/bin/python3

import sys

def utopianTree(n):
    height = 1
    for i in range(n+1):
        if (i==0):
            pass
        elif (i%2==0):
            height = height + 1
        elif (i%2!=0):
            height = height * 2
    
    return height            

if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        n = int(input().strip())
        result = utopianTree(n)
        print(result)
