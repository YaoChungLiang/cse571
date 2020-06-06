import numpy as np

from utils import minimized_angle
import soccer_field as sf

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
        """ z=h

        """
        """Update the state estimate after taking an action and receiving a landmark
        observation.
        alphas = np.array([0.05**2, 0.005**2, 0.1**2, 0.01**2])   [2.5e-03 2.5e-05 1.0e-02 1.0e-04]
        beta = np.diag([np.deg2rad(5)**2])                        [[0.00761544]]

        env = Field(args.data_factor * alphas, args.data_factor * beta)
        policy = policies.OpenLoopRectanglePolicy()

        initial_mean = np.array([180, 50, 0]).reshape((-1, 1)) [[180]
                                                                [ 50]
                                                                [  0]]
        initial_cov = np.diag([10, 10, 1]) [[10  0  0]
                                            [ 0 10  0]
                                            [ 0  0  1]]
        u: action
        z: landmark observation
        marker_id: landmark ID
        
    
        """
        # self.mu = x y theta
        # 
        
        
        
        
        self.env=env
        self.u=u
        self.z=z
        self.marker_id=marker_id

        # YOUR IMPLEMENTATION HERE
        gt=sf.Field.G(self.mu,self.u)
        vt=sf.Field.V(self.mu,self.u)
        Ht=sf.Field.H(u,marker_id)
        Rt=
        
        
        
        return self.mu, self.sigma
