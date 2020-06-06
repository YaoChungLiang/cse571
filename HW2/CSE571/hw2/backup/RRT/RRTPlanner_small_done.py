import numpy
import numpy as np
from RRTTree import RRTTree
from matplotlib import pyplot as plt
import copy

class RRTPlanner(object):

    def __init__(self, planning_env):
        self.planning_env = planning_env
        self.tree = RRTTree(self.planning_env)
        

    def Plan(self, start_config, goal_config, epsilon = 0.001):
        
        
################### ver 3 ##########################################
        plan=[]
        plan.append(start_config)
        edge=dict()
        dist=[]
        start_config=list(start_config)
        goal_config=list(goal_config)
        next_point = None
        last_point=start_config
        while last_point != goal_config:
            #print(plan[len(plan)-1])
            dist=[]
            if numpy.random.rand()<0.05:
                candidate_next_point=copy.deepcopy(goal_config)
                for j in range(len(plan)):
                    dist+=[self.planning_env.compute_distance(plan[j],candidate_next_point)]
                min_idx = dist.index(min(dist))
                len_candidate_next_point=dist[min_idx]
                x_vec=candidate_next_point[0]-plan[min_idx][0]
                y_vec=candidate_next_point[1]-plan[min_idx][1]
                x_unit_vec=x_vec/len_candidate_next_point

                y_unit_vec=y_vec/len_candidate_next_point

                next_point=[plan[min_idx][0]+x_unit_vec,plan[min_idx][1]+y_unit_vec]

                if self.planning_env.RRT_state_validity_checker(next_point):
                    
                    edge[len(plan)]=min_idx
                    plan.append(next_point)
                    last_point = copy.deepcopy( next_point)
                    if self.planning_env.compute_distance(last_point,goal_config) < 1:
                        break
                else:
                    last_point = plan[len(plan)-1]
            else:
                rand_x= np.random.rand()*8
                rand_y= np.random.rand()*8
                candidate_next_point = [rand_x,rand_y]
                for j in range(len(plan)):
                    dist+=[self.planning_env.compute_distance(plan[j],candidate_next_point)]
                min_idx = dist.index(min(dist))        
                
                len_candidate_next_point=dist[min_idx]
                
                x_vec=candidate_next_point[0]-plan[min_idx][0]
                y_vec=candidate_next_point[1]-plan[min_idx][1]
                x_unit_vec=x_vec/len_candidate_next_point
                y_unit_vec=y_vec/len_candidate_next_point

                next_point=[plan[min_idx][0]+x_unit_vec,plan[min_idx][1]+y_unit_vec]

                if self.planning_env.RRT_state_validity_checker(next_point):
                    edge[len(plan)]=min_idx
                    plan.append(next_point)
                    last_point = copy.deepcopy( next_point)
                    if self.planning_env.compute_distance(last_point,goal_config) < 1:
                        break         
                else:
                    last_point= plan[len(plan)-1]
        traverse_path=[]
        last_index = len(plan)-1
        while last_index!=0:
            traverse_path.append(plan[last_index])
            last_index=edge[last_index]
        traverse_path.append(start_config)
        plan = traverse_path
                #                 print('min_idx')
#                print(min_idx)
#                print("dist")
#                print(dist)
                #next_point = copy.deepcopy(candidate_next_point)
#            else:
#                rand_x = np.random.random_sample()*8
#                rand_y = np.random.random_sample()*8
#                next_point = [rand_x,rand_y]
#            print("next point")
#            print(next_point)
        #plan=[[3,3]]
        #print(plan)
#################  ver 2 ##########################################33
        # Initialize an empty plan.
#        plan = []
#        dist=[]
#        edge=dict()
#        start_config=list(start_config)
#        goal_config=list(goal_config)
#        plan.append(start_config)
#        last_config = None
#        next_point = None
#        while last_config != goal_config:
#            print(plan[len(plan)-1])
#            if numpy.random.rand()<0.05:
#                dist=[]
#                next_point = copy.deepcopy(goal_config)
#                for j in range(len(plan)):
#                    dist=dist+[self.planning_env.compute_distance(plan[j],next_point)]
#                    
#                min_idx = dist.index(min(dist))
#                    
#                x_vec= next_point[0]-plan[(min_idx)][0]
#                y_vec= next_point[1]-plan[(min_idx)][1]
#                len_vec=np.sqrt(x_vec**2+y_vec**2)
#                x_vec=x_vec/len_vec
#                y_vec=y_vec/len_vec
#                candidate_next_point=[plan[min_idx][0]+x_vec,plan[min_idx][1]+y_vec]
#                if self.planning_env.state_validity_checker(candidate_next_point) :
#                    last_config = candidate_next_point
#                    plan.append(candidate_next_point)
#                    edge[len(plan)-1]=min_idx
#            else:
#                dist=[]
#                rand_x = np.random.random_sample()*450
#                rand_y = np.random.random_sample()*450
#                next_point = ([rand_x,rand_y])
#                for j in range(len(plan)):
#                    dist=dist+[self.planning_env.compute_distance(plan[j],next_point)]
#                min_idx = dist.index(min(dist))
#                x_vec= next_point[0]-plan[(min_idx)][0]
#                y_vec= next_point[1]-plan[(min_idx)][1]
#                len_vec=np.sqrt(x_vec**2+y_vec**2)
#                x_vec=x_vec/len_vec
#                y_vec=y_vec/len_vec
#                candidate_next_point=[plan[min_idx][0]+x_vec,plan[min_idx][1]+y_vec]
#                if self.planning_env.state_validity_checker(candidate_next_point) :
#                    last_config = candidate_next_point
#                    plan.append(candidate_next_point)
#                    edge[len(plan)-1]=min_idx                    
#        last_index = len(plan)-1
#        father_index= None
#        traverse_path=[goal_config]
#        while father_index !=0:
#            father_index = edge[last_index]
#            traverse_path.append(plan[father_index])
#            last_index=father_index
#        traverse_path.append(plan[0])
#        plan=traverse_path

