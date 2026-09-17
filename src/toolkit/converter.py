def convert(Value, From, To):
    Value = int(Value)
    metrics=From+"_to_"+To # Создаем вид для словаря
    metrics_dict={"mm_to_cm": "-10", #- Означает, что нужно делить
                  "cm_to_mm": "+10", #+ Означает, что нужно умножить
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
    # Если это температура (нелинейный перевод)
    if metrics == "c_to_f": 
        return (Value*9/5)+32
    elif metrics == "f_to_c":
        return (Value-32)*5/9

    # Если линейный перевод величин возможен:
    elif metrics in metrics_dict:
        if metrics_dict[metrics][0]=="-": # Если надо делить
            return (Value/int(metrics_dict[metrics][1:]))
        else: # Если надо умножать
            return (Value*int(metrics_dict[metrics][1:])) 