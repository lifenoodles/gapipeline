import pypline


def initialise_random_de(pop_size, solution_size, lower, upper):
    """
    Construct a random population of n vectors based on upper and lower limit
    """
    import random
    import representations
    dePayload = representations.DePayload()
    top_range = upper - lower
    solutions = []
    for i in xrange(pop_size):
        solution = representations.Solution()
        solution.genes = [random.random() * top_range - abs(lower)
                          for n in xrange(solution_size)]
        solutions.append(solution)
    dePayload.population = solutions
    return dePayload


class DeInitialiser(pypline.Task):
    def process(self, message, pipeline):
        pass


if __name__ == "__main__":
    p = initialise_random_de(10, 10, 0, 1)
    print p.population
