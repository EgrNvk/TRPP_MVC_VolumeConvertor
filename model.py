conversion = {"m3": 1, "dm3": 0.001, "cm3": 0.000001, "mm3": 0.000000001}

def convert_volume(value, from_unit, to_unit):
    from_unit = from_unit.strip()
    to_unit = to_unit.strip()

    if from_unit not in conversion or to_unit not in conversion:
        raise ValueError("Помилка: використовуйте тільки м3, дм3, см3 або мм3")

    value_in_m3=value*conversion[from_unit]
    result=value_in_m3/conversion[to_unit]
    return result