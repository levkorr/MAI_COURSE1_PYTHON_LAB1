import pytest
import re
from toolkit.tokenizer import tokenize, shunting_yard
from toolkit.calculator import calculate
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
def test_valid_expression(expression, expected):
    assert calculate(shunting_yard(tokenize(expression))
                     ) == pytest.approx(expected)


# Неуспешные запуски
@pytest.mark.parametrize(
    "expression, error",
    [
        # Две операции подряд
        ("2*/3", "Sequential Operations: */"),
        ("24**3", "Sequential Operations: **"),
        # Разделенное пробелом число
        ("2 4+-3", "Number is split: ...2 4..."),
        ("28 *25 66", "Number is split: ...5 6..."),
        # Ошибочное написание вещественного числа
        ("24.5.6+3", "Float mistake: 24.5.6"),
        ("5986/253.", "Float mistake: 253."),
        # Операция перед первым операндом
        ("*24+3", "Operation before the first operand: *"),
        ("/24+3", "Operation before the first operand: /"),
        # Нет операнда после последней операции
        ("24+3/", "No operand after operation: /"),
        ("24+3+", "No operand after operation: +"),
        # Неизвестные символы
        ("2+a", "Unknown symbols: a "),
        ("26^a", "Unknown symbols: ^ a ")
    ]
)
def test_invalid_expression(expression, error):
    with pytest.raises(ValueError, match=re.escape(error)):
        initial_validation_calc(expression)
        validation_calc(tokenize(expression))
