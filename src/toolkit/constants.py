import operator

OPERATIONS = ["+", "-", "*", "/", "//", "%"]
ALPHABET = "0123456789. +-*/%"
UNITS = ["cm", "mm", "m", "km", "kg", "g", "c", "f", "k"]
LENGTH = ["cm", "mm", "m"]
WEIGHT = ["kg","g"]
TEMPERATURE = ["c", "f", "k"]
PRECEDANCE = {"+": 1, "-": 1, "*": 2, "/": 2, "//": 2, "%": 2}
TRUE_OPERATIONS = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv,
    "//": operator.floordiv,
    "%": operator.mod}
