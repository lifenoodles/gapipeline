import pypline


@pypline.requires("population", "trials")
class BetterReplacer(pypline.Task):
    def process(self, message, pipeline):
        assert(len(message.population) == len(message.trials),
               "Population length and candidate length are not equal!")
        for i in xrange(len(message.population)):
            if message.trials[i].fitness < message.population[i].fitness:
                message.population[i] = message.trials[i]
        return message


@pypline.requires("population", "trials")
class AllReplacer(pypline.Task):
    def process(self, message, pipeline):
        assert(len(message.population) == len(message.trials),
               "Population length and candidate length are not equal!")
        message.population = list(message.trials)
        return message
