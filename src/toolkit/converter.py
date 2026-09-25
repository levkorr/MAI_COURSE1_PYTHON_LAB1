import json


with open("src/toolkit/config_units.json", "r", encoding="utf-8") as file: #  Чтение конфигурационного файла
    config = json.load(file)

def convert(value, from_unit, to_unit):
    ''' Переводит число из одной величины в другую

    Args:
        value: Значение которое нужно перевести
        from_unit: Из какой величины нужно перевести значение
        to_unit: В какую величину нужно перевести значение

    Returns:
        result: Конвертированное значение
    '''
    result = 0
    for category in config: # Пробегаем по величиным в джейсоне
        if category == "temperature":
            # Если наши данные - температура
            if from_unit in config[category]:
                from_unit_data = config["temperature"][from_unit]  # Импортируем данные из config
                to_unit_data = config["temperature"][to_unit]  # Импортируем данные из config

                # Переводим исходное значение в Кельвины
                kelvin = (value - from_unit_data["zero_offset"]) / from_unit_data["coef"]
                # Переводим значение в базовую единицу
                result = kelvin * to_unit_data["coef"] + to_unit_data["zero_offset"]

        else:
            # Если наши данные - не температура
            if from_unit in config[category]:
                from_coef = config[category][from_unit]
                to_coef = config[category][to_unit]

                # Переводим значение в базовую единицу
                origin = value/from_coef
                # Переводим значение в нужную единицу
                result = origin * to_coef
    return result
