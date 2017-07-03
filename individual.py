from copy import deepcopy


class Individual:
    def __init__(self, environment, DNA = []):
        self.environment = deepcopy(environment)
        self.fitness = 0
        if DNA == []:
            self.dna = []
            self.born()
        else:
            self.dna = DNA
            self.create()

    def born(self):
        environment = self.environment
        while environment.total_demand() != 0:
            for vehicle in environment.vehicles:
                if vehicle.position != vehicle.target:
                    vehicle.travel()
                elif environment.demand(vehicle) == 0:
                    vehicle.set_random_next_target(environment.roadmap)
                    vehicle.travel()
                elif environment.time in environment.time_window(vehicle):
                    vehicle.deliver(environment.roadmap)
                    vehicle.set_random_next_target(environment.roadmap)
                else:
                    vehicle.wait()
            environment.clock()
        for vehicle in environment.vehicles:
            vehicle.traveled_path.append(vehicle.position)
            self.dna.append(vehicle.traveled_path)
            self.fitness += vehicle.total_travel_time

    def create(self):
        environment = self.environment
        temp = deepcopy(self.dna)
        temp.reverse()
        for vehicle in environment.vehicles:
            vehicle.set_path(temp.pop())
        i = 0
        while environment.total_demand() != 0 and i < 1000:
            i += 1
            for vehicle in environment.vehicles:
                if vehicle.position != vehicle.target:
                    vehicle.travel()
                elif environment.demand(vehicle) == 0:
                    vehicle.set_next_target(environment.roadmap)
                    vehicle.travel()
                elif environment.time in environment.time_window(vehicle):
                    vehicle.deliver(environment.roadmap)
                    vehicle.set_next_target(environment.roadmap)
                else:
                    vehicle.wait()
            environment.clock()
        for vehicle in environment.vehicles:
            vehicle.traveled_path.append(vehicle.position)
            self.dna.append(vehicle.traveled_path)
            self.fitness += vehicle.total_travel_time

    def is_abnormal(self):
        if self.environment.total_demand == 0:
            return False
        else:
            return True
