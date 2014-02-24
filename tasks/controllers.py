import pypline


@pypline.requires("initialisation")
class GenerationController(pypline.Task):
    """
    Generational controller, signals the end of the algorithm if it falls to
    0 generations or reaches target fitness
    """
    epsilon = 10e-7

    def __init__(self, generations):
        self.generations = generations
        self.starting_generations = generations

    def process(self, message, pipeline):
        assert message.generation <= self.generations, \
            "%d is greater than cutoff of %d." % \
            (message.generation, self.generations)
        if message.best is not None \
            and (abs(message.best.fitness - message.target_fitness) \
                < GenerationController.epsilon or \
                message.best.fitness < message.target_fitness):
            return True
        message.generation += 1
        message.percent = float(message.generation) / \
            float(self.generations) * 100
        return message.generation > self.generations

    def getDescription(self):
        return {"controller": "Generation Controller",
                "generations": self.starting_generations}
