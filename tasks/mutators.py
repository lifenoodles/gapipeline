import pypline
import sys
sys.path.append("tasks")
sys.path.append("math")
import representations
import vector


@pypline.requires("difference_solutions", "base_solutions")
@pypline.provides("trials")
class DeMutator(pypline.Task):
    """
    Standard DE mutation, generates trial vectors based on difference solutions
    (i.e. solutions selected to be used to generate difference vectors) used
    to perturb base solutions (e.g. rand, best etc.)
    """
    def __init__(self, f):
        self.f = f

    def process(self, message, pipeline):
        assert len(message.base_solutions) == \
            len(message.difference_solutions) == \
            len(message.population), \
            "population, base solutions and difference solutions must" \
            "have equal length"
        for i in xrange(len(message.population)):
            diff_count = len(message.difference_solutions[i])
            diff_vector = message.difference_solutions[i][0].genes
            for k in range(1, diff_count // 2):
                diff_vector = vector.add_vector(
                    diff_vector, message.difference_solutions[i][k].genes)
            for k in range(diff_count // 2, diff_count):
                diff_vector = vector.subtract_vector(
                    diff_vector, message.difference_solutions[i][k].genes)
            trial = representations.Solution()
            trial.genes = vector.add_vector(
                message.base_solutions[i].genes,
                vector.multiply_scalar(diff_vector, self.f))
            trial.generation = message.generation
            message.trials[i] = trial
        assert len(message.population) == len(message.trials), \
            "population and trials must be of equal length"
        return message

    def getDescription(self):
        return {"mutation_type": "Standard Mutation", "mutation_rate": self.f}
