import numpy
import numpy as np
from RRTTree import RRTTree
from matplotlib import pyplot as plt
import copy
import operator
import time

class RRTPlanner(object):

    def __init__(self, planning_env):
        self.planning_env = planning_env
        self.tree = RRTTree(self.planning_env)
        self.bias = 0.05

    def Plan(self, start_config, goal_config, epsilon = 1):
################   v6  reach to sampled  #######################
        plan=[]
        plan.append(list(start_config))
        edge=dict()
        dist=[]
        start_config=list(start_config)
        goal_config=list(goal_config)
        next_point = None
        last_point=start_config
        start_time = time.time()
        while last_point != goal_config:
            dist=[]
            if numpy.random.rand()< self.bias:
                candidate_next_point=copy.deepcopy(goal_config)
                for j in range(len(plan)):
                    dist+=[self.planning_env.compute_distance(plan[j],candidate_next_point)]
                min_idx, min_dist=min(enumerate(dist), key=operator.itemgetter(1) )
                len_candidate_next_point=dist[min_idx]
                x_vec=candidate_next_point[0]-plan[min_idx][0]
                y_vec=candidate_next_point[1]-plan[min_idx][1]

                next_point=[plan[min_idx][0]+x_vec,plan[min_idx][1]+y_vec]

                if self.planning_env.RRT_state_validity_checker(next_point) \
                and (self.planning_env.collision_free([plan[min_idx][0],plan[min_idx][1]],next_point)):
                    
                    edge[len(plan)]=min_idx
                    plan.append(next_point)
                    last_point = copy.deepcopy( next_point)
                    if self.planning_env.compute_distance(last_point,goal_config) < 2:
                        break
                else:
                    last_point = plan[len(plan)-1]
            else:
                rand_x= np.random.rand()*(self.planning_env.xlimit[1]-self.planning_env.xlimit[0])+self.planning_env.xlimit[0]
                rand_y= np.random.rand()*(self.planning_env.ylimit[1]-self.planning_env.ylimit[0])+self.planning_env.ylimit[0]
                
                candidate_next_point = [rand_x,rand_y]
                for j in range(len(plan)):
                    dist+=[self.planning_env.compute_distance(plan[j],candidate_next_point)]
                min_idx, min_dist=min(enumerate(dist), key=operator.itemgetter(1))       
                
                #len_candidate_next_point=dist[min_idx]
                
                x_vec=candidate_next_point[0]-plan[min_idx][0]
                y_vec=candidate_next_point[1]-plan[min_idx][1]

                next_point=[plan[min_idx][0]+x_vec,plan[min_idx][1]+y_vec]

                if self.planning_env.RRT_state_validity_checker(next_point) \
                and (self.planning_env.collision_free([plan[min_idx][0],plan[min_idx][1]],next_point)):
                    edge[len(plan)]=min_idx
                    plan.append(next_point)
                    last_point = copy.deepcopy( next_point)
                    if self.planning_env.compute_distance(last_point,goal_config) < 2:
                        break         
                else:
                    last_point= plan[len(plan)-1]
        total_time = time.time()-start_time
        print("total_time(s) =",total_time)
        traverse_path=[]
        last_index = len(plan)-1
        while last_index!=0:
            traverse_path.append(plan[last_index])
            last_index=edge[last_index]
        traverse_path.append(start_config)
############# original cost   ###############
        og_cost = self.cal_cost(traverse_path)
        

###########  shorten path #####################
        rev_trav_path = traverse_path[::-1]
        
        node = 0
        tmp_path = [rev_trav_path[0]]
        for i in range(1,len(rev_trav_path)):
            if not self.planning_env.collision_free(rev_trav_path[node],rev_trav_path[i]):
                tmp_path.append(rev_trav_path[i-1])
                node = i-1
        tmp_path.append(rev_trav_path[len(rev_trav_path)-1])
        shortened_cost = self.cal_cost(tmp_path)
        
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
        plt.title('p={}, reach to sample point'.format(self.bias))
        plt.xlabel('time = {:.1f} (s),original cost={:.2f},shortened cost ={:.1f}'.format(total_time,og_cost,shortened_cost))
        return numpy.array(tmp_path)
