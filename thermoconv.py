def celsius_to_fahrenheit(c):
    return round(c * 9 / 5 + 32, 2)


def fahrenheit_to_celsius(f):
    return round((f - 32) * 5 / 9, 2)


def celsius_to_kelvin(c):
    return round(c + 273.15, 2)


def read_number(prompt):
    raw = input(prompt).strip().replace(",", ".")
    try:
        if raw.upper().endswith("F"):
            return fahrenheit_to_celsius(float(raw[:-1]))
        return float(raw)
    except ValueError:
        print("Нужно ввести число")
        raise SystemExit(1)


c = read_number("Температура (например, 36,6 или 98F): ")

f = celsius_to_fahrenheit(c)
print(f"Результат: {c}°C → {f}°F")
print(f"{c} °C = {celsius_to_kelvin(c)} K")
