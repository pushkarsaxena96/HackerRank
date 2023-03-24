#!/bin/python3

import sys

def hurdleRace(k, height):
    new = []
    newk = k
    height = sorted(height)
    for elements in height : 
        if elements >= k :
            new.append(elements)
    if new == []:
        return 0
    else :
        newk = newk + (i-newk)
        return newk
    

if __name__ == "__main__":
    n, k = input().strip().split(' ')
    n, k = [int(n), int(k)]
    height = list(map(int, input().strip().split(' ')))
    result = hurdleRace(k, height)
    print(result)
