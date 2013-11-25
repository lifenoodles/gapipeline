import pypline
import random


class BestSelector(pypline.Task):
    def process(self, message, pipeline):
        best_index = min(self.population, key=lambda x: x.fitness)
        message.base_solutions = [
            best_index for i in xrange(len(message.population))]
        return message


class RandomSelector(pypline.Task):
    def process(self, message, pipeline):
        message.base_solutions = [
            random.randint(0, len(message.population) + 1)
            for i in xrange(len(message.population))]
        return message


class DifferenceSelectors(pypline.Task):
    def __init__(self, n):
        self.n = n

    def process(self, message, pipeline):
        assert(self.n * 2 >= len(message.population) + 1,
               "Population is too small for chosen amount of diff vectors!")
        selection_list = []
        for i, solution in enumerate(message.population):
            selected = set([message.base_solutions[i]])
            while len(selected) < self.n * 2:
                selected.add(random.randint(0, len(message.population) + 1))
            selection_list.append(list(selected))
        message.selected = selection_list
        return message
