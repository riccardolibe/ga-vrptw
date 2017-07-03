import networkx as nx
from random import *
import matplotlib.pyplot as plt
from customer import Customer
from networkx import Graph


class RoadMap(Graph):

    def __init__(self, n):
        self.map = nx.geographical_threshold_graph(n, 0)
        self.set_travel_time()
        self.set_travel_cost()
        self.set_customers()

    def show_map(self):
        nx.draw(self.map)
        plt.show()

    def set_travel_time(self):
        for i, j in self.map.edges():
            self.map[i][j]['travel_time'] = randint(1, 10)

    def set_travel_cost(self):
        for i, j in self.map.edges():
            self.map[i][j]['cost'] = int(0.2 * self.map[i][j]['travel_time'])

    def set_customers(self):
        for i in self.map.nodes():
            self.map.node[i]['customer'] = Customer()

    def get_customer(self, node):
        return self.map.node[node]['customer']

    def get_travel_time(self, position, destination):
        return self.map[position][destination]['travel_time']

    def get_nodes(self):
        return self.map.nodes()

    def get_neighbors(self, node):
        return self.map.neighbors(node)
