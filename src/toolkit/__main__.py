from sys import argv
from tokenizer import tokenize
from tokenizer import shunting_yard
from calculator import calculate
from errors import *
from validator import validation

if __name__ == "__main__":
    s = "136+25266+24.3/-4*+4-+5/-6"
    tokenized_s = tokenize(s)
    print(tokenized_s)
    validation(tokenized_s)
    rpn_s = shunting_yard(tokenized_s)
    print(rpn_s)
    calculated_s = calculate(rpn_s)
    print(calculated_s)