import pypline


class BetterReplacer(pypline.Task):
    def process(self, message, pipeline):
        assert(len(message.population) == len(message.candidates),
               "Population length and candidate length are not equal!")
        for i in xrange(len(message.population)):
            if message.candidates[i].fitness < message.population[i].fitness:
                message.population[i] = message.candidates[i]
        return message
