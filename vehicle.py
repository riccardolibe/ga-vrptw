from random import randint


class Vehicle:

    def __init__(self, capacity=500):
        self.capacity = capacity
        self.goods = capacity
        self.position = 0
        self.path = []
        self.target = 0
        self.traveled_path = []
        self.total_travel_time = 0
        self.travel_time_to_target = 0

    def deliver(self, roadmap):
        """
        Checks available goods and delivers
        """
        customer = roadmap.get_customer(self.position)

        #if self.goods >= customer.demand:
        #    self.goods = self.goods - customer.demand
        customer.demand = 0

        self.total_travel_time += 1

    def wait(self):
        self.total_travel_time += 1

    def travel(self):
        if self.travel_time_to_target != 0:
            self.travel_time_to_target -= 1
            self.total_travel_time += 1
        else:
            self.traveled_path.append(self.position)
            self.position = self.target

    def set_random_next_target(self, roadmap):
        neighbors = roadmap.get_neighbors(self.position)
        i = randint(0, len(neighbors)-1)
        self.travel_time_to_target = roadmap.get_travel_time(self.position,neighbors[i])
        self.target = neighbors[i]
        #    if self.target == 0:
        #        self.goods = self.capacity

    def set_next_target(self, roadmap):
        if self.path:
            self.target = self.path.pop()
            self.travel_time_to_target = roadmap.get_travel_time(self.position, self.target)

    def set_path(self, p):
        self.path = p
        self.path.reverse()
        self.path.pop()