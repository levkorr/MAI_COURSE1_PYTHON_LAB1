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

if __name__ == "__main__":
    s = "136+25266+24.3/-4*+4-+5/-6"
    tokenized_s = tokenize(s)
    print(tokenized_s)
    validation(tokenized_s)
    rpn_s = shunting_yard(tokenized_s)
    print(rpn_s)
    calculated_s = calculate(rpn_s)
    print(calculated_s)
