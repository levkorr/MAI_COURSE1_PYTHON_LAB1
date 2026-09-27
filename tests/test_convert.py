import re

import pytest

from toolkit.converter import convert
from toolkit.errors import ConverterError
from toolkit.validator import validation_convert


# Успешные запуски
@pytest.mark.parametrize(
    "value, from_unit, to_unit, expected",
    [
        # Длина
        (1000, "mm", "m", 1.0),
        (1, "km", "cm", 100000.0),
        # Масса
        (1000, "g", "kg", 1.0),
        (2.5, "kg", "g", 2500.0),
        # Температура
        (0, "c", "f", 32.0),
        (273.15, "k", "c", 0.0),
    ]
)
def test_valid_conversion(value, from_unit, to_unit, expected):
    assert convert(value, from_unit, to_unit) == pytest.approx(expected)


# Неуспешные запуски
@pytest.mark.parametrize(
    "value, from_unit, to_unit, error",
    [
        # Неизвестные единицы
        (100, "m", "abc", "Unknown units: abc"),
        (100, "abc", "xyz", "Unknown units: abc xyz"),
        # Несовместимые единицы
        (100, "m", "kg", "Different unit types: m, kg"),
        (100, "c", "kg", "Different unit types: c, kg"),
        # Температура ниже абсолютного нуля
        (-300, "c", "f", "Temperature below absolute zero: -300c"),
        (-1, "k", "c", "Temperature below absolute zero: -1k"),
    ]
)
def test_invalid_conversion(value, from_unit, to_unit, error):
    with pytest.raises(ConverterError, match=re.escape(error)):
        validation_convert(value, from_unit, to_unit)
        