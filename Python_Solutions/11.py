def convert_kg_to_pound(kilogram):
    pound = kilogram * 2.20462
    return pound
kilogram = float(input("Enter weight in kilograms: "))
pound = convert_kg_to_pound(kilogram)
print(f"Weight in pounds: {pound}")