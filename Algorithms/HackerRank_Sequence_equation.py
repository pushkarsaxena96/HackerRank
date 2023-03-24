#!/bin/python3

import sys

def squares(a, b):
    li=[]
    for i in arange(a,b):
        li.append(i)
    print(li)
    count = 0
    for i in range(0,b+1):
        print(i)
        if i**2 in li :
            print("enter")
            count+=1
    return count

if __name__ == "__main__":
    q = int(input().strip())
    for a0 in range(q):
        a, b = input().strip().split(' ')
        a, b = [int(a), int(b)]
        result = squares(a, b)
        print(result)