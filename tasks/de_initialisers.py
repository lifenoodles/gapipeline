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
    dePayload.population = solutions
    return dePayload


class DeInitialiser(pypline.Task):
    def process(self, message, pipeline):
        pass


if __name__ == "__main__":
    p = initialise_random_de(10, 10, 0, 1)
    print p.population
