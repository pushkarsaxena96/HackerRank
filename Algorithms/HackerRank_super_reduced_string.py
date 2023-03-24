#!/bin/python3

import sys

def super_reduced_string(S):
    LS = list(S)
    i = 0 
    while i < len(LS)-1:
        if LS[i]==LS[i+1]:
            del LS[i]
            del LS[i]
            i = 0
            if len(LS) == 0:
                print ('Empty String')
                break
        else:
            i+=1
    return (''.join(LS))

s = input().strip()
result = super_reduced_string(s)
print(result)
