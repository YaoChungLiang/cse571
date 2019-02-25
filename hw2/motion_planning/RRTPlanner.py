import numpy
from RRTTree import RRTTree

class RRTPlanner(object):

    def __init__(self, planning_env):
        self.planning_env = planning_env
        self.tree = RRTTree(self.planning_env)
        

    def Plan(self, start_config, goal_config, epsilon = 0.001):
        
        # Initialize an empty plan.
        plan = []

        # Start with adding the start configuration to the tree.
        self.tree.AddVertex(start_config)

        # TODO (student): Implement your planner here.
        plan.append(start_config)
        plan.append(goal_config)
        return numpy.array(plan)

    def extend(self):
        # TODO (student): Implement an extend logic.
        pass

    def ShortenPath(self, path):
        # TODO (student): Postprocessing of the plan.
        return path
