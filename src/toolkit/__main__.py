from sys import argv, exit
from .tokenizer import tokenize, shunting_yard
from .calculator import calculate
from .validator import validation_calc, validation_convert, initial_validation_calc
from .converter import convert

# python -m toolkit calc "-136++25266++24.3-4*+4-+5--.6"
# python -m toolkit convert 129 --from kg --to g
# "-136++25266++24.3-4*+4-+5--.6"

if __name__ == "__main__":
    if argv[1]=="calc": # Если калькуляция
        expr = argv[2] # Выражение

        initial_validation_calc(expr) # Предварительная валидация выражения
        tokenized_expression = tokenize(expr) # Токенизация выражения
        validation_calc(tokenized_expression) # Валиадция токенизированного выражения
        rpn_expression = shunting_yard(tokenized_expression) # Обратная польская нотация токенизированного выражения
        calculated_expression = calculate(rpn_expression) # Итоговый подсчет

        print(calculated_expression) # Итоговый вывод
        exit(0) # Успешное завершение программы

    elif argv[1]=="convert": # Если конвертация
        Value = float(argv[2]) # Значение
        From = argv[4].lower() # Из какой величины
        To = argv[6].lower() # В какую величину

        validation_convert(Value,From,To) # Валидация 
        converted_value = convert(Value, From, To) # Перевод величин

        print(converted_value) # Итоговый вывод
        exit(0) # Успешное завершение программы