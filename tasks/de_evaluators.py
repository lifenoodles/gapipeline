import pypline


@pypline.requires("trials")
@pypline.provides("best")
class DeJongOneEvaluator(pypline.Task):
    """
    DejongOne function evaluator, unimodal function so trivial to solve optimally
    """
    def process(self, message, pipeline):
        for solution in message.trials:
            fitness = 0
            for gene in solution.genes:
                fitness += gene * gene
            solution.fitness = fitness
            if message.best is None or solution.fitness < message.best.fitness:
                message.best = solution
        return message

    def getDescription(self):
        return { "problem": "Dejong1" }
