import argparse
import sys

from .calculator import calculate
from .converter import convert
from .json_dump import calc_dump, convert_dump
from .tokenizer import compress, shunting_yard, tokenize
from .validator import initial_validation_calc, validation_calc, validation_convert
from .errors import InvalidValueError

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
    # Создаем парсер через argparse
    parser = argparse.ArgumentParser(
        prog="toolkit",
        description="Calculator and unit converter.",
        usage="toolkit <command> [arguments]",
        epilog="Use \"python -m toolkit <command> --help\" for more information."
    )
    commands = parser.add_subparsers(dest="command")

    # Для команды calc
    parse_calc = commands.add_parser(
        "calc",
        description="Calculates mathematical expression",
        epilog="Example: \"python -m toolkit calc \"2+3\"\""
    )
    parse_calc.add_argument("expression")

    # Для команды convert
    parse_convert = commands.add_parser(
        "convert",
        description= "Converts value from one unit to another",
        epilog="Example: \"python -m toolkit convert 10 --from kg --to g\""
    )
    parse_convert.add_argument("value")
    parse_convert.add_argument("--from", dest="from_unit", required="True")
    parse_convert.add_argument("--to", dest="to_unit", required="True")

    # Аргументы парсера
    args = parser.parse_args()

    if args.command == "calc":  # Если калькуляция
        expr = args.expression

        compressed_expression = compress(expr) #  Совмещаем все + и -
        initial_validation_calc(compressed_expression)  # Предварительная валидация выражения
        tokenized_expression = tokenize(compressed_expression)  # Токенизация выражения
        validation_calc(tokenized_expression)  # Валиадция токенизированного выражения
        rpn_expression = shunting_yard(tokenized_expression)  # ОПЗ токенизированного выражения
        calculated_expression = calculate(rpn_expression)  # Итоговый подсчет

        print(calculated_expression)
        calc_dump(expr, calculated_expression)  # Выгрузка успешного запуска
        sys.exit(0)  # Успешное завершение программы

    elif args.command == "convert":
        try:
            value = float(args.value)
        except:
            raise InvalidValueError(args.value)
        from_unit = args.from_unit
        to_unit =  args.to_unit

        validation_convert(value, from_unit, to_unit)  # Валидация
        converted_value = convert(value, from_unit, to_unit)  # Перевод величин

        print(converted_value)  # Итоговый вывод
        convert_dump(value, converted_value, from_unit, to_unit)  # Выгрузка успешного запуска
        sys.exit(0)  # Успешное завершение программы

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e, file=sys.stderr)
        sys.exit(2)
