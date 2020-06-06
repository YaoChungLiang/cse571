import numpy as np

from utils import minimized_angle


class ParticleFilter:
    def __init__(self, mean, cov, num_particles, alphas, beta):
        self.alphas = alphas
        self.beta = beta

        self._init_mean = mean
        self._init_cov = cov
        self.num_particles = num_particles
        self.reset()

    def reset(self):
        self.particles = np.zeros((self.num_particles, 3))
        for i in range(self.num_particles):
            self.particles[i, :] = np.random.multivariate_normal(
                self._init_mean.ravel(), self._init_cov)
        self.weights = np.ones(self.num_particles) / self.num_particles

    def update(self, env, u, z, marker_id):
        """Update the state estimate after taking an action and receiving a landmark
        observation.

        u: action
        z: landmark observation
        marker_id: landmark ID
        """
        #print(self.particles) # [180 48 -0.3]
        #print(self.particles.shape) #(100,3)
        #print(self.weights) #(1,100) 0.01
        


        # YOUR IMPLEMENTATION HERE
        mean, cov = self.mean_and_variance(self.particles)

        #for i in range(self.num_particles):
            
        return mean, cov

    def resample(self, particles, weights):
        """Sample new particles and weights given current particles and weights. Be sure
        to use the low-variance sampler from class.

        particles: (n x 3) matrix of poses
        weights: (n,) array of weights
        """
        new_particles, new_weights = particles, weights
        # YOUR IMPLEMENTATION HERE

        print(particles)
        return new_particles, new_weights

    def mean_and_variance(self, particles):
        """Compute the mean and covariance matrix for a set of equally-weighted
        particles.

        particles: (n x 3) matrix of poses
        """
        mean = particles.mean(axis=0)
        mean[2] = np.arctan2(
            np.cos(particles[:, 2]).sum(),
            np.sin(particles[:, 2]).sum()
        )

        zero_mean = particles - mean
        for i in range(zero_mean.shape[0]):
            zero_mean[i, 2] = minimized_angle(zero_mean[i, 2])
        cov = np.dot(zero_mean.T, zero_mean) / self.num_particles

        return mean.reshape((-1, 1)), cov
'''
class bayes:
    def __init__(self):
        self._container=dict()
    def set_prb(self,x,prb):
        self.x=x
        self.prb=prb
        self._container[x]=prb
    def multi(self,x,prb):
        pre_prb=self._container[x]
        self._container[x]=pre_prb*prb
    def normalize(self):
        count = 0
        for hypothis in self._container.values():
            count=count+hypothis
        for hypothis,prob in self._container.items():
            self._container[hypothis]=self._container[hypothis]/count
    def prb(self,x):
        prb=self._container[x]
        return prb
    '''    
