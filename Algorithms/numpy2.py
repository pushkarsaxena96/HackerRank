import numpy as np
empty_array = np.zeros((3,4))
ones_array = np.ones((6,4))
#print(empty_array)
#print(ones_array)
all_array = np.vstack((empty_array, ones_array))
print(all_array[:,1])