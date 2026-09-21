from .errors import *

# Валидация токенизированного выражения для калькуляции
# В случае ошибки выводит ошибку в stderr и программа завершается с кодом 2
def validation_calc(tokens):
    if operation_before_first_operand(tokens)[0]:
        raise ValueError(f"Operation before the first operand: {operation_before_first_operand(tokens)[1]}")
    if sequential_operations(tokens)[0]:
        raise ValueError(f"Sequential Operations: {sequential_operations(tokens)[1]}")
    if float_mistake(tokens)[0]:
        raise ValueError(f"Float mistake: {float_mistake(tokens)[1]}")
    return tokens

# Изначальная валидация выражения для калькуляции
# В случае ошибки выводит ошибку в stderr и программа завершается с кодом 2
def initial_validation_calc(expr):
    if division_by_zero(expr)[0]:
        raise ZeroDivisionError(f"Division by zero occurred: {division_by_zero(expr)[1]}")
    if no_operand_after_operation(expr)[0]:
        raise ValueError(f"No operand after operation: {no_operand_after_operation(expr)[1]}")
    if split_number(expr)[0]:
        raise ValueError(f"Number is split: {split_number(expr)[1]}")
    if unknown_symbols(expr)[0]:
        raise ValueError(f"Unknown symbols: {unknown_symbols(expr)[1]}")
    return expr

# Валидация конвертации
# В случае ошибки выводит ошибку в stderr и программа завершается с кодом 2
def validation_convert(Value, From, To):
    if unknown_metrics(Value, From, To)[0]:
        raise ValueError(f"Unknown metrics: {unknown_metrics(Value, From, To)[1]}")
    if wrong_metrics_type(Value, From, To)[0]:
        raise ValueError(f"Cant convert between different Types: from {From} to {To}")
    if below_absolute_zero(Value, From, To)[0]:
        raise ValueError(f"Temperature below absolute zero: {Value}{From}")
    return (Value, From, To)

def cli_validation(argv):
    if len(argv)<2:
        raise ValueError("Not enough arguments, try \"python -m toolkit --help\"")
    else:
        if argv[1]=="calc":
            if len(argv)<3:
                raise ValueError("Not enough arguments, try \"python -m toolkit --help\"")
        elif argv[2]=="convert":
            if len(argv)<6:
                raise ValueError("Not enough arguments, try \"python -m toolkit --help\"")
            if argv[3]!="--from":
                raise ValueError(f"Unknown argument: {argv[3]}, try \"python -m toolkit --help\"")
            if argv[5]!="--to":
                raise ValueError(f"Unknown argument: {argv[5]}, try \"python -m toolkit --help\"")
        else:
            raise ValueError(f"Unknown argument: {argv[2]}, try \"python -m toolkit --help\"")