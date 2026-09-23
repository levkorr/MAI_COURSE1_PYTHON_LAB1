import sys
import argparse
from .json_dump import calc_dump, convert_dump
from .calculator import calculate
from .tokenizer import tokenize, shunting_yard
from .validator import validation_convert, validation_calc, initial_validation_calc
from .converter import convert

def main():
    # Создаем парсер через argparse
    parser = argparse.ArgumentParser(prog="toolkit")
    commands = parser.add_subparsers(dest="command", required=True)

    # Для команды calc
    parse_calc = commands.add_parser("calc")
    parse_calc.add_argument("expression")

    # Для команды convert
    parse_convert = commands.add_parser("convert")
    parse_convert.add_argument("value")
    parse_convert.add_argument("--from", dest="from_metric", required=True)
    parse_convert.add_argument("--to", dest="to_metric", required=True)

    args = parser.parse_args()

    if args.command == "calc":  # Если калькуляция
        expr = args.expression

        initial_validation_calc(expr)  # Предварительная валидация выражения
        tokenized_expression = tokenize(expr)  # Токенизация выражения
        validation_calc(tokenized_expression)  # Валиадция токенизированного выражения
        rpn_expression = shunting_yard(tokenized_expression)  # Обратная польская нотация токенизированного выражения
        calculated_expression = calculate(rpn_expression)  # Итоговый подсчет

        print(calculated_expression)
        calc_dump(expr, calculated_expression)  # Выгрузка успешного запуска
        sys.exit(0)  # Успешное завершение программы

    elif args.command == "convert":
        value = float(args.value)
        from_metric = args.from_metric
        to_metric =  args.to_metric

        validation_convert(value, from_metric, to_metric)  # Валидация
        converted_value = convert(value, from_metric, to_metric)  # Перевод величин

        print(converted_value)  # Итоговый вывод
        convert_dump(value, converted_value, from_metric, to_metric)  # Выгрузка успешного запуска
        sys.exit(0)  # Успешное завершение программы



if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e, file=sys.stderr)
