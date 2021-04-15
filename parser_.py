from tokens import TokenType
from nodes import NumberNode, AddNode, SubtractNode, MultiplyNode, DivideNode


class Parser:
    def __init__(self, tokens):
        self.tokens = iter(tokens)
        self.move_to_next()

    def move_to_next(self):
        try:
            self.current_token = next(self.tokens)
        except StopIteration:
            self.current_token = None

    def parse(self):
        if self.current_token is None:
            return None

        result = self.expr()

        if self.current_token is not None:
            raise Exception("Invalid Syntax")

        return result

    def expr(self):
        result = self.term()

        while self.current_token is not None and self.current_token.token_type in (TokenType.PLUS, TokenType.MINUS):

            if self.current_token.token_type == TokenType.PLUS:
                self.move_to_next()
                result = AddNode(result, self.term())

            elif self.current_token.token_type == TokenType.MINUS:
                self.move_to_next()
                result = SubtractNode(result, self.term())

        return result

    def term(self):
        result = self.factor()

        print(self.current_token.token_type)
        while self.current_token is not None and self.current_token.token_type in (TokenType.MULTIPLY, TokenType.DIVIDE):


            if self.current_token.token_type == TokenType.MULTIPLY:
                self.move_to_next()
                result = MultiplyNode(result, self.factor())

            elif self.current_token.token_type == TokenType.DIVIDE:
                self.move_to_next()
                result = DivideNode(result, self.factor())

            return result

    def factor(self):

        token = self.current_token

        if token.token_type == TokenType.NUMBER:
            self.move_to_next()
            return NumberNode(token.value)

        raise Exception("Invalid Syntax")
