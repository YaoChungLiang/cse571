import sys
import time
import numpy
import matplotlib.pyplot as plt
import queue
class AStarPlanner(object):  
    EPS = 1
    DXY = (
        (-1, 0), (-1, 1), (0, 1),
        (1, 1), (1, 0), (1, -1),
        (0, -1), (-1, -1)
    ) 
    def __init__(self, planning_env):
        self.planning_env = planning_env
        self.nodes = dict()

    def Plan(self, start_config, goal_config):

        start_config = tuple(start_config)
        goal_config = tuple(goal_config)

        # TODO (student): Implement your planner here.
        dist = {start_config: 0}
        pred = {start_config: None}
        # not the abtract open set, may have elements with same config
        open = queue.PriorityQueue()
        close = set()
        open.put( (0, start_config) )  # (f = g+h, config), the 0 here does not matter

        while (not open.empty()):
            est_total_dist, config = open.get()
            if config == goal_config: break
            if config in close: continue
            close.add(config)

            for i in range(len(self.DXY)):
                next_config = (config[0] + self.DXY[i][0], config[1] + self.DXY[i][1])
                if not self.planning_env.state_validity_checker(next_config): continue
                if next_config in close: continue
                dist_next = dist[config] + numpy.sqrt(self.DXY[i][0]**2 + self.DXY[i][1]**2)

                if (next_config not in dist) or (dist_next < dist[next_config]):
                    dist[next_config] = dist_next
                    pred[next_config] = config
                    h = self.planning_env.compute_heuristic(next_config)
                    open.put( (dist_next + self.EPS * h, next_config) )

        print("states explored (collision states excluded):", len(dist))
        print("final cost:", dist[goal_config])
        explore = numpy.array(list(dist.keys()))
        plt.scatter(explore[:,1], explore[:,0], color='y', marker='.')
        return numpy.array(self._construct_path(pred, goal_config))

    def ShortenPath(self, path):

        # TODO (student): Postprocess the planner.
        new_path = [path[-1]]
        goal = len(path) - 1
        while goal > 0:
            pred = 0
            while pred < goal and self.planning_env.edge_validity_checker(path[pred], path[goal]):
                pred += 1
            new_path.append(path[pred])
            goal = pred
        new_path.reverse()
        return numpy.array(new_path)

    def _construct_path(self, pred, goal):
        path = []
        node = goal
        while node:
            path.append(node)
            node = pred[node]
        path.reverse()
        return numpy.array(path)