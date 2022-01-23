import matplotlib.pyplot as plt
import numpy as np
import math

def ship(p,c):
    return pow((abs(p.real) + complex(0,1)*abs(p.imag)), 2) + c

def simple(p,c):
    return p*p + c

def converge(c):
    def func(c,p,it):
        if it > 64 or abs(p) >= 2:
            return it
        else:
            return func(c,ship(p,c),it+1)
    return func(c,c,0)

def setData():
    complexes = []
    for i in np.linspace(-2,1,900):
        for j in np.linspace(-1.5,1.5,900):
            c = complex(i,j)
            iterations = math.log(converge(c)+1)
            complexes.append([c, iterations])
    return np.array(complexes)

data = setData()
x = data[:,0].real
y = data[:,0].imag
fig = plt.figure()
ax = fig.add_subplot(111)
ax.scatter(x,y, c=data[:,1])
plt.show()