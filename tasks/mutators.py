import pypline
import sys
sys.path.append("tasks")
import representations


class DeMutator(pypline.Task):
    def __init__(self, f):
        self.f = f

    def process(self, message, pipeline):
        for i in xrange(len(message.population)):
            diff_vector = []
            solution_size = len(message.population[i].genes)
            diff_count = len(message.selected[i])
            for j in xrange(solution_size):
                diff = 0
                for k in range(diff_count // 2):
                    diff += message.selected[i][k]
                for k in range(diff_count // 2, diff_count):
                    diff -= message.selected[i][k]
                diff_vector.append(diff)
            trial = representations.Solution()
            trial.genes = [x + (self.f * y)
                           for x, y in
                           zip(message.base_solutions[i].genes, diff_vector)]
            trial.generation = message.generation
            message.trials[i] = trial
        return message
