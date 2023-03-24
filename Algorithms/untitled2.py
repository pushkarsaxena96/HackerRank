import numpy as np
import csv
f = open("winequality-red.csv","r")
wines = list(csv.reader(f, delimiter=";"))
qual = []
total = 0
count = 0

# different types of arrays

wines = np.array(wines[1:], dtype = np.float)
#print(wines)
empty_array = np.zeros((3,4), dtype = np.float)
random_array = np.random.rand(3,4)

#qualities = [float(item[-1]) for item in wines[1:]]
#print(sum(qualities)/len(qualities))
#print(wines.shape)
#print(empty_array)
#print(random_array)

# Reading CSV directly from numpy
wines = np.genfromtxt("winequality-red.csv", delimiter=";", skip_header=1)
print(wines[:,3]) # all elements in 4th column
print(wines[3,:]) # all elements in 3rd row
print(np.transpose(wines).shape)
print(wines.ravel())



"""
import numpy as np
empty_array = np.zeros((3,4))
ones_array = np.ones((6,4))
#print(empty_array)
#print(ones_array)
all_array = np.vstack((empty_array, ones_array))
print(all_array[:,1])
"""