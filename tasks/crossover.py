import pypline
import random


class BinomialCrossover(pypline.Task):
    def __init__(self, cr):
        self.cr = cr

    def process(self, message, pipeline):
        assert len(message.trials) == len(message.crossover_solutions), \
            "Trial vector count does not equal crossover solution count"
        for i in xrange(len(message.trials)):
            a = message.crossover_solutions[i]
            for j in xrange(len(message.trials[i].genes)):
                if random.random() > self.cr and i != j:
                    message.trials[i].genes[j] = a.genes[j]
        return message


class ExponentialCrossover(pypline.Task):
    def __init__(self, cr):
        self.cr = cr

    def process(self, message, pipeline):
        assert len(message.trials) == len(message.crossover_solutions), \
            "Trial vector count does not equal crossover solution count"
        for i in xrange(len(message.trials)):
            length = len(message.population[i].genes)
            index = random.randint(0, length - 1)
            a = message.crossover_solutions[i]
            for j in xrange(length):
                while random.random() < self.cr:
                    message.trials[i].genes[index] = a.genes[index]
                    index = (index + 1) % length
        return message
