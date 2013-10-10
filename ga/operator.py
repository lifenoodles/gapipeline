import abc
from parameter import Parameter


class Operator(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def execute(self, memory):
        raise NotImplementedError

    @abc.abstractmethod
    def parameter_list(self):
        raise NotImplementedError


class TestOperator(Operator):
    def __init__(self):
        pass

    def execute(self, memory):
        print "Test executed"

    def parameter_list(self):
        return []


class TestOperator2(Operator):
    def __init__(self, param):
        self.param = param

    def execute(self, memory):
        print "Test 2 executed: %s" % str(self.param)

    def parameter_list(self):
        return [Parameter(int, "Test Parameter")]


if __name__ == "__main__":
    import doctest
    doctest.testmod()

