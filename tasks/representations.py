class Solution(object):
    __slots__ = ["genes", "fitness", "generation", "parents"]

    def __init__(self):
        self.genes = []
        self.fitness = None
        self.generation = None
        self.parents = []

    def __str__(self):
        return "[%s]" % ", ".join(
            [("%.2f" % x) for x in self.genes])

    def __repr__(self):
        return str(self)


class DePayload(object):
    def __init__(self):
        self.population = []
        self.trials = []
        self.parents = []
        self.selected = []
        self.base_solutions = []
        self.best = None
        self.generation = 1
        self.target_fitness = 0
        self.population_size = 0
        self.solution_size = 0

    def __str__(self):
        string = "Generation: %s\nBest: %s\n" % (self.generation, self.best)
        return string

    def __repr__(self):
        return str(self)

if __name__ == "__main__":
    payload = DePayload()
    print payload
