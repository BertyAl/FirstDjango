import random
from typing import List, Tuple, Dict

# Define the Item class to hold item values and weights
class Item:
    def __init__(self, value: int, weight: int):
        self.value = value
        self.weight = weight

# Sample items (value, weight)
items = [
    Item(60, 10), Item(100, 20), Item(120, 30),
    Item(70, 12), Item(50, 5), Item(30, 3)
]

MAX_KNAPSACK_WEIGHT = 50  # Example maximum knapsack weight
MUTATION_RATE = 0.01  # Example mutation rate
REPRODUCTION_RATE = 0.5  # Example reproduction rate
CROSSOVER_RATE = 0.7  # Example crossover rate

# Individual class representing a solution
class Individual:
    def __init__(self, bits: List[int]):
        self.bits = bits

    def fitness(self) -> float:
        total_value = sum([
            bit * item.value
            for item, bit in zip(items, self.bits)
        ])

        total_weight = sum([
            bit * item.weight
            for item, bit in zip(items, self.bits)
        ])

        if total_weight <= MAX_KNAPSACK_WEIGHT:
            return total_value

        return 0

# Memoization dictionary for knapsack function
memo: Dict[Tuple[int, int], int] = {}

def knapsack(W: int, w: List[int], v: List[int], n: int) -> int:
    if n == 0 or W == 0:
        return 0

    if w[n - 1] > W:
        return knapsack(W, w, v, n - 1)

    if (W, n) in memo:
        return memo[(W, n)]

    value_picked = v[n - 1] + knapsack(W - w[n - 1], w, v, n - 1)
    value_notpicked = knapsack(W, w, v, n - 1)
    value_max = max(value_picked, value_notpicked)

    memo[(W, n)] = value_max
    return value_max

def generate_initial_population(count=6) -> List[Individual]:
    population = set()
    while len(population) != count:
        bits = [
            random.choice([0, 1])
            for _ in items
        ]
        population.add(Individual(bits))
    return list(population)

def selection(population: List[Individual]) -> List[Individual]:
    parents = []
    random.shuffle(population)
    if population[0].fitness() > population[1].fitness():
        parents.append(population[0])
    else:
        parents.append(population[1])
    if population[2].fitness() > population[3].fitness():
        parents.append(population[2])
    else:
        parents.append(population[3])
    return parents

