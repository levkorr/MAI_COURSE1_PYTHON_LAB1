from errors import *

def validation(tokens):
    if operation_before_first_operand(tokens)[0]:
            raise ValueError(f"Operation before the first operand: {operation_before_first_operand(tokens)[1]}")
    if sequential_operations(tokens)[0]:
        raise ValueError(f"Sequential Operations: {"".join(sequential_operations(tokens)[1])}")
    if float_mistake(tokens)[0]:
        raise ValueError(f"Float mistake: {float_mistake(tokens)[1]}")
    if no_operand_after_operation(tokens)[0]:
        raise ValueError(f"No operand after operation: {no_operand_after_operation(tokens)[1]}")
    return True