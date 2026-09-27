import sys

from .errors import CalculatorError, ConverterError, InvalidValueError
from .manager import help, parse, full_calc, full_convert


def main():
    ''' Являетсе единственным входом и выходом программы
    Обрабатывает ввод в CLI, входные аргументы
    Отвечает за запуск нужных функций
    Хранит основную логику calc и convert

    Args:
        None

    Returns:
        None
    '''
    help(sys.argv)  # Обработка выражения на --help

    args = parse()  # Создаем парсер через argparse

    # Работа с аргументами
    if args.command == "calc":  # Если калькуляция
        expr = args.expression
        full_calc(expr)

    elif args.command == "convert":  # Если конвертация
        # Получение аргументов
        try:
            value = float(args.value)
        except ValueError:
            raise InvalidValueError(args.value)
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
    except Exception as error:
        print(f"UnexpectedError: {error}", file=sys.stderr)
        sys.exit(2)
