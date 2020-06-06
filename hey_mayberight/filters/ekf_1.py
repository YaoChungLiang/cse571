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
        Gt=env.G(self.mu,u) #(3,3)
        Vt=env.V(self.mu,u)
        ######Mt=env.noise_from_motion(self.mu,self.alphas)
        Mt=env.noise_from_motion(u,self.alphas)
        #####x_,y_,theta_=env.forward(self.mu,u)
        mu_t_bar=env.forward(self.mu,u)
        '''
        self.all_x=all_x=[]
        self.all_x=all_y=[]
        all_x=all_x+self.mu[0]
        all_y=all_y+self.mu[1]
        Rt_x=np.std(all_x)**2
        Rt_y=np.std(all_y)**2
        '''
        ###########Rt=??? 
        Rt=np.dot(np.dot(Vt,Mt),np.transpose(Vt))
        #Qt=??? self.beta
        cov_t_bar=np.dot(np.dot(Gt,self.sigma),np.transpose(Gt))+Rt #(3,3)
        ########Ht=env.H(self.mu,marker_id) #(1,3)
        Ht=env.H(mu_t_bar,marker_id)
        
        #mu_t_bar=np.array([self.mu[0]+u[1]*np.cos(u[0]+self.mu[2]),
        #                   self.mu[1]+u[1]*np.sin(u[0]+self.mu[2]),
        #                   self.mu[2]+u[0]+u[2]                   ]) #(3,1)
        #print(mu_t_bar)
        #print(mu_t_bar.shape)
        '''
        mu_t_bar=np.array([self.mu[0]+u[1]*np.cos(u[0]+self.mu[2]),
                           self.mu[1]+u[1]*np.sin(u[0]+self.mu[2]),
                           self.mu[2]+u[0]+u[2]                   ])
        '''
        #mu_t_bar=np.transpose(mu_t_bar)
 
        


        #correction
        Q_t=self.beta
        #numpy.linalg.inv(x)
        K_t=np.dot(np.dot(cov_t_bar,np.transpose(Ht)),np.linalg.inv(np.dot(np.dot(Ht,cov_t_bar),np.transpose(Ht))+Q_t))
        # K_t  (3,1)
        #print(K_t.shape)
        #print(mu_t_bar_13) #3 by 1
        #a=np.dot(Ht,mu_t_bar) #(1,1)
        #print(Gt.shape)
        #b=np.dot(a,np.transpose(Ht))
        #print(np.transpose(Ht).shape)
        #############mu_t=mu_t_bar+K_t*(z-minimized_angle(np.arctan2(y_-self.mu[1],x_-self.mu[0])+u[2]))
        mu_t=mu_t_bar+K_t*(minimized_angle(z-env.observe(mu_t_bar,marker_id)))
        mu_t[2]=minimized_angle(mu_t[2])
        #I=np.array()
        cov_t=np.dot((np.identity(3)-np.dot(K_t,Ht)),cov_t_bar)
        self.mu=mu_t
        self.sigma=cov_t
        return self.mu, self.sigma
