import pypline
import random


class BinomialCrossover(pypline.Task):
    def __init__(self, cr):
        self.cr = cr

    def process(self, message, pipeline):
        for i in xrange(len(message.trials)):
            for j in xrange(len(message.trials[i].genes)):
                if random.random() > self.cr and i != j:
                    message.trials[i].genes[j] = message.population[i].genes[j]
        return message


class ExponentialCrossover(pypline.Task):
    def __init__(self, cr):
        self.cr = cr

    def process(self, message, pipeline):
        for i in xrange(len(message.trials)):
            length = len(message.population[i].genes)
            index = random.randint(0, length - 1)
            for j in xrange(length):
                while random.random() < self.cr:
                    message.trials[index].genes[j] = message.population[index].genes[j]
                    index = (index + 1) % length
        return message
