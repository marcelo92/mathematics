import matplotlib.pyplot as plt
import numpy as np

def converge(c):
    def func(c,p,it):
        if it > 100:
            return True
        elif abs(p) >= 2:
            return False
        else:
            next = p*p + c
            return func(c,next,it+1)
    return func(c,c,0)

def setData():
    complexes = []
    rg = np.linspace(-2,2,900)
    for i in rg:
        for j in rg:
            c = complex(i,j)
            if converge(c):
                complexes.append(c)
    return np.array(complexes)

data = setData()
x = data.real
y = data.imag
plt.plot(x,y, 'g*')
plt.show()