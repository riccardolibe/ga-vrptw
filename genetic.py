from individual import Individual
from environment import Environment

env = Environment(5,2)

dna = [[1,2,3,4,5],[1,2,3,4,5]]

ind = Individual(env,dna)

print(ind.dna, ind.fitness)
