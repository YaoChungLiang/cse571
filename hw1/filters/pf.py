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
        # YOUR IMPLEMENTATION HERE

        # resampling from motion model
        ## --- forward motion model to get new particles
        flag = 2
        if flag == 2:
            for i in range(self.num_particles):
                u_noise = env.sample_noisy_action(u, self.alphas)
                self.particles[i, :] = env.forward(self.particles[i, :], u_noise).ravel()
                zt = env.observe(self.particles[i, :], marker_id)
                self.weights[i] = env.likelihood(zt.ravel()-z.ravel(), self.beta)    
            self.weights += 1.e-300
        # normalizer
        self.weights = self.weights / self.weights.sum()

        # resampling
        if self.neff(self.weights) < self.num_particles/2:
            self.particles, self.weights = self.resample1(self.particles, self.weights)
        mean, cov = self.mean_and_variance(self.particles)
        return mean, cov

    def neff(self, weights):
        return 1. / np.sum(np.square(weights))

    def resample1(self, particles, weights):
        """Sample new particles and weights given current particles and weights. Be sure
        to use the low-variance sampler from class.

        particles: (n x 3) matrix of poses
        weights: (n,) array of weights
        """
        # new_particles, new_weights = particles, weights 
        ## this misled me a lot !!!! be careful about reference in Python !!!shit.
        # new_particles = np.zeros([self.num_particles, 3])
        # new_weights = np.zeros(self.num_particles)
        particles_lst = []
        weights_lst = []
        # YOUR IMPLEMENTATION HERE
        r = np.random.uniform(0, 1/self.num_particles) 
        c = weights[0]
        i = 0
        for k in range(self.num_particles):
            U = r + k / self.num_particles
            while U > c:
                i += 1
                c += weights[i]
            particles_lst.append(particles[i, :])
            weights_lst.append(weights[i])
            # new_particles[k, :] = particles[i, :]
            # new_weights[k] = weights[i]
        # self.num_particles = len(particles_lst) # Systematic sampling doesn't change M
        new_particles = np.asarray(particles_lst)
        new_weights = np.asarray(weights_lst)
        new_weights = new_weights / new_weights.sum()
        print(self.num_particles)
        return new_particles, new_weights

    def resample2(self, particles, weights):
        new_particles, new_weights = particles, weights
        cumulative_sum = np.cumsum(self.weights)
        cumulative_sum[-1] = 1. # avoid round-off error
        indexes = np.searchsorted(cumulative_sum, np.random.uniform(low=0.0, high=1.0, size=self.num_particles))
        
        # resample according to indexes
        new_particles = particles[indexes]
        new_weights = weights[indexes]
        new_weights /= np.sum(new_weights) # normalize
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
        # why do we need do this????

        zero_mean = particles - mean
        for i in range(zero_mean.shape[0]):
            zero_mean[i, 2] = minimized_angle(zero_mean[i, 2])
        cov = np.dot(zero_mean.T, zero_mean) / self.num_particles

        return mean.reshape((-1, 1)), cov
