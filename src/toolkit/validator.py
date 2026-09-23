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
    unknown_metrics,
    wrong_metrics_type,
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



def validation_convert(value, from_metric, to_metric):
    ''' Выполняет валидацию конвертации

    Args:
        value: Значение которое нужно перевести
        from_metric: Из какой величины нужно перевести значение
        to_metric: В какую величину нужно перевести значение

    Returns:
        True, если валидация пройдена

    Raises:
        ValueError с указанием на ошибку: если есть ошибка
    '''
    if unknown_metrics(from_metric, to_metric)[0]:
        raise ValueError(
            f"Unknown metrics: {unknown_metrics(from_metric, to_metric)[1]}")
    if wrong_metrics_type(from_metric, to_metric)[0]:
        raise ValueError(
            f"Cant convert between different Types: from {from_metric} to {to_metric}")
    if below_absolute_zero(value, from_metric)[0]:
        raise ValueError(
            f"Temperature below absolute zero: {value}{from_metric}")
    return True
'''
def argparse_validation(args):
    if args.command is None:
        raise ValueError("You need to specify a command: calc or convert")
    if args.command == "calc":
        if args.expression is None:
            raise ValueError("You need to specify a valid math expression after \"calc\"")
        '''