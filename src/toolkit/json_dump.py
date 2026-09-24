import json

def calc_dump(expr, calculated_expression):
    ''' Пополняет историю успешных выполнений программы в successful_launches.json
    
    Args:
        expr: Строка, математическое выражение в инфиксной записи
        calculated_expression: Вещественное число, результат математического выражения

    Returns:
        None
    '''
    data = {
        "type": "calculation",
        "expression": expr,
        "result": calculated_expression}

    with open("logs/successful_launches.json", "r", encoding="utf-8") as file:
        launches = json.load(file)

    launches.append(data)

    with open("logs/successful_launches.json", "w", encoding="utf-8") as file:
        json.dump(launches, file, indent=2)

def convert_dump(value, converted_value, from_unit, to_unit):
    ''' Пополняет историю успешных выполнений программы в successful_launches.json

    Args:
        value: Значение которое нужно перевести
        converted_value: Переведенное значение
        from_unit: Из какой был совершен перевод
        to_unit: В какую величину был совершен перевод
        
    Returns:
        None
    '''
    data = {
        "type": "convertation",
        "value": str(value)+from_unit,
        "converted value": str(converted_value)+to_unit}

    with open("logs/successful_launches.json", "r", encoding="utf-8") as file:
        launches = json.load(file)

    launches.append(data)

    with open("logs/successful_launches.json", "w", encoding="utf-8") as file:
        json.dump(launches, file, indent=2)
