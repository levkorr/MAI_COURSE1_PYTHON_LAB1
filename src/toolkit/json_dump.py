import json

def dump(expr, calculated_expression):
    ''' История успешных операций в successful_launches.json
    
    Args:
        expr: Строка, математическое выражение в инфиксной записи
        calculated_expression: Вещественное число, результат математического выражения

    Returns:
        None
    '''
    data = {
        "expression": expr,
        "result": calculated_expression}

    with open("successful_launches.json", "r") as file:
        launches = json.load(file)

    launches.append(data)

    with open("successful_launches.json", "w") as file:
        json.dump(launches, file, indent=2)