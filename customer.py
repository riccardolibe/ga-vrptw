from numpy.random import normal

class Customer:
    def __init__(self, demand=0, time_window=(0, 0)):
        self.demand = demand
        self.time_window = time_window

    def set_time_window(self, mean, variance):
        """
        :returns
        Sets a random time window
        :keyword
        mean -- mean of the gaussian distribution
        variance -- variance of the gaussian distribution
        """
        t1, t2 = 0, 0
        while t1 <= 0:
            t1 = int(normal(mean-1, variance, 1))
        while t2 <= t1:
            t2 = int(normal(mean+1, variance, 1))
        self.time_window = (t1, t2)

    def receive_goods(self, roadmap):
        roadmap.total_demand -= self.demand
        self.demand = 0
