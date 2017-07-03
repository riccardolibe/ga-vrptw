from random import randint, gauss


class Customer:

    def __init__(self, demand=0, time_window=(0, 0)):
        self.demand = randint(50, 100)
        self.set_time_window(12, 4)

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
            t1 = int(gauss(mean-1, variance)) % 24
        while t2 <= t1:
            t2 = int(gauss(mean+1, variance)) % 24
        self.time_window = range(t1, t2+1)

    def receive(self):
        self.demand = 0
