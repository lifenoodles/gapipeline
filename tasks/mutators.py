import pypline
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
                for k in range(len(diff_count // 2)):
                    diff += message.population[message.selected[k]]
                for k in range(len(diff_count // 2), len(diff_count)):
                    diff -= message.population[message.selected[k]]
                diff_vector.append[diff]
            trial = representations.Solution()
            base_solution = message.population[message.base_solutions[i]]
            trial.genes = [x + (self.f * y)
                           for x, y in zip(base_solution.genes, diff_vector)]
            trial.generation = message.generation
            message.trials[i] = trial
        return message
