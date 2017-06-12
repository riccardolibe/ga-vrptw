import networkx as nx
import random
from random import randint
import matplotlib.pyplot as plt
from customer import Customer
from networkx import Graph


class RoadMap(Graph):

    def __init__(self, n):
        self.total_demand = 0
        self.map = nx.gnp_random_graph(n, random.random())
        self.set_time()
        self.set_cost()
        self.set_customers()

    def show_map(self):

        nx.draw(self.map)
        plt.show()

    def set_time(self):
        for i, j in self.map.edges():
            self.map[i][j]['travel_time'] = randint(0, 20)

    def set_cost(self):
        #todo migliorare la funzione del costo in fuznione del tempo
        for i, j in self.map.edges():
            self.map[i][j]['cost'] = int(0.2 * self.map[i][j]['travel_time'])

    def set_customers(self):

        for i in self.map.nodes():
            demand = randint(0, 100)
            self.total_demand = self.total_demand + demand
            customer = Customer(demand)
            customer.set_time_window(12, 8)
            self.map.node[i]['customer'] = customer