import csv
from datetime import datetime

expenses = []

try:
    current_month = datetime.now().month
    current_year = datetime.now().year
    with open("expenses.csv", "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            expense_date = datetime.strptime(row["date"], "%Y-%m-%d")
            if (expense_date.month == current_month and
                    expense_date.year == current_year):

                expenses.append({
                    "date": row["date"],
                    "amount": float(row["amount"]),
                    "category": row["category"]
                })

    category_totals = {}

    for expense in expenses:
        category = expense["category"]
        amount = expense["amount"]

        if category in category_totals:
            category_totals[category] += amount
        else:
            category_totals[category] = amount

    print("----- Current Month Expense Summary -----")

    for category, total in category_totals.items():
        print(f"{category}: ₹{total}")

    total_expense = sum(category_totals.values())

    print(f"\nTotal Expense: ₹{total_expense}")

except FileNotFoundError:
    print("Error: expenses.csv file not found.")

except Exception as e:
    print("Error:", e)