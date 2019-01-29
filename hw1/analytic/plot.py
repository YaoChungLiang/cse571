import numpy as np
from matplotlib import pyplot as plt

def gen_data():
	num=100
	x=np.zeros([num,1])
	for i in range(num):
		x[i,:] = i/num
	return x

def pc(x):
	return (0.24*x+0.36)/(0.16*x+0.44)

if __name__ == "__main__":
	x = gen_data()
	y = pc(x)
	plt.plot(x,y)
	plt.title("bayes rule")
	plt.xlabel("c")
	plt.ylabel("$p(x_{t+1}=clean)$")
	plt.show()	
	