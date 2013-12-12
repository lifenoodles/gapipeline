import pypline
import random


@pypline.requires("crossover_solutions", "trials")
class BinomialCrossover(pypline.Task):
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


@pypline.requires("crossover_solutions", "trials")
class ExponentialCrossover(pypline.Task):
    def __init__(self, cr):
        self.cr = cr

    def process(self, message, pipeline):
        assert len(message.trials) == len(message.crossover_solutions), \
            "Trial vector count does not equal crossover solution count"
        for i, trial in enumerate(message.trials):
            length = len(trial.genes)
            index = random.randint(0, length - 1)
            c = message.crossover_solutions[i]
            for j in xrange(length):
                while random.random() > self.cr:
                    trial.genes[index] = c.genes[index]
                    index = (index + 1) % length
        return message
