class Solution(object):
    def __init__(self):
        self.genes = []
        self.fitness = -1

    def __str__(self):
        return "[%s]" % ", ".join([("%.2f" % x) for x in self.genes])

    def __repr__(self):
        return str(self)


class DePayload(object):
    def __init__(self):
        self.population = []
        self.best = None
        self.generation = 0
