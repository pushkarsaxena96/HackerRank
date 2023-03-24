#!/bin/python3

import sys
import numpy as np
from scipy import stats

t = int(input().strip())
n = list(map(int, input().strip().split(' ')))
    
mean1 = np.average(n)
median1 = np.median(n)

        
#print(mean1)
#print(median1)
#print(mode1[0])