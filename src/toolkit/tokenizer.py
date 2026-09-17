

from errors import *
from validator import *

def tokenize(expr):
    tokens = []
    state = "START"
    current_token = ""

    for char in expr:
        if state=="START":
            if char.isdigit():
                state="NUMBER"
                current_token+=char
            elif char in ["-","+"]:
                current_token=char
                state="NUMBER"
        elif state=="NUMBER":
            if char.isdigit() or char==".":
                current_token+=char
            elif char in ["+","-","*","/"]:
                tokens.append(current_token)
                tokens.append(char)
                current_token=""
                state = "START"
    tokens.append(current_token)
    return tokens


def shunting_yard(tokens):
    output = []
    operators = []

    weight = {"+": 1, "-": 1, "*": 2, "/": 2}

    for token in tokens:
        if token.lstrip("+-").isdigit() or "." in token:
            output.append(token)
        elif token in ["+","-","*","/"]:
            while len(operators)!=0 and weight[operators[-1]] >= weight[token]:
                output.append(operators.pop())
            operators.append(token)
    while len(operators)!=0:
        output.append(operators.pop())
    return output

if __name__ == "__main__":
    s = "136+25266+24..3/-4*+4-+5/-6"
    tokenized_s = tokenize(s)
    print(tokenized_s)
    validation(tokenized_s)

#rpn_s = shunting_yard(tokenized_s)
#print(rpn_s)