from tabulate import tabulate


class Converter:

    def celsius_to_fahrenheit(self, c):
        return (c * 9/5) + 32

    def celsius_to_kelvin(self, c):
        return c + 273.15

    def fahrenheit_to_celsius(self, f):
        return (f - 32) * 5/9

    def fahrenheit_to_kelvin(self, f):
        return ((f - 32) * 5/9) + 273.15

    def kelvin_to_celsius(self, k):
        return k - 273.15

    def kelvin_to_fahrenheit(self, k):
        return ((k - 273.15) * 9/5) + 32


converter = Converter()

print("----- Temperature Converter -----")
print("1. Celsius to Fahrenheit & Kelvin")
print("2. Fahrenheit to Celsius & Kelvin")
print("3. Kelvin to Celsius & Fahrenheit")

choice = int(input("Enter your choice: "))
temp = float(input("Enter temperature value: "))

table = []

if choice == 1:
    f = converter.celsius_to_fahrenheit(temp)
    k = converter.celsius_to_kelvin(temp)

    table = [
        ["Celsius", f"{temp:.2f} °C"],
        ["Fahrenheit", f"{f:.2f} °F"],
        ["Kelvin", f"{k:.2f} K"]
    ]

elif choice == 2:
    c = converter.fahrenheit_to_celsius(temp)
    k = converter.fahrenheit_to_kelvin(temp)

    table = [
        ["Fahrenheit", f"{temp:.2f} °F"],
        ["Celsius", f"{c:.2f} °C"],
        ["Kelvin", f"{k:.2f} K"]
    ]

elif choice == 3:
    c = converter.kelvin_to_celsius(temp)
    f = converter.kelvin_to_fahrenheit(temp)

    table = [
        ["Kelvin", f"{temp:.2f} K"],
        ["Celsius", f"{c:.2f} °C"],
        ["Fahrenheit", f"{f:.2f} °F"]
    ]

else:
    print("Invalid choice")

if table:
    print("\nConversion Result:")
    print(tabulate(table, headers=["Scale", "Value"], tablefmt="grid"))