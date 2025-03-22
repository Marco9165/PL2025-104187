import sys
import ply.lex as lex

# Analisador léxico

literals = ['+', '-', '*', '/', '(', ')']
tokens = ['NUMBER']

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

t_ignore = ' \t\r'

def t_error(t):
    raise ValueError()

lexer = lex.lex()

# Parte sintática

def parse(tokens):
    def rec_expr():
        nonlocal tokens
        node = rec_term()
        while tokens and tokens[0].type in ['+', '-']:
            operator = tokens.pop(0).value
            node = (operator, node, rec_term())
        return node
    
    def rec_term():
        nonlocal tokens
        node = rec_factor()
        while tokens and tokens[0].type in ['*', '/']:
            operator = tokens.pop(0).value
            node = (operator, node, rec_factor())
        return node
    
    def rec_factor():
        nonlocal tokens
        if not tokens:
            raise ValueError()
        token = tokens.pop(0)
        if token.type == 'NUMBER':
            return token.value
        elif token.type == '(':
            node = rec_expr()
            if not tokens or tokens[0].type != ')':
                raise ValueError()
            tokens.pop(0)  # Consumir ')'
            return node
        else:
            raise ValueError()
    
    return rec_expr()

# Parte semântica

def evaluate(tree):
    if isinstance(tree, int):
        return tree
    op, left, right = tree
    left_val = evaluate(left)
    right_val = evaluate(right)
    if op == '+':
        return left_val + right_val
    elif op == '-':
        return left_val - right_val
    elif op == '*':
        return left_val * right_val
    elif op == '/':
        return left_val / right_val
    else:
        raise ValueError()

if __name__ == '__main__':
    while True:
        try:
            expr = input("Escreva uma expressão: ")
            lexer.input(expr)
            tokens = list(iter(lexer.token, None))
            tree = parse(tokens)
            res = evaluate(tree)
            print(f"{expr} = {res}")
        except ValueError:
            print(f'Expressão inválida: {expr}', file=sys.stderr)
        except EOFError:
            break
