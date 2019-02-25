import numpy
import numpy as np
from IPython import embed
from matplotlib import pyplot as plt

class MapEnvironment(object):
    
    def __init__(self, mapfile, start, goal):

        # Obtain the boundary limits.
        # Check if file exists.
        self.map = numpy.loadtxt(mapfile)
        self.xlimit = [0, numpy.shape(self.map)[0]-1] # TODO (avk): Check if this needs to flip.
        self.ylimit = [0, numpy.shape(self.map)[1]-1]

        # Check if start and goal are within limits and collision free
        if not self.state_validity_checker(start) or not self.state_validity_checker(goal):
            raise ValueError('Start and Goal state must be within the map limits');
            exit(0)

        # Display the map
        plt.imshow(self.map, interpolation='nearest')

    def compute_distance(self, start_config, end_config):
        #
        # TODO: Implement a function which computes the distance between
        # two configurations.
        #
        dx = start_config[0] - end_config[0]
        dy = start_config[1] - end_config[1]
        distance = np.sqrt(dx**2+dy**2)
        return 

    def state_validity_checker(self, config):
        #
        # TODO: Implement a state validity checker
        # Return true if valid.
        #
        x, y = config[0], config[1]
        checker1 = self.map[x, y] == 0
        checker2 = (x >= self.xlimit[0] and x <= self.xlimit[1])
        checker3 = (y >= self.ylimit[0] and y <= self.ylimit[1])
        if checker1 and checker2 and checker3:
            return True
        else:
            return False

    def edge_validity_checker(self, config1, config2):
        #
        # TODO: Implement an edge validity checker
        #
        if state_validity_checker(config1) and state_validity_checker(config2):
            return True
        else:
            return False

    def compute_heuristic(self, config):
        
        #
        # TODO: Implement a function to compute heuristic.
        #
        return self.compute_distance(config, self.goal)
        
    def visualize_plan(self, plan):
        '''
        Visualize the final path
        @param plan Sequence of states defining the plan.
        '''
        plt.imshow(self.map, interpolation='nearest')
        for i in range(numpy.shape(plan)[0] - 1):
            x = [plan[i,0], plan[i+1, 0]]
            y = [plan[i,1], plan[i+1, 1]]  
            plt.plot(y, x, 'k')
        plt.show()