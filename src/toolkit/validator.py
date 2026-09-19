from .errors import *
import sys

# Валидация токенизированного выражения для калькуляции
# В случае ошибки выводит ошибку в stderr и программа завершается с кодом 2
def validation_calc(tokens):
    if operation_before_first_operand(tokens)[0]:
            print(f"Operation before the first operand: {operation_before_first_operand(tokens)[1]}", file=sys.stderr)
            sys.exit(2)
    if sequential_operations(tokens)[0]:
        print(f"Sequential Operations: {sequential_operations(tokens)[1]}", file=sys.stderr)
        sys.exit(2)
    if float_mistake(tokens)[0]:
        print(f"Float mistake: {float_mistake(tokens)[1]}", file=sys.stderr)
        sys.exit(2)
    if no_operand_after_operation(tokens)[0]:
        print(f"No operand after operation: {no_operand_after_operation(tokens)[1]}", file=sys.stderr)
        sys.exit(2)
    if division_by_zero(tokens)[0]:
         print(f"Division by zero occurred: {"".join(division_by_zero(tokens)[1])}", file=sys.stderr)
         sys.exit(2)
    return True

# Изначальная валидация выражения для калькуляции
# В случае ошибки выводит ошибку в stderr и программа завершается с кодом 2
def initial_validation_calc(str):
    if split_number(str)[0]:
        print(f"Number is split: {split_number(str)[1]}", file=sys.stderr)
        sys.exit(2)
    if unknown_symbols(str)[0]:
        print(f"Unknown symbols: {unknown_symbols(str)[1]}", file = sys.stderr)
        sys.exit(2)
    return True

# Валидация конвертации
# В случае ошибки выводит ошибку в stderr и программа завершается с кодом 2
def validation_convert(Value, From, To):
    if unknown_metrics(Value, From, To)[0]:
        print(f"Unknown metrics: {unknown_metrics(Value, From, To)[1]}", file=sys.stderr)
        sys.exit(2)
    elif wrong_metrics_type(Value, From, To)[0]:
        print(f"Cant convert between different Types: from {From} to {To}", file=sys.stderr)
        sys.exit(2)
    elif below_absolute_zero(Value, From, To)[0]:
        print(f"Temperature below absolute zero: {Value}{From}", file=sys.stderr)
        sys.exit(2)
    return True