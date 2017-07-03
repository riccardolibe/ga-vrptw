from individual import Individual
from environment import Environment
from random import randint

MAX_ITERATIONS = 100

map_size = 10
population_size = 10
vehicles_number = 2

environment = Environment(map_size, vehicles_number)

individuals = [Individual(environment) for i in range(population_size)]

for i in individuals:
    print(i.fitness)

def tournament_selection(population, k):
    """
    Binary tournament selection of parents
    :param population: size of population
    :param k: partecipants of tournament
    :return: best parent
    """
    best = None
    for i in range(k):
        ind = population[randint(0, population_size-1)]
        if (best is None) or ind.fitness > best.fitness:
            best = ind
    return best


def crossover(m, f):
    child_dna = []
    check = []
    for ch_m, ch_f in zip(m.dna, f.dna):
        #check the shorter path/chromosome and pass it to child
        if len(ch_m) < len(ch_f):
            child_dna.append(ch_m)
            check += ch_m
        else:
            child_dna.append(ch_f)
            check += ch_f

    for i in range(vehicles_number):
        if not i in check:
            return []
    return child_dna



for i in range(MAX_ITERATIONS):
    #print(i)
    mother = None
    father = None
    while mother == father:
        mother = tournament_selection(individuals, int(population_size/2))
        father = tournament_selection(individuals, int(population_size/2))

    new_dna = crossover(mother,father)
    if new_dna:
        child = Individual(environment,new_dna)
        if not child.is_abnormal():
            individuals.append(child)
            individuals.remove(mother)
            individuals.remove(father)
            individuals.append(Individual(environment))
        else:
            print('abnormal')


best_solution = tournament_selection(individuals, population_size)

print('Best solution fitness:', best_solution.fitness)


