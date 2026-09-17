def sequential_operations(tokens):
    for i in range(len(tokens)-1):
        if tokens[i] in ["+","-","*","/"] and tokens[i+1] in ["+","-","*","/"]:
            return [True, [tokens[i],tokens[i+1]]]
    return [False,0]

def float_mistake(tokens):
    for token in tokens:
        if token.count(".")>1:
            return [True, token]
    return [False, 0]
