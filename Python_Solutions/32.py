def expenses(expense_list):
    expense_amount = 500
    if expense_amount < 0:
        print("Expense amount cannot be negative.")
    expense_list.append(expense_amount)

expense_list = [200,300,400]
print("Expenses before adding new expense:", expense_list)
expenses(expense_list)
print("Expenses after adding new expense:", expense_list)