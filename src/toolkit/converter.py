def convert(value, from_unit, to_unit):
    ''' Переводит число из одной величины в другую

    Args:
        value: Значение которое нужно перевести
        from_unit: Из какой величины нужно перевести значение
        to_unit: В какую величину нужно перевести значение

    Returns:
        Конвертированное значение
    '''
    result = 0

    units = from_unit+"_to_"+to_unit  # Создаем вид для словаря
    units_dict = {"mm_to_cm": "-10",  # - Означает, что нужно делить
                    "cm_to_mm": "+10",  # + Означает, что нужно умножить
                    "mm_to_m": "-1000",
                    "m_to_mm": "+1000",
                    "mm_to_km": "-1000000",
                    "km_to_mm": "+1000000",
                    "cm_to_m": "-100",
                    "m_to_cm": "+100",
                    "cm_to_km": "-100000",
                    "km_to_cm": "+100000",
                    "m_to_km": "-1000",
                    "km_to_m": "+1000",

                    "g_to_kg": "-1000",
                    "kg_to_g": "+1000"}

    # Если линейный перевод величин возможен:
    if units in units_dict:
        if units_dict[units][0] == "-":  # Если надо делить
            result = value/int(units_dict[units][1:])
        else:  # Если надо умножать
            result = value*int(units_dict[units][1:])

    # Если это температура (нелинейный перевод)
    elif units == "c_to_f":
        result = value*9/5+32
    elif units == "f_to_c":
        result = (value-32)*5/9
    elif units == "c_to_k":
        result = value+273.15
    elif units == "k_to_c":
        result = value-273.15
    elif units == "f_to_k":
        result = (value - 32) * 5/9 + 273.15
    elif units == "k_to_f":
        result = (value - 273.15) * 9/5 + 32
    return result
