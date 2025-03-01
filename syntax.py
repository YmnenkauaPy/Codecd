from BasicParser import *
from BasicLexer import Lexer
import os
from rply.errors import ParsingError, LexingError
from functions import error_sym, not_found

dir = os.path.join(os.path.dirname(__file__))
for file in os.listdir(dir):
    if file.endswith(".cd"):
        with open(file, 'r', encoding='utf-8') as f:
            text = f.read()

lexer = Lexer().get_lexer()
pg = Parser()
text = text.splitlines()
pg.parse('line')
parser = pg.get_parser()
for line in text:
    if line: 
        tokens = lexer.lex(line)
        try:
            parser.parse(tokens, line)
        except ParsingError:
            num_line = text.index(line)
            error_sym(num_line,line)
        except LexingError as e:
            source_pos = e.getsourcepos()
            if source_pos is not None:
                idx = source_pos.idx
                lines = text.index(line)
                colno = source_pos.colno
                symbol = text[lines][idx] 
                not_found(symbol, line)