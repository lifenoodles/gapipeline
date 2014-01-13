import pypline
import sys
sys.path.append("tasks")
import representations


@pypline.requires("difference_solutions", "base_solutions")
@pypline.provides("trials")
class DeMutator(pypline.Task):
    def __init__(self, f):
        self.f = f

    def process(self, message, pipeline):
        for i in xrange(len(message.population)):
            diff_vector = []
            solution_size = len(message.population[i].genes)
            diff_count = len(message.difference_solutions[i])
            for j in xrange(solution_size):
                diff = 0
                for k in range(diff_count // 2):
                    diff += message.difference_solutions[i][k].genes[j]
                for k in range(diff_count // 2, diff_count):
                    diff -= message.difference_solutions[i][k].genes[j]
                diff_vector.append(diff)
            trial = representations.Solution()
            trial.genes = [x + (self.f * y)
                           for x, y in
                           zip(message.base_solutions[i].genes, diff_vector)]
            trial.generation = message.generation
            message.trials[i] = trial
        return message
