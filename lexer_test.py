import unittest
from tokens import TokenType, Token
from lexer import Lexer


class TestLexer(unittest.TestCase):

    def test_empty_string(self):
        tokens = self.get_tokens("")
        self.assertEqual(tokens, [])

        tokens = self.get_tokens("\n \t  ")
        self.assertEqual(tokens, [])

    def test_numbers(self):
        tokens = self.get_tokens("123 123.455 123. .456 .")

        self.assertEqual(tokens, [
            Token(TokenType.NUMBER, 123.000),
            Token(TokenType.NUMBER, 123.455),
            Token(TokenType.NUMBER, 123.000),
            Token(TokenType.NUMBER, 000.456),
            Token(TokenType.NUMBER, 000.000),
        ])

    def test_operators(self):
        tokens = self.get_tokens("+-*/")

        self.assertEqual(tokens, [
            Token(TokenType.PLUS),
            Token(TokenType.MINUS),
            Token(TokenType.MULTIPLY),
            Token(TokenType.DIVIDE),
        ])

    def test_parens(self):
        tokens = self.get_tokens("()")

        self.assertEqual(tokens, [
            Token(TokenType.LPAREN),
            Token(TokenType.RPAREN)
        ])

    def test_all(self):
        tokens = self.get_tokens("27 + (43 / 36 - 48) * 51")

        self.assertEqual(tokens, [
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
        ])

    @staticmethod
    def get_tokens(_str):
        return list(Lexer(_str).generate_tokens())
