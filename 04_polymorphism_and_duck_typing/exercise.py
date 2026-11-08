"""Milestone 04 Exercise: Polymorphism & Duck Typing in Berry's Pizza.

Instructions:
1. Implement classes with polymorphic interfaces:
   - PizzaItem
   - BeverageItem
   - SideItem
   - DeliveryFeeItem (Duck typing example: not a food item, but quacks like a billable item!)
2. Implement Cart that calculates totals and renders receipts without type checks.
"""

from typing import List

class PizzaItem:
    def __init__(self, name: str, size: str, base_price: float, toppings_count: int):
        self.name = name
        self.size = size
        self.base_price = float(base_price)
        self.toppings_count = toppings_count

    def get_total_price(self) -> float:
        """Returns base_price + (toppings_count * 1.50)."""
        # TODO: Implement get_total_price
        pass

    def get_receipt_line(self) -> str:
        """Returns: '{size} {name} (w/ {toppings_count} toppings): ${price:.2f}'
        e.g. 'Large Margherita (w/ 2 toppings): $15.00'
        """
        # TODO: Implement get_receipt_line
        pass


class BeverageItem:
    def __init__(self, name: str, unit_price: float, quantity: int = 1):
        self.name = name
        self.unit_price = float(unit_price)
        self.quantity = quantity

    def get_total_price(self) -> float:
        """Returns unit_price * quantity."""
        # TODO: Implement get_total_price
        pass

    def get_receipt_line(self) -> str:
        """Returns: '{quantity}x {name}: ${total:.2f}'
        e.g. '2x Cold Brew: $6.00'
        """
        # TODO: Implement get_receipt_line
        pass


class SideItem:
    def __init__(self, name: str, price: float, dip_sauce: str = "Garlic Mayo"):
        self.name = name
        self.price = float(price)
        self.dip_sauce = dip_sauce

    def get_total_price(self) -> float:
        """Returns self.price."""
        # TODO: Implement get_total_price
        pass

    def get_receipt_line(self) -> str:
        """Returns: '{name} with {dip_sauce}: ${price:.2f}'
        e.g. 'Garlic Knots with Garlic Mayo: $5.00'
        """
        # TODO: Implement get_receipt_line
        pass


class DeliveryFeeItem:
    """Pure Duck Typing: This is a service fee, NOT a food menu item,
    yet it implements the identical interface!
    """
    def __init__(self, distance_miles: float, rate_per_mile: float = 1.25):
        self.distance_miles = float(distance_miles)
        self.rate_per_mile = float(rate_per_mile)

    def get_total_price(self) -> float:
        """Returns distance_miles * rate_per_mile."""
        # TODO: Implement get_total_price
        pass

    def get_receipt_line(self) -> str:
        """Returns: 'Delivery Fee ({distance_miles:.1f} miles): ${price:.2f}'"""
        # TODO: Implement get_receipt_line
        pass


class Cart:
    """Polymorphic Shopping Cart. It has NO idea what concrete classes are inside;
    it only trusts that every item responds to .get_total_price() and .get_receipt_line().
    """
    def __init__(self):
        self.items = []

    def add_item(self, item) -> None:
        """Add any item that has get_total_price and get_receipt_line methods.
        If it doesn't have both callable attributes, raise TypeError("Item must be billable").
        """
        # TODO: Check duck typing compliance, then append to self.items
        pass

    def calculate_total(self) -> float:
        """Polymorphic sum of all items in cart."""
        # TODO: Implement calculate_total
        pass

    def generate_receipt(self) -> str:
        """Generate formatted multi-line receipt:
        Each line from item.get_receipt_line()
        Followed by '---'
        Followed by 'TOTAL: ${total:.2f}'
        """
        # TODO: Implement generate_receipt
        pass
