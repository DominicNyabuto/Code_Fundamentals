"""Milestone 04 Reference Solution."""

class PizzaItem:
    def __init__(self, name: str, size: str, base_price: float, toppings_count: int):
        self.name = name
        self.size = size
        self.base_price = float(base_price)
        self.toppings_count = toppings_count

    def get_total_price(self) -> float:
        return self.base_price + (self.toppings_count * 1.50)

    def get_receipt_line(self) -> str:
        price = self.get_total_price()
        return f"{self.size} {self.name} (w/ {self.toppings_count} toppings): ${price:.2f}"


class BeverageItem:
    def __init__(self, name: str, unit_price: float, quantity: int = 1):
        self.name = name
        self.unit_price = float(unit_price)
        self.quantity = quantity

    def get_total_price(self) -> float:
        return self.unit_price * self.quantity

    def get_receipt_line(self) -> str:
        total = self.get_total_price()
        return f"{self.quantity}x {self.name}: ${total:.2f}"


class SideItem:
    def __init__(self, name: str, price: float, dip_sauce: str = "Garlic Mayo"):
        self.name = name
        self.price = float(price)
        self.dip_sauce = dip_sauce

    def get_total_price(self) -> float:
        return self.price

    def get_receipt_line(self) -> str:
        return f"{self.name} with {self.dip_sauce}: ${self.price:.2f}"


class DeliveryFeeItem:
    def __init__(self, distance_miles: float, rate_per_mile: float = 1.25):
        self.distance_miles = float(distance_miles)
        self.rate_per_mile = float(rate_per_mile)

    def get_total_price(self) -> float:
        return self.distance_miles * self.rate_per_mile

    def get_receipt_line(self) -> str:
        price = self.get_total_price()
        return f"Delivery Fee ({self.distance_miles:.1f} miles): ${price:.2f}"


class Cart:
    def __init__(self):
        self.items = []

    def add_item(self, item) -> None:
        if not hasattr(item, "get_total_price") or not callable(item.get_total_price):
            raise TypeError("Item must be billable")
        if not hasattr(item, "get_receipt_line") or not callable(item.get_receipt_line):
            raise TypeError("Item must be billable")
        self.items.append(item)

    def calculate_total(self) -> float:
        return sum(item.get_total_price() for item in self.items)

    def generate_receipt(self) -> str:
        lines = [item.get_receipt_line() for item in self.items]
        lines.append("---")
        lines.append(f"TOTAL: ${self.calculate_total():.2f}")
        return "\n".join(lines)
