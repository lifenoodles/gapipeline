import pypline


@pypline.requires("best")
class TerminalLogger(pypline.Task):
    def process(self, message, pipeline):
        print "Generation: %s" % message.generation
        print "Best: %s" % message.best
        print "Fitness: %f" % message.best.fitness
        return message


@pypline.requires("initialisation")
class PercentRemainingLogger(pypline.Task):
    def process(self, message, pipeline):
        import sys
        print "\r%.1f%%..." % message.percent,
        sys.stdout.flush()
        return message
