import numpy
import numpy as np
from RRTTree import RRTTree
import copy
from matplotlib import pyplot as plt
import math
import time
class RRTStarPlanner(object):
    
    def __init__(self, planning_env):
        self.planning_env = planning_env
        self.tree = RRTTree(self.planning_env)
        self.bias=0.2

    def Plan(self, start_config, goal_config, epsilon = 1):
        
###########  v9  works for step size ###################
        
        plan=[]
        start_config=list(start_config)
        plan.append(start_config)
        edge=dict()
        k=20
        last_point = start_config
        start_time = time.time()
        while last_point != goal_config:
            dist=[]
            k=20
            if np.random.rand()<0.2:
                x_rand = copy.deepcopy(goal_config)
                for j in range(len(plan)):
                    dist+=[self.planning_env.compute_distance(plan[j],x_rand)]               
                min_idx = dist.index(min(dist))
                x_nearest=plan[min_idx]
                
                vec=[x_rand[0]-x_nearest[0],x_rand[1]-x_nearest[1]]
                len_vec=np.sqrt(vec[0]**2+vec[1]**2)
                x_vec=vec[0]/len_vec*epsilon
                y_vec=vec[1]/len_vec*epsilon
                x_new=[x_nearest[0]+x_vec,x_nearest[1]+y_vec]
                if self.planning_env.RRT_state_validity_checker(x_new) and \
                self.planning_env.RRT_state_validity_checker(x_nearest) and \
                self.planning_env.collision_free(x_new,x_nearest):
                    k= min(k,len(plan)-1)
                    knnIDs , Xnear =self.tree.RRTstargetKNN(plan,x_new,k)
                    plan.append(x_new)
                    x_min=copy.deepcopy(x_nearest)
                    c_min=self.planning_env.compute_distance(x_nearest,start_config)+self.planning_env.compute_distance(x_nearest,x_new)
                    for x_near in Xnear :        
                        if self.planning_env.collision_free(x_near,x_new) and \
                            (self.planning_env.compute_distance(x_near,start_config)+ \
                             self.planning_env.compute_distance(x_near,x_new))<c_min :
                            x_min=x_near
                            c_min=self.planning_env.compute_distance(x_near,start_config)+ \
                            self.planning_env.compute_distance(x_near,x_new)
                    if self.planning_env.collision_free(plan[len(plan)-1],plan[plan.index(x_min)]):
                        edge[len(plan)-1]=plan.index(x_min)
                    else:
                        plan.pop()
                        continue
                    for x_near in Xnear:
                        if self.planning_env.collision_free(x_near,x_new) and \
                        (self.planning_env.compute_distance(x_near,start_config)+ \
                         self.planning_env.compute_distance(x_near,x_new))< \
                         self.planning_env.compute_distance(x_near,start_config):
                             edge[plan.index(x_near)]=len(plan)-1
                             #edge[len(plan)-1]=plan.index(x_near)
                    last_point= x_new
                if self.planning_env.compute_distance(last_point,goal_config) < 2:
                    last_point=plan[len(plan)-1]
                    break
                last_point=plan[len(plan)-1]
            else:
                k=20
                rand_x= np.random.rand()*(self.planning_env.xlimit[1]-self.planning_env.xlimit[0])+self.planning_env.xlimit[0]
                rand_y= np.random.rand()*(self.planning_env.ylimit[1]-self.planning_env.ylimit[0])+self.planning_env.ylimit[0]
                x_rand = [rand_x,rand_y]
                for j in range(len(plan)):
                    dist+=[self.planning_env.compute_distance(plan[j],x_rand)]               
                min_idx = dist.index(min(dist))
                x_nearest=plan[min_idx]
                
                vec=[x_rand[0]-x_nearest[0],x_rand[1]-x_nearest[1]]
                len_vec=np.sqrt(vec[0]**2+vec[1]**2)
                x_vec=vec[0]/len_vec*epsilon
                y_vec=vec[1]/len_vec*epsilon
                x_new=[x_nearest[0]+x_vec,x_nearest[1]+y_vec]
                if self.planning_env.RRT_state_validity_checker(x_new) and \
                self.planning_env.RRT_state_validity_checker(x_nearest)and \
                self.planning_env.collision_free(x_new,x_nearest):
                    k= min(k,len(plan)-1)
                    knnIDs , Xnear =self.tree.RRTstargetKNN(plan,x_new,k)
                    plan.append(x_new)
                    x_min=copy.deepcopy(x_nearest)
                    c_min=self.planning_env.compute_distance(x_nearest,start_config)+self.planning_env.compute_distance(x_nearest,x_new)
                    for x_near in Xnear :
                        if self.planning_env.RRT_state_validity_checker(x_near) and \
                            self.planning_env.RRT_state_validity_checker(x_new) and \
                            (self.planning_env.compute_distance(x_near,start_config)+ \
                             self.planning_env.compute_distance(x_near,x_new))<c_min:
                            x_min=x_near
                            c_min=self.planning_env.compute_distance(x_near,start_config)+ \
                            self.planning_env.compute_distance(x_near,x_new)
                    if self.planning_env.collision_free(plan[len(plan)-1],plan[plan.index(x_min)]):
                        edge[len(plan)-1]=plan.index(x_min)
                    else:
                        plan.pop()
                        continue
                    for x_near in Xnear:
                        if self.planning_env.RRT_state_validity_checker(x_near) and \
                        self.planning_env.RRT_state_validity_checker(x_new) and \
                        (self.planning_env.compute_distance(x_near,start_config)+ \
                         self.planning_env.compute_distance(x_near,x_new))< \
                         self.planning_env.compute_distance(x_near,start_config):
                             edge[plan.index(x_near)]=len(plan)-1
                             #edge[len(plan)-1]=plan.index(x_near)
                    last_point=x_new
                if self.planning_env.compute_distance(last_point,goal_config) < 2:
                    last_point=plan[len(plan)-1]
                    break
                last_point=plan[len(plan)-1] 
        total_time = time.time()-start_time
        print("total_time(s) =",total_time)       
        traverse_path=[]
        last_index = plan.index(last_point)
        while last_index!=0:
            traverse_path.append(plan[last_index])
            last_index=edge[last_index]
        traverse_path.append(start_config)    
        og_cost = self.cal_cost(traverse_path)
        
        original_tree = []
        for child,father in edge.items():
            original_tree.append(plan[father])
            original_tree.append(plan[child])
        plan = traverse_path
        
        plt.imshow(self.planning_env.map, interpolation='nearest')
        for i in range(((numpy.shape(original_tree)[0])//2)-1):
            j=2*i
            x = [original_tree[j][0], original_tree[j+1][0]]
            y = [original_tree[j][1], original_tree[j+1][ 1]]
            plt.plot(y, x, 'g')
        plt.title('p={}, reach to sample point '.format(self.bias))
        plt.xlabel('time = {:.1f} (s),original cost={:.2f}'.format(total_time,og_cost))  
##########   v8  works for go to point directly ############################
#        
#        plan=[]
#        start_config=list(start_config)
#        plan.append(start_config)
#        edge=dict()
#        k=10
#        last_point = start_config
#        start_time = time.time()
#        while last_point != goal_config:
#            dist=[]
#            k=10
#            if np.random.rand()<0.2:
#                x_rand = copy.deepcopy(goal_config)
#                for j in range(len(plan)):
#                    dist+=[self.planning_env.compute_distance(plan[j],x_rand)]               
#                min_idx = dist.index(min(dist))
#                x_nearest=plan[min_idx]
#                
##                vec=[x_rand[0]-x_nearest[0],x_rand[1]-x_nearest[1]]
##                len_vec=np.sqrt(vec[0]**2+vec[1]**2)
##                x_vec=vec[0]/len_vec*epsilon
##                y_vec=vec[1]/len_vec*epsilon
#                x_new=x_rand
#                if self.planning_env.RRT_state_validity_checker(x_new) and \
#                self.planning_env.RRT_state_validity_checker(x_nearest) and \
#                self.planning_env.collision_free(x_new,x_nearest):
#                    k= min(k,len(plan)-1)
#                    knnIDs , Xnear =self.tree.RRTstargetKNN(plan,x_new,k)
#                    plan.append(x_new)
#                    x_min=copy.deepcopy(x_nearest)
#                    c_min=self.planning_env.compute_distance(x_nearest,start_config)+self.planning_env.compute_distance(x_nearest,x_new)
#                    for x_near in Xnear :        
#                        if self.planning_env.collision_free(x_near,x_new) and \
#                            (self.planning_env.compute_distance(x_near,start_config)+ \
#                             self.planning_env.compute_distance(x_near,x_new))<c_min :
#                            x_min=x_near
#                            c_min=self.planning_env.compute_distance(x_near,start_config)+ \
#                            self.planning_env.compute_distance(x_near,x_new)
#                    if self.planning_env.collision_free(plan[len(plan)-1],plan[plan.index(x_min)]):
#                        edge[len(plan)-1]=plan.index(x_min)
#                    else:
#                        plan.pop()
#                        continue
#                    for x_near in Xnear:
#                        if self.planning_env.collision_free(x_near,x_new) and \
#                        (self.planning_env.compute_distance(x_near,start_config)+ \
#                         self.planning_env.compute_distance(x_near,x_new))< \
#                         self.planning_env.compute_distance(x_near,start_config):
#                             edge[plan.index(x_near)]=len(plan)-1
#                             #edge[len(plan)-1]=plan.index(x_near)
#                    last_point= x_new
#                if self.planning_env.compute_distance(last_point,goal_config) < 2:
#                    last_point=plan[len(plan)-1]
#                    break
#                last_point=plan[len(plan)-1]
#            else:
#                k=10
#                rand_x= np.random.rand()*(self.planning_env.xlimit[1]-self.planning_env.xlimit[0])+self.planning_env.xlimit[0]
#                rand_y= np.random.rand()*(self.planning_env.ylimit[1]-self.planning_env.ylimit[0])+self.planning_env.ylimit[0]
#                x_rand = [rand_x,rand_y]
#                for j in range(len(plan)):
#                    dist+=[self.planning_env.compute_distance(plan[j],x_rand)]               
#                min_idx = dist.index(min(dist))
#                x_nearest=plan[min_idx]
#                
##                vec=[x_rand[0]-x_nearest[0],x_rand[1]-x_nearest[1]]
##                len_vec=np.sqrt(vec[0]**2+vec[1]**2)
##                x_vec=vec[0]/len_vec*epsilon
##                y_vec=vec[1]/len_vec*epsilon
#                x_new=x_rand
#                if self.planning_env.RRT_state_validity_checker(x_new) and \
#                self.planning_env.RRT_state_validity_checker(x_nearest)and \
#                self.planning_env.collision_free(x_new,x_nearest):
#                    k= min(k,len(plan)-1)
#                    knnIDs , Xnear =self.tree.RRTstargetKNN(plan,x_new,k)
#                    plan.append(x_new)
#                    x_min=copy.deepcopy(x_nearest)
#                    c_min=self.planning_env.compute_distance(x_nearest,start_config)+self.planning_env.compute_distance(x_nearest,x_new)
#                    for x_near in Xnear :
#                        if self.planning_env.RRT_state_validity_checker(x_near) and \
#                            self.planning_env.RRT_state_validity_checker(x_new) and \
#                            (self.planning_env.compute_distance(x_near,start_config)+ \
#                             self.planning_env.compute_distance(x_near,x_new))<c_min:
#                            x_min=x_near
#                            c_min=self.planning_env.compute_distance(x_near,start_config)+ \
#                            self.planning_env.compute_distance(x_near,x_new)
#                    if self.planning_env.collision_free(plan[len(plan)-1],plan[plan.index(x_min)]):
#                        edge[len(plan)-1]=plan.index(x_min)
#                    else:
#                        plan.pop()
#                        continue
#                    for x_near in Xnear:
#                        if self.planning_env.RRT_state_validity_checker(x_near) and \
#                        self.planning_env.RRT_state_validity_checker(x_new) and \
#                        (self.planning_env.compute_distance(x_near,start_config)+ \
#                         self.planning_env.compute_distance(x_near,x_new))< \
#                         self.planning_env.compute_distance(x_near,start_config):
#                             edge[plan.index(x_near)]=len(plan)-1
#                             #edge[len(plan)-1]=plan.index(x_near)
#                    last_point=x_new
#                if self.planning_env.compute_distance(last_point,goal_config) < 2:
#                    last_point=plan[len(plan)-1]
#                    break
#                last_point=plan[len(plan)-1] 
#        total_time = time.time()-start_time
#        print("total_time(s) =",total_time)       
#        traverse_path=[]
#        last_index = plan.index(last_point)
#        while last_index!=0:
#            traverse_path.append(plan[last_index])
#            last_index=edge[last_index]
#        traverse_path.append(start_config)    
#        og_cost = self.cal_cost(traverse_path)
#        
#        original_tree = []
#        for child,father in edge.items():
#            original_tree.append(plan[father])
#            original_tree.append(plan[child])
#        plan = traverse_path
#        
#        plt.imshow(self.planning_env.map, interpolation='nearest')
#        for i in range(((numpy.shape(original_tree)[0])//2)-1):
#            j=2*i
#            x = [original_tree[j][0], original_tree[j+1][0]]
#            y = [original_tree[j][1], original_tree[j+1][ 1]]
#            plt.plot(y, x, 'g')
#        plt.title('p={}, reach to sample point '.format(self.bias))
#        plt.xlabel('time = {:.1f} (s),original cost={:.2f}'.format(total_time,og_cost))    

        return numpy.array(plan)

        
    def cal_cost(self,path):
        cost=0
        for i in range(len(path)-1):
            cost+=np.sqrt((path[i][0]-path[i+1][0])**2+(path[i][1]-path[i+1][1])**2)
        return cost 

    def extend(self):
        # TODO (student): Implement an extend logic.
        pass

    def ShortenPath(self, path):
        # TODO (student): Postprocessing of the plan.
        return path
