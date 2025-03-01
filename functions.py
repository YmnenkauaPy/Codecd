import re

def Print(*text):
    result = re.findall(r"'(.*?)'", str(text))
    result2=''
    for i in range(len(result)):
        if (i) % 2!=0:
            result2 = result2 + result[i]
    result2 = result2[:-1]
    result2 = result2[1:]
    print(result2)

def print_var(text):
    print(text)

def factorial(n):
    res = 1
    i = 1
    while i < n:
        res *= i * (i + 1)
        i += 2
    if n % 2 == 1:
        res *= n
    print(res)
    return res

def count(text, exp):
    result = re.findall(r"'(.*?)'", str(exp))
    print(result, type(result))
    result2=''
    for i in range(len(result)):
        if (i) % 2!=0:
            for b in result[i]:
                if b == '!':
                    print(result2)
                    fact = []
                    for i in result2:
                        try:
                            fact.append(str(int(i)))
                        except:
                            fact.clear()

                    fact_ = factorial(int(''.join(fact)))
                    result2 = result2[:len(result2)-1] + str(fact_)

                if b != '!':
                    result2 = result2 + b
    try:
        return eval(result2)
    except ZeroDivisionError:
        error_div(text)

def error_sym(num_line,text):
    print('line: ' +str(num_line))
    print(text)
    print("SyntaxError: BadInput")

def error_div(text):
    print(text)
    print("DivError: Division By Zero")

def not_found(*text):
    print('NotFound: { '+str(text[0])+' }')
    print("in { " + text[1] + ' }')

def error_var(text):
    print('VarError: Variable { '+ str(text) +' } is not found')
