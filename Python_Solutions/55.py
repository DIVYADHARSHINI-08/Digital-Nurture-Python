import matplotlib.pyplot as plt


class Category:

    def __init__(self, name, limit):
        self.name = name
        self.limit = limit
        self.spent = 0

    def add_expense(self, amount):
        self.spent += amount

    def check_budget(self):

        if self.spent > self.limit:
            print(f"Alert: {self.name} exceeded the budget!")

    def remaining(self):
        return self.limit - self.spent


categories = {}

num = int(input("Enter number of categories: "))

for i in range(num):

    name = input("Enter category name: ")
    limit = float(input(f"Enter budget limit for {name}: "))

    categories[name] = Category(name, limit)

while True:

    print("\n1. Add Expense")
    print("2. View Summary")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":

        category_name = input("Enter category: ")

        if category_name in categories:

            amount = float(input("Enter expense amount: "))

            categories[category_name].add_expense(amount)

            categories[category_name].check_budget()

        else:
            print("Category not found")

    elif choice == "2":

        print("\n----- Budget Summary -----")

        for category in categories.values():

            print(
                f"{category.name} | "
                f"Limit: ₹{category.limit} | "
                f"Spent: ₹{category.spent} | "
                f"Remaining: ₹{category.remaining()}"
            )

    elif choice == "3":
        break

    else:
        print("Invalid choice")


labels = [category.name for category in categories.values()]
amounts = [category.spent for category in categories.values()]

plt.pie(amounts, labels=labels, autopct="%1.1f%%")
plt.title("Monthly Budget Spending")
plt.show()