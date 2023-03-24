#!/bin/python3

import sys

def camelcase(s):
    count = 1
    for i in range(len(s)-1) :
        if s[i] == s[i].upper() :
            print(s[i], count)
            count+=1
    
    return count
            

if __name__ == "__main__":
    s = input().strip()
    result = camelcase(s)
    print(result)
