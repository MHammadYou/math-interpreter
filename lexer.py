from tokens import Token, TokenType


class Lexer(object):

    WHITESPACE = ' \n\t'
    DIGITS = '0123456789'

    def __init__(self, text):
        self.text = iter(text)
        self.move_to_next()

    def move_to_next(self):
        try:
            self.current_char = next(self.text)
        except StopIteration:
            self.current_char = None

    def generate_tokens(self):
        while self.current_char is not None:

            if self.current_char in self.WHITESPACE:
                self.move_to_next()

            elif self.current_char == '.' or self.current_char in self.DIGITS:
                yield self.generate_number()

    def generate_number(self):
        number_str = self.current_char
        decimal_point_count = 0

        self.move_to_next()

        while self.current_char is not None and (self.current_char == '.' or self.current_char in self.DIGITS):
            if self.current_char == '.':
                decimal_point_count += 1

                if decimal_point_count > 1:
                    break

            number_str += self.current_char
            self.move_to_next()

        if number_str.startswith('.'):
            number_str = f'0{number_str}'

        if number_str.endswith('.'):
            number_str += 0

        return Token(TokenType.NUMBER, float(number_str))
