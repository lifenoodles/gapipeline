import pypline
import math
import random


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
class DeJongThreeEvaluator(pypline.Task):
    """
    DejongThree function evaluator
    """
    def process(self, message, pipeline):
        for solution in message.trials:
            fitness = 6 * len(solution.genes)
            for gene in solution.genes:
                fitness += math.floor(gene)
            solution.fitness = fitness
            if message.best is None or solution.fitness < message.best.fitness:
                message.best = solution
        return message

    def getDescription(self):
        return { "problem": "Dejong3" }


@pypline.requires("trials")
@pypline.provides("best")
class DeJongFourEvaluator(pypline.Task):
    """
    DejongFour modified as per Storn95
    """
    def process(self, message, pipeline):
        for solution in message.trials:
            fitness = 0
            for i, gene in enumerate(solution.genes):
                fitness += (gene ** 4) * (i + 1) + random.random()
            solution.fitness = fitness
            if message.best is None or solution.fitness < message.best.fitness:
                message.best = solution
        return message

    def getDescription(self):
        return { "problem": "Dejong3" }


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


@pypline.requires("trials")
@pypline.provides("best")
class PolynomialFittingEvaluator(pypline.Task):
    """
    Polynomial fitting evaluator for clogj * z^j for j = (0..2k)
    """
    def fc(self, cs, z):
        f = 0
        for j, c in enumerate(cs):
            f += c * (z ** j)

    def t2k(self, z):


    def process(self, message, pipeline):
        for solution in message.trials:
            fitness = 0
            for p in xrange(100):
                pi = random.random() * 2 - 1
                # compute fc(pi)
                fcpi = self.fc(solution.genes, pi)
                if -1 > fcpi or fcpi > 1:
                    fitness += (1 - fcpi) ** 2
            fcpi = fc(solution.genes, 1.2)


            fcpi = fc(solution.genes, -1.2)

            solution.fitness = fitness
            if message.best is None or solution.fitness < message.best.fitness:
                message.best = solution
        return message

    def getDescription(self):
        return { "problem": "RastriginSix" }
