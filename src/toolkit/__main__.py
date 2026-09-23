import sys
from sys import argv
from .tokenizer import tokenize, shunting_yard
from .calculator import calculate
from .validator import validation_calc, validation_convert, initial_validation_calc
from .converter import convert

# python -m toolkit calc "-136++25266++24.3-4*+4-+5--.6"
# python -m toolkit convert 129 --from kg --to g
# "-136++25266++24.3-4*+4-+5--.6"

if __name__ == "__main__":
    try:
        #cli_validation(argv)
        if argv[1] == "calc":  # Если калькуляция
            expr = argv[2] # Выражение

            initial_validation_calc(expr)  # Предварительная валидация выражения
            tokenized_expression = tokenize(expr)  # Токенизация выражения
            # Валиадция токенизированного выражения
            validation_calc(tokenized_expression)
            # Обратная польская нотация токенизированного выражения
            rpn_expression = shunting_yard(tokenized_expression)
            calculated_expression = calculate(rpn_expression)  # Итоговый подсчет

            print(calculated_expression)  # Итоговый вывод
            sys.exit(0)  # Успешное завершение программы

        elif argv[1] == "convert":  # Если конвертация
            value = float(argv[2])  # Значение
            from_metric = argv[4].lower()  # Из какой величины
            to_metric = argv[6].lower()  # В какую величину

            validation_convert(value, from_metric, to_metric)  # Валидация
            converted_value = convert(value, from_metric, to_metric)  # Перевод величин

            print(converted_value)  # Итоговый вывод
            sys.exit(0)  # Успешное завершение программы
    except Exception as e:
        print(e, file=sys.stderr)
        sys.exit(2)
