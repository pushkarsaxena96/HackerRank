#!/bin/python3

import sys

def solve(n, s, d, m):
    start = 0
    end = m
    count = 0
    while end <= len(s):
        if (sum(s[start:end]) == d) :
            count += 1
    
        start+=1
        end+=1
    
    return count

n = int(input().strip())
s = list(map(int, input().strip().split(' ')))
d, m = input().strip().split(' ')
d, m = [int(d), int(m)]
result = solve(n, s, d, m)
print(result)