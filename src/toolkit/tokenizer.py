from .constants import OPERATIONS, PRECEDANCE

def compress(expr):
    ''' Совмещает + и - перед числами

    Args:
        expr: Строка, математическое выражение в инфиксной записи

    Returns:
        output: Строка, без лишних + и - перед числами
    '''
    output = ""
    for char in expr:
        if char in "+-":
            if len(output)!=0 and output[-1] in "+-":
                if char == "+":
                    pass
                if char == "-":
                    if output[-1]=="-":
                        output = output[:-1]+"+"
                    else:
                        output = output[:-1]+"-"
            else:
                output+=char
        else:
            output+=char
    return(output)

def tokenize(expr):
    ''' Токенизирует математическое выражение, 
        токен это операция или число или число с бинарным символом

    Args:
        expr: Строка, математическое выражение в инфиксной записи

    Returns:
        tokens: Список, токенезированное математическое выражение в инфиксной записи
    '''
    expr = expr.replace(" ", "")
    expr = expr.replace("//","|")  # Замена // на |
    tokens = []
    state = "START"
    current_token = ""

    for char in expr:  # Проходим по числам
        if state == "START":  # Если это новый символ
            if char.isdigit():  # Если это число
                state = "NUMBER"
                current_token += char
            # Если это ведущий +- или опустили целую нулевую часть числа
            elif char in ["-", "+", "."]:
                current_token = char
                state = "NUMBER"
            elif char in ["*", "/", "|", "%"]:  # Если это лишняя операция
                tokens.append(char)
        elif state == "NUMBER":  # Если число уже началось
            if char.isdigit() or char == ".":  # Если это составляющая числа
                current_token += char
            elif char in ["-", "+", "*", "/", "|", "%"]:  # Если это конец числа
                tokens.append(current_token)
                tokens.append(char)
                current_token = ""
                state = "START"
    tokens.append(current_token)  # Последний токен
    for token_id, token in enumerate(tokens): # Обратная замена | на //
        if token=="|":
            tokens[token_id]="//"
    return tokens


def shunting_yard(tokens):
    ''' Переводит токенезированное выражение в обратную польскую нотацию

    Args:
        tokens: Список, токенезированное математическое выражение в инфиксной записи

    Returns:
        output: Список, токенизированное математическое выражение в постфиксной записи
    '''
    output = []
    operators = []

    weight = PRECEDANCE  # Приоритеты операций

    for token in tokens:
        if token.lstrip("+-").isdigit() or "." in token:  # Если это число
            output.append(token)
        elif token in OPERATIONS:  # Если это операция
            while len(operators) != 0 and weight[operators[-1]] >= weight[token]:
                output.append(operators.pop())
            operators.append(token)
    while len(operators) != 0:  # Добавляем оставшиеся операции
        output.append(operators.pop())
    if output[-1] == "":  # Проверка на пустой символ
        output.pop()
    return output
