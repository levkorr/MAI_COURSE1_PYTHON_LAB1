from .errors import *

# Если ошибка есть, пишет сообщение с указателем на ошибку
def validation_calc(tokens):
    if operation_before_first_operand(tokens)[0]:
            raise ValueError(f"Operation before the first operand: {operation_before_first_operand(tokens)[1]}")
    if sequential_operations(tokens)[0]:
        raise ValueError(f"Sequential Operations: {sequential_operations(tokens)[1]}")
    if float_mistake(tokens)[0]:
        raise ValueError(f"Float mistake: {float_mistake(tokens)[1]}")
    if no_operand_after_operation(tokens)[0]:
        raise ValueError(f"No operand after operation: {no_operand_after_operation(tokens)[1]}")
    if division_by_zero(tokens)[0]:
         raise ZeroDivisionError(f"Division by zero occurred: {"".join(division_by_zero(tokens)[1])}")
    return True