import pypline
import random


@pypline.requires("crossover_solutions", "trials")
class BinomialCrossover(pypline.Task):
    """
    Implements binomial crossover. This is effectively the same as uniform
    crossover in a standard GA
    """
    def __init__(self, cr):
        self.cr = cr

    def process(self, message, pipeline):
        assert len(message.trials) == len(message.crossover_solutions), \
            "Trial vector count does not equal crossover solution count"
        for i, trial in enumerate(message.trials):
            c = message.crossover_solutions[i]
            for j in xrange(len(trial.genes)):
                if random.random() > self.cr and i != j:
                    trial.genes[j] = c.genes[j]
        return message

    def getDescription(self):
        return { "crossover_type": "Binomial Crossover", "CR": self.cr }


@pypline.requires("crossover_solutions", "trials")
class ExponentialCrossover(pypline.Task):
    """
    Implements exponentioal crossover. This is effectively the same as point
    based crossover in a standard GA
    """
    def __init__(self, cr):
        self.cr = cr

    def process(self, message, pipeline):
        assert len(message.trials) == len(message.crossover_solutions), \
            "Trial vector count does not equal crossover solution count"
        for i, trial in enumerate(message.trials):
            length = len(trial.genes)
            index = random.randint(0, length - 1)
            count = 0
            c = message.crossover_solutions[i]
            while random.random() <= self.cr and count < length:
                index = (index + 1) % length
                count += 1
            while count < length:
                trial.genes[index] = c.genes[index]
                index = (index + 1) % length
                count += 1
        return message

    def getDescription(self):
        return { "crossover_type": "Exponential Crossover", "CR": self.cr }
