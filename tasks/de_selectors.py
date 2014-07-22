import pypline
import random


@pypline.requires("population")
@pypline.provides("crossover_solutions")
class CrossoverSelectorEach(pypline.Task):
    """
    implements a selector that chooses each individual in the population
    to be used for crossover
    """
    def process(self, message, pipeline):
        message.crossover_solutions = message.population[:]
        return message

    def getDescription(self):
        return {"selector": "Each"}


@pypline.requires("population", "ancestors")
@pypline.provides("crossover_solutions")
class CrossoverSelectorEachAncestor(pypline.Task):
    """
    implements a selector that chooses each individual in the population
    to be used for crossover

    Arguments:
    pr -- The probability that the selected solutions ancestor will
        be used instead
    """
    def __init__(self, pr):
        self.pr = pr

    def process(self, message, pipeline):
        crossover_solutions = []
        for solution in message.population:
            if random.random() < self.pr and solution.has_parents():
                crossover_solutions.append(random.choice(solution.parents))
            else:
                crossover_solutions.append(solution)
        message.crossover_solutions = crossover_solutions
        assert len(crossover_solutions) == len(message.population), \
            "crossover_solutions length must be equal to population length."
        return message

    def getDescription(self):
        return {"selector": "Each w/ Ancestor", "replacement_rate": self.pr}


@pypline.requires("population")
@pypline.provides("base_solutions", "base_solutions_indices")
class BestSelector(pypline.Task):
    """
    implements a selector that chooses the best individual in the population
    to be the base for every crossover event
    """
    def process(self, message, pipeline):
        best_index, best = min(enumerate(message.population),
                               key=lambda x, y: y.fitness)
        message.base_solutions = [
            best for i in xrange(len(message.population))]
        message.base_solutions_indices = [
            best_index for i in xrange(len(message.population))]
        return message

    def getDescription(self):
        return {"selector": "Best"}


@pypline.requires("population")
@pypline.provides("base_solutions", "base_solutions_indices")
class RandomSelector(pypline.Task):
    """
    implements a selector that chooses a random individual in the population
    to be the base for every crossover event
    """
    def process(self, message, pipeline):
        base_solutions = []
        base_solutions_indices = []
        for i in xrange(len(message.population)):
            rand = random.randint(0, len(message.population) - 1)
            # make sure that the base vector is not i
            while rand == i:
                rand = random.randint(0, len(message.population) - 1)
            base_solutions.append(message.population[rand])
            base_solutions_indices.append(rand)
        message.base_solutions = base_solutions
        message.base_solutions_indices = base_solutions_indices
        return message

    def getDescription(self):
        return {"selector": "Random"}


@pypline.requires("population", "base_solutions",
                  "base_solutions_indices")
@pypline.provides("difference_solutions")
class DifferenceSelector(pypline.Task):
    """
    implements a selector that chooses a set of individuals in the
    population to be used for difference vector generation

    Arguments:
    n -- The target number of difference vectors
    """
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
            selected_list = list(selected)
            random.shuffle(selected_list)
            selection_list.append([
                message.population[x] for x in selected_list])
        message.difference_solutions = selection_list
        assert len(message.difference_solutions[0]) == self.n * 2, \
            "Incorrect number of solutions selected for difference" \
            "vector generation, expected {}, but found {}".format(
                (self.n * 2, len(message.difference_solutions[0])))
        return message

    def getDescription(self):
        return {"difference_selector": "Random", "difference_n": self.n}


@pypline.requires("population", "base_solutions",
                  "base_solutions_indices")
@pypline.provides("difference_solutions")
class DifferenceSelectorAncestor(pypline.Task):
    """
    implements a difference selector that occasionally selects a
    parent of a random solution from the population instead of the
    random solution itself

    Arguments:
    n -- The number of pairs to select from the population
    pr -- The probability that the selected solutions ancestor will be
        used instead
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
            selected_list = list(selected)
            random.shuffle(selected_list)
            selected_solutions = []
            for j in selected_list:
                if message.population[j].has_parents() \
                        and random.random() <= self.pr:
                    selected_solutions.append(
                        random.choice(message.population[j].parents))
                else:
                    selected_solutions.append(message.population[j])
            selection_list.append(selected_solutions)
        message.difference_solutions = selection_list
        assert len(message.difference_solutions[0]) == self.n * 2, \
            "Incorrect number of solutions selected for difference vector" \
            "generation, expected %d, but found %d" % \
            (self.n * 2, len(message.difference_solutions[0]))
        return message

    def getDescription(self):
        return {"difference_selector": "Random", "difference_n": self.n,
                "difference_replacement_rate": self.pr}


@pypline.requires("population", "base_solutions",
                  "base_solutions_indices")
@pypline.provides("difference_solutions")
class DeDifferenceSelectorPool(pypline.Task):
    pass


@pypline.requires("difference_solutions", "trials")
@pypline.provides("ancestors")
class DeParentAllocatorDifference(pypline.Task):
    """
    allocates parents to solutions from the difference vector pool
    """
    def process(self, message, pipeline):
        for i, trial in enumerate(message.trials):
            trial.parents = message.difference_solutions[i]
        return message

    def getDescription(self):
        return {"parent_allocation": "Difference Vector"}


@pypline.requires("crossover_solutions", "trials")
@pypline.provides("ancestors")
class DeParentAllocatorCrossover(pypline.Task):
    """
    allocates parents to solutions from the crossover pool
    """
    def __init__(self, u):
        self.u = u

    def process(self, message, pipeline):
        for cs, bs, trial in zip(
                message.crossover_solutions,
                message.base_solutions,
                message.trials):
            if not trial.has_parents() or random.random() < self.u:
                trial.parents = [cs, bs]
            else:
                trial.parents = random.choice([cs, bs]).parents
        return message

    def getDescription(self):
        return {"parent_allocation": "Crossover"}
