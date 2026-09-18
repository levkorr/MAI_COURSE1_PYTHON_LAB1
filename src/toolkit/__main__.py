from sys import argv
from .tokenizer import tokenize, shunting_yard
from .calculator import calculate
from .validator import validation_calc, validation_convert, initial_validation_calc
from .converter import convert

# python -m toolkit calc "-136++25266++24.3-4*+4-+5--.6"
# python -m toolkit convert 129 --from kg --to g
# "-136++25266++24.3-4*+4-+5--.6"

if __name__ == "__main__":
    if argv[1]=="calc":
        expr = argv[2]
        initial_validation_calc(expr)
        tokenized_expression = tokenize(expr)
        print(tokenized_expression)
        validation_calc(tokenized_expression)
        rpn_expression = shunting_yard(tokenized_expression)
        calculated_expression = calculate(rpn_expression)
        print(calculated_expression)

    elif argv[1]=="convert":
        Value = int(argv[2])
        From = argv[4]
        To = argv[6]
        validation_convert(Value,From,To)
        print(convert(Value, From, To))