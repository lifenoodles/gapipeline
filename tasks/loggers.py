import pypline


class TerminalLogger(pypline.Task):
    def process(self, message, pipeline):
        print "Generation: %s" % message.generation
        print "Best: %s" % message.best
        print "Parents: %d" % len(message.best.parents)
        print "Fitness: %f" % message.best.fitness
        return message
