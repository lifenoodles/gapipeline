import pypline


class TerminalLogger(pypline.Task):
    def process(self, message, pipeline):
        print "Generation: %s" % message.generation
        print "Best: %s" % message.best
        print "Fitness: %f" % message.best.fitness
        return message
