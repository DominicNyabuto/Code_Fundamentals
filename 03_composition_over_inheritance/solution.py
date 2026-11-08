"""Milestone 03 Reference Solution."""

from typing import List

class Crust:
    def __init__(self, name: str, extra_cost: float = 0.0):
        self.name = name
        self.extra_cost = float(extra_cost)


class Sauce:
    def __init__(self, name: str, is_spicy: bool = False):
        self.name = name
        self.is_spicy = is_spicy


class Topping:
    def __init__(self, name: str, price: float = 1.50):
        self.name = name
        self.price = float(price)


class MenuItem:
    def __init__(self, name: str, base_price: float):
        self.name = name
        self.base_price = float(base_price)

    def get_price(self) -> float:
        return self.base_price


class Beverage(MenuItem):
    def __init__(self, name: str, base_price: float, size_oz: int):
        super().__init__(name, base_price)
        self.size_oz = size_oz


class Pizza(MenuItem):
    def __init__(self, name: str, base_price: float, crust: Crust, sauce: Sauce):
        super().__init__(name, base_price)
        self.crust = crust
        self.sauce = sauce
        self.toppings: List[Topping] = []

    def add_topping(self, topping: Topping) -> None:
        if not isinstance(topping, Topping):
            raise TypeError("Must be a Topping instance")
        self.toppings.append(topping)

    def get_price(self) -> float:
        toppings_cost = sum(t.price for t in self.toppings)
        return self.base_price + self.crust.extra_cost + toppings_cost

    def get_ingredients_summary(self) -> str:
        topping_names = ", ".join(t.name for t in self.toppings) if self.toppings else "None"
        return f"Crust: {self.crust.name}, Sauce: {self.sauce.name}, Toppings: {topping_names}"
