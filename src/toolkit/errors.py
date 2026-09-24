from .constants import ALPHABET, LENGTH, UNITS, OPERATIONS, TEMPERATURE, WEIGHT

# Ошибки для валидации токенизированного выражения калькуляции

def sequential_operations(tokens):
    '''Проверяет нет ли двух операций подряд

    Args:
        tokens: Список, токенезированное математическое выражение в инфиксной записи

    Returns:
        Список из двух элементов:
            Если ошибка найдена: True и найденные операции
            Если ошибка не найдена: False и 0
    '''
    for i in range(len(tokens)-1):
        if tokens[i] in OPERATIONS and tokens[i+1] in OPERATIONS:
            return [True, tokens[i]+tokens[i+1]]
    return [False, 0]


def float_mistake(tokens):
    '''Проверяет не допущена ли ошибка в записи вещественного числа

    Args:
        tokens: Список, токенезированное математическое выражение в инфиксной записи

    Returns:
        Список из двух элементов:
            Если ошибка найдена: True и найденное вещественное число
            Если ошибка не найдена: False и 0
    '''
    for token in tokens:
        if token.count(".") > 1 or token[-1] == ".":
            return [True, token]
    return [False, 0]


def operation_before_first_operand(tokens):
    '''Проверяет не начинается ли выражение с операции

    Args:
        tokens: Список, токенезированное математическое выражение в инфиксной записи

    Returns:
        Список из двух элементов:
            Если ошибка найдена: True и найденная операция
            Если ошибка не найдена: False и 0
    '''
    if tokens[0] in OPERATIONS:
        return [True, tokens[0]]
    return [False, 0]


# Ошибки для валидации иначального выражения калькуляции


def division_by_zero(expr):
    '''Проверяет нет ли деления на 0

    Args:
        expr: Строка, математическое выражение в инфиксной записи

    Returns:
        Список из двух элементов:
            Если ошибка найдена: True и найденная операция деления на 0
            Если ошибка не найдена: False и 0
    '''
    expr = expr.replace(" ", "")
    if "//0" in expr:
        return [True, "//0"]
    if "/0" in expr:
        return [True, "/0"]
    return [False, 0]


def no_operand_after_operation(expr):
    '''Проверяет не заканчивается ли выражение на операцию

    Args:
        expr: Строка, математическое выражение в инфиксной записи

    Returns:
        Список из двух элементов:
            Если ошибка найдена: True и найденная операция
            Если ошибка не найдена: False и 0
    '''
    expr = expr.replace(" ", "")
    if expr[-1] in OPERATIONS:
        return [True, expr[-1]]
    return [False, 0]


def unknown_symbols(expr):
    '''Проверяет нет ли в записи выражения неизвестных символов

    Args:
        expr: Строка, математическое выражение в инфиксной записи

    Returns:
        Список из двух элементов:
            Если ошибка найдена: True и найденные неизвестные символы
            Если ошибка не найдена: False и 0
    '''
    unknown = ""
    for char in expr:
        if char not in ALPHABET:
            unknown += f"{char} "
    if len(unknown) != 0:
        return [True, unknown]
    return [False, 0]


def split_number(expr):
    '''Проверяет нет ли в записи выражения чисел, символы которых разделены пробелами

    Args:
        expr: Строка, математическое выражение в инфиксной записи

    Returns:
        Список из двух элементов:
            Если ошибка найдена: True и найденная часть числа разделенного пробелом
            Если ошибка не найдена: False и 0
    '''
    expr = expr.split()
    for i in range(len(expr)-1):
        if (expr[i][-1].isdigit() or expr[i][-1] == ".") and \
            (expr[i+1][0].isdigit() or expr[i+1][0] == "."):
            return [True, f"...{expr[i][-1]} {expr[i+1][0]}..."]
    return [False, 0]


# Ошибки для валидации конвертации


def unknown_units(from_unit, to_unit):
    ''' Проверяет, нет ли неизвестных величин

    Args:
        from_unit: Из какой величины нужно перевести значение
        to_unit: В какую величину нужно перевести значение

    Returns:
        Список из двух элементов:
            Если ошибка найдена: True и найденные неизвестные величины
            Если ошибка не найдена: False и 0
    '''
    unknown = ""
    if from_unit not in UNITS:
        unknown += f"{from_unit} "
    if to_unit not in UNITS:
        unknown += f"{to_unit}"
    if len(unknown) != 0:
        return [True, unknown]
    return [False, 0]


def wrong_units_type(from_unit, to_unit):
    ''' Проверяет что все величины относятся к одной группе

    Args:
        from_unit: Из какой величины нужно перевести значение
        to_unit: В какую величину нужно перевести значение

    Returns:
        Список из двух элементов:
            Если ошибка найдена: True и величина из неправильной группы
            Если ошибка не найдена: False и 0
    '''
    if from_unit in LENGTH and to_unit not in LENGTH:
        return [True, to_unit]
    if from_unit in WEIGHT and to_unit not in WEIGHT:
        return [True, to_unit]
    if from_unit in TEMPERATURE and to_unit not in TEMPERATURE:
        return [True, to_unit]
    return [False, 0]


def below_absolute_zero(value, from_unit):
    ''' Проверяет, не является ли значение температуры ниже абсолютного нуля

    Args:
        value: Значение которое нужно перевести
        from_unit: Из какой величины нужно перевести значение

    Returns:
        Список из двух элементов:
            Если ошибка найдена: True и значение температуры
            Если ошибка не найдена: False и 0
    '''
    if from_unit == "c" and value < -273.15:
        return [True, value]
    if from_unit == "f" and value < -459.67:
        return [True, value]
    if from_unit == "k" and value < 0:
        return [True, value]
    return [False, 0]
