import pypline


class GeneralController(pypline.Task):
    epsilon = 10e-7

    def __init__(self, generations):
        self.generations = generations

    def process(self, message, pipeline):
        if message.best is not None \
            and abs(message.best.fitness - message.target_fitness) \
                < GeneralController.epsilon:
            return True
        terminate = message.generation == self.generations
        message.generation += 1
        return terminate
