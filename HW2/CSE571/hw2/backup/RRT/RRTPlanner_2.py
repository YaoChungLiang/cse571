import numpy
import numpy as np
from RRTTree import RRTTree
from matplotlib import pyplot as plt


class RRTPlanner(object):

    def __init__(self, planning_env):
        self.planning_env = planning_env
        self.tree = RRTTree(self.planning_env)
        

    def Plan(self, start_config, goal_config, epsilon = 0.001):
        
        # Initialize an empty plan.
        plan = []
        nodes=[]
        nodes_knear=[]
        dist=[]
        edge=dict()
        start_config=list(start_config)
        goal_config=list(goal_config)
        plan.append(start_config)
        last_config = None
#        while last_config != goal_config:
#            if numpy.random.rand() < 0.02:
#                last_config  = goal_config
#            else:
#                rand_x = numpy.random.randint(1,500)
#                rand_y = numpy.random.randint(1,500)
#                last_config = [rand_x,rand_y]
#                plan.append(last_config)
#                if self.planning_env.state_validity_checker(last_config) :
#                    # find nearest point from tree
#                    
#                    # if no obstacle between next point and 
#                    path=[]
                    
                        # add the the vertex to tree
                        
                        # add the edge
                         # self.tree.
        while last_config != goal_config:
            print(plan[len(plan)-1])
            if numpy.random.rand() < 0.1:
                dist=[]
                last_config  = goal_config
                next_point=last_config
                
                if len(plan)>5:
                    
                    for j in range(len(plan)-5,len(plan)):
                        dist=dist+[self.planning_env.compute_distance(plan[j],next_point)]
                        min_idx = dist.index(min(dist))
                    min_idx=len(plan)-5+min_idx
                    x_vec= next_point[0]-plan[(min_idx)][0]
                    y_vec= next_point[1]-plan[(min_idx)][1]
                    len_vec=np.sqrt(x_vec**2+y_vec**2)
                    x_vec=x_vec/len_vec
                    y_vec=y_vec/len_vec
                    candidate_next_point=[plan[min_idx][0]+x_vec,plan[min_idx][1]+y_vec]
                    if self.planning_env.state_validity_checker(candidate_next_point) :
                        last_config=candidate_next_point
                        plan.append(candidate_next_point)
                        edge[len(plan)-1]=min_idx
                        if self.planning_env.compute_distance(candidate_next_point,goal_config)<3:
                            break
                else:
                    for j in range(len(plan)):
                        dist=dist+[self.planning_env.compute_distance(plan[j],next_point)]
                        min_idx = dist.index(min(dist))
                    x_vec= next_point[0]-plan[(min_idx)][0]
                    y_vec= next_point[1]-plan[(min_idx)][1]
                    len_vec=np.sqrt(x_vec**2+y_vec**2)
                    x_vec=x_vec/len_vec*5
                    y_vec=y_vec/len_vec*5
                    candidate_next_point=[plan[min_idx][0]+x_vec,plan[min_idx][1]+y_vec]
                    if self.planning_env.state_validity_checker(candidate_next_point) :
                        last_config=candidate_next_point
                        plan.append(candidate_next_point)
                        edge[len(plan)-1]=min_idx       
                        if self.planning_env.compute_distance(candidate_next_point,goal_config)<3:
                            break
            else:
                dist=[]
                rand_x = np.random.random_sample()*450
                rand_y = np.random.random_sample()*450
                next_point = ([rand_x,rand_y])
                if self.planning_env.state_validity_checker(next_point) :
                    #plan.append(next_point)
                    #print('plan')
                    #print(plan)
                    if len(plan)>5:
                        for j in range(len(plan)-5,len(plan)):
                            dist=dist+[self.planning_env.compute_distance(plan[j],next_point)]
                            min_idx = dist.index(min(dist))
                        min_idx=len(plan)-5+min_idx
                        x_vec= next_point[0]-plan[min_idx][0]
                        y_vec= next_point[1]-plan[min_idx][1]
                        len_vec=np.sqrt(x_vec**2+y_vec**2)
                        x_vec=x_vec/len_vec
                        y_vec=y_vec/len_vec
                        candidate_next_point=[plan[min_idx][0]+x_vec,plan[min_idx][1]+y_vec]
                        if self.planning_env.state_validity_checker(candidate_next_point) :
                            last_config=candidate_next_point
                            plan.append(candidate_next_point)
                            edge[len(plan)-1]=min_idx
                            if self.planning_env.compute_distance(candidate_next_point,goal_config)<3:
                                break
                    else:
                        for j in range(len(plan)):
                            dist=dist+[self.planning_env.compute_distance(plan[j],next_point)]
                            min_idx = dist.index(min(dist))
                        x_vec= next_point[0]-plan[min_idx][0]
                        y_vec= next_point[1]-plan[min_idx][1]
                        len_vec=np.sqrt(x_vec**2+y_vec**2)
                        x_vec=x_vec/len_vec*5
                        y_vec=y_vec/len_vec*5
                        candidate_next_point=[plan[min_idx][0]+x_vec,plan[min_idx][1]+y_vec]
                        if self.planning_env.state_validity_checker(candidate_next_point) :
                            last_config=candidate_next_point
                            plan.append(candidate_next_point)
                            edge[len(plan)-1]=min_idx
                            if self.planning_env.compute_distance(candidate_next_point,goal_config)<3:
                                break
        new_plan=[goal_config]
        last_index=len(plan)-1
        while last_index != 0:
            last_index=edge[last_index]
            new_plan.append(plan[last_index])
        plan=new_plan
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
