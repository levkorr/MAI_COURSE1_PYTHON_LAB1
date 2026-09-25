class CalculatorError(Exception):
    # Parent ошибка для калькулятора
    pass

class ConverterError(Exception):
    # Parent ошибка для конвертера
    pass

class SequentialOperationsError(CalculatorError):
    def __init__(self, operations):
        super().__init__(f"Sequential Operations: {operations}")

class FloatOperandError(CalculatorError):
    def __init__(self, operand):
        super().__init__(f"Float mistake: {operand}")

class OperationStartError(CalculatorError):
    def __init__(self, operation):
        super().__init__(f"Expression starts with operation: {operation}")

class DivisionByZeroError(CalculatorError):
    def __init__(self, operation_operand):
        super().__init__(f"Division by zero occurred: {operation_operand}")

class OperationEndError(CalculatorError):
    def __init__(self, operation):
        super().__init__(f"Expression ends with operation: {operation}")

class SplitNumberError(CalculatorError):
    def __init__(self, operation):
        super().__init__(f"Number is split: {operation}")

class UnknownSymbolsError(CalculatorError):
    def __init__(self, symbols):
        super().__init__(f"Unknown symbols: {symbols}")

class IntSpecialOperationsError(CalculatorError):
    def __init__(self, operation, number1, number2):
        super().__init__(f"The operation {operation} only works with int: {number1}{operation}{number2}")

class UnknownUnitsError(ConverterError):
    def __init__(self, symbols):
        super().__init__(f"Unknown units: {symbols}")

class DifferentUnitTypesError(ConverterError):
    def __init__(self, from_unit, to_unit):
        super().__init__(f"Different unit types: {from_unit}, {to_unit}")

class BelowAbsoluteZeroError(ConverterError):
    def __init__(self, value, from_unit):
        super().__init__(f"Temperature below absolute zero: {value}{from_unit}")
