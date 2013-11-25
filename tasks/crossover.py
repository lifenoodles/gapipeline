import pypline
import random


class BinomialCrossover(pypline.Task):
    def __init__(self, cr):
        self.cr = cr

    def process(self, message, pipeline):
        for i in xrange(len(message.trials)):
            for j in xrange(len(message.population[i].genes)):
                if random.random() > self.cr and i != j:
                    message.trials[i][j] = message.population[i][j]
        return message
