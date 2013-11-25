import pypline


class BetterReplacer(pypline.Task):
    def process(self, message, pipeline):
        assert(len(message.population) == len(message.trials),
               "Population length and candidate length are not equal!")
        for i in xrange(len(message.population)):
            if message.trials[i].fitness < message.population[i].fitness:
                message.population[i] = message.trials[i]
        return message


class AllReplacer(pypline.Task):
    def process(self, message, pipeline):
        assert(len(message.population) == len(message.trials),
               "Population length and candidate length are not equal!")
        for i in xrange(len(message.population)):
            message.population[i] = message.trials[i]
        return message
