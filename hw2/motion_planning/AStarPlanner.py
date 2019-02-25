import sys
import time
import numpy
import numpy as np

class AStarPlanner(object):    
    def __init__(self, planning_env):
        self.planning_env = planning_env
        self.nodes = dict()

    def Plan(self, start_config, goal_config):

        plan = []

        # TODO (student): Implement your planner here.

        plan.append(start_config)
        plan.append(goal_config)

        return numpy.array(plan)

    def ShortenPath(self, path):

        # TODO (student): Postprocess the planner.
        return path
