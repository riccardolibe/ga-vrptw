from parent import Parent


class Genetic:

    def __init__(self, environment):
        """
        Construct a genetic environment
        :param environment: 
        """
        self.population = []
        self.environment = environment

    def generate_population(self, pop_size):
        for i in range(pop_size):
            self.population.append(Parent(self.environment))
