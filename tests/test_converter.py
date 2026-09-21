import pytest
import re
from toolkit.converter import convert
from toolkit.validator import validation_convert


# Успешные запуски
@pytest.mark.parametrize(
    "value, from_metric, to_metric, expected",
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
def test_valid_conversion(value, from_metric, to_metric, expected):
    assert convert(value, from_metric, to_metric) == pytest.approx(expected)


# Неуспешные запуски
@pytest.mark.parametrize(
    "value, from_metric, to_metric, error",
    [
        # Неизвестные единицы
        (100, "abc", "m", "Unknown metrics: abc"),
        (100, "m", "abc", "Unknown metrics: abc"),
        (100, "abc", "xyz", "Unknown metrics: abc xyz"),
        # Несовместимые единицы
        (100, "m", "kg", "Cant convert between different Types: from m to kg"),
        (100, "c", "kg", "Cant convert between different Types: from c to kg"),
        # Температура ниже абсолютного нуля
        (-300, "c", "f", "Temperature below absolute zero: -300c"),
        (-1, "k", "c", "Temperature below absolute zero: -1k"),
    ]
)
def test_invalid_conversion(value, from_metric, to_metric, error):
    with pytest.raises(ValueError, match=re.escape(error)):
        validation_convert(value, from_metric, to_metric)