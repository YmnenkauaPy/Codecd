from rply import LexerGenerator

class Lexer():
    def __init__(self):
        self.lexer = LexerGenerator()

    def add_tokens(self):
        # Комментарии
        self.lexer.add('COMM', '(.*)--.*$')
        # Команды
        self.lexer.add('PRINT', r'write')
        # Элементы
        self.lexer.add('COLON', r'\:')
        # Операторы
        self.lexer.add('EQUAL', r'\=')
        # строки, числа
        self.lexer.add('EXP', r'[\d+*/()! -]+')
        self.lexer.add('STR', r'\[[^]]+\]')
        self.lexer.add('VAR', r'''[a-zA-Z-_]+''')
        # Игнор
        self.lexer.ignore('\s+')

    def get_lexer(self):
        self.add_tokens()
        return self.lexer.build()