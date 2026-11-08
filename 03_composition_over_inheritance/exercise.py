"""Milestone 03 Exercise: Inheritance vs Composition in Berry's Pizza.

Instructions:
1. Implement component classes: Crust, Sauce, Topping.
2. Implement base class MenuItem and derived class Beverage (Inheritance).
3. Implement Pizza using Crust, Sauce, and Toppings (Composition + Inheritance from MenuItem).
"""

from typing import List

class Crust:
    """Represents a pizza crust option."""
    def __init__(self, name: str, extra_cost: float = 0.0):
        self.name = name
        self.extra_cost = float(extra_cost)


class Sauce:
    """Represents a pizza sauce option."""
    def __init__(self, name: str, is_spicy: bool = False):
        self.name = name
        self.is_spicy = is_spicy


class Topping:
    """Represents an individual pizza topping."""
    def __init__(self, name: str, price: float = 1.50):
        self.name = name
        self.price = float(price)


class MenuItem:
    """Base class for any item sold on Berry's menu (Inheritance)."""
    def __init__(self, name: str, base_price: float):
        self.name = name
        self.base_price = float(base_price)

    def get_price(self) -> float:
        """Return the calculated price of this item."""
        return self.base_price


class Beverage(MenuItem):
    """A drink sold at the pizzeria (Is-A MenuItem)."""
    def __init__(self, name: str, base_price: float, size_oz: int):
        # TODO: Call super().__init__ with name and base_price
        # Set self.size_oz
        pass


class Pizza(MenuItem):
    """A Pizza is a MenuItem, but is COMPOSED OF Crust, Sauce, and Toppings."""
    def __init__(self, name: str, base_price: float, crust: Crust, sauce: Sauce):
        """Initialize Pizza as a MenuItem, storing crust and sauce components,
        and an empty list of Topping objects.
        """
        # TODO: Call super().__init__
        # TODO: Store self.crust (Crust), self.sauce (Sauce), self.toppings (List[Topping])
        pass

    def add_topping(self, topping: Topping) -> None:
        """Add a Topping instance to toppings.
        Raise TypeError("Must be a Topping instance") if not an instance of Topping.
        """
        # TODO: Implement add_topping
        pass

    def get_price(self) -> float:
        """Calculate total price:
        base_price + crust.extra_cost + sum of all topping prices.
        """
        # TODO: Implement get_price
        pass

    def get_ingredients_summary(self) -> str:
        """Return a string listing crust, sauce, and toppings.
        Format: 'Crust: {crust.name}, Sauce: {sauce.name}, Toppings: {toppings or 'None'}'
        """
        # TODO: Implement get_ingredients_summary
        pass
