import sys
import time
import numpy
from pr_que import *

class AStarPlanner(object):    
    def __init__(self, planning_env):
        self.planning_env = planning_env
        self.nodes = dict()

    def Plan(self, start_config, goal_config):

        plan = []

        # TODO (student): Implement your planner here.
        Pr_queue=PriorityQueue()
        Pr_queue.put(start_config,0)
        came_from=dict()
        cost_so_far=dict()
        print(start_config)
        came_from[start_config]=None
        cost_so_far[start_config]=0
        while not Pr_queue.empty():
            current=Pr_queue.get()
            if current== goal_config:
                break
            for next in self.planning_env.neighbors(current):
                new_cost=cost_so_far[current]+10
                if next not in cost_so_far or new_cost < cost_so_far[next]:
                    cost_so_far[next]=new_cost
                    priority = new_cost+self.planning_env.compute_heuristic
                    Pr_queue.put(next,priority)
                    came_from[next]=current
        current = goal_config
        path=[]
        while current != start_config :
            path.append(current)
            current=came_from[current]
        path.append(start_config)
        path.reverse()
        plan=path
        
        #plan.append(start_config)
        #plan.append(goal_config)
        #print(plan) #[[321,148],[106,202]]
        
        return numpy.array(plan)

    def ShortenPath(self, path):
        
        # TODO (student): Postprocess the planner.
        return path
