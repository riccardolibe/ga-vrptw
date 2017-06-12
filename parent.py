from vehicle import Vehicle
from random import randint

class Parent:
    def __init__(self, roadmap, veichles):
        self.cost = 0
        self.vehicles = veichles
        self.roadmap = roadmap
        self.time = 0

    def run(self):
        while self.roadmap.total_demand != 0:
            for v in self.vehicles:
                self.time += v.visit_next(self.roadmap)
                self.time = self.time % 24
                customer = self.roadmap.map.node[v.position]['customer']
                if v.unload(customer, self.time):
                    customer.receive_goods(self.roadmap)
        for v in self.vehicles:
            self.cost += v.tot_cost
