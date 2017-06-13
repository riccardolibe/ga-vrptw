from numpy.random import normal


class Customer:

    def __init__(self, demand=0, time_window=(0, 0)):
        """
        Construct a new customer
        :param demand: quantity of goods needed
        :param time_window: window of time in which is possible to receive goods
        """
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
        """
        Decrease the customer demand to 0 and the general demand by the units of goods 
        :param roadmap: set of nodes
        :return: void
        """
        roadmap.total_demand -= self.demand
        self.demand = 0
