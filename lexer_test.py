import unittest
from tokens import TokenType, Token
from lexer import Lexer


class TestLexer(unittest.TestCase):

    def test_empty_string(self):
        tokens = list(Lexer("").generate_tokens())
        self.assertEqual(tokens, [])

        tokens = list(Lexer("\n \t  ").generate_tokens())
        self.assertEqual(tokens, [])

    def test_numbers(self):
        tokens = list(Lexer("123 123.455 123. .456 .").generate_tokens())

        self.assertEqual(tokens, [
            Token(TokenType.NUMBER, 123.000),
            Token(TokenType.NUMBER, 123.455),
            Token(TokenType.NUMBER, 123.000),
            Token(TokenType.NUMBER, 000.455),
            Token(TokenType.NUMBER, 000.000),
        ])
