from roadmap import RoadMap
from vehicle import Vehicle


class Environment:

    def __init__(self, n, k):
        self.roadmap = RoadMap(n)
        self.vehicles = [Vehicle() for i in range(k)]
        self.time = 0

    def clock(self, h=1):
        self.time = (self.time + h) % 24

    def total_demand(self):
        total_demand = 0
        for node in self.roadmap.get_nodes():
            customer = self.roadmap.get_customer(node)
            total_demand += customer.demand
        return total_demand

    def time_window(self, vehicle):
        customer = self.roadmap.get_customer(vehicle.position)
        return customer.time_window

    def demand(self, vehicle):
        customer = self.roadmap.get_customer(vehicle.position)
        return customer.demand
