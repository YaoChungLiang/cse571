import sys
import time
import numpy
import numpy as np
from utils import *
from matplotlib import pyplot as plt
#import queue
import operator
class AStarPlanner(object):
    eps = 1
    def __init__(self, planning_env):
        self.planning_env = planning_env
        self.nodes = dict()

#    def Plan(self, start_config, goal_config):
#        pr_que = queue.PriorityQueue()
#        start_config = tuple(start_config)
#        goal_config = tuple(goal_config)
#        
#        ######### v1 fail ####################
##        print(start_config)
##        print(goal_config)
##        dist_from_start = {start_config:0}
##        future_cost = {start_config:None}
##        open_area = queue.PriorityQueue()
##        explored_area = set()
##        open_area.put((0,start_config))
##        while (not open_area.empty()):
##            est_total_dist , current = open_area.get()
##            if current == goal_config: break
##            explored_area.add(current)
##            for next_point in self.planning_env.neighbors(current):
##                if self.planning_env.state_validity_checker(next_point): continue
##                next_x = next_point[0]
##                next_y = next_point[1]
##                current_x = current[0]
##                current_y = current[1]
##                add_dist = np.sqrt((next_x-current_x)**2+(next_y-current_y)**2)
##                dist_next = dist_from_start[current] + add_dist
##                #h_next = self.planning_env.compute_heuristic(next_point)
##                if (next_point not in dist_from_start) or (dist_next < dist_from_start[next_point]):
##                    dist_from_start[next_point] = dist_next
##                    future_cost[next_point] = current
##                    h = self.planning_env.compute_heuristic(next_point)
##                    open_area.put((dist_next + self.eps*h, next_point))
#                    
#        #print(dist_from_start)
#        came_from = dict()
#        came_from[goal_config] = start_config
#        # TODO (student): Implement your planner here.
#        #came_from, cost_so_far = self.a_star_search(self.planning_env, start_config, goal_config)
#        #print('cost=',cost_so_far[tuple(goal_config)])
#        plan = self.planning_env.reconstruct_path(came_from, start_config, goal_config)
#        return numpy.array(plan)
    def Plan(self, start_config, goal_config):
        came_from, cost_so_far = self.a_star_search(self.planning_env, start_config, goal_config)
        plan = self.planning_env.reconstruct_path(came_from, start_config, goal_config)
        return numpy.array(plan)
    def ShortenPath(self, path):
        
        # TODO (student): Postprocess the planner.
        return path

    def a_star_search(self, graph, start, goal):
#        pr_que = PriorityQueue()
#        parent = dict()
#        F_value = None
#        H_value = None
#        open_list = dict()
#        close_list = dict()
#        open_g = dict()
#        open_f = dict()
#        open_g[start] = 0
#        open_f[start] = np.Inf
#        pr_que.put((0,start))
#        while not pr_que.empty():
#            current = pr_que.get()
#            if current ==goal:
#                break
#            for next_point in graph.neighbors(current):
#                if next_point not in :
                    
        #stats = {'a':1000, 'b':3000, 'c': 100}
        #min(stats.iteritems(), key=operator.itemgetter(1))[0]
###############   version 2 ################   
#        eps = 5
#        frontier = PriorityQueue()
#        frontier.put(start, 0)
#        came_from = dict()
#        cost_so_far = dict()
#        came_from[start] = None
#        cost_so_far[start] = 0
#        
#        states_explored = set()
#        while not frontier.empty():
#            current = frontier.get()            
#            if current == goal:
#                break            
#            for next in graph.neighbors(current):
#                if graph.state_validity_checker(next):
#                    tup_next = tuple(next)
#                    states_explored.add(tup_next)
#                    current_x = current[0]
#                    current_y = current[1]
#                    next_x = next[0]
#                    next_y = next[1]
#                    dist = np.abs(current_x-next_x)+np.abs(current_y-next_y)
#                    if dist > 1.2:
#                        new_cost = cost_so_far[current] + np.sqrt(2)
#                    else:
#                        new_cost = cost_so_far[current] + 1
#                        if next not in cost_so_far or new_cost < cost_so_far[next]:
#                            cost_so_far[next] = new_cost
#                            priority = new_cost + graph.compute_heuristic(next)*eps
#                            frontier.put(next, priority)
#                            came_from[next] = current
#        print('states_explored = ',len(states_explored))
#        print("total_cost = ",cost_so_far[goal])
        
############## version 1######################        
        eps = 10
        frontier = PriorityQueue()
        frontier.put(start, 0)
        came_from = dict()
        cost_so_far = dict()
        came_from[start] = None
        cost_so_far[start] = 0
        
        states_explored = set()
        while not frontier.empty():
            current = frontier.get()            
            if current == goal:
                break            
            for next in graph.neighbors(current):
                tup_next = tuple(next)
                states_explored.add(tup_next)
                current_x = current[0]
                current_y = current[1]
                next_x = next[0]
                next_y = next[1]
                dist = np.abs(current_x-next_x)+np.abs(current_y-next_y)
                if dist > 1.5:
                    new_cost = cost_so_far[current]+np.sqrt(2)
                else:
                    new_cost = cost_so_far[current]+1
                if next not in cost_so_far or new_cost < cost_so_far[next]:
                    #states_explored.add(tuple(next))
                    cost_so_far[next] = new_cost
                    priority = new_cost + graph.compute_heuristic(next)*eps*0
                    frontier.put(next, priority)
                    came_from[next] = current
        print('states_explored = ',len(states_explored))
        print("total_cost = ",cost_so_far[goal])
        
        
        original_tree = list(states_explored)
        plt.imshow(self.planning_env.map, interpolation='nearest')
        for i in range(numpy.shape(original_tree)[0]):
            j=i
            x = [original_tree[j][0]]
            y = [original_tree[j][1]]
            plt.plot( y,x, 'gs')
####################################################
       
        
        return came_from, cost_so_far
        