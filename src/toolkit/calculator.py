from errors import *
from tokenizer import *
from validator import *

if __name__ == "__main__":
    s = "136+25266+24.3/-4*+4-+5/-6"
    tokenized_s = tokenize(s)
    print(tokenized_s)
    validation(tokenized_s)
    rpn_s = shunting_yard(tokenized_s)
    print(rpn_s)
