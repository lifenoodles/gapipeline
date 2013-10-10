import abc
from task import Task, Parameter, ParameterisedMixin, MemoryUnitsMixin

class GaTask(Task, ParameterisedMixin, MemoryUnitsMixin):
    __metaclass__ = abc.ABCMeta

class Test(GaTask):
    def __init__(self):
        pass

    def __call__(self, message):
        print "Test executed"

    def parameter_list(self):
        return []


class Test2(GaTask):
    def __init__(self, param):
        self.param = param

    def __call__(self, message):
        print "Test 2 executed: %s" % str(self.param)

    def parameter_list(self):
        return [Parameter(int, "Test Parameter")]

    def requires(self):
        return [True]


if __name__ == "__main__":
    import doctest
    doctest.testmod()
