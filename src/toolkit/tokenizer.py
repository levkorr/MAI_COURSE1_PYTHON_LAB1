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
            elif char in ["*","/"]:
                tokens.append(char)
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
    if output[-1]=="":
        output.pop()
    return output