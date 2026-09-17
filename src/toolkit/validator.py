#tokenized_s = ['136', '+', '25266', '+', '24.3.', '/', '-4', '*', '+4', '-', '+5', '/', '-6']
from errors import *

def validation(tokens):
    if sequential_operations(tokens)[0]:
        raise ValueError(f"Sequential Operations: {"".join(sequential_operations(tokens)[1])}")
    if float_mistake(tokens)[0]:
        raise ValueError(f"Float mistake: {float_mistake(tokens)[1]}")
    return True
#validation(tokenized_s)