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
        
        particles=self.particles
        weights=self.weights
        sum_weights=0
        
        for i in range(self.num_particles):
            noise_act=env.sample_noisy_action(u,self.alphas)
            x_bar=env.forward(self.particles[i],noise_act)
            particles[i,0]=x_bar[0]
            particles[i,1]=x_bar[1]
            particles[i,2]=x_bar[2]
            inno= minimized_angle(z-env.observe(x_bar,marker_id)) 
            weights[i]=env.likelihood(inno,self.beta)
            sum_weights=sum_weights+weights[i]
            
        norm_weights=weights/sum_weights
        
        self.particles=self.resample(particles,norm_weights)
        
        mean, cov = self.mean_and_variance(self.particles)
        return mean, cov

    def resample(self, particles, weights):
        """Sample new particles and weights given current particles and weights. Be sure
        to use the low-variance sampler from class.

        particles: (n x 3) matrix of poses
        weights: (n,) array of weights
        """
        '''
        new_particles, new_weights = particles, weights
        # YOUR IMPLEMENTATION HERE
        '''
        n=self.num_particles
        pointer=np.random.uniform(0,1/n)
        
        new_particles=np.zeros((n,3))
        cum_weights=np.cumsum(weights)
        for i in range(n):
            index=np.searchsorted(cum_weights,pointer)
            new_particles[i,:]=particles[index]
            pointer=pointer+1/n
            
        return new_particles

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
