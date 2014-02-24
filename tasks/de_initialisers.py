import pypline
import random
import time
import sys
sys.path.append("tasks")
import de_evaluators


def generate_random_vector(size, lower, upper):
    top_range = upper - lower
    return [random.random() * top_range - abs(lower)
            for n in xrange(size)]


def initialise_random_de(pop_size, solution_size, lower, upper, target_fitness=0):
    """
    Construct a random population of n vectors based on upper and lower limit
    """
    import representations
    dePayload = representations.DePayload()
    dePayload.lower = lower
    dePayload.upper = upper
    solutions = []
    for i in xrange(pop_size):
        solution = representations.Solution()
        solution.genes = generate_random_vector(solution_size, lower, upper)
        solutions.append(solution)
        solution.generation = 0
    dePayload.population = solutions
    dePayload.trials = solutions[:]
    dePayload.solution_size = solution_size
    dePayload.population_size = pop_size
    dePayload.start_time = time.time()
    dePayload.percent = 0.0
    dePayload.target_fitness = target_fitness
    return dePayload


@pypline.provides("population", "initialisation")
class DeInitialiser(pypline.Task):
    def __init__(self, pop_size, solution_size):
        self.pop_size = pop_size
        self.solution_size = solution_size

    def process(self, message, pipeline):
        raise NotImplementedError("Base DeInitialiser should not be called!")

    def getDescription(self):
        return {"population": self.pop_size, "solution_size": self.solution_size}


class DeJongOneInitialiser(DeInitialiser):
    def __init__(self, pop_size, solution_size):
        super(DeJongOneInitialiser, self).__init__(pop_size, solution_size)

    def process(self, message, pipeline):
        de = initialise_random_de(self.pop_size, self.solution_size, -5.12, 5.12)
        de_evaluators.DeJongOneEvaluator().process(de, None)
        return de


class DeJongTwoInitialiser(DeInitialiser):
    def __init__(self, pop_size, solution_size):
        super(DeJongTwoInitialiser, self).__init__(pop_size, solution_size)

    def process(self, message, pipeline):
        de = initialise_random_de(self.pop_size, self.solution_size, -2.048, 2.048)
        de_evaluators.DeJongTwoEvaluator().process(de, None)
        return de


class DeJongThreeInitialiser(DeInitialiser):
    def __init__(self, pop_size, solution_size):
        super(DeJongThreeInitialiser, self).__init__(pop_size, solution_size)

    def process(self, message, pipeline):
        de = initialise_random_de(self.pop_size, self.solution_size, -5.12, 5.12)
        de_evaluators.DeJongThreeEvaluator().process(de, None)
        return de


class RastriginSixInitialiser(DeInitialiser):
    def __init__(self, pop_size, solution_size):
        super(RastriginSixInitialiser, self).__init__(pop_size, solution_size)

    def process(self, message, pipeline):
        de = initialise_random_de(self.pop_size, self.solution_size, -5.12, 5.12)
        de_evaluators.RastriginSixEvaluator().process(de, None)
        return de
