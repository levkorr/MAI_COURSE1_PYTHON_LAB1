import re

import pytest

from toolkit.calculator import calculate
from toolkit.errors import CalculatorError
from toolkit.tokenizer import shunting_yard, tokenize
from toolkit.validator import initial_validation_calc, validation_calc


# Успешные запуски
@pytest.mark.parametrize(
    "expression, expected",
    [
        # Порядок операций
        ("2+2/2", 3.0),
        ("2+3*4", 14.0),
        # Отрицательные числа
        ("-2 * -3", 6.0),
        ("-10/-2.5", 4.0),
        # Унарные плюсы и минусы
        ("1+-2", -1.0),
        ("+1/-2", -0.5),
        # Вещественные числа
        ("2.5*-10", -25.0),
        ("10.56/+10", 1.056),
        # Пробелы между токенами
        ("56 * - 3 - 28", -196.0),
        ("280 /- 3+ 27*-4", -201.33333333333331),
        # Огромное выражение со всеми проверками
        ("-136 + 25266 / +24.3 - 4 * + 4 - + 5 / - .6", 896.0864197530865),
    ]
)
def test_valid_calculation(expression, expected):
    assert calculate(shunting_yard(tokenize(expression))) == pytest.approx(expected)


# Неуспешные запуски
@pytest.mark.parametrize(
    "expression, error",
    [
        # Две операции подряд
        ("2/ /3", "Sequential Operations: //"),
        ("24**3", "Sequential Operations: **"),
        # Разделенное пробелом число
        ("2 4+-3", "Number is split: ...2 4..."),
        ("28 *25 66", "Number is split: ...5 6..."),
        # Ошибочное написание вещественного числа
        ("24.5.6+3", "Float mistake: 24.5.6"),
        ("5986/253.", "Float mistake: 253."),
        # Операция перед первым операндом
        ("*24+3", "Expression starts with operation: *"),
        ("/24+3", "Expression starts with operation: /"),
        # Нет операнда после последней операции
        ("24+3/", "Expression ends with operation: /"),
        ("24+3+", "Expression ends with operation: +"),
        # Неизвестные символы
        ("2+a", "Unknown symbols: a "),
        ("26^a", "Unknown symbols: ^ a "),
        # Неправильная работа операторов % и //
        ("2.5*4//2", "The operation // only works with int: 10.0//2"),
        ("24-32.5*29%7", "The operation % only works with int: 942.5%7"),
        # Деление на 0
        ("2/0","Division by zero occurred: /0"),
        ("25+21//0","Division by zero occurred: //0")
    ]
)
def test_invalid_calculation(expression, error):
    with pytest.raises(CalculatorError, match=re.escape(error)):
        initial_validation_calc(expression)
        validation_calc(tokenize(expression))
        calculate(shunting_yard(tokenize(expression)))