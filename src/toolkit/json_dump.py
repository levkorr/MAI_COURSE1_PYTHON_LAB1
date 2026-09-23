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
        "expression": expr,
        "result": calculated_expression}

    with open("logs/successful_launches.json", "r") as file:
        launches = json.load(file)

    launches.append(data)

    with open("logs/successful_launches.json", "w") as file:
        json.dump(launches, file, indent=2)

def convert_dump(value, converted_value, from_metric, to_metric):
    ''' Пополняет историю успешных выполнений программы в successful_launches.json

    Args:
        value: Значение которое нужно перевести
        converted_value: Переведенное значение
        from_metric: Из какой был совершен перевод
        to_metric: В какую величину был совершен перевод
        
    Returns:
        None
    '''
    data = {
        "value": str(value)+from_metric,
        "converted value": str(converted_value)+to_metric}

    with open("logs/successful_launches.json", "r") as file:
        launches = json.load(file)

    launches.append(data)

    with open("logs/successful_launches.json", "w") as file:
        json.dump(launches, file, indent=2)
