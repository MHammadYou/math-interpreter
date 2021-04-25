import unittest
from tokens import Token, TokenType
from parser_ import Parser
from nodes import *


class TestParser(unittest.TestCase):

    def test_empty_tokens(self):
        tokens = []
        node = self.get_parsed_val(tokens)
        self.assertEqual(node, None)

    def test_numbers(self):
        tokens = [Token(TokenType.NUMBER, 45.320)]
        node = self.get_parsed_val(tokens)
        self.assertEqual(node, NumberNode(45.320))

    def test_operations(self):
        tokens = [
            Token(TokenType.NUMBER, 23),
            Token(TokenType.PLUS),
            Token(TokenType.NUMBER, 47),
        ]
        node = self.get_parsed_val(tokens)
        self.assertEqual(node, AddNode(NumberNode(23), NumberNode(47)))

        tokens = [
            Token(TokenType.NUMBER, 23),
            Token(TokenType.MINUS),
            Token(TokenType.NUMBER, 47),
        ]
        node = self.get_parsed_val(tokens)
        self.assertEqual(node, SubtractNode(NumberNode(23), NumberNode(47)))

        tokens = [
            Token(TokenType.NUMBER, 23),
            Token(TokenType.MULTIPLY),
            Token(TokenType.NUMBER, 47),
        ]
        node = self.get_parsed_val(tokens)
        self.assertEqual(node, MultiplyNode(NumberNode(23), NumberNode(47)))

        tokens = [
            Token(TokenType.NUMBER, 23),
            Token(TokenType.DIVIDE),
            Token(TokenType.NUMBER, 47),
        ]
        node = self.get_parsed_val(tokens)
        self.assertEqual(node, DivideNode(NumberNode(23), NumberNode(47)))

    def test_expression(self):
        tokens = [
            # 27 + (43 / 36 - 48) * 51
            Token(TokenType.NUMBER, 27.0),
            Token(TokenType.PLUS),
            Token(TokenType.LPAREN),
            Token(TokenType.NUMBER, 43.0),
            Token(TokenType.DIVIDE),
            Token(TokenType.NUMBER, 36.0),
            Token(TokenType.MINUS),
            Token(TokenType.NUMBER, 48.0),
            Token(TokenType.RPAREN),
            Token(TokenType.MULTIPLY),
            Token(TokenType.NUMBER, 51.0),
        ]

        node = self.get_parsed_val(tokens)
        self.assertEqual(node,
            AddNode(
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
        )

    @staticmethod
    def get_parsed_val(_tokens):
        return Parser(_tokens).parse()
