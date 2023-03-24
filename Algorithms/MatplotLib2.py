from numpy import *
import matplotlib.pyplot as plt
x = arange(0.,10.,0.1)
y = sin(x)
print(x)
print(y)
ll = plt.plot(x,y)
print(ll)