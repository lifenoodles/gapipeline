import pypline


@pypline.requires("initialisation")
class GenerationController(pypline.Task):
    epsilon = 10e-7

    def __init__(self, generations):
        self.generations = generations

    def process(self, message, pipeline):
        assert message.generation <= self.generations, \
            "%d is greater than cutoff of %d." % \
            (message.generation, self.generations)
        if message.best is not None \
            and abs(message.best.fitness - message.target_fitness) \
                < GenerationController.epsilon:
            return True
        message.generation += 1
        return message.generation > self.generations
