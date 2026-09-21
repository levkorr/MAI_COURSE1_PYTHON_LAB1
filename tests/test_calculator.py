import pytest
import re
from toolkit.tokenizer import tokenize, shunting_yard
from toolkit.calculator import calculate
from toolkit.validator import initial_validation_calc, validation_calc


def full_cycle(expr):
    return calculate(shunting_yard(tokenize(expr)))

# Успешные запуски
@pytest.mark.parametrize(
    "expression, expected",
    [
        ("24.9/-43.8*-20", 11.36986301369863),
        ("-3++4", 1.0),
        ("2+2*2", 6.0),
        ("-136 + 25266 / +24.3 - 4 * + 4 - + 5 / - .6", 896.0864197530865),
    ]
)
def test_valid_expression(expression, expected):
    assert full_cycle(expression) == pytest.approx(expected)


# Неуспешные запуски
@pytest.mark.parametrize(
    "expression, error",
    [
        ("24---3", "Sequential Operations: --"),
        ("24++-3", "Sequential Operations: ++"),
        ("24**3", "Sequential Operations: **"),
        ("24//3", "Sequential Operations: //"),
        ("24.5.6+3", "Float mistake: 24.5.6"),
        ("*24+3", "Operation before the first operand: *"),
        ("/24+3", "Operation before the first operand: /"),
        ("24+3/", "No operand after operation: /"),
        ("24+3+", "No operand after operation: +"),
        ("24+a", "Unknown symbols: a "),
    ]
)
def test_invalid_expression(expression, error):
    with pytest.raises(ValueError, match=re.escape(error)):
        initial_validation_calc(expression)
        validation_calc(tokenize(expression))