import argparse
import sys

from .calculator import calculate
from .converter import convert
from .json_dump import calc_dump, convert_dump
from .tokenizer import compress, shunting_yard, tokenize
from .validator import initial_validation_calc, validation_calc, validation_convert
from .errors import FailedSaveError


def custom_help(argv):
    ''' Модуль создающий кастомный хелп в зависмиости от аргументов

    Args:
        argv: Список аргументов, поступивших в программу 
    
    Returns:
        None
    '''
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
        
        WARNING:
            If your expression starts with '--':
            Put additional '--' before the expression 
    
        Examples of working programs:
            python -m toolkit calc "2+2"             Returns 4
            python -m toolkit calc "8.5/4.25"        Returns 2.0
            python -m toolkit calc -- "--23+24"      Returns 47 
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
                
        Examples of working programs:
            python -m toolkit convert 100 --from g --to kg      Returns 0.1
            python -m toolkit convert 50 --from f --to c        Returns 10.0
            python -m toolkit convert 25 --from m --to mm       Returns 25000.0
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
    ''' Модуль создающий парсер
    
    Args:
        None
    
    Returns:
        args: Аргументы парсера
    '''
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
    ''' Весь цикл работы модуля calc, 
    От получения аргументов, до вывода ответа, выгрузки успешного запуска и завершения программы
    
    Args:
        expr: Матемтическое выражение
    
    Returns:
        None
    '''
    compressed_expression = compress(expr) #  Совмещаем все + и -
    initial_validation_calc(compressed_expression)  # Предварительная валидация выражения
    tokenized_expression = tokenize(compressed_expression)  # Токенизация выражения
    validation_calc(tokenized_expression)  # Валиадция токенизированного выражения
    rpn_expression = shunting_yard(tokenized_expression)  # ОПЗ токенизированного выражения
    calculated_expression = calculate(rpn_expression)  # Итоговый подсчет

    print(calculated_expression)
    try:
        calc_dump(expr, calculated_expression)  # Выгрузка успешного запуска
    except Exception:
        raise FailedSaveError()
    sys.exit(0)  # Успешное завершение программы


def full_convert(value,from_unit,to_unit):
    ''' Весь цикл работы модуля convert, 
    От получения аргументов, до вывода ответа, выгрузки успешного запуска и завершения программы
    
    Args:
        value: Значение, которое надо перевести
        from_unit: Величина из которой надо перевести
        to_unit: Величина в которую надо перевести

    Returns:
        None
    '''
    validation_convert(value, from_unit, to_unit)  # Валидация
    converted_value = convert(value, from_unit, to_unit)  # Перевод величин
    formatted_value = f"{converted_value:.15f}".rstrip("0").rstrip(".")

    if formatted_value.isdigit():
        formatted_value=float(formatted_value)

    print(formatted_value)  # Итоговый вывод
    try:
        convert_dump(value, formatted_value, from_unit, to_unit)  # Выгрузка успешного запуска
    except Exception:
        raise FailedSaveError()
    sys.exit(0)  # Успешное завершение программы
