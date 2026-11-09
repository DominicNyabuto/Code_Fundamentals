"""Milestone 01 Exercise: Transform Procedural Pizza Code into Classes & Objects.

Instructions:
1. Complete the `Pizza` class with its attributes, `add_topping`, and `calculate_price` methods.
2. Complete the `CustomerOrder` class that aggregates multiple pizzas for a customer.
3. Validate by running `python3 test_milestone.py`.
"""

from typing import List

class Pizza:
    """Class for a customizable Pizza."""

    SIZE_PRICES = {
        "small": 8.0,
        "medium": 10.0,
        "large": 12.0
    }
    TOPPING_PRICE = 1.50

    def __init__(self, size: str, crust: str):
        """Initialize pizza with a size and crust type.
        
        Size should be converted to lower-case.
        Validate that size is one of: "small", "medium", "large".
        If invalid, raise ValueError("Invalid pizza size").
        Crust should be lower-case string.
        Initialize an empty list of toppings.
        """
        # TODO: Implement __init__
        pass

    def add_topping(self, topping: str) -> None:
        """Add a lower-case topping string to self.toppings."""
        # TODO: Implement add_topping
        pass

    def calculate_price(self) -> float:
        """Calculate total price: base size price + (number of toppings * TOPPING_PRICE)."""
        # TODO: Implement calculate_price
        pass

    def get_description(self) -> str:
        """Return formatted description string.
        Format:
        '{size} pizza with {crust} crust topped with: {comma separated toppings or 'Cheese Only'}'
        Example: 'large pizza with thin crust topped with: mushrooms, olives'
        Example (no toppings): 'small pizza with stuffed crust topped with: Cheese Only'
        """
        # TODO: Implement get_description
        pass


class CustomerOrder:
    """Represents a customer's total order containing one or more pizzas."""

    def __init__(self, customer_name: str):
        """Initialize with customer name and an empty list of pizzas."""
        # TODO: Implement __init__
        pass

    def add_pizza(self, pizza: Pizza) -> None:
        """Add a Pizza instance to this order.
        If the passed object is not an instance of Pizza, raise TypeError("Item must be a Pizza").
        """
        # TODO: Implement add_pizza
        pass

    def calculate_total(self) -> float:
        """Sum up the prices of all pizzas in the order."""
        # TODO: Implement calculate_total
        pass

