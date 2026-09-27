import argparse
import sys

from .calculator import calculate
from .converter import convert
from .json_dump import calc_dump, convert_dump
from .tokenizer import compress, shunting_yard, tokenize
from .validator import initial_validation_calc, validation_calc, validation_convert


def help(argv):
    if "--help" in argv:
            if "calc" in argv:
                print("""
        Calculator module
    
        Arguments:
            EXPRESSION      Mathematical expression
        
        Support:
            Operations: '+', '-', '*', '/', '//', '%'
            Float and Int numbers
            Any amount of '+' and '-' before numbers
            Spaces between parts of expression
            Priorities of operations
    
        Examples of working programs:
            python -m toolkit calc "2+2"            Returns 4
            python -m toolkit calc "8.5/4.25"       Returns 2.0
                """)
                sys.exit(0)
            
            elif "convert" in argv:
                print("""
        Converter module
    
        Arguments:
            VALUE       Value to convert
            --from      Auxiliary argument
            UNIT        Unit to convert from
            --to        Auxiliary argument
            UNIT        Unit to convert to
    
        Support:
            Unary '+' and '-'
            Length: 'mm', 'cm', 'm', 'km'
            Weight: 'g', 'kg'
            Temperature: 'c', 'f', 'k'
                """)
                sys.exit(0)
    
            print("""
        Calculator and unit converter.
    
        Arguments:
            calc       Calculates mathematical expression
            convert    Converts value from one unit to another
                
        Usage:
            python -m toolkit calc "EXPRESSION"
            python -m toolkit convert VALUE --from UNIT --to UNIT
                
        For further help use:
            python -m toolkit calc --help
            python -m toolkit convert --help
            """)
            sys.exit(0)

def parse():
    parser = argparse.ArgumentParser(
        prog="toolkit",
        description="Calculator and unit converter.",
        usage="toolkit <command> [arguments]",
        add_help=False
    )
    commands = parser.add_subparsers(dest="command")

    # Для команды calc
    parse_calc = commands.add_parser("calc", add_help=False)
    parse_calc.add_argument("expression")

    # Для команды convert
    parse_convert = commands.add_parser("convert")
    parse_convert.add_argument("value")
    parse_convert.add_argument("--from", dest="from_unit", required=True)
    parse_convert.add_argument("--to", dest="to_unit", required=True)

    # Аргументы парсера
    args = parser.parse_args()
    return args


def full_calc(expr):

    compressed_expression = compress(expr) #  Совмещаем все + и -
    initial_validation_calc(compressed_expression)  # Предварительная валидация выражения
    tokenized_expression = tokenize(compressed_expression)  # Токенизация выражения
    validation_calc(tokenized_expression)  # Валиадция токенизированного выражения
    rpn_expression = shunting_yard(tokenized_expression)  # ОПЗ токенизированного выражения
    calculated_expression = calculate(rpn_expression)  # Итоговый подсчет

    print(calculated_expression)
    calc_dump(expr, calculated_expression)  # Выгрузка успешного запуска
    sys.exit(0)  # Успешное завершение программы


def full_convert(value,from_unit,to_unit):

    validation_convert(value, from_unit, to_unit)  # Валидация
    converted_value = convert(value, from_unit, to_unit)  # Перевод величин
     
    print(converted_value)  # Итоговый вывод
    convert_dump(value, converted_value, from_unit, to_unit)  # Выгрузка успешного запуска
    sys.exit(0)  # Успешное завершение программы