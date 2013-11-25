import pypline
import random


def generate_random_vector(size, lower, upper):
    top_range = upper - lower
    return [random.random() * top_range - abs(lower)
            for n in xrange(size)]


def initialise_random_de(pop_size, solution_size, lower, upper):
    """
    Construct a random population of n vectors based on upper and lower limit
    """
    import representations
    dePayload = representations.DePayload()
    solutions = []
    for i in xrange(pop_size):
        solution = representations.Solution()
        solution.genes = generate_random_vector(solution_size, lower, upper)
        solutions.append(solution)
        solution.generation = 0
    dePayload.population = solutions
    dePayload.trials = solutions[:]
    dePayload.best = solutions[0]
    dePayload.best.fitness = -1
    return dePayload


class DeJongOneInitialiser(pypline.Task):
    def __init__(self, pop_size, solution_size):
        self.pop_size = pop_size
        self.solution_size = solution_size

    def process(self, message, pipeline):
        de = initialise_random_de(self.pop_size, self.solution_size, -5.12, 5.12)
        de.solution_size = self.solution_size
        de.population_size = self.pop_size
        return de

if __name__ == "__main__":
    p = initialise_random_de(10, 10, 0, 1)
    print p.population
