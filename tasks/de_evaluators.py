import pypline


class DeJongOneEvaluator(pypline.Task):
    def process(self, message, pipeline):
        for solution in message.population:
            print solution
