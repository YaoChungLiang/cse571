import sys
import time
import numpy
import numpy as np
from utils import *

class AStarPlanner(object):    
    def __init__(self, planning_env):
        self.planning_env = planning_env
        self.nodes = dict()

    def Plan(self, start_config, goal_config):
        # TODO (student): Implement your planner here.
        came_from, cost_so_far = self.a_star_search(self.planning_env, start_config, goal_config)
        #print('cost=',cost_so_far[tuple(goal_config)])
        plan = self.planning_env.reconstruct_path(came_from, start_config, goal_config)
        return numpy.array(plan)

    def ShortenPath(self, path):
        
        # TODO (student): Postprocess the planner.
        return path

    def a_star_search(self, graph, start, goal):
        eps = 1
        frontier = PriorityQueue()
        frontier.put(start, 0)
        #print('frontier=',frontier)
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
                    new_cost = cost_so_far[current] + 1.414*eps
                else:
                    new_cost = cost_so_far[current] + 1*eps
                if next not in cost_so_far or new_cost < cost_so_far[next]:
                    cost_so_far[next] = new_cost
                    priority = new_cost + graph.compute_heuristic(next)
                    frontier.put(next, priority)
                    came_from[next] = current
        print('states_explored = ',len(states_explored))
        print("total_cost = ",cost_so_far[goal])
        return came_from, cost_so_far
        