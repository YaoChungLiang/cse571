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
        plan = self.planning_env.reconstruct_path(came_from, start_config, goal_config)
        return numpy.array(plan)

    def ShortenPath(self, path):

        # TODO (student): Postprocess the planner.
        return path

    def a_star_search(self, graph, start, goal):

        frontier = PriorityQueue()
        frontier.put(start, 0)
        came_from = {}
        cost_so_far = {}
        came_from[start] = None
        cost_so_far[start] = 0
        
        while not frontier.empty():
            current = frontier.get()            
            if current == goal:
                break            
            for next in graph.neighbors(current):
                new_cost = cost_so_far[current] + 10
                if next not in cost_so_far or new_cost < cost_so_far[next]:
                    cost_so_far[next] = new_cost
                    priority = new_cost + graph.compute_heuristic(next)
                    frontier.put(next, priority)
                    came_from[next] = current
        
        return came_from, cost_so_far
