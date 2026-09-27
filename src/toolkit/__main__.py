import sys

from .errors import CalculatorError, ConverterError, InvalidValueError
from .manager import custom_help, full_calc, full_convert, parse


def main():
    ''' Являетсе единственным входом и выходом программы
    Обрабатывает ввод в CLI, входные аргументы
    Отвечает за запуск нужных функций
    Хранит основную логику calc и convert

    Args:
        None

    Returns:
        None
    
    Raises:
        InvalidValueError: Если непраивльное значение для конвертера
    '''
    custom_help(sys.argv)  # Обработка выражения на --help

    args = parse()  # Создаем парсер через argparse

    # Работа с аргументами
    if args.command == "calc":  # Если калькуляция
        expr = args.expression
        full_calc(expr)

    elif args.command == "convert":  # Если конвертация
        # Получение аргументов
        try:
            value = float(args.value)
        except Exception as exc:
            raise InvalidValueError(args.value) from exc
        from_unit = args.from_unit
        to_unit = args.to_unit

        full_convert(value, from_unit, to_unit)


if __name__ == "__main__":
    try:
        main()
    except CalculatorError as error:
        print(f"Expected Error: {error}", file=sys.stderr)
        sys.exit(2)
    except ConverterError as error:
        print(f"Expected Error: {error}", file=sys.stderr)
        sys.exit(2)
    except Exception as error:  # noqa: BLE001
        print(f"UnexpectedError: {error}", file=sys.stderr)
        sys.exit(2)
