import math

class CartItem:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def item_total(self):
        return self.price * self.quantity


class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item_name):
        self.items = [
            item for item in self.items if item.name != item_name
        ]

    def calculate_total(self):
        return sum(item.item_total() for item in self.items)

    def print_receipt(self):
        print("----- Shopping Receipt -----")

        for item in self.items:
            print(
                f"{item.name} - ₹{item.price} x {item.quantity} = ₹{item.item_total()}"
            )

        subtotal = self.calculate_total()
        gst = subtotal * 0.18
        final_total = subtotal + gst

        print(f"\nSubtotal : ₹{subtotal}")
        print(f"GST (18%): ₹{gst}")
        print(f"Final Total : ₹{math.ceil(final_total)}")


cart = ShoppingCart()

cart.add_item(CartItem("Laptop", 50000, 1))
cart.add_item(CartItem("Mouse", 800, 2))
cart.add_item(CartItem("Keyboard", 1500, 1))

cart.remove_item("Mouse")

cart.print_receipt()