import numpy as np

def A(x):
	A = np.array([x, x**2])
	return A

mu = np.array([0])
beta = np.diag([np.deg2rad(5)**2])
print(beta.shape)
z = np.random.multivariate_normal(mu, beta)

print(A(10))
print(z)