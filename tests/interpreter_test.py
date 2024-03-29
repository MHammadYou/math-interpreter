import unittest
from src.nodes import *
from src.interpreter import Interpreter
from src.values import Number


class TestInterpreter(unittest.TestCase):

    def test_numbers(self):
        value = self.get_value(NumberNode(51.2))
        self.assertEqual(value, Number(51.2))

    def test_operators(self):
        value = self.get_value(AddNode(NumberNode(27), NumberNode(14)))
        self.assertEqual(value, Number(41))

        value = self.get_value(SubtractNode(NumberNode(27), NumberNode(14)))
        self.assertEqual(value, Number(13))

        value = self.get_value(MultiplyNode(NumberNode(5), NumberNode(7)))
        self.assertEqual(value, Number(35))

        value = self.get_value(DivideNode(NumberNode(35), NumberNode(5)))
        self.assertEqual(value, Number(7))

        with self.assertRaises(Exception):
            self.get_value(DivideNode(NumberNode(5), NumberNode(0)))

    def test_expression(self):
        tree = AddNode(
                NumberNode(27),
                MultiplyNode(
                    SubtractNode(
                        DivideNode(
                            NumberNode(43), NumberNode(36)
                        ),
                        NumberNode(48)
                    ),
                    NumberNode(51)
                )
            )
        value = self.get_value(tree)
        self.assertEqual(value, Number(-2360.0833333333335))

    def test_expression_2(self):
        # expression => (25 / 5 + 5) / (5 * 2)
        tree = DivideNode(
            AddNode(
                DivideNode(
                    NumberNode(25), NumberNode(5)
                ),
                NumberNode(5)
            ),
            MultiplyNode(
                NumberNode(5), NumberNode(2)
            )
        )
        value = self.get_value(tree)
        self.assertEqual(value, Number(1.0))

    @staticmethod
    def get_value(node):
        return Interpreter().visit(node)
