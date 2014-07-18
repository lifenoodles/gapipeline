import pypline
import cPickle


@pypline.requires("trials")
class ParentLogger(pypline.Task):
    def process(self, message, pipeline):
        for i, trial in enumerate(message.trials):
            print "%i: (%i parents) %s" % (i, len(trial.parents), trial)
            for parent in trial.parents:
                print parent
        return message


@pypline.requires("best")
class TerminalLogger(pypline.Task):
    def process(self, message, pipeline):
        print "Generation:%s" % message.generation,
        print " Fitness:%f" % message.best.fitness,
        avg_fitness = sum(x.fitness for x in message.population) \
            / len(message.population)
        print " Average:{}".format(avg_fitness)
        return message


@pypline.requires("initialisation")
class PercentRemainingLogger(pypline.Task):
    def process(self, message, pipeline):
        import sys
        print "\r%.1f%%..." % message.percent,
        sys.stdout.flush()
        return message


@pypline.requires("best")
class BestPickler(pypline.Task):
    def __init__(self, fileName="output.txt"):
        self._file = open(fileName, "w")

    def process(self, message, pipeline):
        cPickle.dump(message.best, self._file)
        return message