def crossover(parents: List[Individual]) -> List[Individual]:
    N = len(items)
    child1 = parents[0].bits[:N//2] + parents[1].bits[N//2:]
    child2 = parents[0].bits[N//2:] + parents[1].bits[:N//2]
    return [Individual(child1), Individual(child2)]

def mutate(individuals: List[Individual]) -> None:
    for individual in individuals:
        for i in range(len(individual.bits)):
            if random.random() < MUTATION_RATE:
                individual.bits[i] = 1 - individual.bits[i]  # Flip the bit

def next_generation(population: List[Individual]) -> List[Individual]:
    next_gen = []
    while len(next_gen) < len(population):
        parents = selection(population)
        children = []
        if random.random() < REPRODUCTION_RATE:
            children = parents
        else:
            if random.random() < CROSSOVER_RATE:
                children = crossover(parents)
            if random.random() < MUTATION_RATE:
                mutate(children)
        next_gen.extend(children)
    return next_gen[:len(population)]

def average_fitness(population: List[Individual]) -> float:
    total_fitness = sum(individual.fitness() for individual in population)
    return total_fitness / len(population)

def solve_knapsack() -> Individual:
    population = generate_initial_population()
    avg_fitnesses = []
    for _ in range(500):
        avg_fitnesses.append(average_fitness(population))
        population = next_generation(population)
    population = sorted(population, key=lambda i: i.fitness(), reverse=True)
    return population[0]

def main():
    best_solution = solve_knapsack()
    print ("{bes_solution.bits}")
    print("\nAvailable Items:")
    print("-------------------------------------")
    for idx, item in enumerate(items):
        print(f"Item {idx + 1}: Value = {item.value}, Weight = {item.weight}")
    print("-------------------------------------")
    print("\nBest Solution Found:")
    print("-------------------------------------")
    print(f"Bit Representation: {best_solution.bits}")
    print(f"Total Value: {best_solution.fitness()}")
    print("-------------------------------------")
    print("\nItems Included in the Best Solution:")
    print("-------------------------------------")
    total_weight = 0
    for bit, item in zip(best_solution.bits, items):
        if bit == 1:
            print(f"Value: {item.value}, Weight: {item.weight}")
            total_weight += item.weight
    print("-------------------------------------")

    print(f"\nTotal Weight: {total_weight}")

if __name__ == "__main__":
    main()

# memo = {}
# from typing import List, Tuple, Dict

# def knapsack(W, w, v, n):
#     if n == 0 or W == 0:
#         return 0
  
#     # if weight of the nth item is more than the weight
#     # available in the knapsack the skip it
#     if (w[n - 1] > W):
#         return knapsack(W, w, v, n - 1)
    
#     # Check if we already have an answer to the sunproblem
#     if (W, n) in memo:
#         return memo[(W, n)]
  
#     # find value of the knapsack when the nth item is picked
#     value_picked = v[n - 1] + knapsack(W - w[n - 1], w, v, n - 1)

#     # find value of the knapsack when the nth item is not picked
#     value_notpicked = knapsack(W, w, v, n - 1)

#     # return the maxmimum of both the cases
#     # when nth item is picked and not picked
#     value_max = max(value_picked, value_notpicked)

#     # store the optimal answer of the subproblem
#     memo[(W, n)] = value_max

#     return value_max

# def generate_initial_population(count=6) -> List[Individual]:
#     population = set()

#     # generate initial population having `count` individuals
#     while len(population) != count:
#         # pick random bits one for each item and 
#         # create an individual 
#         bits = [
#             random.choice([0, 1])
#             for _ in items
#         ]
#         population.add(Individual(bits))

#     return list(population)

# def fitness(self) -> float:
#     total_value = sum([
#         bit * item.value
#         for item, bit in zip(items, self.bits)
#     ])

#     total_weight = sum([
#         bit * item.weight
#         for item, bit in zip(items, self.bits)
#     ])

#     if total_weight <= MAX_KNAPSACK_WEIGHT:
#         return total_value
    
#     return 0

# def selection(population: List[Individual]) -> List[Individual]:
#     parents = []
    
#     # randomly shuffle the population
#     random.shuffle(population)

#     # we use the first 4 individuals
#     # run a tournament between them and
#     # get two fit parents for the next steps of evolution

#     # tournament between first and second
#     if population[0].fitness() > population[1].fitness():
#         parents.append(population[0])
#     else:
#         parents.append(population[1])
    
#     # tournament between third and fourth
#     if population[2].fitness() > population[3].fitness():
#         parents.append(population[2])
#     else:
#         parents.append(population[3])

#     return parents

# def crossover(parents: List[Individual]) -> List[Individual]:
#     N = len(items)

#     child1 = parents[0].bits[:N//2] + parents[1].bits[N//2:]
#     child2 = parents[0].bits[N//2:] + parents[1].bits[:N//2]

#     return [Individual(child1), Individual(child2)]

# def mutate(individuals: List[Individual]) -> List[Individual]:
#     for individual in individuals:
#         for i in range(len(individual.bits)):
#             if random.random() < MUTATION_RATE:
#                 # Flip the bit
#                 individual.bits[i] = ~individual.bits[i]

# def next_generation(population: List[Individual]) -> List[Individual]:
#     next_gen = []
#     while len(next_gen) < len(population):
#         children = []

#         # we run selection and get parents
#         parents = selection(population)

#         # reproduction
#         if random.random() < REPRODUCTION_RATE:
#             children = parents
#         else:
#             # crossover
#             if random.random() < CROSSOVER_RATE:
#                 children = crossover(parents)
            
#             # mutation
#             if random.random() < MUTATION_RATE:
#                 mutate(children)

#         next_gen.extend(children)

#     return next_gen[:len(population)]


# def solve_knapsack() -> Individual:
#     population = generate_initial_population()

#     avg_fitnesses = []

#     for _ in range(500):
#         avg_fitnesses.append(average_fitness(population))
#         population = next_generation(population)

#     population = sorted(population, key=lambda i: i.fitness(), reverse=True)
#     return population[0]

