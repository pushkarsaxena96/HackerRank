import numpy as np
print(np.__version__)
np.show_config()
z = np.zeros(10)
print(z)
z = np.zeros(10)
z[4] =1
print(z)
z = np.arange(10,50)
print(z)
z = np.arange(50)
print(z[::-1])
z = np.arange(9).reshape(3,3)
print(z)
nz = np.nonzero([1,2,0,0,4,7,4,0])
print(nz)
z = np.eye(5)
print(z)
z = np.random.randint(100, size=(3,3,3))
zmin, zmax, mean = z.min(), z.max(), z.mean()
print(z)
print(zmin,"|", zmax,"|", mean)
z = np.tile( np.array([[0,1],[1,0]]), (4))
print(z)
print(z)
z = np.random.randint(5, size=(5,5))
print("After This")
print(z)
znor = (z - z.min())/(z.max() - z.min())
print(znor)
color = np.dtype([("r", np.ubyte, 1),
                  ("g", np.ubyte, 1),
                  ("b", np.ubyte, 1),
                  ("a", np.ubyte, 1)])
print(color)
z = np.dot(np.ones((5,3)), np.ones((3,2)))
print(z)

z= np.arange(11)
z[(z>3) & (z<=8)]*= -1
print(z)


