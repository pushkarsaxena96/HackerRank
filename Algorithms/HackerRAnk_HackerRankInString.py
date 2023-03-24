#!/bin/python3

import sys

def hackerrankInString(s):
    # Complete this function
    p = 0
    for e in 'hackerrank':
        if e in s[p:]:
            p = s.index(e,p) + 1
        else:
            return 'NO'
    return 'YES'

if __name__ == "__main__":
    q = int(input().strip())
    for a0 in range(q):
        s = input().strip()
        result = hackerrankInString(s)
        print(result)
