import pytest
from toolkit.tokenizer import tokenize, shunting_yard
from toolkit.calculator import calculate
from toolkit.validator import initial_validation_calc, validation_calc

def full_cycle(expr):
    return calculate(shunting_yard(tokenize(expr)))


@pytest.mark.parametrize(
    "expression, expected",
    [
        # Успешные тесты
        ("24.9/-43.8*-20", 11.36986301369863),
        ("-3++4", 1.0),
        ("2+2*2", 6.0),
        ("-136 + 25266 / +24.3 - 4 * + 4 - + 5 / - .6", 896.0864197530865)
        # Неуспешные тесты...
    ]
)

def test_full_cycle(expression, expected):
    assert full_cycle(expression) == pytest.approx(expected)