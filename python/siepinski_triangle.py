import matplotlib.pyplot as plt
import numpy as np
from random import randint

def halfway(p, v):
    return [(p[0]+v[0])/2,(p[1]+v[1])/2]

def triangle():
    vertexes = np.array([[1,1],[0,0],[2,0]])
    next = [0,0]
    points = []
    for i in range(int(5E+5)):
        next = halfway(next, vertexes[randint(0,2)%3])
        points.append(next)
    return np.concatenate((np.array(points), vertexes))

points = triangle()
plt.plot(points[:,0], points[:,1], 'g*')
plt.show()