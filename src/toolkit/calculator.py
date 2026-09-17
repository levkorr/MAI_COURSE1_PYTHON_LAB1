from errors import *
from tokenizer import *
from validator import *

def calculate(rpn_tokens):
    stack = []

    for token in rpn_tokens:
        if token.lstrip("+-").isdigit() or "." in token:
            stack.append(float(token))
        else:
            b = stack.pop()
            a = stack.pop()

            if token == "+":
                stack.append(a+b)
            elif token == "-":
                stack.append(a-b)
            elif token == "/":
                stack.append(a/b)
            elif token == "*":
                stack.append(a*b)

    return stack[0]