###################### ver 5 add color + step size = 1####################################
#        plan=[]
#        plan.append(list(start_config))
#        edge=dict()
#        dist=[]
#        start_config=list(start_config)
#        goal_config=list(goal_config)
#        next_point = None
#        last_point=start_config
#        start_time = time.time()
#        while last_point != goal_config:
#            dist=[]
#            if numpy.random.rand()< self.bias:
#                candidate_next_point=copy.deepcopy(goal_config)
#                for j in range(len(plan)):
#                    dist+=[self.planning_env.compute_distance(plan[j],candidate_next_point)]
#                min_idx, min_dist=min(enumerate(dist), key=operator.itemgetter(1) )
#                len_candidate_next_point=dist[min_idx]
#                x_vec=candidate_next_point[0]-plan[min_idx][0]
#                y_vec=candidate_next_point[1]-plan[min_idx][1]
#                x_unit_vec=x_vec/len_candidate_next_point*epsilon
#                y_unit_vec=y_vec/len_candidate_next_point*epsilon
#
#                next_point=[plan[min_idx][0]+x_unit_vec,plan[min_idx][1]+y_unit_vec]
#
#                if self.planning_env.RRT_state_validity_checker(next_point):
#                    
#                    edge[len(plan)]=min_idx
#                    plan.append(next_point)
#                    last_point = copy.deepcopy( next_point)
#                    if self.planning_env.compute_distance(last_point,goal_config) < 2:
#                        break
#                else:
#                    last_point = plan[len(plan)-1]
#            else:
#                rand_x= np.random.rand()*(self.planning_env.xlimit[1]-self.planning_env.xlimit[0])+self.planning_env.xlimit[0]
#                rand_y= np.random.rand()*(self.planning_env.ylimit[1]-self.planning_env.ylimit[0])+self.planning_env.ylimit[0]
#                
#                candidate_next_point = [rand_x,rand_y]
#                for j in range(len(plan)):
#                    dist+=[self.planning_env.compute_distance(plan[j],candidate_next_point)]
#                min_idx, min_dist=min(enumerate(dist), key=operator.itemgetter(1))       
#                
#                len_candidate_next_point=dist[min_idx]
#                
#                x_vec=candidate_next_point[0]-plan[min_idx][0]
#                y_vec=candidate_next_point[1]-plan[min_idx][1]
#                x_unit_vec=x_vec/len_candidate_next_point*epsilon
#                y_unit_vec=y_vec/len_candidate_next_point*epsilon
#
#                next_point=[plan[min_idx][0]+x_unit_vec,plan[min_idx][1]+y_unit_vec]
#
#                if self.planning_env.RRT_state_validity_checker(next_point):
#                    edge[len(plan)]=min_idx
#                    plan.append(next_point)
#                    last_point = copy.deepcopy( next_point)
#                    if self.planning_env.compute_distance(last_point,goal_config) < 2:
#                        break         
#                else:
#                    last_point= plan[len(plan)-1]
#        total_time = time.time()-start_time
#        print("total_time(s) =",total_time)
#        traverse_path=[]
#        last_index = len(plan)-1
#        while last_index!=0:
#            traverse_path.append(plan[last_index])
#            last_index=edge[last_index]
#        traverse_path.append(start_config)

#        og_cost = self.cal_cost(traverse_path)
#        
#
#        rev_trav_path = traverse_path[::-1]
#        #print(rev_trav_path)
#        
#        node = 0
#        tmp_path = [rev_trav_path[0]]
#        for i in range(1,len(rev_trav_path)):
#            if not self.planning_env.collision_free(rev_trav_path[node],rev_trav_path[i]):
#                tmp_path.append(rev_trav_path[i-1])
#                node = i-1
#        tmp_path.append(rev_trav_path[len(rev_trav_path)-1])
#        #plan = tmp_path
#        shortened_cost = self.cal_cost(tmp_path)

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
#        plt.title('p={}, {} step size'.format(self.bias,epsilon))
#        plt.xlabel('time = {:.1f} (s),original cost={:.2f},shortened cost ={:.1f}'.format(total_time,og_cost,shortened_cost))
#        return numpy.array(tmp_path)
#############################################################################################
    def extend(self,start,end):
        # TODO (student): Implement an extend logic.
        pass
    def ShortenPath(self, path):
        # TODO (student): Postprocessing of the plan.
        pass
    
    def cal_cost(self,path):
        cost=0
        for i in range(len(path)-1):
            cost+=np.sqrt((path[i][0]-path[i+1][0])**2+(path[i][1]-path[i+1][1])**2)
        return cost 