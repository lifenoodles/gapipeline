class Parameter(object):
    """
    >>> p = Parameter(int, "Name")
    >>> p.is_ok(2)
    True
    >>> p.is_ok(3.4)
    True
    >>> p.is_ok("Hi")
    False
    """
    def __init__(self, typ, name):
        self.type = typ
        self.name = name

    def is_ok(self, param):
        try:
            self.type(param)
            return True
        except:
            return False


if __name__ == "__main__":
    import doctest
    doctest.testmod()
