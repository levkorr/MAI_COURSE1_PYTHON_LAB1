from .errors import (
    # validation_calc:
    operation_before_first_operand,
    sequential_operations,
    float_mistake,
    # initial_validation_calc:
    division_by_zero,
    no_operand_after_operation,
    split_number,
    unknown_symbols,
    # validation_convert
    unknown_units,
    wrong_units_type,
    below_absolute_zero,
)


def validation_calc(tokens):
    ''' Выполняет валидацию токенизированного выражения калькулятора.

    Args:
        tokens: Список токенов арифметического выражения

    Returns:
        True, если валидация пройдена

    Raises:
        ValueError с указанием на ошибку: если выражение содержит ошибку
    '''
    if operation_before_first_operand(tokens)[0]:
        raise ValueError(
            f"Operation before the first operand: {operation_before_first_operand(tokens)[1]}")
    if sequential_operations(tokens)[0]:
        raise ValueError(
            f"Sequential Operations: {sequential_operations(tokens)[1]}")
    if float_mistake(tokens)[0]:
        raise ValueError(f"Float mistake: {float_mistake(tokens)[1]}")
    return True



def initial_validation_calc(expr):
    ''' Выполняет предварительную валидацию арифметического выражения

    Args:
        tokens: Список токенов арифметического выражения

    Returns:
        True, если валидация пройдена

    Raises:
        ValueError c указанием на ошибку: если выражение содержит ошибку
        ZeroDivisionError с указанием на деление: При делении на 0
    '''
    if division_by_zero(expr)[0]:
        raise ZeroDivisionError(
            f"Division by zero occurred: {division_by_zero(expr)[1]}")
    if no_operand_after_operation(expr)[0]:
        raise ValueError(
            f"No operand after operation: {no_operand_after_operation(expr)[1]}")
    if split_number(expr)[0]:
        raise ValueError(f"Number is split: {split_number(expr)[1]}")
    if unknown_symbols(expr)[0]:
        raise ValueError(f"Unknown symbols: {unknown_symbols(expr)[1]}")
    return True



def validation_convert(value, from_unit, to_unit):
    ''' Выполняет валидацию конвертации

    Args:
        value: Значение которое нужно перевести
        from_unit: Из какой величины нужно перевести значение
        to_unit: В какую величину нужно перевести значение

    Returns:
        True, если валидация пройдена

    Raises:
        ValueError с указанием на ошибку: если есть ошибка
    '''
    if unknown_units(from_unit, to_unit)[0]:
        raise ValueError(
            f"Unknown units: {unknown_units(from_unit, to_unit)[1]}")
    if wrong_units_type(from_unit, to_unit)[0]:
        raise ValueError(
            f"Cant convert between different types of units: from {from_unit} to {to_unit}")
    if below_absolute_zero(value, from_unit)[0]:
        raise ValueError(
            f"Temperature below absolute zero: {value}{from_unit}")
    return True
