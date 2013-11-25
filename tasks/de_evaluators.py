import pypline


class DeJongOneEvaluator(pypline.Task):
    def process(self, message, pipeline):
        for solution in message.candidates:
            fitness = 0
            for gene in solution.genes:
                fitness += gene * gene
            solution.fitness = fitness
        return message
