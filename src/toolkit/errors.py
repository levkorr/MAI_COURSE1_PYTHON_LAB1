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
