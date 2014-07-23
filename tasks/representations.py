class Solution(object):
    __slots__ = ["genes", "fitness", "generation", "parents"]

    def __init__(self):
        self.genes = []
        self.fitness = None
        self.generation = None
        self.parents = []

    def __str__(self):
        return "DE({})[{}]".format(
            self.generation, ", ".join(
                [("%.2f" % x) for x in self.genes]))

    def __repr__(self):
        return str(self)

    def __getstate__(self):
        return [self.genes, self.fitness, self.generation, self.parents]

    def __setstate__(self, array):
        self.genes = array[0]
        self.fitness = array[1]
        self.generation = array[2]
        self.parents = array[3]

    def has_parents(self):
        return len(self.parents) > 0


class DePayload(object):
    def __init__(self):
        self.population = []
        self.trials = []
        self.difference_solutions = []
        self.base_solutions = []
        self.base_solutions_indices = []
        self.crossover_solutions = []
        self.best = None
        self.generation = 1
        self.target_fitness = 0
        self.population_size = 0
        self.solution_size = 0
        self.start_time = 0
        self.lower = 0
        self.upper = 1

    def __str__(self):
        string = "Generation: %s\nBest: %s\n" % (self.generation, self.best)
        return string

    def __repr__(self):
        return str(self)

if __name__ == "__main__":
    payload = DePayload()
    print payload
