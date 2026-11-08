"""Milestone 01 Reference Solution."""

from typing import List

class Pizza:
    """Blueprint for a customizable Pizza."""

    SIZE_PRICES = {
        "small": 8.0,
        "medium": 10.0,
        "large": 12.0
    }
    TOPPING_PRICE = 1.50

    def __init__(self, size: str, crust: str):
        size = size.lower()
        if size not in self.SIZE_PRICES:
            raise ValueError(f"Invalid pizza size. Must be one of {list(self.SIZE_PRICES.keys())}")
        self.size = size
        self.crust = crust.lower()
        self.toppings: List[str] = []

    def add_topping(self, topping: str) -> None:
        self.toppings.append(topping.lower())

    def calculate_price(self) -> float:
        base_price = self.SIZE_PRICES[self.size]
        toppings_cost = len(self.toppings) * self.TOPPING_PRICE
        return base_price + toppings_cost

    def get_description(self) -> str:
        toppings_str = ", ".join(self.toppings) if self.toppings else "Cheese Only"
        return f"{self.size} pizza with {self.crust} crust topped with: {toppings_str}"


class CustomerOrder:
    """Represents a customer's total order containing one or more pizzas."""

    def __init__(self, customer_name: str):
        self.customer_name = customer_name
        self.pizzas: List[Pizza] = []

    def add_pizza(self, pizza: Pizza) -> None:
        if not isinstance(pizza, Pizza):
            raise TypeError("Item must be a Pizza")
        self.pizzas.append(pizza)

    def calculate_total(self) -> float:
        return sum(pizza.calculate_price() for pizza in self.pizzas)
