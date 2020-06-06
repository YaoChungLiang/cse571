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
        start_config=list(start_config)
        goal_config=list(goal_config)
        plan.append(start_config)
        plan.append(goal_config)
        return numpy.array(plan)

#        for i in range(10):
#            rand_x = numpy.random.randint(1,500)
#            rand_y = numpy.random.randint(1,500)
#            next_point = ([rand_x,rand_y])
#            if self.planning_env.state_validity_checker(next_point):
                
'''
        current_node=([])
        # Start with adding the start configuration to the tree.
        self.tree.AddVertex(start_config)
        self.tree.AddVertex(goal_config)
        self.tree.AddEdge(1,0)
        print("tree vertices")
        print(self.tree.vertices)
        print(self.tree.edges)        
        print(start_config)
        plan.append(start_config)

        for i in range(10):
            rand_x = numpy.random.randint(1,500)
            rand_y = numpy.random.randint(1,500)
            next_point = ([rand_x,rand_y])
            if self.planning_env.state_validity_checker(next_point) :
                plan.append(next_point)
'''        
        #print(plan[0,0])
        

        # TODO (student): Implement your planner here.
        #plan.append(start_config)
        #plt.plot([100,200],[100,300],'k')
#        for i in range(10):
#            plan.append((10*i,10*i))
        #return numpy.array(plan)

    def extend(self):
        # TODO (student): Implement an extend logic.
        pass

    def ShortenPath(self, path):
        # TODO (student): Postprocessing of the plan.
        return path
