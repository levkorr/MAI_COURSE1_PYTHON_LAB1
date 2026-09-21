# Ошибки для валидации токенизированного выражения калькуляции

# Проверяет что нет двух операций подряд
# В случае двух операций подряд, возвращает True и сами операции
def sequential_operations(tokens):
    for i in range(len(tokens)-1):
        if tokens[i] in ["+", "-", "*", "/"] and tokens[i+1] in ["+", "-", "*", "/"]:
            return [True, tokens[i]+tokens[i+1]]
    return [False, 0]

# Проверяет что нет неправильно написанных нецелых чисел
# В случае неправильного нецелого числа, возвращает True и это неправильно написанное число
def float_mistake(tokens):
    for token in tokens:
        if token.count(".") > 1:
            return [True, token]
    return [False, 0]

# Проверяем что выражение не начинается с операции
# В случае когда выражение начинается с операции, возвращает True и эту операцию
def operation_before_first_operand(tokens):
    if tokens[0] in ["*", "/", "-", "+"]:
        return [True, tokens[0]]
    return [False, 0]

# Ошибки для валидации иначального выражения калькуляции

# Проверяет что нет ЯВНОГО деления на 0
# В случае ЯВНОГО деления на 0, возвращает True и это деление на 0
def division_by_zero(expr):
    expr = expr.replace(" ","")
    if "/0" in expr:
        return [True, "/0"]
    return [False, 0]

# Проверяем что выражение не заканчивается на операцию
# В случае когда выражение заканчивается на операцию, возвращает True и эту операцию
def no_operand_after_operation(expr):
    expr = expr.replace(" ","")
    if expr[-1] in ["+", "-", "*", "/"]:
        return [True, expr[-1]]
    return [False, 0]

# Проверяет нет ли неизвестных символов
# В случае неизвестных символов, возвращает True и все неизвестные символы
def unknown_symbols(expr):
    unknown = ""
    for char in expr:
        if char not in "0123456789/*+-. ":
            unknown += f"{char} "
    if len(unknown) != 0:
        return [True, unknown]
    return [False, 0]

# Проверяем что нет чисел с пробелом внутри
# В случае если такое число есть, возвращаем True и цифры, находящиеся вокруг пробела
def split_number(expr):
    expr = expr.split()
    for i in range(len(expr)-1):
        if (expr[i][-1].isdigit() or expr[i][-1]==".") and (expr[i+1][0].isdigit() or expr[i+1][0]=="."):
            return [True, f"...{expr[i][-1]} {expr[i+1][0]}..."]
    return [False, 0]


# Ошибки для валидации конвертации

# Проверяет что нет есть неизвестные выличины
# В случае когда есть, возвращает True и неизвестную величину (может несколько)
def unknown_metrics(Value, From, To):
    unknown = ""
    if From not in ["cm", "mm", "m", "km", "kg", "g", "c", "f", "k"]:
        unknown += f"{From} "
    if To not in ["cm", "mm", "m", "km", "kg", "g", "c", "f", "k"]:
        unknown += f"{To}"
    if len(unknown) != 0:
        return [True, unknown]
    return [False, 0]

# Проверят что все величины относятся к одной группе (длина, масса, температура)
# В случае если величины из разных групп, возвращает True
def wrong_metrics_type(Value, From, To):
    if From in ["cm", "mm", "m", "km"] and To not in ["cm", "mm", "m", "km"]:
        return [True, To]
    elif From in ["g", "kg"] and To not in ["g", "kg"]:
        return [True, To]
    elif From in ["c", "f", "k"] and To not in ["c", "f", "k"]:
        return [True, To]
    return [False, 0]

# Проверяет что у температуры значение не ниже абсолютного нуля
# В случае когда температура ниже абсолютного нуля, возвращает True
def below_absolute_zero(Value, From, To):
    if From == "c":
        if Value < -273.15:
            return [True, Value]
    if From == "f":
        if Value < -459.67:
            return [True, Value]
    if From == "k":
        if Value < 0:
            return [True, Value]
    return [False, 0]