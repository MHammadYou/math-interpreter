

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
        pass
