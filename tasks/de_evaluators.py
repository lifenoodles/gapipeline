import pypline
import math


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


@pypline.requires("trials")
@pypline.provides("best")
class DeJongTwoEvaluator(pypline.Task):
    """
    DejongTwo function evaluator
    """
    def process(self, message, pipeline):
        for solution in message.trials:
            fitness = 0
            genes = solution.genes
            for i in xrange(len(solution.genes) - 1):
                fitness += (100 * (genes[i] - genes[i + 1]**2)**2) + (1 - genes[i])**2
            solution.fitness = fitness
            if message.best is None or solution.fitness < message.best.fitness:
                message.best = solution
        return message

    def getDescription(self):
        return { "problem": "Dejong2" }


@pypline.requires("trials")
@pypline.provides("best")
class RastriginSixEvaluator(pypline.Task):
    """
    RastriginSix function evaluator
    """
    def process(self, message, pipeline):
        for solution in message.trials:
            genes = solution.genes
            fitness = 10 * len(genes)
            for i in xrange(len(solution.genes)):
                fitness += genes[i]**2 - (10 * math.cos(2 * math.pi * genes[i]))
            solution.fitness = fitness
            if message.best is None or solution.fitness < message.best.fitness:
                message.best = solution
        return message

    def getDescription(self):
        return { "problem": "RastriginSix" }
