from random import randint


class Vehicle:

    def __init__(self, capacity=1000, maximum_trip=8):
        self.capacity = capacity
        self.maximum_trip = maximum_trip
        self.goods = capacity
        self.position = 0
        self.past_path = []
        self.tot_time = 0
        self.tot_cost = 0

    def unload(self, customer, time):
        """
        Checks available goods and delivers
        """
        t1 = customer.time_window[0]
        t2 = customer.time_window[1]
        if self.goods >= customer.demand and \
                        t1 <= time and \
                        time <= t2  :

            self.goods = self.goods - customer.demand
            return True
        else:
            return False

    def visit_next(self, roadmap):
        """
        Visits a random next neighbour, store the old position
        """
        neighbors = roadmap.map.neighbors(self.position)
        i = randint(0, len(neighbors)-1)
        self.past_path.append(self.position)
        travel_time = roadmap.map[self.position][neighbors[i]]['travel_time']
        self.tot_time += travel_time
        self.tot_cost += roadmap.map[self.position][neighbors[i]]['cost']
        self.position = neighbors[i]
        return travel_time

    def reset(self):
        self.past_path = []
        self.tot_time = 0
        self.tot_cost = 0

    def visit_path(self,roadmap, path):
        self.reset()
        for node in path:
            self.past_path.append(node)
            self.tot_time += roadmap.map[self.position][node]['travel_time']
            self.tot_cost = roadmap.map[self.position][node]['cost']
            self.position = node