##############   ver 1 #######################################################
#        plan = []
#        dist=[]
#        edge=dict()
#        start_config=list(start_config)
#        goal_config=list(goal_config)
#        plan.append(start_config)
#        last_config = None
#        next_point = None
#        while last_config != goal_config:
#            print(plan[len(plan)-1])
#            if numpy.random.rand() < 0.01:
#                dist=[]
#                last_config  =copy.deepcopy( goal_config)
#                next_point= copy.deepcopy (goal_config)
#                
#                if len(plan)>5:
#                    
#                    for j in range(len(plan)-5,len(plan)):
#                        dist=dist+[self.planning_env.compute_distance(plan[j],next_point)]
#                        min_idx = dist.index(min(dist))
#                    min_idx=len(plan)-5+min_idx
#                    x_vec= next_point[0]-plan[(min_idx)][0]
#                    y_vec= next_point[1]-plan[(min_idx)][1]
#                    len_vec=np.sqrt(x_vec**2+y_vec**2)
#                    x_vec=x_vec/len_vec
#                    y_vec=y_vec/len_vec
#                    candidate_next_point=[plan[min_idx][0]+x_vec,plan[min_idx][1]+y_vec]
#                    if self.planning_env.state_validity_checker(candidate_next_point) :
#                        last_config=candidate_next_point
#                        plan.append(candidate_next_point)
#                        edge[len(plan)-1]=min_idx
#                        if self.planning_env.compute_distance(candidate_next_point,goal_config)<1:
#                            break
#                else:
#                    for j in range(len(plan)):
#                        dist=dist+[self.planning_env.compute_distance(plan[j],next_point)]
#                        min_idx = dist.index(min(dist))
#                    x_vec= next_point[0]-plan[(min_idx)][0]
#                    y_vec= next_point[1]-plan[(min_idx)][1]
#                    len_vec=np.sqrt(x_vec**2+y_vec**2)
#                    x_vec=x_vec/len_vec
#                    y_vec=y_vec/len_vec
#                    candidate_next_point=[plan[min_idx][0]+x_vec,plan[min_idx][1]+y_vec]
#                    if self.planning_env.state_validity_checker(candidate_next_point) :
#                        last_config=candidate_next_point
#                        plan.append(candidate_next_point)
#                        edge[len(plan)-1]=min_idx       
#                        if self.planning_env.compute_distance(candidate_next_point,goal_config)<1:
#                            break
#            else:
#                dist=[]
#                last_config  =copy.deepcopy( goal_config)
#                next_point= copy.deepcopy (goal_config)
#                rand_x = np.random.random_sample()*8
#                rand_y = np.random.random_sample()*8
#                next_point = ([rand_x,rand_y])
#                if self.planning_env.state_validity_checker(next_point) :
#
#                    if len(plan)>5:
#                        for j in range(len(plan)-5,len(plan)):
#                            dist=dist+[self.planning_env.compute_distance(plan[j],next_point)]
#                            min_idx = dist.index(min(dist))
#                        min_idx=len(plan)-5+min_idx
#                        x_vec= next_point[0]-plan[min_idx][0]
#                        y_vec= next_point[1]-plan[min_idx][1]
#                        len_vec=np.sqrt(x_vec**2+y_vec**2)
#                        x_vec=x_vec/len_vec
#                        y_vec=y_vec/len_vec
#                        candidate_next_point=[plan[min_idx][0]+x_vec,plan[min_idx][1]+y_vec]
#                        if self.planning_env.state_validity_checker(candidate_next_point) :
#                            last_config=candidate_next_point
#                            plan.append(candidate_next_point)
#                            edge[len(plan)-1]=min_idx
#                            if self.planning_env.compute_distance(candidate_next_point,goal_config)<1:
#                               break
#                    else:
#                        for j in range(len(plan)):
#                            dist=dist+[self.planning_env.compute_distance(plan[j],next_point)]
#                            min_idx = dist.index(min(dist))
#                        x_vec= next_point[0]-plan[min_idx][0]
#                        y_vec= next_point[1]-plan[min_idx][1]
#                        len_vec=np.sqrt(x_vec**2+y_vec**2)
#                        x_vec=x_vec/len_vec
#                        y_vec=y_vec/len_vec
#                        candidate_next_point=[plan[min_idx][0]+x_vec,plan[min_idx][1]+y_vec]
#                        if self.planning_env.state_validity_checker(candidate_next_point) :
#                            last_config=candidate_next_point
#                            plan.append(candidate_next_point)
#                            edge[len(plan)-1]=min_idx
#                            if self.planning_env.compute_distance(candidate_next_point,goal_config)<3:
#                                break
#
#        new_plan=[goal_config]
#        last_index=len(plan)-1
#        while last_index != 0:
#            last_index=edge[last_index]
#            new_plan.append(plan[last_index])
#        plan=new_plan
        
#############################################################################3
                #plan.append(next_point)
                #edge.setdefault(min_idx,[]).append(len(plan)-1)
                #edge[len(plan)-1]=min_idx
                #edge[min_idx]=len(plan)
                #print('j')
                #print(j)
        
        #print('edge')
        #print(edge)
                    
        #plan.append(last_config)
        return numpy.array(plan)


    def extend(self,start,end):
        # TODO (student): Implement an extend logic.
        
        
            
        pass
    def ShortenPath(self, path):
        # TODO (student): Postprocessing of the plan.
        return path
