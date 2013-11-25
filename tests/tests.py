import unittest
import sys
sys.path.append("../tasks")
import de_initialisers
import de_evaluators


class InitialiserTester(unittest.TestCase):
    def test_dejong_one(self):
        init = de_initialisers.DeJongOneInitialiser(10, 10)
        message = init.process(None, None)
        self.assertIsNotNone(message.best)
        self.assertEquals(len(message.best.genes), 10)
        self.assertEquals(len(message.candidates), 10)


class EvaluatorTester(unittest.TestCase):
    def setUp(self):
        self.message = de_initialisers.DeJongOneInitialiser(10, 10).process(None, None)

    def test_dejong_one_evaluator(self):
        evaluator = de_evaluators.DeJongOneEvaluator()
        self.message = evaluator.process(self.message, None)
        for solution in self.message.population:
            self.assertIsNotNone(solution.fitness)

if __name__ == "__main__":
    unittest.main()
