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
        #self.mu[2]=self.mu[2]-10
        #print(self.mu) # state[[180],[150],[0]]
        #print(self.sigma)# covariance [[10 0 0],[0 10 0],[0 0 1]
        #print(self.beta) # [[0.0076154]]
        #print(self.alphas) #[2.5e-03 2.5e-05 1.0e-02 1.0e-04]
        #print(env) # Field
        #print(u) # action 1 by 3 [rot1,trans,rot2] [[0],[10],[0]]
        #print(z) #[-3.13~3.13]
        #print(marker_id) # 1 1 2 2 3 3 4 4 5 5 6 6
        #print(Gt=env.G([prex,prey,pretheta],[rot1,trans,rot2]))
        #print(Vt=env.V([prex,prey,pretheta],[rot1,trans,rot2]))
        #print(env.H)
        #print([x',y',theta']=env.forward(self.mu,u))
        #print(env.observe(self.mu,marker_id)) # phi [3.14~-3.14]
        
        #prediction
        # YOUR IMPLEMENTATION HERE
        Gt=env.G(self.mu,u)
        Vt=env.V(self.mu,u)
        Mt=env.noise_from_motion(u,self.alphas)  # why
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
