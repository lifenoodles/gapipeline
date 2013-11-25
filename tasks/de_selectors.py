import pypline
import random


class BestSelector(pypline.Task):
    def process(self, message, pipeline):
        best_index = min(self.population, key=lambda x: x.fitness)
        message.base_solutions = [
            message.population[best_index] for i in xrange(len(message.population))]
        message.base_solutions_indices = [
            best_index for i in xrange(len(message.population))]
        return message


class RandomSelector(pypline.Task):
    def process(self, message, pipeline):
        base_solutions = []
        base_solutions_indices = []
        for i in xrange(len(message.population)):
            rand = random.randint(0, len(message.population) + 1)
            base_solutions.append(message.population[rand])
            base_solutions_indices.append(rand)
        message.base_solutions = base_solutions
        message.base_solutions_indices = base_solutions_indices
        return message


class DifferenceSelector(pypline.Task):
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
