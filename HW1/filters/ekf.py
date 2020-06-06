import numpy as np

from utils import minimized_angle


class ExtendedKalmanFilter:
    def __init__(self, mean, cov, alphas, beta):
        self.alphas = alphas
        self.beta = beta

        self._init_mean = mean
        self._init_cov = cov
        self.reset()

    def reset(self):
        self.mu = self._init_mean
        self.sigma = self._init_cov

    def update(self, env, u, z, marker_id):
        """Update the state estimate after taking an action and receiving a landmark
        observation.

        u: action
        z: landmark observation
        marker_id: landmark ID
        """
        
        #prediction
        # YOUR IMPLEMENTATION HERE
        Gt=env.G(self.mu,u)
        Vt=env.V(self.mu,u)
        Mt=env.noise_from_motion(u,self.alphas) 
        mu_t_bar=env.forward(self.mu,u)
        Rt=Vt.dot(Mt).dot(Vt.T)
        sigma_t_bar=Gt.dot(self.sigma).dot(Gt.T)+Rt
        Qt=self.beta
        Ht=env.H(mu_t_bar,marker_id)
        Kt=sigma_t_bar.dot(Ht.T).dot(np.linalg.inv(Ht.dot(sigma_t_bar).dot(Ht.T)+Qt))
        h_mu_t=env.observe(mu_t_bar,marker_id)
        mu_t=mu_t_bar+Kt.dot(minimized_angle(z-h_mu_t))
        sigma_t=(np.identity(3)-Kt.dot(Ht)).dot(sigma_t_bar)
        
        

        
        self.mu=mu_t
        self.sigma=sigma_t
        return self.mu, self.sigma
