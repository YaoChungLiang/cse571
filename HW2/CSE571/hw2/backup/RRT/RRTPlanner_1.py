import numpy
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
        for i in range(10):
            dist=[]
            rand_x = numpy.random.randint(1,500)
            rand_y = numpy.random.randint(1,500)
            next_point = ([rand_x,rand_y])
            if self.planning_env.state_validity_checker(next_point) :
                #plan.append(next_point)
                print('plan')
                print(plan)
                for j in range(len(plan)):
                    dist=dist+[self.planning_env.compute_distance(plan[j],next_point)]
                    min_idx = dist.index(min(dist))
                plan.append(next_point)
                #edge.setdefault(min_idx,[]).append(len(plan)-1)
                edge[len(plan)-1]=min_idx
                #edge[min_idx]=len(plan)
                print('j')
                print(j)
        print('edge')
        print(edge)
                    
        plan.append(goal_config)
        return numpy.array(plan)


    def extend(self,start,end):
        # TODO (student): Implement an extend logic.
        
        
            
        pass
    def ShortenPath(self, path):
        # TODO (student): Postprocessing of the plan.
        return path
