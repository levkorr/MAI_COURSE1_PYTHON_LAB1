def convert(value, from_metric, to_metric):
    ''' Переводит число из одной величины в другую

    Args:
        value: Значение которое нужно перевести
        from_metric: Из какой величины нужно перевести значение
        to_metric: В какую величину нужно перевести значение

    Returns:
        Конвертированное значение
    '''
    metrics = from_metric+"_to_"+to_metric  # Создаем вид для словаря
    metrics_dict = {"mm_to_cm": "-10",  # - Означает, что нужно делить
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
    if metrics in metrics_dict:
        if metrics_dict[metrics][0] == "-":  # Если надо делить
            return (value/int(metrics_dict[metrics][1:]))
        else:  # Если надо умножать
            return (value*int(metrics_dict[metrics][1:]))

    # Если это температура (нелинейный перевод)
    elif metrics == "c_to_f":
        return (value*9/5)+32
    elif metrics == "f_to_c":
        return (value-32)*5/9
    elif metrics == "c_to_k":
        return (value+273.15)
    elif metrics == "k_to_c":
        return (value-273.15)
    elif metrics == "f_to_k":
        return (value - 32) * 5/9 + 273.15
    elif metrics == "k_to_f":
        return (value - 273.15) * 9/5 + 32
