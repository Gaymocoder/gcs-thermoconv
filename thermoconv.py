def celsius_to_fahrenheit(c):
    return round(c * 9 / 5 + 32, 2)


def celsius_to_kelvin(c):
    return round(c + 273.15, 2)


def read_number(prompt):
    try:
        return float(input(prompt).replace(",", "."))
    except ValueError:
        print("Нужно ввести число")
        raise SystemExit(1)


c = read_number("Температура в °C: ")

f = celsius_to_fahrenheit(c)
print(f"Результат: {c}°C → {f}°F")
print(f"{c} °C = {celsius_to_kelvin(c)} K")
