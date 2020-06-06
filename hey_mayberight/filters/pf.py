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
        #print(env) # call Field functions
        #print(self.weights) # [0.01 0.01 ~~~0.01] 1 by 100
        #print(self.num_particles) #100

        
        
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
            # determine the importace
            innovation = minimized_angle(z-env.observe(x_bar,marker_id)) #???
            weights[i]=env.likelihood(innovation,self.beta)
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
        pointer=np.random.uniform(0,1/self.num_particles)
        pt_new=np.zeros((self.num_particles,3))
        cum_weights=[]
        cum_weights=np.cumsum(weights)
        for i in range(self.num_particles):
            index=np.searchsorted(cum_weights,pointer)
            pt_new[i,0]=new_particles[index][0]
            pt_new[i,1]=new_particles[index][1]
            pt_new[i,2]=new_particles[index][2]
            pointer=pointer+ 1/self.num_particles
        new_particles=pt_new
        '''
        n=self.num_particles
        ptr=np.random.uniform(0,1/n)
        cum_weights=np.cumsum(weights)
        new_particles=np.zeros((self.num_particles,3))
        for i in range(n):
            idx=np.searchsorted(cum_weights,ptr)
            new_particles[i,:]=particles[idx]
            ptr=ptr+1/n
            
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
