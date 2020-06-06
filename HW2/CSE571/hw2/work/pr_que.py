import collections
import heapq


class PriorityQueue:
    def __init__(self):
        self.elements = []
    
    def empty(self):
        return len(self.elements) == 0
    
    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))
    
    def get(self):
        # get the cost, cuz it's a tuple (item, cost)
        return heapq.heappop(self.elements)[1]