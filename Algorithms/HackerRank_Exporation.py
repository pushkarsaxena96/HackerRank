#!/bin/python3

import sys

def marsExploration(s):
    count = 0
    for i in range(0,len(s)-1,3):
        if s[i]!="s": 
            #print("1")
            count+=1
        
        if s[i+1]!="o": 
            #print("2")
            count+=1
        
        if s[i+2]!="s": 
            #print("3")
            count+=1
        
        
    return count

if __name__ == "__main__":
    s = input().strip()
    result = marsExploration(s)
    print(result)


