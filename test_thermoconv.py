import sys

from thermoconv import celsius_to_fahrenheit, celsius_to_kelvin, fahrenheit_to_celsius

CHECKS = [
    ("celsius_to_fahrenheit(100)", celsius_to_fahrenheit(100), 212),
    ("celsius_to_fahrenheit(-40)", celsius_to_fahrenheit(-40), -40),
    ("celsius_to_kelvin(0)", celsius_to_kelvin(0), 273.15),
    ("fahrenheit_to_celsius(212)", fahrenheit_to_celsius(212), 100),
]

failed = 0
for name, got, want in CHECKS:
    if got != want:
        print(f"ОШИБКА: {name} = {got}, ожидалось {want}")
        failed += 1
print("Все проверки пройдены" if not failed else f"Провалено проверок: {failed}")
sys.exit(1 if failed else 0)
