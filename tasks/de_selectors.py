import pypline
import random


class BestSelector(pypline.Task):
    def process(self, message, pipeline):
        best_index, best = min(enumerate(message.population),
                               key=lambda (x, y): y.fitness)
        message.base_solutions = [best for i in xrange(len(message.population))]
        message.base_solutions_indices = [
            best_index for i in xrange(len(message.population))]
        return message


class RandomSelector(pypline.Task):
    def process(self, message, pipeline):
        base_solutions = []
        base_solutions_indices = []
        for i in xrange(len(message.population)):
            rand = random.randint(0, len(message.population) - 1)
            base_solutions.append(message.population[rand])
            base_solutions_indices.append(rand)
        message.base_solutions = base_solutions
        message.base_solutions_indices = base_solutions_indices
        return message


class DifferenceSelector(pypline.Task):
    def __init__(self, n):
        self.n = n

    def process(self, message, pipeline):
        assert self.n * 2 <= len(message.population) + 1, \
            "Population is too small for chosen amount of diff vectors!"
        selection_list = []
        for i, solution in enumerate(message.population):
            selected = set([message.base_solutions_indices[i]])
            while len(selected) < self.n * 2:
                selected.add(random.randint(0, len(message.population) - 1))
            selection_list.append([message.population[x] for x in
                                  sorted(list(selected))])
        message.selected = selection_list
        return message


class AncestorDifferenceSelector(pypline.Task):
    """
    implements a difference selector that occasionally selects a parent instead
    of a random solution from the population instead of the random solution itself

    Arguments:
    n -- The number of pairs to select from the population
    pr -- The probability that the selected solutions ancestor will be used instead
    """
    def __init__(self, n, pr):
        self.n = n
        self.pr = pr

    def process(self, message, pipeline):
        assert self.n * 2 <= len(message.population) + 1, \
            "Population is too small for chosen amount of diff vectors!"
        selection_list = []
        for i, solution in enumerate(message.population):
            selected = set([message.base_solutions_indices[i]])
            while len(selected) < self.n * 2:
                selected.add(random.randint(0, len(message.population) - 1))
            selected_solutions = []
            for j in sorted(list(selected)):
                if len(message.population[j].parents) > 0 \
                        and random.random() < self.pr:
                    selected_solutions.append(
                        random.choice(message.population[j].parents))
                else:
                    selected_solutions.append(message.population[j])
            selection_list.append(selected_solutions)
        message.selected = selection_list
        return message


class DeParentAllocator(pypline.Task):
    def process(self, message, pipeline):
        for i, solution in enumerate(message.trials):
            solution.parents = message.selected[i]
        return message
