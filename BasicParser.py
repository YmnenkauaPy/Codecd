from rply import ParserGenerator
from functions import Print, factorial, count, print_var, error_var
import re

variables = {}

class Parser():
    def __init__(self):
        self.pg = ParserGenerator(
            # Список всех токенов, принятых парсером
            ['STR', 'PRINT', 'VAR', 'EXP',
             'COLON', 'COMM', 'EQUAL']
        )

    def parse(self, line):
        global variables
        @self.pg.production('program : COMM')
        def program(line, p):
            pass

        @self.pg.production('program : VAR EQUAL STR')
        def program(line, p):
            result = re.findall(r"'(.*?)'", str(p))
            result2 = []
            for i in range(len(result)):
                if i == 1:
                    result[i] = result[i].replace(' ', '')
                    result2.append(result[i])
                elif i == 5:
                    result[i] = result[i][:-1]
                    result[i] = result[i][1:]
                    result2.append(result[i])

            variables[result2[0]] = result2[1]
            return variables

        @self.pg.production('program : VAR EQUAL EXP')
        def program(line,p):
            result = re.findall(r"'(.*?)'", str(p))
            for i in range(len(result)):
                if i == 1:
                    result[i] = result[i].replace(' ', '')
                    variables[result[i]] = count(p, p[2])
            return variables

        @self.pg.production('program : VAR EQUAL VAR')
        def program(line, p):
            result = re.findall(r"'(.*?)'", str(p))
            if result[5] in variables.keys():
                result2 =''
                for i in range(len(result)):
                    if i == 1:
                        result[i] = result[i].replace(' ', '')
                        result2=result[i]
                    if i == 5:
                        variables[result2] = variables[result[i]]
                return variables
            else:
                return error_var(result2[i])


        @self.pg.production('program : PRINT COLON VAR')
        def program(line, p):
            for i in variables:
                result = re.findall(r"'(.*?)'", str(p))
                for b in range(len(result)):
                    if b == 5:
                        if result[b] == i:
                            return print_var(variables[i])
            return error_var(result[b])

        @self.pg.production('program : PRINT COLON STR')
        def program(line, p):
            return Print(p[2])

        @self.pg.production('program : PRINT COLON EXP')
        def program(line,p):
            print(p, p[2])
            print(count(p, p[2]))

    def get_parser(self):
        return self.pg.build()