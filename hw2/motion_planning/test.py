import numpy as np
import numpy
from matplotlib import pyplot as plt

plan = np.zeros([10,2])
for i in range(5):
	plan[i,0], plan[i,1] = i, i
for i in range(5,10):
	plan[i,0], plan[i,1] = 5, i

for i in range(numpy.shape(plan)[0] - 1):
    x = [plan[i,0], plan[i+1, 0]]
    y = [plan[i,1], plan[i+1, 1]]
    plt.plot(y, x, 'k')
plt.show()