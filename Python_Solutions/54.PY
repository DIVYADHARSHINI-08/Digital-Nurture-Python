class Product:

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def display(self):
        return f"{self.name} - ₹{self.price}"


class Perishable(Product):

    def __init__(self, name, price, expiry_date):
        super().__init__(name, price)
        self.expiry_date = expiry_date

    def display(self):
        return (
            f"{self.name} - ₹{self.price} "
            f"(Expiry: {self.expiry_date})"
        )


class Electronics(Product):

    def __init__(self, name, price, warranty):
        super().__init__(name, price)
        self.warranty = warranty

    def display(self):
        return (
            f"{self.name} - ₹{self.price} "
            f"(Warranty: {self.warranty})"
        )


inventory = {}

inventory["Milk"] = {
    "product": Perishable("Milk", 50, "2026-06-10"),
    "stock": 5
}

inventory["Bread"] = {
    "product": Perishable("Bread", 40, "2026-06-07"),
    "stock": 2
}

inventory["Laptop"] = {
    "product": Electronics("Laptop", 60000, "2 Years"),
    "stock": 10
}

inventory["Mobile"] = {
    "product": Electronics("Mobile", 25000, "1 Year"),
    "stock": 3
}

low_stock_alerts = set()

for item, details in inventory.items():

    if details["stock"] < 5:
        low_stock_alerts.add(item)

print("----- Inventory Summary -----")

for item, details in inventory.items():

    print(
        f"{details['product'].display()} | "
        f"Stock: {details['stock']}"
    )

print("\n----- Low Stock Alerts -----")

for item in low_stock_alerts:
    print(item)