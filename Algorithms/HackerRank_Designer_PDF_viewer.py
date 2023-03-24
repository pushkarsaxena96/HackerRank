#!/bin/python3

import sys
import string as s

def designerPdfViewer(h, word):
    heightlist=[]
    for i in range(len(word)-1):
        a=s.ascii_lowercase.index(word[i])
        heightlist.append(h[a])
     
    area = max(heightlist) * len(word)
    return area
if __name__ == "__main__":
    h = list(map(int, input().strip().split(' ')))
    word = input().strip()
    result = designerPdfViewer(h, word)
    print(result)
