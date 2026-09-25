import operator

ALPHABET = "0123456789. +-*/%"
UNITS = ["cm", "mm", "m", "km", "kg", "g", "c", "f", "k"]
LENGTH = ["cm", "mm", "m", "km"]
WEIGHT = ["kg", "g"]
TEMPERATURE = ["c", "f", "k"]
PRECEDANCE = {"+": 1, "-": 1, "*": 2, "/": 2, "//": 2, "%": 2}
OPERATIONS = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv,
    "//": operator.floordiv,
    "%": operator.mod}
