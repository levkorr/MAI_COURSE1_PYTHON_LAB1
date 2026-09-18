# Проверяет что нет двух операций подряд
# В случае двух операций подряд, возвращает True и сами операции
def sequential_operations(tokens):
    for i in range(len(tokens)-1):
        if tokens[i] in ["+","-","*","/"] and tokens[i+1] in ["+","-","*","/"]:
            return [True, tokens[i]+tokens[i+1]]
    return [False,0]

# Проверяет что нет неправильно написанных нецелых чисел
# В случае неправильного нецелого числа, возвращает True и это неправильно написанное число
def float_mistake(tokens):
    for token in tokens:
        if token.count(".")>1:
            return [True, token]
    return [False, 0]

# Проверяем что выражение не заканчивается на операцию
# В случае когда выражение заканчивается на операцию, возвращает True и эту операцию
def no_operand_after_operation(tokens):
    if tokens[-1] in ["+","-","*","/",""]:
        return [True, tokens[-1]]
    return [False, 0]

# Проверяем что выражение не начинается с операции
# В случае когда выражение начинается с операции, возвращает True и эту операцию
def operation_before_first_operand(tokens):
    if tokens[0] in ["*","/","-","+"]:
        return [True, tokens[0]]
    return [False, 0]

# Проверяет что нет ЯВНОГО деления на 0
# В случае ЯВНОГО деления на 0, возвращает True и это деление на 0
def division_by_zero(tokens):
    for i in range(len(tokens)-1):
            if tokens[i] == "/" and tokens[i+1] == "0":
                return [True, [tokens[i],tokens[i+1]]]
    return [False, 0]


def split_number(str):
    str = str.split()
    for i in range(len(str)-1):
        if str[i][-1].isdigit() and str[i+1][0].isdigit():
            return [True, f"...{str[i][-1]} {str[i+1][0]}..."]
    return [False, 0]


def unknown_metrics(Value, From, To):
    unknown = ""
    if From not in ["cm","mm","m","km","kg","g","c","f","k"]:
        unknown+=f"{From} "
    if To not in ["cm","mm","m","km","kg","g","c","f","k"]:
        unknown+=f"{To}"
    if len(unknown)!=0:
        return [True, unknown]
    return [False, 0]

def wrong_metrics_type(Value, From, To):
    if From in ["cm","mm","m","km"] and To not in ["cm","mm","m","km"]:
        return [True, To]
    elif From in ["g","kg"] and To not in ["g","kg"]:
        return [True, To]
    elif From in ["c","f","k"] and To not in ["c","f","k"]:
        return [True, To]
    return [False, 0]

def below_absolute_zero(Value, From, To):
    if From == "c":
        if Value< -273.15:
            return [True, Value]
    if From == "f":
        if Value < -459.67:
            return [True, Value]
    if From == "k":
        if Value < 0:
            return [True, Value]
    return [False, 0]