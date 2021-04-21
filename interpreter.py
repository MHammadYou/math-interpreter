from nodes import *
from values import Number


class Interpreter(object):
    def visit(self, node):
        method_name = f'visit_{type(node).__name__}'
        method = getattr(self, method_name)

        return method(node)
