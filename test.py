
import numpy as np
import matplotlib.pyplot as plt
p = [10, 30, 40]
c = 2
for k in p:
    print(k*c)
result = []
for k in p:
    twd = k*c
    result.append(twd)
print(result)    
prices = np.array(p)
print(prices)
print(prices * c)

grades = np.array([85, 70, 82])
weights = np.array([0.3, 0.4, 0.3])
g = grades * weights
print(g)
print(g.sum())
print(np.dot(grades, weights))