import numpy as np

from utils import minimized_angle, smul

# smul: do a series of successive matrix multiplication



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
        z: landmark observation  ??? this observation is from a totally 
        noised model without KF, how could we use this data?

        marker_id: landmark ID
        """
        # YOUR IMPLEMENTATION HERE
        Gt = env.G(self.mu, u)
        Vt = env.V(self.mu, u)
        Mt = env.noise_from_motion(u, self.alphas)

        Rt = smul([Vt, Mt, Vt.T]) # Motion error
        Qt = env.beta # Sensor error | it's a 1x1 cov matrix
        # step 1,2
        mu_bar = env.forward(self.mu, u)
        sigma_bar = smul([Gt, self.sigma, Gt.T]) + Rt
        Ht = env.H(mu_bar, marker_id) 
        # step 3
        tmp1 = smul([Ht, sigma_bar, Ht.T]) + Qt
        tmp2 = np.linalg.inv(tmp1)
        Kt = smul([sigma_bar, Ht.T, tmp2])
        # step 4
        z_bar = env.observe(mu_bar, marker_id)  ## why ?
        dz = z - z_bar
        mu = mu_bar + smul([Kt, dz])
        # step 5
        dim = Kt.shape[0]
        tmp3 = np.eye(dim, dim) - smul([Kt, Ht])
        sigma = smul([tmp3, sigma_bar])

        self.mu, self.sigma = mu, sigma
        return self.mu, self.sigma






